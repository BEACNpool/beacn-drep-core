"""Claude reasoning layer for the BEACN DRep pipeline — the stages that need real
language understanding.

  Stage 1 — extract_claims(): read the proposal's cached anchor document and
    extract structured intake facts + claim rows (economic / technical /
    governance / adoption), each tagged by how well the document supports it.
    Feeds the assessment's evidence table and the human message.

  Stage 1.5 — assess_lean(): read the claims, the deterministic assessment, and
    the matching soul DOCTRINE, and return a BOUNDED score adjustment + direction
    with a written rationale. This is the one place the reasoning layer is allowed
    to influence the vote, and only within strict limits (see contract below).

  Stage 6 — write_human_message(): turn the *already-decided* deterministic
    assessment + score + recommendation into a plain-English explanation. It
    explains the vote; it cannot alter it.

Determinism / safety contract:
  * The HARD GATES (stale data, unknown action type, missing baseline evidence,
    treasury-needs-dossier, hard blocker, high unmitigated flags) are pure
    deterministic Python and run BEFORE any LLM influence. The reasoning layer
    can NEVER rescue or override a gated action.
  * For a non-gated action, assess_lean may nudge the score by at most
    ±LLM_SCORE_ADJUST_CAP (config; default 0.05). The engine clamps the value
    regardless of what the model returns, records the raw score, the clamped
    adjustment, the rationale, and prompt/output hashes, so every run is
    auditable and the influence is fully transparent on the public record.
  * With no ANTHROPIC_API_KEY / anthropic SDK / BEACN_DREP_DISABLE_LLM, the live
    path is unavailable; the pipeline still runs. Under BEACN_DREP_OFFLINE_REVIEW
    a deterministic, doctrine-aware lean is produced instead (reproducible, so
    replay stays clean). With nothing available the adjustment is 0 (no change).

Model defaults to claude-opus-4-8 (override with BEACN_DREP_MODEL).
"""
from __future__ import annotations

import hashlib
import json
import os
import re

MODEL = os.environ.get("BEACN_DREP_MODEL", "claude-opus-4-8")

_CACHE: dict | None = None
_CACHE_LOADED = False


def _disabled() -> bool:
    return os.environ.get("BEACN_DREP_DISABLE_LLM", "").strip().lower() in ("1", "true", "yes")


def _offline_review_enabled() -> bool:
    return os.environ.get("BEACN_DREP_OFFLINE_REVIEW", "").strip().lower() in ("1", "true", "yes")


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _cache() -> dict:
    """Precomputed model outputs, keyed by action_id, from BEACN_DREP_LLM_CACHE.

    Shape: { action_id: { "claims": {request, claims, summary}, "message": str } }.
    Lets a reasoning pass (or an offline/cached run) supply Stage 1 / Stage 6 outputs
    without a live API call, while the engine stays the single writer of artifacts.
    """
    global _CACHE, _CACHE_LOADED
    if _CACHE_LOADED:
        return _CACHE or {}
    _CACHE_LOADED = True
    path = os.environ.get("BEACN_DREP_LLM_CACHE", "").strip()
    if path:
        try:
            with open(path, encoding="utf-8") as f:
                _CACHE = json.load(f)
        except Exception:
            _CACHE = None
    return _CACHE or {}


def _client():
    """Return an Anthropic client, or None if the model layer is unavailable."""
    if _disabled() or not os.environ.get("ANTHROPIC_API_KEY"):
        return None
    try:
        import anthropic  # imported lazily so the deterministic pipeline needs no SDK
    except Exception:
        return None
    try:
        return anthropic.Anthropic()
    except Exception:
        return None


def _text_of(resp) -> str:
    return "".join(b.text for b in resp.content if getattr(b, "type", None) == "text").strip()


def _clean_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
        value = re.sub(r"`([^`]+)`", r"\1", value)
        value = re.sub(r"[*_#>]+", " ", value)
        return re.sub(r"\s+", " ", value).strip()
    if isinstance(value, (int, float)):
        return str(value)
    return ""


def _anchor_json(anchor_text: str | None):
    if not anchor_text:
        return None
    try:
        return json.loads(anchor_text)
    except Exception:
        return None


