#!/usr/bin/env python3
"""Build the public JSON artifact bundle for beacn-drep-web consumption."""
import csv
import glob
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime, timezone

from ..config import CORE_REPO, SOUL_REPO, RESOURCES_REPO
from ..ids import canonical_action_id
from ..vote_snapshots import load_snapshots, latest_snapshot

OUT = CORE_REPO / "data" / "output" / "public"
RUNS = CORE_REPO / "data" / "output"
ACTIONS_CSV = RESOURCES_REPO / "data" / "input" / "governance" / "governance_actions_all.csv"
ANCHOR_INDEX_CSV = RESOURCES_REPO / "data" / "input" / "governance" / "anchor_documents_index.csv"
FLAGS_CSV = RESOURCES_REPO / "data" / "input" / "governance" / "governance_action_flags.csv"
POLICY_STATE = RESOURCES_REPO / "data" / "input" / "governance" / "treasury_policy_state.json"
PORTFOLIO = RESOURCES_REPO / "data" / "input" / "governance" / "treasury_portfolio.json"
DEEP_CSV = RESOURCES_REPO / "data" / "input" / "governance" / "decision_support" / "deep_research_dossiers.csv"
DOSSIER_DIR = RESOURCES_REPO / "data" / "input" / "governance" / "decision_support" / "dossiers"
_DOSSIER_SECTIONS = ("proposal_summary", "budget_analysis", "feasibility_assessment",
                     "risk_analysis", "alternatives_analysis", "failure_mode_analysis",
                     "community_impact")


