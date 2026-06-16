"""Claude reasoning layer for the BEACN DRep pipeline — the two stages that need
real language understanding. Both are NON-AUTHORITATIVE over the vote.

  Stage 1 — extract_claims(): read the proposal's cached anchor document and
    extract structured intake facts + claim rows (economic / technical /
    governance / adoption), each tagged by how well the document supports it.
    This feeds the assessment's evidence table and the human message. It never
    feeds a gate and cannot change the recommendation.

  Stage 6 — write_human_message(): turn the *already-decided* deterministic
    assessment + score + recommendation into a plain-English explanation of the
    facts behind the decision. It explains the vote; it cannot alter it.

Determinism contract: the directional vote (engine gates + score) is pure
deterministic Python and is the binding record. This module only adds advisory
claim context and explanatory prose, and records prompt/output hashes so a run
is auditable. With no ANTHROPIC_API_KEY, no `anthropic` SDK, or
BEACN_DREP_DISABLE_LLM set, both functions return an `available: False` sentinel
and the pipeline proceeds exactly as the deterministic engine always did.

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
        "source": "codex-offline-review",
        "reason": None,
        "model": "codex-offline-local",
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


def _offline_human_message(action: dict, title: str, rationale: dict, assessment: dict, claims: dict | None) -> dict:
    rec = rationale.get("recommendation") or "ABSTAIN"
    reason = rationale.get("abstain_reason_code") or rationale.get("needs_more_info_reason_code")
    atype = action.get("action_type") or "governance action"
    req = (claims or {}).get("request") or {}
    claim_rows = (claims or {}).get("claims") or []
    supported = [c for c in claim_rows if c.get("support") in ("supported_in_proposal", "independently_verifiable")]
    weak = [c for c in claim_rows if c.get("support") in ("unsupported", "proposer_asserted") and c.get("materiality") != "low"]
    blockers = assessment.get("blocking_questions") or []

    opener = f"BEACN records {rec} on {title or action.get('action_id')}."
    if rec == "YES":
        opener += " The deterministic gates found enough evidence and no decisive blocker."
    elif rec == "NO":
        opener += " The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented."
    elif rec == "NEEDS_MORE_INFO":
        opener += " This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record."
    else:
        opener += " This is a conservative abstention because the evidence does not justify stronger certainty."

    amount = req.get("amount_ada") or _action_amount(action)
    second = f"The action is a {atype}. The cached anchor describes the request as: {req.get('what') or title or 'not stated'}."
    if amount and amount != "not stated in document":
        second += f" The recorded treasury amount is {amount}."
    if supported:
        second += f" The strongest grounded claim is: {supported[0].get('claim')}"
    elif claim_rows:
        second += f" The anchor's clearest claim is: {claim_rows[0].get('claim')}"

    third_parts = []
    if weak:
        third_parts.append(f"A material weak point is that this claim remains proposer-asserted or thinly supported: {weak[0].get('claim')}")
    if blockers:
        third_parts.append("The blocking questions are: " + "; ".join(blockers[:3]) + ".")
    if reason:
        third_parts.append(f"Reason code: {reason}.")
    if not third_parts:
        third_parts.append("Residual uncertainty remains limited to the replayed evidence and the public resources cited by the run manifest.")
    third = " ".join(third_parts)

    text = "\n\n".join([opener, second, third])
    return {
        "stage": "human_message",
        "available": True,
        "source": "codex-offline-review",
        "reason": None,
        "model": "codex-offline-local",
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


def _build_claims_user(action: dict, anchor_text: str) -> str:
    return (
        f"Action id: {action.get('action_id')}\n"
        f"Action type: {action.get('action_type')}\n"
        f"Title (from chain metadata): {action.get('metadata_title') or '(none)'}\n"
        f"Treasury amount (lovelace, if any): {action.get('treasury_amount_lovelace') or '(none)'}\n\n"
        "ANCHOR DOCUMENT TEXT (verbatim, possibly JSON-LD):\n"
        "-----8<-----\n"
        f"{anchor_text}\n"
        "-----8<-----\n\n"
        "Extract the intake request and the claim/evidence rows as structured JSON."
    )


def extract_claims(action: dict, anchor_text: str | None) -> dict:
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

    user = _build_claims_user(action, anchor_text)
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


def write_human_message(action: dict, title: str, rationale: dict, assessment: dict, claims: dict | None) -> dict:
    """Stage 6. Returns {available, text, reason, model, hashes}. Non-authoritative:
    it explains `rationale['recommendation']`, which is already fixed."""
    base = {"stage": "human_message", "available": False, "source": None, "reason": None, "model": MODEL, "text": ""}
    cached = _cache().get(action.get("action_id")) or {}
    if cached.get("message"):
        text = cached["message"]
        base.update(available=True, source="precomputed", text=text, output_sha256=_sha(text))
        return base
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