def _walk(obj):
    if isinstance(obj, dict):
        yield obj
        for key, value in obj.items():
            if key == "@context":
                continue
            yield from _walk(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from _walk(value)


def _first_text(obj, keys: list[str]) -> str:
    wanted = {k.lower() for k in keys}
    for node in _walk(obj):
        for key, value in node.items():
            if key.lower().split(":")[-1] in wanted:
                text = _clean_text(value)
                if text.startswith(("CIP", "http://", "https://")) and ":" in text:
                    continue
                if text:
                    return text
    return ""


def _all_text(obj, keys: list[str], limit: int = 8) -> list[str]:
    wanted = {k.lower() for k in keys}
    out: list[str] = []
    seen: set[str] = set()
    for node in _walk(obj):
        for key, value in node.items():
            if key.lower().split(":")[-1] in wanted:
                text = _clean_text(value)
                if text.startswith(("CIP", "http://", "https://")) and ":" in text:
                    continue
                if text and text not in seen:
                    out.append(text)
                    seen.add(text)
                    if len(out) >= limit:
                        return out
    return out


def _reference_count(obj) -> int:
    count = 0
    for node in _walk(obj):
        for key, value in node.items():
            if key.lower().split(":")[-1] in ("uri", "url") and _clean_text(value).startswith(("http://", "https://", "ipfs://")):
                count += 1
    return count


def _sentences(text: str, limit: int = 6) -> list[str]:
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+", text)
    out = []
    for part in parts:
        part = part.strip(" -")
        if len(part) < 35:
            continue
        if len(part) > 260:
            part = part[:257].rstrip() + "..."
        out.append(part)
        if len(out) >= limit:
            break
    return out


def _readable_text_fallback(anchor_text: str) -> str:
    text = re.sub(r'"@context"\s*:\s*\{.*?\}\s*,', " ", anchor_text, flags=re.DOTALL)
    text = re.sub(r'"(CIP\d+|hashAlgorithm|authors?|witness|signature|publicKey|referenceHash)"\s*:\s*("[^"]*"|\{.*?\}|\[.*?\])\s*,?', " ", text, flags=re.DOTALL)
    text = re.sub(r'https?://\S+', " ", text)
    text = re.sub(r'ipfs://\S+', " ", text)
    text = re.sub(r'[{}\[\]",]', " ", text)
    return _clean_text(text)


def _regex_text_fields(anchor_text: str) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for key in ("title", "abstract", "motivation", "rationale", "description", "summary"):
        pattern = rf'"{key}"\s*:\s*"((?:\\.|[^"\\])*)"' 
        for match in re.finditer(pattern, anchor_text, flags=re.IGNORECASE):
            raw = match.group(1)
            try:
                text = json.loads(f'"{raw}"')
            except Exception:
                text = raw
            text = _clean_text(text)
            if not text or text.startswith("CIP") or "CIP108:" in text or "@id" in text:
                continue
            if len(text) < 20 and key != "title":
                continue
            if text not in seen:
                out.append(text)
                seen.add(text)
    return out


def _action_amount(action: dict) -> str:
    raw = action.get("treasury_amount_lovelace")
    try:
        lovelace = int(raw or 0)
    except Exception:
        lovelace = 0
    if lovelace <= 0:
        return "not stated in document"
    ada = lovelace / 1_000_000
    if ada >= 1_000_000:
        return f"{ada / 1_000_000:.2f}M ADA"
    if ada >= 1_000:
        return f"{ada / 1_000:.1f}k ADA"
    return f"{ada:.0f} ADA"


def _claim_category(action: dict, text: str) -> str:
    atype = (action.get("action_type") or "").lower()
    lower = text.lower()
    if "parameter" in atype or "hardfork" in atype or any(w in lower for w in ("plutus", "protocol", "technical", "node", "infrastructure")):
        return "technical"
    if "treasury" in atype or any(w in lower for w in ("budget", "fund", "ada", "cost", "milestone")):
        return "economic"
    if any(w in lower for w in ("governance", "constitution", "committee", "drep", "vote")):
        return "governance"
    if any(w in lower for w in ("community", "adoption", "users", "ecosystem")):
        return "adoption"
    return "other"


def _claim_support(text: str, refs: int) -> str:
    lower = text.lower()
    if "audit" in lower or "report" in lower or "github" in lower or "on-chain" in lower or refs >= 3:
        return "independently_verifiable"
    if any(w in lower for w in ("will ", "expected", "aims", "intends", "believe", "should")):
        return "proposer_asserted"
    if len(text) > 120 or refs > 0:
        return "supported_in_proposal"
    return "proposer_asserted"


def _materiality(text: str) -> str:
    lower = text.lower()
    if any(w in lower for w in ("treasury", "fund", "budget", "parameter", "constitution", "committee", "hard fork", "security", "risk", "throughput", "finality", "protocol-revenue")):
        return "high"
    if any(w in lower for w in ("milestone", "deliverable", "community", "governance", "technical")):
        return "medium"
    return "low"


def _offline_extract_claims(action: dict, anchor_text: str | None) -> dict:
    base = {
        "stage": "claim_extraction",
        "available": False,
        "source": "deterministic-heuristic",
        "reason": None,
        "model": "local-deterministic",
        "request": {},
        "claims": [],
        "summary": "",
    }
    if not anchor_text:
        base["reason"] = "no cached anchor document text to read"
        return base

    obj = _anchor_json(anchor_text)
    title = action.get("metadata_title") or ""
    refs = 0
    text_blocks: list[str] = []
    if obj is not None:
        title = _first_text(obj, ["title"]) or title
        text_blocks = _all_text(obj, ["abstract", "motivation", "rationale", "description", "summary"], limit=10)
        refs = _reference_count(obj)
    if not text_blocks:
        regex_blocks = _regex_text_fields(anchor_text)
        if regex_blocks:
            if not title:
                title = regex_blocks[0]
            text_blocks = regex_blocks[1:] if len(regex_blocks) > 1 else regex_blocks
    if not text_blocks:
        text_blocks = [_readable_text_fallback(anchor_text)[:3000]]

    summary_source = " ".join(text_blocks[:2])
    summary_sentences = _sentences(summary_source, limit=2)
    summary = " ".join(summary_sentences) or f"{title or action.get('action_id')} is reviewed from its cached governance anchor."
    claim_texts: list[str] = []
    for block in text_blocks:
        claim_texts.extend(_sentences(block, limit=4))
        if len(claim_texts) >= 8:
            break
    if not claim_texts and title:
        claim_texts = [f"The proposal asks governance to consider: {title}."]

    claims = []
    seen = set()
    for claim in claim_texts:
        if claim in seen:
            continue
        seen.add(claim)
        claims.append({
            "claim": claim,
            "category": _claim_category(action, claim),
            "support": _claim_support(claim, refs),
            "materiality": _materiality(claim),
        })
        if len(claims) >= 8:
            break

    base.update(
        available=True,
        request={
            "what": title or action.get("action_type") or "not stated in document",
            "recipient": _first_text(obj, ["recipient", "beneficiary", "withdrawalRecipient"]) if obj is not None else "not stated in document",
            "amount_ada": _action_amount(action),
            "deliverables": claim_texts[:4] or ["not stated in document"],
            "deadline": action.get("expires_after_epoch") or "not stated in document",
        },
        claims=claims,
        summary=summary,
        prompt_sha256=_sha("codex-offline-review\n" + (anchor_text or "")[:60000]),
        output_sha256=_sha(json.dumps({"request": title, "claims": claims, "summary": summary}, sort_keys=True)),
    )
    return base


def _sentence(text: str) -> str:
    """One clean sentence: collapse whitespace, strip trailing periods, add one."""
    text = re.sub(r"\s+", " ", (text or "").strip()).rstrip(".")
    return f"{text}." if text else ""


def _ada_amount_label(value: str | None) -> str:
    """Normalize a claims-cache amount ('3,961,538', '0', '5.10M ADA') for prose."""
    s = (value or "").strip()
    if not s or s in ("0", "0 ADA") or s.lower().startswith("not stated"):
        return ""
    if "ada" not in s.lower():
        s += " ADA"
    return s


def _offline_human_message(action: dict, title: str, rationale: dict, assessment: dict, claims: dict | None) -> dict:
    rec = rationale.get("recommendation") or "ABSTAIN"
    reason = rationale.get("abstain_reason_code") or rationale.get("needs_more_info_reason_code")
    atype = action.get("action_type") or "governance action"
    req = (claims or {}).get("request") or {}
    claim_rows = (claims or {}).get("claims") or []
    supported = [c for c in claim_rows if c.get("support") in ("supported_in_proposal", "independently_verifiable")]
    weak = [c for c in claim_rows if c.get("support") in ("unsupported", "proposer_asserted") and c.get("materiality") != "low"]
    blockers = assessment.get("blocking_questions") or []
    # Dossier-section blockers are BEACN's own unfinished diligence, not the
    # proposal's failings; the public message must attribute them honestly.
    own_diligence = [b for b in blockers if b.startswith("missing ")]
    other_blockers = [b for b in blockers if not b.startswith("missing ")]

    opener = _sentence(f"BEACN records {rec} on {title or action.get('action_id')}")
    if rec == "YES":
        opener += " The deterministic gates found enough evidence and no decisive blocker."
    elif rec == "NO":
        opener += (" On the evidence available to BEACN's published review, the request does not "
                   "clear the bar for spending shared treasury funds.")
    elif rec == "NEEDS_MORE_INFO":
        opener += " This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record."
    else:
        opener += " This is a conservative abstention because the evidence does not justify stronger certainty."

    amount = _ada_amount_label(req.get("amount_ada")) or _ada_amount_label(_action_amount(action))
    second = f"The action is a {atype}. " + _sentence(
        f"The cached anchor describes the request as: {req.get('what') or title or 'not stated'}")
    if amount:
        second += f" It asks the treasury for {amount}."
    if supported:
        second += " " + _sentence(f"The strongest grounded claim is: {supported[0].get('claim')}")
    elif claim_rows:
        second += " " + _sentence(f"The anchor's clearest claim is: {claim_rows[0].get('claim')}")

    third_parts = []
    if weak:
        if rec == "YES":
            third_parts.append(_sentence(
                "A residual watch item: this claim remains proposer-asserted rather than "
                f"independently shown: {weak[0].get('claim')}"))
        else:
            third_parts.append(_sentence(
                f"A material claim remains proposer-asserted or thinly supported: {weak[0].get('claim')}"))
    if other_blockers:
        third_parts.append(_sentence("Open blockers: " + "; ".join(other_blockers[:3])))
    if own_diligence:
        third_parts.append(_sentence(
            "BEACN's own independent diligence is also incomplete — before this vote could move to "
            "YES, BEACN's published review still needs " +
            "; ".join(x.replace("missing ", "") for x in own_diligence[:3])))
    if reason:
        third_parts.append(f"Reason code: {reason}.")
    if not third_parts:
        third_parts.append("Residual uncertainty remains limited to the replayed evidence and the public resources cited by the run manifest.")
    third = " ".join(third_parts)

    text = "\n\n".join([opener, second, third])
    return {
        "stage": "human_message",
        "available": True,
        "source": "deterministic-heuristic",
        "reason": None,
        "model": "local-deterministic",
        "text": text,
        "prompt_sha256": _sha("codex-offline-message\n" + json.dumps({
            "action_id": action.get("action_id"),
            "recommendation": rec,
            "claims": claim_rows,
            "assessment": assessment.get("overall_status"),
        }, sort_keys=True)),
        "output_sha256": _sha(text),
    }


# --------------------------------------------------------------------------- #
# Stage 1: claim extraction
# --------------------------------------------------------------------------- #

CLAIMS_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "request": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "what": {"type": "string"},
                "recipient": {"type": "string"},
                "amount_ada": {"type": "string"},
                "deliverables": {"type": "array", "items": {"type": "string"}},
                "deadline": {"type": "string"},
            },
            "required": ["what", "recipient", "amount_ada", "deliverables", "deadline"],
        },
        "claims": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "claim": {"type": "string"},
                    "category": {
                        "type": "string",
                        "enum": ["economic", "technical", "governance", "adoption", "other"],
                    },
                    "support": {
                        "type": "string",
                        "enum": [
                            "supported_in_proposal",
                            "independently_verifiable",
                            "proposer_asserted",
                            "unsupported",
                        ],
                    },
                    "materiality": {"type": "string", "enum": ["high", "medium", "low"]},
                },
                "required": ["claim", "category", "support", "materiality"],
            },
        },
        "summary": {"type": "string"},
    },
    "required": ["request", "claims", "summary"],
}