def _git_commit(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def _load_actions_map():
    """Action rows keyed by CANONICAL id, so a row filed under either id spelling is found.

    Rows also stay reachable under their original id (harmless aliases) -- the canonical key
    is what the export loop looks up.
    """
    out = {}
    with ACTIONS_CSV.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            raw = r["action_id"]
            out[raw] = r
            key = canonical_action_id(raw)
            prev = out.get(key)
            # Prefer the richer row (a title present) if the same action appears twice.
            if not prev or (not prev.get("metadata_title") and r.get("metadata_title")):
                out[key] = r
    return out


def _load_deep_research_map():
    out = {}
    if not DEEP_CSV.exists():
        return out
    with DEEP_CSV.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out[r.get("action_id", "")] = r
    return out


def _deep_research_block(aid: str, deep_row: dict | None) -> dict | None:
    """Publish the diligence dossier + its verification attestation so the human
    role in the fully-agentic workflow — random spot-checks — is possible from
    the website alone."""
    if not deep_row:
        return None
    dossier_md = DOSSIER_DIR / f"{aid}.md"
    receipt_path = DOSSIER_DIR / f"{aid}.receipt.json"
    block = {
        "status": deep_row.get("status", ""),
        "dossier_complete": deep_row.get("dossier_complete", ""),
        "sections_grounded": sum(
            1 for s in _DOSSIER_SECTIONS if deep_row.get(f"{s}_complete") == "yes"),
        "sections_total": len(_DOSSIER_SECTIONS),
        "owner": deep_row.get("owner", ""),
    }
    if dossier_md.exists():
        out_dir = OUT / "dossiers"
        out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(dossier_md, out_dir / dossier_md.name)
        block["dossier_path"] = f"/data/output/public/dossiers/{dossier_md.name}"
    if receipt_path.exists():
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        out_dir = OUT / "dossiers"
        out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(receipt_path, out_dir / receipt_path.name)
        block["receipt_path"] = f"/data/output/public/dossiers/{receipt_path.name}"
        verification = receipt.get("verification") or {}
        if verification:
            block["verification"] = {
                "passed": verification.get("passed"),
                "verified_at_utc": verification.get("verified_at_utc"),
                "model": verification.get("model"),
                "fact_count": verification.get("fact_count"),
                "supported": verification.get("supported"),
                "support_ratio": verification.get("support_ratio"),
                "material_discrepancies": len(verification.get("material_discrepancies") or []),
            }
    return block


def _load_anchor_index_map():
    out = {}
    if not ANCHOR_INDEX_CSV.exists():
        return out
    with ANCHOR_INDEX_CSV.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            aid = r.get("action_id", "")
            if aid:
                out[aid] = r
    return out


def _proposal_ext(content_type: str) -> str:
    c = (content_type or "").lower()
    if "json" in c:
        return ".json"
    if "pdf" in c:
        return ".pdf"
    if "html" in c:
        return ".html"
    if "text" in c:
        return ".txt"
    return ".bin"


def _anchor_fetch_stats(anchor_map: dict[str, dict]) -> dict:
    rows = list(anchor_map.values())
    total = len(rows)
    if total == 0:
        return {
            "total": 0,
            "ok": 0,
            "ok_cached": 0,
            "failed": 0,
            "coverage_pct": 0.0,
            "failure_buckets": {},
        }

    ok = sum(1 for r in rows if (r.get("fetch_status") or "") in ("ok", "ok_cached"))
    ok_cached = sum(1 for r in rows if (r.get("fetch_status") or "") == "ok_cached")

    failures: dict[str, int] = {}
    for r in rows:
        st = (r.get("fetch_status") or "").strip() or "unknown"
        if st in ("ok", "ok_cached"):
            continue
        code = (r.get("http_status") or "").strip()
        key = f"{st}:{code}" if code else st
        failures[key] = failures.get(key, 0) + 1

    failed = total - ok
    return {
        "total": total,
        "ok": ok,
        "ok_cached": ok_cached,
        "failed": failed,
        "coverage_pct": round((ok / total) * 100.0, 2),
        "failure_buckets": dict(sorted(failures.items(), key=lambda kv: kv[1], reverse=True)),
    }


def _copy_proposal_snapshot(aid: str, anchor_row: dict) -> dict:
    if not anchor_row:
        return {"available": False, "reason": "no_anchor_index_row"}

    fetch_status = anchor_row.get("fetch_status", "")
    rel_path = anchor_row.get("file_path", "")
    if fetch_status not in ("ok", "ok_cached") or not rel_path:
        return {
            "available": False,
            "fetch_status": fetch_status,
            "reason": anchor_row.get("error") or "anchor_not_fetched",
        }

    src = RESOURCES_REPO / rel_path
    if not src.exists():
        return {"available": False, "fetch_status": fetch_status, "reason": "pinned_file_missing"}

    proposal_dir = OUT / "proposals"
    proposal_dir.mkdir(parents=True, exist_ok=True)
    ext = _proposal_ext(anchor_row.get("content_type", ""))
    dst_name = f"{aid}{ext}"
    dst = proposal_dir / dst_name
    shutil.copyfile(src, dst)

    preview = ""
    if ext in (".json", ".txt", ".html"):
        try:
            txt = src.read_text(encoding="utf-8", errors="replace")
            preview = txt[:1200]
        except Exception:
            preview = ""

    return {
        "available": True,
        "fetch_status": fetch_status,
        "content_type": anchor_row.get("content_type", ""),
        "http_status": anchor_row.get("http_status", ""),
        "source_anchor_url": anchor_row.get("anchor_url", ""),
        "anchor_hash": anchor_row.get("anchor_hash", ""),
        "file_sha256": anchor_row.get("file_sha256", ""),
        "content_bytes": anchor_row.get("content_bytes", ""),
        "fetched_at_utc": anchor_row.get("fetched_at_utc", ""),
        "download_path": f"/proposals/{dst_name}",
        "preview": preview,
    }


def _to_int(v) -> int:
    try:
        return int(float(str(v).strip()))
    except (TypeError, ValueError):
        return 0


def _load_onchain_anchors() -> dict[str, dict]:
    """The anchor hash the CHAIN records for each vote BEACN cast.

    This is the ONLY hash the public verifier may check a published rationale against. The local
    run's `rationale_anchor_hash` is recomputed every time the engine re-scores on fresh evidence,
    so checking against it would compare a file to its own hash — a check that always passes and
    proves nothing. The chain's copy is immutable and beyond our reach to revise, which is exactly
    what makes it worth anything.
    """
    path = RESOURCES_REPO / "data" / "input" / "governance" / "onchain_vote_anchors.json"
    if not path.exists():
        return {}
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for aid, row in (raw.get("anchors") or {}).items():
        out[canonical_action_id(aid)] = row
    return out


def _proof_of_vote_block(frozen: dict | None, current_eval: dict, onchain_anchor: dict | None) -> dict:
    """The vote-time truth for a cast vote, taken from the frozen submission snapshot.

    Before this existed, proof_of_vote republished the LATEST engine run, so every re-score
    quietly rewrote the score/confidence/hashes shown as evidence of a vote cast weeks earlier.
    A frozen snapshot is written once by the live-vote path and never recomputed; `reconstructed`
    marks the historic entries rebuilt from chain anchors + receipts rather than written live.
    """
    # The anchor the CHAIN records for the vote actually cast. Immutable, beyond BEACN's
    # reach to revise, and therefore the only hash a public verifier should trust. The
    # rationale it commits to is still served, byte-for-byte, at /r/<hash[:24]>.md.
    chain_fields = {
        "onchain_anchor_hash": (onchain_anchor or {}).get("anchor_hash"),
        "onchain_anchor_url": (onchain_anchor or {}).get("anchor_url"),
        "onchain_vote": (onchain_anchor or {}).get("vote"),
    }
    if not frozen:
        return {**current_eval, "frozen": False, **chain_fields}
    anchor_hash = frozen.get("rationale_anchor_hash")
    return {
        "frozen": True,
        "reconstructed": bool(frozen.get("reconstructed")),
        "vote": frozen.get("vote"),
        "recommendation": frozen.get("recommendation"),
        "score": frozen.get("score"),
        "confidence": frozen.get("confidence"),
        "transaction_hash": frozen.get("tx_hash"),
        "submitted_at": frozen.get("submitted_at"),
        "run_id": frozen.get("run_id"),
        "input_hash": frozen.get("input_hash"),
        "snapshot_bundle_hash": frozen.get("snapshot_bundle_hash"),
        "soul_commit": frozen.get("soul_commit"),
        "resources_commit": frozen.get("resources_commit"),
        "rationale_anchor_hash": anchor_hash,
        "rationale_markdown_path": f"/data/output/public/r/{anchor_hash[:24]}.md" if anchor_hash else None,
        **chain_fields,
    }


def _load_flags_map() -> dict[str, list[dict]]:
    """Per-action risk flags. These are WHY a proposal drew scrutiny, and the public record was
    hiding all 169 of them — including 6 RED (NO_METADATA, HASH_MISMATCH). A reader asking
    "why didn't this pass?" deserves to see them."""
    out: dict[str, list[dict]] = {}
    if not FLAGS_CSV.exists():
        return out
    with FLAGS_CSV.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            key = canonical_action_id(r.get("action_id", ""))
            if not key:
                continue
            out.setdefault(key, []).append({
                "flag": (r.get("flag") or "").strip(),
                "severity": (r.get("severity") or "").strip(),
                "detail": (r.get("detail") or "").strip(),
            })
    return out


def _load_treasury_capacity() -> dict:
    """The Net Change Limit and what is left of it — published so anyone can check the arithmetic.

    This is the single hardest gate a treasury proposal faces, so the public must be able to see
    the number, where it came from, and the honest caveat that no NCL is ever formally enacted.
    """
    try:
        policy = json.loads(POLICY_STATE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    try:
        portfolio = json.loads(PORTFOLIO.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        portfolio = {}
    ncl = policy.get("ncl_lovelace")
    if not ncl:
        return {
            "verified": False,
            "why": "No Net Change Limit is currently pinned from chain evidence, so BEACN will not "
                   "vote directionally on any treasury withdrawal.",
        }
    spent = policy.get("withdrawals_in_period_lovelace") or 0
    return {
        "verified": True,
        "ncl_lovelace": ncl,
        "period_start_epoch": policy.get("period_start_epoch"),
        "period_end_epoch": policy.get("period_end_epoch"),
        "withdrawals_in_period_lovelace": spent,
        "remaining_capacity_lovelace": policy.get("remaining_capacity_lovelace",
                                                  max(0, int(ncl) - int(spent))),
        "spend_basis": policy.get("spend_basis"),
        "source_action_id": policy.get("source_action_id"),
        "source_anchor_hash": policy.get("source_anchor_hash"),
        "drep_support": policy.get("drep_support"),
        "verification_status": policy.get("verification_status"),
        "caveat": policy.get("caveat"),
        "portfolio_status": portfolio.get("status"),
    }


def _resolve_vote_receipt(action_id: str, latest_run_dir: Path) -> dict:
    """Find the submitted vote receipt for an action, across ALL of its run dirs.

    A vote is a fact about an *action*, not about one run. Run dirs are named
    `<action_id>-<input_hash12>`, so any change to the inputs mints a NEW dir — while the
    receipt stays behind in the dir that existed when the vote was actually cast. Reading
    only the latest run dir therefore found a receipt for 0 of 31 voted actions, which is
    why the public site published `transaction_hash: null` everywhere and `votes_cast: 0`
    despite 31 real on-chain votes.

    Prefer the most recently submitted receipt; fall back to the newest receipt present.
    """
    want = canonical_action_id(action_id)
    candidates: list[dict] = []
    for receipt_path in RUNS.glob("*/vote_receipt.json"):
        try:
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        got = receipt.get("action_id")
        # Match on the CANONICAL id: the vote may have been cast under the other id
        # spelling than the one this decision is filed under. Never attribute another
        # action's vote to this one.
        if not got or canonical_action_id(got) != want:
            continue
        receipt["_mtime"] = receipt_path.stat().st_mtime
        candidates.append(receipt)

    if not candidates:
        legacy = latest_run_dir / "vote_receipt.json"
        if legacy.exists():
            try:
                return json.loads(legacy.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                return {}
        return {}

    submitted = [c for c in candidates if c.get("submitted")]
    pool = submitted or candidates
    best = max(pool, key=lambda c: (c.get("submitted_at") or "", c["_mtime"]))
    best.pop("_mtime", None)
    return best


def _load_rationales_latest():
    """Latest decision per action, keyed by CANONICAL action id.

    Keying by the raw action_id published the same action twice (once per id spelling) and
    could show two different verdicts for it. Keying by canonical id means the most recent
    run wins regardless of which spelling produced it -- one action, one current position.
    """
    by_action = {}
    for d in RUNS.iterdir():
        if not d.is_dir() or d.name == "public":
            continue
        p = d / "rationale.json"
        if not p.exists():
            continue
        j = json.loads(p.read_text())
        aid = j.get("action_id")
        if not aid:
            continue
        key = canonical_action_id(aid)
        mtime_ns = p.stat().st_mtime_ns
        prev = by_action.get(key)
        if not prev or mtime_ns > prev["mtime_ns"]:
            by_action[key] = {
                "run_id": d.name,
                "run_dir": d,
                "mtime_ns": mtime_ns,
                "rationale": j,
                "source_action_id": aid,
                "md_path": f"/data/output/public/rationales/{d.name}.md",
            }
    return by_action


def _assessment_extract(r: dict) -> dict:
    """Pull the decisive material out of the review tree: the counterargument
    pass, blocking questions, and the specific per-section missing items. This
    is what makes the public summary say WHY, not just quote a generic fact."""
    a = r.get("assessment") or {}
    out = {
        "strongest_yes": "", "strongest_no": "", "strongest_hold": "",
        "blocking": [str(b) for b in (a.get("blocking_questions") or [])],
        "specific_missing": [],
    }
    for s in a.get("sections") or []:
        title = s.get("title") or ""
        if title == "Counterargument pass":
            for f in s.get("findings") or []:
                for key, label in (("strongest_yes", "Strongest YES:"),
                                   ("strongest_no", "Strongest NO:"),
                                   ("strongest_hold", "Strongest hold:")):
                    if str(f).startswith(label):
                        out[key] = str(f)[len(label):].strip()
        elif title != "Synthesis":  # Synthesis repeats the blocking questions
            for m in s.get("missing") or []:
                m = str(m)
                if m not in out["specific_missing"]:
                    out["specific_missing"].append(m)
    return out


def _fix_phrase(m: str) -> str:
    """Turn a raw missing-item into an actionable ask for the proposer."""
    m = m.strip().rstrip(".")
    low = m.lower()
    if low.startswith("independent evidence for"):
        return f"Provide {m[0].lower()}{m[1:]}."
    if low.startswith(("missing ", "provide ", "add ", "include ", "document ", "show ", "publish ")):
        return (m[8].upper() + m[9:] + "." if low.startswith("missing ") else m + ".")
    return f"Provide {m}."


def _top_fixes(action_row: dict, r: dict) -> list[str]:
    fixes: list[str] = []
    action_type = (action_row.get("action_type") or r.get("action_type") or "").lower()

    # Direct missing-evidence-driven fixes first.
    for m in (r.get("missing_evidence") or []):
        if len(fixes) >= 3:
            break
        fixes.append(f"Provide: {m}")

    # Then the proposal-specific gaps found by the review tree — these are the
    # real "what would change this vote" items, ahead of any generic template.
    for m in _assessment_extract(r)["specific_missing"]:
        if len(fixes) >= 3:
            break
        phrased = _fix_phrase(m)
        if phrased not in fixes and len(phrased) <= 170:
            fixes.append(phrased)

    facts = " ".join((r.get("facts") or [])).lower()
    unc = " ".join((r.get("uncertainty") or [])).lower()

    if "treasury" in action_type:
        candidates = [
            "Add line-item budget with milestone-gated disbursement and objective completion checks.",
            "Document downside risks, mitigations, and what gets cut first if delivery slips.",
            "Show sustainability path and explain why spend is justified under current treasury pressure.",
        ]
    elif "parameter" in action_type:
        candidates = [
            "Include SPO/operator impact envelope (CPU/RAM/network/storage) with measurable assumptions.",
            "Add rollback/containment plan and explicit halt criteria.",
            "Provide stronger evidence that expected benefits outweigh system-wide risk.",
        ]
    elif "hardfork" in action_type:
        candidates = [
            "Provide migration readiness evidence across tooling/wallet/exchange dependencies.",
            "Publish rollback/contingency plan and incident response playbook.",
            "Define objective go/no-go criteria and post-upgrade validation checks.",
        ]
    else:
        candidates = [
            "Clarify governance intent and expected measurable outcome.",
            "Map each major claim to primary receipts and stable source links.",
            "Address prior NO rationale points directly with concrete revisions.",
        ]

    # Context-sensitive reinforcement.
    if "anchor" in unc or "anchor" in facts:
        candidates.insert(0, "Use stable, reproducible anchor links (commit-pinned when possible).")
    if "no drep distribution" in unc:
        candidates.append("Include broader governance context so directional confidence does not rely on missing distribution signals.")

    for c in candidates:
        if len(fixes) >= 3:
            break
        if c not in fixes:
            fixes.append(c)

    return fixes[:3]


def _human_summary(r: dict, action_row: dict) -> str:
    decision = (r.get("recommendation") or "ABSTAIN").upper()
    action_type = action_row.get("action_type") or r.get("action_type") or "governance action"
    status = (action_row.get("status") or "unknown").lower()
    reason = r.get("abstain_reason_code")
    score = r.get("score")
    conf = r.get("confidence")
    facts = [x for x in (r.get("facts") or []) if x]
    inf = [x for x in (r.get("inferences") or []) if x]
    unc = [x for x in (r.get("uncertainty") or []) if x]
    missing = [x for x in (r.get("missing_evidence") or []) if x]

    if decision == "YES":
        lead = f"Vote: YES. For this {action_type} ({status}), available evidence supports proceeding, with risk judged manageable under current context."
    elif decision == "NO":
        lead = f"Vote: NO. For this {action_type} ({status}), downside risk and/or weak safeguards outweighed demonstrated benefit in the current evidence set."
    elif decision == "NEEDS_MORE_INFO":
        lead = f"Vote: NEEDS_MORE_INFO. For this {action_type} ({status}), critical information needed for a responsible directional vote is still missing."
    else:
        lead = f"Vote: ABSTAIN. For this {action_type} ({status}), evidence quality was insufficient for a reliable YES or NO decision."

    reason_map = {
        "RISK_HIGH": "Primary blocker: risk indicators remained elevated relative to confirmed mitigations.",
        "CONTEXT_THIN_ANCHOR_UNPINNED": "Primary blocker: source/anchor context was incomplete or not verifiably pinned.",
        "DREP_DISTRIBUTION_MISSING": "Primary blocker: DRep distribution signal was unavailable for this action.",
        "RULE_THRESHOLD_UNMET": "Primary blocker: evidence did not clear the directional decision threshold.",
        "HARD_BLOCKER_PRESENT": "Primary blocker: a defined readiness hard-blocker remained open.",
    }
    blocker = reason_map.get(reason, "")

    # The decisive reason and the acknowledged counter-case come from the review
    # tree's counterargument pass — never from a generic fact bullet.
    ax = _assessment_extract(r)
    if decision == "NO":
        decisive = ax["strongest_no"]
        counter = ax["strongest_yes"]
    elif decision == "YES":
        decisive = ax["strongest_yes"]
        counter = ax["strongest_no"]
    else:
        decisive = ax["strongest_hold"]
        counter = ax["strongest_yes"]
    if not decisive:
        decisive = (ax["blocking"][0] + "." if ax["blocking"]
                    else (facts[0] if facts else (inf[0] if inf else
                          "Deterministic policy checks were applied to admitted resources.")))

    fixes = _top_fixes({}, r)
    change_items = [f.rstrip(".") for f in fixes[:2]] or [m for m in missing[:2]]
    if decision == "YES":
        change_label = "What could still change this vote to NO"
        change = ("Material counter-evidence on the decisive points above, or failure "
                  "of the stated safeguards, would trigger a revision.")
    else:
        change_label = "What would change this vote to YES" if decision == "NO" else \
                       "What would enable a directional vote"
        change = "; ".join(change_items) + "." if change_items else ""

    unc_txt = f"Residual uncertainty: {unc[0]}" if unc else ""

    sc_txt = ""
    try:
        sc_txt = f"Confidence context: score {float(score):.2f}; confidence {float(conf)*100:.1f}%."
    except Exception:
        pass

    parts = [lead, blocker, f"Decisive reason: {decisive}"]
    if counter:
        parts.append(f"Weighed against it: {counter}")
    if change:
        parts.append(f"{change_label}: {change}")
    if unc_txt:
        parts.append(unc_txt)
    if sc_txt:
        parts.append(sc_txt)

    return " ".join(p for p in parts if p).strip()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "actions").mkdir(parents=True, exist_ok=True)
    (OUT / "rationales").mkdir(parents=True, exist_ok=True)
    (OUT / "r").mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    actions = _load_actions_map()
    anchor_map = _load_anchor_index_map()
    anchor_stats = _anchor_fetch_stats(anchor_map)
    rat = _load_rationales_latest()
    deep_map = _load_deep_research_map()
    flags_map = _load_flags_map()
    treasury_capacity = _load_treasury_capacity()
    onchain_anchors = _load_onchain_anchors()
    vote_snapshots = load_snapshots()

    soul_commit = _git_commit(SOUL_REPO)
    res_commit = _git_commit(RESOURCES_REPO)
    core_commit = _git_commit(CORE_REPO)

    items = []
    rationale_items = []
    abstentions = 0
    needs_info = 0
    votes_cast = 0

    for aid, r in rat.items():
        if str(aid).startswith("ga_"):
            continue
        a = actions.get(aid, {})
        decision = r["rationale"].get("recommendation", "ABSTAIN")
        run_id = r["run_id"]
        shutil.copyfile(r["run_dir"] / "rationale.md", OUT / "rationales" / f"{run_id}.md")
        shutil.copyfile(r["run_dir"] / "input_manifest.json", OUT / "rationales" / f"{run_id}.manifest.json")
        assessment = r["rationale"].get("assessment") or {}
        assessment_path = r["run_dir"] / "assessment.json"
        if not assessment and assessment_path.exists():
            assessment = json.loads(assessment_path.read_text(encoding="utf-8"))
        if assessment and assessment_path.exists():
            shutil.copyfile(assessment_path, OUT / "rationales" / f"{run_id}.assessment.json")
        anchor_hash = r["rationale"].get("rationale_anchor_hash")
        onchain_anchor = onchain_anchors.get(aid)
        if anchor_hash:
            shutil.copyfile(r["run_dir"] / "rationale.md", OUT / "r" / f"{anchor_hash[:24]}.md")
        vote_receipt = _resolve_vote_receipt(aid, r["run_dir"])
        if vote_receipt.get("submitted"):
            votes_cast += 1
        if decision == "ABSTAIN":
            abstentions += 1
        if decision == "NEEDS_MORE_INFO":
            needs_info += 1
        title = a.get("metadata_title") or a.get("action_id") or aid
        proposal_snapshot = _copy_proposal_snapshot(aid, anchor_map.get(aid, {}))
        item = {
            "action_id": aid,
            "title": title,
            "type": a.get("action_type", ""),
            "status": a.get("status", ""),
            "decision": decision,
            # Vote proof carried on the list item so the public index can render an
            # on-chain badge + explorer link without fetching ~300 detail files.
            "onchain_vote": vote_receipt.get("recommendation"),
            "submitted": bool(vote_receipt.get("submitted")),
            "transaction_hash": vote_receipt.get("transaction_hash"),
            "submitted_at": vote_receipt.get("submitted_at"),
            # Whether a hash of the written rationale was anchored INTO the vote transaction. The
            # earliest votes predate anchoring; the public verifier needs to distinguish "no anchor
            # exists to check" from "the anchor does not match", which mean opposite things.
            "rationale_anchored": bool((onchain_anchor or {}).get("anchor_hash")),
            # Carried on the list item so the public banner can group the open positions by CAUSE
            # without fetching every detail file. What a reader needs to know is not "11 things are
            # unresolved" but "2 of them BEACN should fix, 7 the proposer must, 1 is scarcity."
            "blocked_reason_code": (r["rationale"].get("needs_more_info_reason_code")
                                    or r["rationale"].get("abstain_reason_code")),
            "missing_evidence": r["rationale"].get("missing_evidence", []),
            "diverged": bool(
                vote_receipt.get("submitted")
                and vote_receipt.get("recommendation")
                and vote_receipt.get("recommendation") != decision
            ),
            "detected_at": a.get("first_seen", ""),
            "published_at": a.get("last_updated", ""),
            "detail_path": f"/actions/{aid}",
            "proposal_available": proposal_snapshot.get("available", False),
            "proposal_path": proposal_snapshot.get("download_path", ""),
        }
        items.append(item)

        human_summary = _human_summary(r["rationale"], a)
        top_fixes = _top_fixes(a, r["rationale"])
        rd = {
            "action_id": aid,
            "title": title,
            "decision": decision,
            "summary": human_summary,
            "summary_raw": (r["rationale"].get("inferences") or [""])[0],
            "top_fixes": top_fixes,
            "published_at": a.get("last_updated", ""),
        }
        rationale_items.append(rd)

        frozen = latest_snapshot(vote_snapshots, aid)
        current_eval = {
            "vote": decision,
            "score": r["rationale"].get("score"),
            "confidence": r["rationale"].get("confidence"),
            "input_hash": r["rationale"].get("input_hash"),
            "snapshot_bundle_hash": r["rationale"].get("snapshot_bundle_hash"),
            "soul_commit": soul_commit,
            "resources_commit": res_commit,
            "core_commit": core_commit,
            "rationale_markdown_path": r["md_path"],
            # The locally-derived anchor for the CURRENT run. This is what a NEXT vote would
            # commit to. It is NOT proof of anything about a vote already cast, because the
            # engine rewrites it every time it re-scores on new evidence.
            "rationale_anchor_url": r["rationale"].get("rationale_anchor_url"),
            "rationale_anchor_hash": r["rationale"].get("rationale_anchor_hash"),
        }
        proof_of_vote = _proof_of_vote_block(frozen, current_eval, onchain_anchor)
        action_detail = {
            "action_id": aid,
            "title": title,
            "type": a.get("action_type", ""),
            "status": a.get("status", ""),
            "source": {
                "origin": "governance fetch pipeline",
                "raw_input_hash": f"sha256:{r['rationale'].get('input_hash', '')}",
                "detected_at": a.get("first_seen", ""),
            },
            "decision": {
                # `vote` is the engine's CURRENT recommendation. `onchain_vote` is the
                # direction actually cast on-chain, read from the vote receipt. They can
                # legitimately differ (evidence moved after the vote was cast, or the
                # revision was debounced/refused), and the public site must never render
                # one as if it were the other.
                "vote": decision,
                "onchain_vote": vote_receipt.get("recommendation"),
                "diverged": bool(
                    vote_receipt.get("submitted")
                    and vote_receipt.get("recommendation")
                    and vote_receipt.get("recommendation") != decision
                ),
                "published_at": a.get("last_updated", ""),
                "signed": bool(vote_receipt.get("signed_tx")),
                "submitted": bool(vote_receipt.get("submitted")),
                "transaction_hash": vote_receipt.get("transaction_hash"),
                "submitted_at": vote_receipt.get("submitted_at"),
            },
            # For a CAST vote this is the frozen vote-time snapshot (vote_time_snapshots.json,
            # written at submission and append-only) — it never moves when the engine re-scores.
            # For an uncast action there is no vote-time truth to freeze, so it falls back to the
            # current derivation. `frozen` says which one a reader is looking at; the re-derived
            # today-values always live in the separate `current` block below.
            "proof_of_vote": proof_of_vote,
            # The engine's CURRENT derivation: what a NEXT vote would commit to. It is NOT proof
            # of anything about a vote already cast, because the engine rewrites it every time it
            # re-scores on new evidence.
            "current": current_eval,
            "rationale": {
                "summary": human_summary,
                "summary_raw": (r["rationale"].get("inferences") or [""])[0],
                "top_fixes": top_fixes,
                "markdown_path": r["md_path"],
                "missing_evidence": r["rationale"].get("missing_evidence", []),
                # WHY the engine stopped short of a directional vote. The public site groups the
                # open positions by this, so a reader can tell the difference between "the proposal
                # will not show its budget", "we ran out of treasury capacity for it", and "BEACN
                # would now vote the other way". Those look identical without it, and a site that
                # blurs them is describing its own confusion rather than the evidence.
                "blocked_reason_code": (r["rationale"].get("needs_more_info_reason_code")
                                        or r["rationale"].get("abstain_reason_code")),
                "assessment_status": r["rationale"].get("assessment_status") or assessment.get("overall_status"),
                "assessment_schema_version": r["rationale"].get("assessment_schema_version") or assessment.get("schema_version"),
                "assessment": assessment,
                "assessment_path": f"/data/output/public/rationales/{run_id}.assessment.json" if assessment and assessment_path.exists() else "",
                "treasury_dimensions": r["rationale"].get("treasury_dimensions"),
                "decision_contract": r["rationale"].get("decision_contract", {}),
                "merit_recommendation": r["rationale"].get("treasury_merit_recommendation"),
                "merit_reason": r["rationale"].get("treasury_merit_reason"),
            },
            "decision_contract": r["rationale"].get("decision_contract", {}),
            "proposal_evidence": proposal_snapshot,
            "deep_research": _deep_research_block(aid, deep_map.get(aid)),
            # Why this proposal drew scrutiny, and — for treasury asks — the capacity arithmetic
            # it had to fit inside. Both were previously invisible to the public.
            "flags": flags_map.get(aid, []),
            "treasury_capacity": (
                {**treasury_capacity,
                 "requested_lovelace": _to_int(a.get("treasury_amount_lovelace")),
                 "fits_remaining": (
                     _to_int(a.get("treasury_amount_lovelace")) > 0
                     and treasury_capacity.get("remaining_capacity_lovelace") is not None
                     and _to_int(a.get("treasury_amount_lovelace"))
                     <= int(treasury_capacity.get("remaining_capacity_lovelace") or 0)
                 )}
                if a.get("action_type") == "TreasuryWithdrawals" and treasury_capacity else None
            ),
            "reproducibility": {
                "soul_repo": "beacn-drep-soul",
                "soul_commit": soul_commit,
                "resources_repo": "beacn-drep-resources",
                "resources_commit": res_commit,
                "core_commit": core_commit,
                "resource_ids_used": r["rationale"].get("resources_used", []),
            },
            "inputs_used": [
                {"resource_id": x, "type": "csv", "path": "registries/resource_registry.csv"}
                for x in r["rationale"].get("resources_used", [])
            ],
            "scoring": {
                "binding_score": r["rationale"].get("score"),
                "raw_score": r["rationale"].get("raw_score"),
                "directional_threshold": r["rationale"].get("directional_threshold"),
                "confidence": r["rationale"].get("confidence"),
                "model_vote_influence": 0,
            },
            "freshness": r["rationale"].get("freshness", {}),
        }
        (OUT / "actions" / f"{aid}.json").write_text(json.dumps(action_detail, indent=2) + "\n")

        human_md = "\n".join([
            f"# {aid}",
            "",
            f"## Vote",
            f"- Decision: **{decision}**",
            f"- Action type: `{a.get('action_type', '')}`",
            f"- Status: `{a.get('status', '')}`",
            f"- Published at: `{a.get('last_updated', '')}`",
            "",
            "## Human-readable rationale",
            human_summary,
            "",
            "## Assessment tree",
            f"- assessment_status: `{r['rationale'].get('assessment_status') or assessment.get('overall_status', '')}`",
            *[
                f"- {section.get('title')}: `{section.get('status')}` — {section.get('conclusion')}"
                for section in (assessment.get("sections") or [])
            ],
            "",
            "## What influenced this vote",
            *(f"- {x}" for x in (r["rationale"].get("facts") or ["No fact lines available."])),
            "",
            "## Remaining uncertainty",
            *(f"- {x}" for x in (r["rationale"].get("uncertainty") or ["No material uncertainty listed."])),
            "",
            "## Top 3 fixes to improve next submission",
            *[f"- {x}" for x in top_fixes],
            "",
            "## Proof of vote" + (" (frozen at submission)" if proof_of_vote.get("frozen") else ""),
            f"- input_hash: `{proof_of_vote.get('input_hash') or ''}`",
            f"- snapshot_bundle_hash: `{proof_of_vote.get('snapshot_bundle_hash') or ''}`",
            f"- soul_commit: `{proof_of_vote.get('soul_commit') or ''}`",
            f"- resources_commit: `{proof_of_vote.get('resources_commit') or ''}`",
            f"- core_commit: `{proof_of_vote.get('core_commit') or ''}`",
            f"- score: `{proof_of_vote.get('score') if proof_of_vote.get('score') is not None else ''}`",
            f"- confidence: `{proof_of_vote.get('confidence') if proof_of_vote.get('confidence') is not None else ''}`",
            "",
        ])
        (OUT / "actions" / f"{aid}.md").write_text(human_md + "\n", encoding="utf-8")

    items.sort(key=lambda x: x["detected_at"], reverse=True)
    rationale_items.sort(key=lambda x: x["published_at"], reverse=True)

    index = {
        "generated_at": now,
        "soul": {"repo": "beacn-drep-soul", "commit": soul_commit, "path": "README.md"},
        "resources": {"repo": "beacn-drep-resources", "commit": res_commit, "registry_path": "registries/resource_registry.csv"},
        "core": {"repo": "beacn-drep-core", "version": "0.2.0", "commit": core_commit},
        "treasury_capacity": treasury_capacity,
        "stats": {
            "actions_seen": len(actions),
            "decisions_published": len(items),
            "votes_cast": votes_cast,
            "abstentions": abstentions,
            "needs_more_info": needs_info,
            "anchor_fetch_total": anchor_stats.get("total", 0),
            "anchor_fetch_ok": anchor_stats.get("ok", 0),
            "anchor_fetch_failed": anchor_stats.get("failed", 0),
            "anchor_fetch_coverage_pct": anchor_stats.get("coverage_pct", 0.0),
        },
        "latest_actions": [
            {
                "action_id": x["action_id"],
                "title": x["title"],
                "type": x["type"],
                "decision": x["decision"],
                "published_at": x["published_at"],
            }
            for x in items[:20]
        ],
    }

    flow_path = RESOURCES_REPO / "data" / "history" / "governance_metrics" / "latest" / "treasury_flow_6m.json"
    flow = {}
    if flow_path.exists():
        try:
            flow = json.loads(flow_path.read_text(encoding="utf-8"))
        except Exception:
            flow = {}

    flow_bases = flow.get("basis") or {}

    # Kept for compatibility only. Its field names are misleading: `inflows_6m` was only ever
    # the FEE-DERIVED slice of treasury inflow (20% of chain fees), while `outflow_inflow_ratio`
    # is measured against TOTAL inflow — two different bases in one block, unlabeled. Renaming
    # the fields would break existing consumers, so the bases are labeled in place and the whole
    # artifact points at its labeled successor.
    treasury_summary = {
        "generated_at": now,
        "deprecated": "superseded by budget_state.json, which labels every number's basis; "
                      "note that treasury.inflows_6m here is FEE-DERIVED inflow only",
        "rolling_6m_fees": [flow.get("chain_fees_6m_lovelace", 0)] if flow else [],
        "treasury": {
            "inflows_6m": flow.get("treasury_fee_inflow_6m_lovelace", 0),
            "inflows_6m_basis": "fee_derived: 20% of chain fees (organic-revenue context only), "
                                "NOT total treasury inflow",
            "outflows_6m": flow.get("treasury_withdrawals_6m_lovelace", 0),
            "outflows_6m_basis": flow_bases.get("outflow", ""),
            "outflow_inflow_ratio": flow.get("outflow_inflow_ratio"),
            "outflow_inflow_ratio_basis": "outflow vs TOTAL treasury inflow — a different basis "
                                          "than inflows_6m above",
            "window_days": flow.get("window_days", 180),
            "treasury_tax_assumed": flow.get("treasury_tax_assumed", 0.20),
        },
    }

    # The honest replacement: every figure carries its basis, and both spend ratios are
    # published side by side so neither the flattering nor the alarming one can be quoted
    # as if it were the only measure.
    inflow_total = _to_int(flow.get("treasury_inflow_total_6m_lovelace"))
    inflow_fee = _to_int(flow.get("treasury_fee_inflow_6m_lovelace"))
    outflow_total = _to_int(flow.get("treasury_withdrawals_6m_lovelace"))
    try:
        ncl_block = json.loads(POLICY_STATE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        ncl_block = {}
    budget_state = {
        "schema_version": 1,
        "generated_at": now,
        "ncl": ncl_block,
        "inflow_36ep": {
            "total": inflow_total,
            "fee_derived": inflow_fee,
            "reserves_derived": max(0, inflow_total - inflow_fee),
            "bases": {
                "total": flow_bases.get("inflow", ""),
                "fee_derived": flow_bases.get("fee_inflow", ""),
                "reserves_derived": "residual: total inflow minus fee-derived inflow "
                                    "(monetary expansion + donations)",
            },
        },
        "outflow_36ep": {
            "total": outflow_total,
            "basis": flow_bases.get("outflow", ""),
        },
        "ratios": {
            "spend_vs_total_inflow": round(outflow_total / inflow_total, 6) if inflow_total else None,
            "spend_vs_fee_inflow": round(outflow_total / inflow_fee, 6) if inflow_fee else None,
        },
    }

    drep_summary = {
        "generated_at": now,
        "beacn_history_count": len(items),
        "consistency": {
            "abstain_rate": round((abstentions / len(items)), 4) if items else 0,
            "needs_more_info_rate": round((needs_info / len(items)), 4) if items else 0,
        },
        "top_n_comparison": {"available": False, "reason": "top_drep_votes.csv not populated"},
    }

    audit_status = {
        "generated_at": now,
        "current_versions": {
            "soul_commit": soul_commit,
            "resources_commit": res_commit,
            "core_commit": core_commit,
        },
        "pipeline": {
            "last_scan_at": now,
            "last_decision_at": now,
            "last_publish_at": now,
            "anchor_fetch": {
                "total": anchor_stats.get("total", 0),
                "ok": anchor_stats.get("ok", 0),
                "ok_cached": anchor_stats.get("ok_cached", 0),
                "failed": anchor_stats.get("failed", 0),
                "coverage_pct": anchor_stats.get("coverage_pct", 0.0),
                "failure_buckets": anchor_stats.get("failure_buckets", {}),
            },
        },
        "integrity": {
            "hidden_inputs_allowed": False,
            "undeclared_resources_allowed": False,
            "manual_override_enabled": False,
            "private_assistant_context_allowed": False,
            "private_memory_allowed": False,
            "policy_doc": "docs/PUBLIC_CONTEXT_AND_LIMITS.md",
        },
    }

    # Publish the doctrine's scoring weights verbatim. The public site renders the weighting system
    # from THIS file, so what a visitor reads is the same bytes the engine scores with — it cannot
    # drift into a flattering description of weights we don't actually use. It also carries its own
    # version + change-control policy, so a weight change is visible rather than silent.
    weights_src = SOUL_REPO / "scoring_weights.json"
    if weights_src.exists():
        (OUT / "scoring_weights.json").write_text(weights_src.read_text(encoding="utf-8"), encoding="utf-8")

    # The rationale files under /r/ are the ONLY copies of what BEACN committed to on-chain. Their
    # names are the first 24 hex of their own blake2b hash, so they are immutable by construction —
    # but they are not immortal. Lose one and the vote it belongs to becomes permanently
    # unverifiable: the chain still holds the hash, and nothing on earth can reproduce the bytes.
    # This is the single most destructive thing that could quietly happen to this repo, so it fails
    # loudly rather than shipping a site whose central promise is broken.
    orphaned = [
        (aid, a["anchor_hash"]) for aid, a in onchain_anchors.items()
        if a.get("anchor_hash") and not (OUT / "r" / f"{a['anchor_hash'][:24]}.md").exists()
    ]
    if orphaned:
        for aid, h in orphaned:
            print(f"  ORPHANED ANCHOR  {aid}  chain expects r/{h[:24]}.md — file is GONE")
        raise SystemExit(
            f"REFUSING TO PUBLISH: {len(orphaned)} vote(s) have an on-chain rationale anchor whose "
            f"published rationale is missing. Those votes would become unverifiable forever. "
            f"Restore the files from git history before publishing.")

    (OUT / "index.json").write_text(json.dumps(index, indent=2) + "\n")
    (OUT / "actions.json").write_text(json.dumps({"generated_at": now, "items": items}, indent=2) + "\n")
    (OUT / "rationales.json").write_text(json.dumps({"generated_at": now, "items": rationale_items}, indent=2) + "\n")
    (OUT / "treasury_summary.json").write_text(json.dumps(treasury_summary, indent=2) + "\n")
    (OUT / "budget_state.json").write_text(json.dumps(budget_state, indent=2) + "\n")
    (OUT / "drep_summary.json").write_text(json.dumps(drep_summary, indent=2) + "\n")
    (OUT / "audit_status.json").write_text(json.dumps(audit_status, indent=2) + "\n")

    print(json.dumps({"actions": len(items), "generated_at": now}))


if __name__ == "__main__":
    main()