CLAIM_SYSTEM = (
    "You are the claim-extraction stage of an autonomous Cardano DRep's review pipeline. "
    "You are given the raw text of a governance proposal's anchor document. Your ONLY job is "
    "to extract structured facts and claims from that text — you do NOT decide, recommend, or "
    "score the vote; a separate deterministic engine does that.\n"
    "Rules:\n"
    "1. Ground everything strictly in the supplied document. Do not use outside knowledge or "
    "invent specifics. If a field is not stated, set it to \"not stated in document\".\n"
    "2. For each material claim the proposer makes, classify its category and how the DOCUMENT "
    "supports it: 'supported_in_proposal' (evidence/detail given), 'independently_verifiable' "
    "(points to a checkable external/on-chain source), 'proposer_asserted' (stated without "
    "evidence), or 'unsupported' (contradicted or missing key backing).\n"
    "3. Rate materiality by how much the claim should weigh on a treasury/governance decision.\n"
    "4. Keep each claim to one sentence. Be neutral and precise. Extract 3-10 claims."
)


def _truncate(s: str, n: int) -> str:
    s = s or ""
    return s if len(s) <= n else s[:n] + " …"


def _build_claims_user(action: dict, anchor_text: str, doctrine_text: str | None = None) -> str:
    doctrine_block = ""
    if doctrine_text:
        doctrine_block = (
            "\nDREP DOCTRINE (BEACN's published standard for this action type — use it to "
            "judge which claims are material, do NOT decide the vote):\n"
            "-----8<-----\n"
            f"{_truncate(doctrine_text, 6000)}\n"
            "-----8<-----\n"
        )
    return (
        f"Action id: {action.get('action_id')}\n"
        f"Action type: {action.get('action_type')}\n"
        f"Title (from chain metadata): {action.get('metadata_title') or '(none)'}\n"
        f"Treasury amount (lovelace, if any): {action.get('treasury_amount_lovelace') or '(none)'}\n"
        f"{doctrine_block}\n"
        "ANCHOR DOCUMENT TEXT (verbatim, possibly JSON-LD):\n"
        "-----8<-----\n"
        f"{anchor_text}\n"
        "-----8<-----\n\n"
        "Extract the intake request and the claim/evidence rows as structured JSON."
    )


def extract_claims(action: dict, anchor_text: str | None, doctrine_text: str | None = None) -> dict:
    """Stage 1. Returns a dict that always has an `available` flag and, when
    available, `request`/`claims`/`summary` plus prompt/output hashes."""
    base = {
        "stage": "claim_extraction",
        "available": False,
        "source": None,
        "reason": None,
        "model": MODEL,
        "request": {},
        "claims": [],
        "summary": "",
    }
    cached = _cache().get(action.get("action_id")) or {}
    if cached.get("claims"):
        c = cached["claims"]
        payload = json.dumps(c, sort_keys=True)
        base.update(
            available=True,
            source="precomputed",
            request=c.get("request", {}) or {},
            claims=c.get("claims", []) or [],
            summary=c.get("summary", "") or "",
            output_sha256=_sha(payload),
        )
        return base
    if _offline_review_enabled():
        return _offline_extract_claims(action, anchor_text)
    if not anchor_text:
        base["reason"] = "no cached anchor document text to read"
        return base
    client = _client()
    if client is None:
        base["reason"] = "model layer unavailable (no ANTHROPIC_API_KEY / anthropic SDK, or disabled)"
        return base

    user = _build_claims_user(action, anchor_text, doctrine_text)
    try:
        resp = client.messages.create(
            model=MODEL,
            max_tokens=4000,
            system=CLAIM_SYSTEM,
            messages=[{"role": "user", "content": user}],
            output_config={"format": {"type": "json_schema", "schema": CLAIMS_SCHEMA}},
        )
    except Exception as e:  # noqa: BLE001 - degrade, never crash the pipeline
        base["reason"] = f"extraction call failed: {e}"
        return base
    if getattr(resp, "stop_reason", None) == "refusal":
        base["reason"] = "model refused extraction"
        return base

    text = _text_of(resp)
    try:
        data = json.loads(text)
    except Exception as e:  # noqa: BLE001
        base["reason"] = f"unparseable extraction output: {e}"
        return base

    base.update(
        available=True,
        source="model",
        request=data.get("request", {}) or {},
        claims=data.get("claims", []) or [],
        summary=data.get("summary", "") or "",
        prompt_sha256=_sha(CLAIM_SYSTEM + "\n" + user),
        output_sha256=_sha(text),
    )
    return base


# --------------------------------------------------------------------------- #
# Stage 1.5: bounded doctrine-aware lean (the one place the LLM touches the vote)
# --------------------------------------------------------------------------- #

def _cap() -> float:
    try:
        return abs(float(os.environ.get("BEACN_LLM_SCORE_ADJUST_CAP", "0.05")))
    except Exception:
        return 0.05


def _clamp_adj(value) -> float:
    cap = _cap()
    try:
        v = float(value or 0.0)
    except Exception:
        v = 0.0
    return max(-cap, min(cap, v))


def _direction_for(adj: float) -> str:
    if adj > 0.005:
        return "YES"
    if adj < -0.005:
        return "NO"
    return "NEUTRAL"


LEAN_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "direction": {"type": "string", "enum": ["YES", "NO", "ABSTAIN", "NEUTRAL"]},
        "score_adjustment": {"type": "number"},
        "confidence": {"type": "number"},
        "rationale": {"type": "string"},
        "doctrine_basis": {"type": "string"},
    },
    "required": ["direction", "score_adjustment", "confidence", "rationale", "doctrine_basis"],
}


def _lean_system() -> str:
    cap = _cap()
    return (
        "You are the bounded reasoning step of an autonomous Cardano DRep that votes real "
        "treasury money. A deterministic engine has ALREADY enforced every hard safety gate "
        "(stale data, missing evidence, treasury-needs-dossier, hard blockers, high risk flags) "
        "and computed a numeric score. Those gates are binding and you cannot override them.\n"
        "Your ONLY job: judge whether the evidence quality and the proposal's alignment with "
        "BEACN's published DOCTRINE justify a SMALL nudge to that score, in either direction, "
        "that the mechanical rules did not already capture.\n"
        "Rules:\n"
        f"1. score_adjustment must be a number within [-{cap}, {cap}]. Positive = lean YES, "
        "negative = lean NO. Use 0 when the rules already captured everything.\n"
        "2. Be conservative. The values hierarchy is: protocol safety > treasury stewardship > "
        "evidence quality/reproducibility > public-benefit growth > speed. When in doubt, nudge "
        "toward caution (0 or negative), never toward spending.\n"
        "3. Ground the rationale ONLY in the supplied claims, assessment, and doctrine. Invent "
        "no facts. Name the doctrine principle you relied on in doctrine_basis.\n"
        "4. You are advisory and clamped; the engine records and limits your adjustment."
    )


def _assessment_digest(assessment: dict | None) -> str:
    a = assessment or {}
    lines = [f"overall_status: {a.get('overall_status', 'unknown')}"]
    for s in a.get("sections", []) or []:
        lines.append(f"- {s.get('title')}: {s.get('status')}")
    blockers = a.get("blocking_questions") or []
    if blockers:
        lines.append("blocking_questions: " + "; ".join(blockers[:6]))
    return "\n".join(lines)


def _offline_assess_lean(action: dict, claims: dict | None, assessment: dict | None,
                         doctrine_text: str | None, family: str) -> dict:
    """Deterministic, doctrine-aware lean for offline runs. Pure function of its
    inputs, so replay stays clean. Mirrors the live model's conservative posture."""
    rows = (claims.get("claims") if (claims and claims.get("available")) else None) or []
    strong = [c for c in rows if c.get("support") in ("supported_in_proposal", "independently_verifiable")]
    weak = [c for c in rows if c.get("support") in ("unsupported", "proposer_asserted") and c.get("materiality") == "high"]
    blockers = (assessment or {}).get("blocking_questions") or []
    status = (assessment or {}).get("overall_status", "unknown")

    adj = 0.0
    notes = []
    if strong:
        adj += 0.02 * min(len(strong), 2)
        notes.append(f"{len(strong)} well-supported claim(s)")
    if weak:
        adj -= 0.025 * min(len(weak), 2)
        notes.append(f"{len(weak)} unsupported high-materiality claim(s)")
    if status == "ready":
        adj += 0.01
    elif status == "blocked":
        adj -= 0.03
        notes.append("assessment blocked")
    elif status in ("incomplete", "thin"):
        adj -= 0.01
    if blockers:
        adj -= 0.01
        notes.append(f"{len(blockers)} open blocker(s)")
    # Doctrine caution: high-scrutiny action families bias toward restraint.
    if family in ("hardfork", "constitution", "parameter", "committee", "treasury"):
        adj -= 0.01
        notes.append(f"{family} doctrine demands elevated scrutiny")

    adj = _clamp_adj(adj)
    direction = _direction_for(adj)
    confidence = max(0.3, min(0.85, 0.5 + 0.08 * len(strong) - 0.05 * len(weak)))
    basis = "values hierarchy: protocol safety & treasury stewardship over speed"
    if doctrine_text:
        first = next((ln.strip("# ").strip() for ln in doctrine_text.splitlines() if ln.strip()), "")
        if first:
            basis = f"{first}; " + basis
    rationale = (
        f"Doctrine-aware offline lean for a {family or 'governance'} action: "
        + (", ".join(notes) if notes else "no decisive evidence or doctrine signal")
        + f". Net bounded adjustment {adj:+.3f} (clamped to ±{_cap()})."
    )
    payload = {"direction": direction, "score_adjustment": adj, "confidence": round(confidence, 3),
               "rationale": rationale, "doctrine_basis": basis}
    return {
        "stage": "assess_lean",
        "available": True,
        "source": "deterministic-heuristic",
        "model": "local-deterministic",
        "reason": None,
        **payload,
        "score_adjustment": adj,
        "prompt_sha256": _sha("codex-offline-lean\n" + json.dumps({
            "action_id": action.get("action_id"), "family": family,
            "claims": rows, "status": status, "blockers": blockers,
        }, sort_keys=True)),
        "output_sha256": _sha(json.dumps(payload, sort_keys=True)),
    }


def assess_lean(action: dict, claims: dict | None, assessment: dict | None,
                doctrine_text: str | None, family: str) -> dict:
    """Stage 1.5. Returns {available, direction, score_adjustment (clamped), confidence,
    rationale, doctrine_basis, hashes}. The engine clamps score_adjustment again and is
    the binding authority; this only proposes a bounded nudge."""
    base = {
        "stage": "assess_lean", "available": False, "source": None, "reason": None,
        "model": MODEL, "direction": "NEUTRAL", "score_adjustment": 0.0,
        "confidence": 0.0, "rationale": "", "doctrine_basis": "",
    }
    cached = _cache().get(action.get("action_id")) or {}
    if isinstance(cached.get("lean"), dict):
        c = cached["lean"]
        adj = _clamp_adj(c.get("score_adjustment"))
        base.update(available=True, source="precomputed", score_adjustment=adj,
                    direction=c.get("direction") or _direction_for(adj),
                    confidence=float(c.get("confidence") or 0.0),
                    rationale=c.get("rationale") or "", doctrine_basis=c.get("doctrine_basis") or "",
                    output_sha256=_sha(json.dumps(c, sort_keys=True)))
        return base
    if _offline_review_enabled():
        return _offline_assess_lean(action, claims, assessment, doctrine_text, family)
    client = _client()
    if client is None:
        base["reason"] = "model layer unavailable (no ANTHROPIC_API_KEY / anthropic SDK, or disabled)"
        return base

    user = (
        f"Action id: {action.get('action_id')}\n"
        f"Action type: {action.get('action_type')}  (family: {family})\n"
        f"Title: {action.get('metadata_title') or '(none)'}\n"
        f"Treasury amount (lovelace, if any): {action.get('treasury_amount_lovelace') or '(none)'}\n\n"
        f"DOCTRINE for this action type:\n-----8<-----\n{_truncate(doctrine_text or '(none on file)', 6000)}\n-----8<-----\n\n"
        f"Extracted proposal claims:\n{_claims_block(claims)}\n\n"
        f"Deterministic assessment tree:\n{_assessment_digest(assessment)}\n\n"
        f"Give your bounded score_adjustment within [-{_cap()}, {_cap()}] and the doctrine-grounded rationale."
    )
    try:
        resp = client.messages.create(
            model=MODEL,
            max_tokens=1500,
            system=_lean_system(),
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": user}],
            output_config={"format": {"type": "json_schema", "schema": LEAN_SCHEMA}},
        )
    except Exception as e:  # noqa: BLE001 - degrade, never crash the pipeline
        base["reason"] = f"lean call failed: {e}"
        return base
    if getattr(resp, "stop_reason", None) == "refusal":
        base["reason"] = "model refused the lean"
        return base
    text = _text_of(resp)
    try:
        data = json.loads(text)
    except Exception as e:  # noqa: BLE001
        base["reason"] = f"unparseable lean output: {e}"
        return base

    adj = _clamp_adj(data.get("score_adjustment"))
    base.update(
        available=True, source="model", score_adjustment=adj,
        direction=data.get("direction") or _direction_for(adj),
        confidence=float(data.get("confidence") or 0.0),
        rationale=data.get("rationale") or "", doctrine_basis=data.get("doctrine_basis") or "",
        prompt_sha256=_sha(_lean_system() + "\n" + user), output_sha256=_sha(text),
    )
    return base


# --------------------------------------------------------------------------- #
# Stage 6: human-readable message
# --------------------------------------------------------------------------- #

MESSAGE_SYSTEM = (
    "You write the public, plain-English explanation of how the BEACN autonomous Cardano DRep "
    "voted on a governance action, for delegators to read on a transparency site. You are given "
    "BEACN's DETERMINISTIC verdict and the structured review that produced it. Your job is to "
    "EXPLAIN that verdict faithfully — never to change it, second-guess it, or add facts that "
    "were not provided.\n"
    "Rules:\n"
    "1. Open with the decision and the single most important reason for it.\n"
    "2. Then give the supporting facts: what was requested, what the proposer claimed, which "
    "claims were well-supported vs unsupported, and which review gates passed or failed.\n"
    "3. If the vote is ABSTAIN or NEEDS_MORE_INFO, state plainly that it is a conservative, "
    "evidence-based hold and name the specific evidence that would unblock a directional vote.\n"
    "4. Use ONLY the supplied data. Invent nothing. Critique the proposal, never people.\n"
    "5. Plain prose for a non-technical delegator: 2-4 short paragraphs, no markdown headings or "
    "bullet lists, no preamble. Be clear over clever; lead with the outcome."
)


def _claims_block(claims: dict | None) -> str:
    if not claims or not claims.get("available"):
        reason = (claims or {}).get("reason") or "not available"
        return f"(proposal claims not extracted — {reason})"
    req = claims.get("request") or {}
    lines = [
        f"Requested: {req.get('what', 'n/a')}",
        f"Recipient: {req.get('recipient', 'n/a')}",
        f"Amount: {req.get('amount_ada', 'n/a')}",
        f"Deliverables: {', '.join(req.get('deliverables') or []) or 'n/a'}",
        f"Deadline: {req.get('deadline', 'n/a')}",
        "Claims:",
    ]
    for c in (claims.get("claims") or [])[:10]:
        lines.append(
            f"  - [{c.get('category')}/{c.get('support')}/{c.get('materiality')}] {c.get('claim')}"
        )
    return "\n".join(lines)


def _build_message_user(action: dict, title: str, rationale: dict, assessment: dict, claims: dict | None) -> str:
    def lines(key):
        items = [x for x in (rationale.get(key) or []) if x]
        return "\n".join(f"- {x}" for x in items) or "- (none)"

    reason = rationale.get("abstain_reason_code") or rationale.get("needs_more_info_reason_code") or "n/a"
    blockers = assessment.get("blocking_questions") or []
    counter = ""
    for s in assessment.get("sections", []):
        if s.get("title") == "Counterargument pass":
            counter = "\n".join(f"- {f}" for f in s.get("findings", []))
            break

    return (
        f"Governance action: {title or action.get('action_id')}\n"
        f"Action type: {rationale.get('action_type')}\n"
        f"BEACN's deterministic verdict: {rationale.get('recommendation')}\n"
        f"Reason code: {reason}\n"
        f"Score: {rationale.get('score')}   Confidence: {rationale.get('confidence')}   "
        f"Readiness: {rationale.get('readiness_score')}\n\n"
        f"Proposal intake & claims:\n{_claims_block(claims)}\n\n"
        f"Facts that drove the verdict:\n{lines('facts')}\n\n"
        f"Inferences:\n{lines('inferences')}\n\n"
        f"Residual uncertainty:\n{lines('uncertainty')}\n\n"
        f"Decisive blockers / open questions:\n" + ("\n".join(f"- {b}" for b in blockers) or "- (none)") + "\n\n"
        f"Counterargument pass:\n{counter or '- (none)'}\n\n"
        f"Write the public explanation of why BEACN voted {rationale.get('recommendation')} on this action."
    )


def message_matches_recommendation(text: str, recommendation: str) -> bool:
    """Does a cached plain-language message describe the CURRENT verdict?

    Cached messages are written once and can outlive a recommendation flip
    (e.g. an ABSTAIN-era explanation glued onto a later NO vote — seen live on
    the Tweag withdrawal 2026-07-01). We look at the verdict the opening of the
    message names; if it names a different one, the cache entry is stale."""
    rec = (recommendation or "").upper().replace(" ", "_")
    head = (text or "")[:240].upper()
    m = re.search(r"\b(ABSTAIN(?:ING|S)?|NEEDS[ _]MORE[ _]INFO|YES|NO)\b", head)
    if not m:
        return True  # can't tell — leave legacy behaviour alone
    named = m.group(1).replace(" ", "_")
    if named.startswith("ABSTAIN"):
        named = "ABSTAIN"
    return named == rec


def write_human_message(action: dict, title: str, rationale: dict, assessment: dict, claims: dict | None) -> dict:
    """Stage 6. Returns {available, text, reason, model, hashes}. Non-authoritative:
    it explains `rationale['recommendation']`, which is already fixed."""
    base = {"stage": "human_message", "available": False, "source": None, "reason": None, "model": MODEL, "text": ""}
    cached = _cache().get(action.get("action_id")) or {}
    if cached.get("message"):
        text = cached["message"]
        if message_matches_recommendation(text, rationale.get("recommendation")):
            base.update(available=True, source="precomputed", text=text, output_sha256=_sha(text))
            return base
        # Stale cache: the message explains a different verdict than the one
        # being published. Fall through and regenerate instead of contradicting
        # the on-chain vote on the public site.
    if _offline_review_enabled():
        return _offline_human_message(action, title, rationale, assessment, claims)
    client = _client()
    if client is None:
        base["reason"] = "model layer unavailable (no ANTHROPIC_API_KEY / anthropic SDK, or disabled)"
        return base

    user = _build_message_user(action, title, rationale, assessment, claims)
    try:
        resp = client.messages.create(
            model=MODEL,
            max_tokens=1200,
            system=MESSAGE_SYSTEM,
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": user}],
        )
    except Exception as e:  # noqa: BLE001
        base["reason"] = f"message call failed: {e}"
        return base
    if getattr(resp, "stop_reason", None) == "refusal":
        base["reason"] = "model refused to write the message"
        return base

    text = _text_of(resp)
    if not text:
        base["reason"] = "model returned an empty message"
        return base

    base.update(
        available=True,
        source="model",
        text=text,
        prompt_sha256=_sha(MESSAGE_SYSTEM + "\n" + user),
        output_sha256=_sha(text),
    )
    return base
