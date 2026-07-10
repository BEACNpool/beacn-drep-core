#!/usr/bin/env python3
"""Agentic deep-research dossier pipeline for treasury actions.

Drafts the 7-section diligence dossier the engine requires for every active
treasury action, grounded ONLY in admitted public inputs (the pinned anchor
document, the exported governance CSVs, and the db-sync-derived risk metrics),
and writes it into beacn-drep-resources with full receipts.

Honesty contract (matches METHODOLOGY.md and doctrine v1.2.0):
  * Machine-drafted diligence is NOT complete independent diligence.
    Section flags are set from what the draft actually grounded, but
    `dossier_complete` stays "no" with status `drafted_pending_review` until a
    human approves it (`--approve <action_id> --approver <name>`), which is the
    explicit, auditable step that lowers the engine's directional threshold.
  * financial/risk profile rows are machine-EXTRACTED from the proposal
    document, never invented: unknown stays "unknown", and
    `independent_assurance_present` can only ever be "no" from this pipeline —
    a genuine third-party audit must be admitted by a human.
  * Existing hand-curated rows are never overwritten (missing-only upsert).
  * Every dossier ships a receipt: anchor sha256, model attestation
    (prompt/output hashes), source-file hashes, doctrine version.

Usage:
  python3 scripts/build_deep_research_dossiers.py --backend codex --missing-only
  python3 scripts/build_deep_research_dossiers.py --approve gov_action1... --approver David
  python3 scripts/build_deep_research_dossiers.py --list   # review queue
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import subprocess
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from beacn_drep import engine as E, llm  # noqa: E402
from beacn_drep.anchors import load_anchor_text  # noqa: E402

RESOURCES = E.RESOURCES_REPO
DS = RESOURCES / "data" / "input" / "governance" / "decision_support"
DOSSIER_DIR = DS / "dossiers"
DEEP_CSV = DS / "deep_research_dossiers.csv"
FIN_CSV = DS / "financial_sustainability_profiles.csv"
RISK_CSV = DS / "risk_mitigation_registry.csv"
VALUE_CSV = DS / "ecosystem_value_profiles.csv"
READY_CSV = DS / "vote_readiness_matrix.csv"
METRICS = RESOURCES / "data" / "history" / "governance_metrics" / "latest"
OWNER = "drep-agent-extract"

CODEX_BIN = os.environ.get(
    "BEACN_CODEX_BIN",
    shutil.which("codex") or str(Path.home() / ".local/bin/codex"),
)

SECTIONS = [
    "proposal_summary",
    "budget_analysis",
    "feasibility_assessment",
    "risk_analysis",
    "alternatives_analysis",
    "failure_mode_analysis",
    "community_impact",
]

_SECTION_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "content": {"type": "string"},
        "grounded": {
            "type": "boolean",
            "description": "true only if the section is substantively supported by the supplied documents",
        },
        "evidence_refs": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["content", "grounded", "evidence_refs"],
}

_TRI = {"type": "string", "enum": ["yes", "no", "unknown"]}
_LEVEL = {"type": "string", "enum": ["low", "medium", "high", "unknown"]}

DOSSIER_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "facts": {"type": "array", "items": {"type": "string"}},
        "inferences": {"type": "array", "items": {"type": "string"}},
        "uncertainty": {"type": "array", "items": {"type": "string"}},
        "sections": {
            "type": "object",
            "additionalProperties": False,
            "properties": {s: _SECTION_SCHEMA for s in SECTIONS},
            "required": SECTIONS,
        },
        "financial_profile": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "budget_granularity": _TRI,
                "milestone_payment_gates": _TRI,
                "clawback_refund_path": _TRI,
                "recurring_funding_dependency": _TRI,
                "runway_clarity": _TRI,
                "sustainability_path_clear": _TRI,
                "cost_benefit_clarity": _TRI,
                "financial_confidence": {"type": "number"},
                "notes": {"type": "string"},
            },
            "required": ["budget_granularity", "milestone_payment_gates", "clawback_refund_path",
                         "recurring_funding_dependency", "runway_clarity", "sustainability_path_clear",
                         "cost_benefit_clarity", "financial_confidence", "notes"],
        },
        "risk_profile": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "execution_risk_level": _LEVEL,
                "governance_risk_level": _LEVEL,
                "technical_risk_level": _LEVEL,
                "treasury_exposure_risk_level": _LEVEL,
                "mitigation_evidence_present": _TRI,
                "rollback_or_remedy_path": _TRI,
                "dependency_map_complete": _TRI,
                "risk_profile_confidence": {"type": "number"},
                "notes": {"type": "string"},
            },
            "required": ["execution_risk_level", "governance_risk_level", "technical_risk_level",
                         "treasury_exposure_risk_level", "mitigation_evidence_present",
                         "rollback_or_remedy_path", "dependency_map_complete",
                         "risk_profile_confidence", "notes"],
        },
        "ecosystem_value_profile": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "critical_infrastructure": _TRI,
                "open_source_public_good": _TRI,
                "measurable_existing_adoption": _TRI,
                "ecosystem_leverage": _TRI,
                "strategic_necessity": _TRI,
                "credible_prior_delivery": _TRI,
                "cost_compared_to_market": _TRI,
                "output_priced": _TRI,
                "material_duplication": _TRI,
                "private_capture_risk": _TRI,
                "evidence_refs": {"type": "array", "items": {"type": "string"}},
                "confidence": {"type": "number"},
            },
            "required": ["critical_infrastructure", "open_source_public_good",
                         "measurable_existing_adoption", "ecosystem_leverage",
                         "strategic_necessity", "credible_prior_delivery",
                         "cost_compared_to_market", "output_priced", "material_duplication",
                         "private_capture_risk", "evidence_refs", "confidence"],
        },
    },
    "required": ["facts", "inferences", "uncertainty", "sections", "financial_profile",
                 "risk_profile", "ecosystem_value_profile"],
}

SYSTEM = (
    "You are the deep-research analyst for an autonomous Cardano DRep that votes real treasury "
    "money. Draft a diligence dossier for ONE governance action, grounded STRICTLY in the "
    "supplied documents (anchor text, on-chain context, doctrine). Rules:\n"
    "1. Invent nothing. Every claim in 'facts' must be traceable to the supplied material; put "
    "the source in evidence_refs (e.g. 'anchor: budget table', 'onchain: recipient history').\n"
    "2. Separate FACTS (document/on-chain supported), INFERENCES (your reasoning, labeled), and "
    "UNCERTAINTY (what cannot be verified from the record). Keep full untruncated numbers and "
    "exact quoted figures.\n"
    "3. Mark a section grounded=true ONLY if the supplied material substantively covers it. A "
    "section that is mostly 'the document does not say' is grounded=false.\n"
    "4. financial/risk profile fields are EXTRACTION, not judgment: 'yes' only when the document "
    "shows it, 'no' when the document makes clear it is absent, else 'unknown'. Confidence in "
    "[0,1] reflects how well the document supports the profile.\n"
    "5. Alternatives analysis must consider: not funding, partial funding, other providers or "
    "mechanisms named in the record, and deferral — from the supplied material and doctrine only.\n"
    "6. Be neutral and precise. Critique proposals, never people. Do not recommend a vote — a "
    "separate deterministic engine decides.\n"
    "7. Extract the ecosystem-value profile conservatively. This draft sees proposer material and "
    "on-chain context only, so these fields remain proposal claims until a separate independent "
    "evidence pass verifies them. Unknown is preferable to inference."
)


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _read_csv(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def _write_csv(path: Path, header: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in header})


def _upsert(path: Path, header: list[str], row: dict, *, overwrite: bool) -> bool:
    """Insert row; refuse to touch an existing row unless overwrite (and even
    then never replace a hand-curated row with a machine one)."""
    hdr, rows = _read_csv(path) if path.exists() else (header, [])
    hdr = hdr or header
    existing = next((r for r in rows if r.get("action_id") == row["action_id"]), None)
    if existing is not None:
        if not overwrite or existing.get("owner") not in ("", OWNER):
            return False
        rows = [r for r in rows if r.get("action_id") != row["action_id"]]
    rows.append(row)
    _write_csv(path, hdr, rows)
    return True


def _onchain_context(action: dict) -> str:
    """Public db-sync-derived context: recipient repeat history + vote profile."""
    lines = []
    tx_hash = (action.get("tx_hash") or "").lower()
    try:
        _, rows = _read_csv(METRICS / "recipient_repeat_risk.csv")
        for r in rows:
            if tx_hash and tx_hash in (r.get("action_tx_hashes") or "").lower():
                lines.append(
                    f"onchain recipient history: stake address {r.get('stake_address')} appears in "
                    f"{r.get('proposal_count')} withdrawal proposals totalling {r.get('total_lovelace')} "
                    f"lovelace (first {r.get('first_seen')}, last {r.get('last_seen')})")
    except Exception:
        pass
    try:
        _, rows = _read_csv(METRICS / "action_vote_profile.csv")
        for r in rows:
            if r.get("action_tx_hash", "").lower() == tx_hash and str(r.get("cert_index")) == str(action.get("cert_index")):
                lines.append(
                    f"onchain DRep vote counts so far: yes={r.get('drep_yes')} no={r.get('drep_no')} "
                    f"abstain={r.get('drep_abstain')} (explicit ballots, not stake-weighted)")
    except Exception:
        pass
    tf = E._load_treasury_flow()
    if tf:
        lines.append(
            f"treasury flow (36 epochs): inflow {tf.get('treasury_inflow_total_6m_lovelace')} lovelace, "
            f"enacted withdrawals {tf.get('treasury_withdrawals_6m_lovelace')} lovelace, "
            f"ratio {tf.get('outflow_inflow_ratio')}")
    return "\n".join(lines) or "(no additional on-chain context rows for this action)"


def _prompt(action: dict, anchor_text: str, doctrine_text: str, onchain: str) -> str:
    return (
        SYSTEM
        + "\n\n========================================\n"
        + f"Action id: {action.get('action_id')}\n"
        + f"Action type: {action.get('action_type')}\n"
        + f"Title: {action.get('metadata_title') or '(none)'}\n"
        + f"Treasury amount (lovelace): {action.get('treasury_amount_lovelace') or '(none)'}\n"
        + f"Proposed epoch: {action.get('proposed_epoch')}  Expires after: {action.get('expires_after_epoch') or action.get('expiration_epoch')}\n\n"
        + "ON-CHAIN CONTEXT (db-sync derived, public):\n-----8<-----\n" + onchain + "\n-----8<-----\n\n"
        + "TREASURY DOCTRINE (BEACN's published standard):\n-----8<-----\n"
        + llm._truncate(doctrine_text or "(none on file)", 6000) + "\n-----8<-----\n\n"
        + "ANCHOR DOCUMENT TEXT (verbatim, possibly JSON-LD):\n-----8<-----\n"
        + llm._truncate(anchor_text or "(no cached anchor document)", 48000) + "\n-----8<-----\n\n"
        + "Produce the dossier JSON."
    )


def call_codex(prompt: str) -> dict:
    with tempfile.TemporaryDirectory() as td:
        schema_f = Path(td) / "schema.json"
        out_f = Path(td) / "out.json"
        schema_f.write_text(json.dumps(DOSSIER_SCHEMA), encoding="utf-8")
        cmd = [
            CODEX_BIN, "exec", "--skip-git-repo-check", "-s", "read-only",
            "-c", "approval_policy=\"never\"",
            "-m", os.environ.get("BEACN_CODEX_MODEL", "gpt-5.5"),
            "--color", "never",
            "--output-schema", str(schema_f),
            "-o", str(out_f), "-",
        ]
        p = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=600)
        raw = out_f.read_text(encoding="utf-8") if out_f.exists() else p.stdout
        if not raw.strip():
            raise RuntimeError(f"codex exec produced no output rc={p.returncode}: {p.stderr.strip()[:300]}")
        start, end = raw.find("{"), raw.rfind("}")
        return json.loads(raw[start:end + 1])


def call_claude(prompt: str) -> dict:
    p = subprocess.run(["claude", "-p", "--output-format", "json", prompt],
                       capture_output=True, text=True, timeout=600)
    if p.returncode != 0:
        raise RuntimeError(f"claude -p failed rc={p.returncode}: {p.stderr.strip()[:300]}")
    env = json.loads(p.stdout)
    raw = str(env.get("result", ""))
    start, end = raw.find("{"), raw.rfind("}")
    return json.loads(raw[start:end + 1])


BACKENDS = {"codex": call_codex, "claude": call_claude}


def _tri(v, default="unknown") -> str:
    return v if v in ("yes", "no", "unknown") else default


def _level(v, default="unknown") -> str:
    return v if v in ("low", "medium", "high", "unknown") else default


def write_dossier(action: dict, data: dict, attestation: dict) -> Path:
    aid = action["action_id"]
    DOSSIER_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines = [
        f"# Deep-research dossier: {action.get('metadata_title') or aid}",
        "",
        f"- action_id: `{aid}`",
        f"- action_type: {action.get('action_type')}",
        f"- requested: {action.get('treasury_amount_lovelace') or 'n/a'} lovelace",
        f"- drafted: {now} by {attestation.get('model')} (machine draft — **pending human review**)",
        f"- status: drafted_pending_review — `dossier_complete` stays 'no' until approved",
        "",
        "## FACTS (document/on-chain supported)",
        *[f"- {x}" for x in data.get("facts") or ["(none extracted)"]],
        "",
        "## INFERENCES (analyst reasoning, labeled)",
        *[f"- {x}" for x in data.get("inferences") or ["(none)"]],
        "",
        "## UNCERTAINTY (cannot be verified from the record)",
        *[f"- {x}" for x in data.get("uncertainty") or ["(none)"]],
        "",
    ]
    for s in SECTIONS:
        sec = (data.get("sections") or {}).get(s) or {}
        lines += [
            f"## {s.replace('_', ' ').title()}",
            f"_grounded: {'yes' if sec.get('grounded') else 'no'}_",
            "",
            (sec.get("content") or "(empty)").strip(),
            "",
            "Evidence refs: " + ("; ".join(sec.get("evidence_refs") or []) or "(none)"),
            "",
        ]
    lines += [
        "---",
        "_Machine-drafted from admitted public inputs only (pinned anchor document, exported",
        "governance CSVs, db-sync metrics). Attestation in the sidecar receipt. This draft does",
        "NOT lower the engine's treasury bar until a human approves it via",
        "`build_deep_research_dossiers.py --approve`._",
    ]
    path = DOSSIER_DIR / f"{aid}.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    (DOSSIER_DIR / f"{aid}.receipt.json").write_text(
        json.dumps(attestation, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def build(args) -> int:
    actions = [a for a in E._load_actions()
               if (a.get("status") or "").lower() == "active"
               and E._action_family(a.get("action_type")) == "treasury"]
    if args.limit:
        actions = actions[:args.limit]
    _, deep_rows = _read_csv(DEEP_CSV)
    have = {r["action_id"] for r in deep_rows}
    doctrine = E._load_doctrine_for("TreasuryWithdrawals")
    tdoc_version = (E._load_treasury_doctrine() or {}).get("version", "unknown")

    deep_hdr = ["action_id", "action_type", *(f"{s}_complete" for s in SECTIONS),
                "dossier_complete", "analyst_notes", "owner", "status"]
    fin_hdr, _ = _read_csv(FIN_CSV)
    risk_hdr, _ = _read_csv(RISK_CSV)
    value_hdr, _ = _read_csv(VALUE_CSV)

    ok = fail = skipped = 0
    for a in actions:
        aid = a["action_id"]
        if args.missing_only and aid in have:
            skipped += 1
            continue
        anchor_text, anchor_meta = load_anchor_text(aid)
        if not anchor_text:
            print(f"  [dossier] SKIP {aid[:24]}..  no cached anchor text")
            skipped += 1
            continue
        onchain = _onchain_context(a)
        prompt = _prompt(a, anchor_text, doctrine.get("text"), onchain)
        try:
            data = BACKENDS[args.backend](prompt)
        except Exception as e:  # noqa: BLE001
            fail += 1
            print(f"  [dossier] FAIL {aid[:24]}..  {type(e).__name__}: {str(e)[:160]}")
            continue

        attestation = {
            "action_id": aid,
            "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "backend": args.backend,
            "model": os.environ.get("BEACN_CODEX_MODEL", "gpt-5.5") if args.backend == "codex" else "claude-cli",
            "anchor": anchor_meta,
            "anchor_sha256": _sha(anchor_text),
            # Frozen inputs so the independent verifier re-checks against exactly
            # what the drafter saw (live ballot counts / flow figures move).
            "onchain_context": onchain,
            "action_metadata": {
                "action_type": a.get("action_type"),
                "metadata_title": a.get("metadata_title"),
                "treasury_amount_lovelace": a.get("treasury_amount_lovelace"),
                "proposed_epoch": a.get("proposed_epoch"),
                "expires_after_epoch": a.get("expires_after_epoch") or a.get("expiration_epoch"),
            },
            "doctrine_files": doctrine.get("files"),
            "doctrine_sha256": doctrine.get("sha256"),
            "treasury_doctrine_version": tdoc_version,
            "prompt_sha256": _sha(prompt),
            "output_sha256": _sha(json.dumps(data, sort_keys=True)),
            "review_status": "drafted_pending_review",
        }
        dossier_path = write_dossier(a, data, attestation)

        sections = data.get("sections") or {}
        deep_row = {
            "action_id": aid, "action_type": a.get("action_type"),
            **{f"{s}_complete": ("yes" if (sections.get(s) or {}).get("grounded") else "no")
               for s in SECTIONS},
            "dossier_complete": "no",
            "analyst_notes": f"machine draft {attestation['generated_at_utc']}; "
                             f"dossier at decision_support/dossiers/{aid}.md; approve via "
                             "build_deep_research_dossiers.py --approve",
            "owner": OWNER, "status": "drafted_pending_review",
        }
        _upsert(DEEP_CSV, deep_hdr, deep_row, overwrite=args.overwrite)

        fp = data.get("financial_profile") or {}
        ada = str(int(float(a.get("treasury_amount_lovelace") or 0) / 1_000_000))
        _upsert(FIN_CSV, fin_hdr, {
            "action_id": aid, "action_type": a.get("action_type"), "requested_ada": ada,
            "budget_granularity": _tri(fp.get("budget_granularity")),
            "milestone_payment_gates": _tri(fp.get("milestone_payment_gates")),
            "clawback_refund_path": _tri(fp.get("clawback_refund_path")),
            "fee_recovery_dependency": "no", "fee_recovery_clarity": "unknown",
            "recurring_funding_dependency": _tri(fp.get("recurring_funding_dependency")),
            "runway_clarity": _tri(fp.get("runway_clarity")),
            "sustainability_path_clear": _tri(fp.get("sustainability_path_clear")),
            "cost_benefit_clarity": _tri(fp.get("cost_benefit_clarity")),
            "financial_confidence": f"{max(0.0, min(1.0, float(fp.get('financial_confidence') or 0.0))):.2f}",
            "financial_blocker": "no",
            "notes": (fp.get("notes") or "")[:300],
            "owner": OWNER, "status": "machine_extracted_from_anchor",
        }, overwrite=args.overwrite)

        rp = data.get("risk_profile") or {}
        _upsert(RISK_CSV, risk_hdr, {
            "action_id": aid, "action_type": a.get("action_type"),
            "execution_risk_level": _level(rp.get("execution_risk_level")),
            "governance_risk_level": _level(rp.get("governance_risk_level")),
            "technical_risk_level": _level(rp.get("technical_risk_level")),
            "treasury_exposure_risk_level": _level(rp.get("treasury_exposure_risk_level")),
            "mitigation_evidence_present": _tri(rp.get("mitigation_evidence_present")),
            # This pipeline can never assert third-party assurance into existence.
            "independent_assurance_present": "no",
            "rollback_or_remedy_path": _tri(rp.get("rollback_or_remedy_path")),
            "dependency_map_complete": _tri(rp.get("dependency_map_complete")),
            "risk_profile_confidence": f"{max(0.0, min(1.0, float(rp.get('risk_profile_confidence') or 0.0))):.2f}",
            "risk_blocker": "no",
            "notes": (rp.get("notes") or "")[:300],
            "owner": OWNER, "status": "machine_extracted_from_anchor",
        }, overwrite=args.overwrite)

        vp = data.get("ecosystem_value_profile") or {}
        _upsert(VALUE_CSV, value_hdr, {
            "action_id": aid, "action_type": a.get("action_type"),
            "critical_infrastructure": _tri(vp.get("critical_infrastructure")),
            "open_source_public_good": _tri(vp.get("open_source_public_good")),
            "measurable_existing_adoption": _tri(vp.get("measurable_existing_adoption")),
            "ecosystem_leverage": _tri(vp.get("ecosystem_leverage")),
            "strategic_necessity": _tri(vp.get("strategic_necessity")),
            "credible_prior_delivery": _tri(vp.get("credible_prior_delivery")),
            "cost_compared_to_market": _tri(vp.get("cost_compared_to_market")),
            "output_priced": _tri(vp.get("output_priced")),
            "material_duplication": _tri(vp.get("material_duplication")),
            "private_capture_risk": _tri(vp.get("private_capture_risk")),
            "evidence_status": "proposal_only",
            "evidence_refs": json.dumps(vp.get("evidence_refs") or [], separators=(",", ":")),
            "confidence": f"{max(0.0, min(1.0, float(vp.get('confidence') or 0.0))):.2f}",
            "owner": OWNER, "status": "awaiting_independent_evidence",
        }, overwrite=args.overwrite)

        ok += 1
        grounded = sum(1 for s in SECTIONS if (sections.get(s) or {}).get("grounded"))
        print(f"  [dossier] ok  {aid[:24]}..  {grounded}/7 sections grounded -> {dossier_path.name}")

    print(f"dossiers: ok={ok} fail={fail} skipped={skipped}")
    return 0 if fail == 0 else 1


def build_readiness_rows() -> int:
    """Deterministic readiness rows for actions with no hand-curated entry."""
    anchor_index = E._load_anchor_index()
    hdr, rows = _read_csv(READY_CSV)
    have = {r["action_id"] for r in rows}
    added = 0
    for a in E._load_actions():
        if (a.get("status") or "").lower() != "active" or a["action_id"] in have:
            continue
        aid = a["action_id"]
        anchor_ok = anchor_index.get(aid, {}).get("fetch_status") in ("ok", "ok_cached")
        meta_ok = bool(a.get("anchor_url") and a.get("anchor_hash") and a.get("metadata_title"))
        drep_ok = any(E._to_float(a.get(k)) > 0 for k in ("drep_yes_pct", "drep_no_pct", "drep_abstain_pct"))
        timeline_ok = bool(a.get("expires_after_epoch") or a.get("expiration_epoch"))
        rows.append({
            "action_id": aid, "action_type": a.get("action_type"),
            "abstain_reason_code": "",
            "anchor_pinned": "yes" if anchor_ok else "no",
            "anchor_fallback_packet": "no",
            "action_metadata_complete": "yes" if meta_ok else "no",
            "timeline_defined": "yes" if timeline_ok else "no",
            "governance_rules_clear": "yes",
            "budget_envelope_clear": "unknown", "milestones_acceptance_clear": "unknown",
            "disbursement_controls_clear": "unknown", "sustainability_path_clear": "unknown",
            "risk_profile_complete": "no",
            "drep_distribution_available": "yes" if drep_ok else "no",
            "hard_blocker": "no", "readiness_score": "",
            "minimum_new_evidence_to_decide": "",
            "owner": OWNER, "status": "machine_derived",
        })
        added += 1
    if added:
        _write_csv(READY_CSV, hdr, rows)
    print(f"readiness: {added} deterministic rows added")
    return 0


def approve(action_id: str, approver: str) -> int:
    hdr, rows = _read_csv(DEEP_CSV)
    row = next((r for r in rows if r.get("action_id") == action_id), None)
    if row is None:
        print(f"no dossier row for {action_id}")
        return 1
    missing = [s for s in SECTIONS if row.get(f"{s}_complete") != "yes"]
    if missing:
        print(f"REFUSED: sections not grounded: {', '.join(missing)} — review/complete the dossier first")
        return 1
    if not (DOSSIER_DIR / f"{action_id}.md").exists():
        print("REFUSED: dossier document missing")
        return 1
    row["dossier_complete"] = "yes"
    row["status"] = "approved"
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    row["analyst_notes"] = (row.get("analyst_notes", "") + f" | APPROVED by {approver} {stamp}").strip(" |")
    _write_csv(DEEP_CSV, hdr, rows)
    receipt = DOSSIER_DIR / f"{action_id}.receipt.json"
    if receipt.exists():
        r = json.loads(receipt.read_text(encoding="utf-8"))
        r["review_status"] = "approved"
        r["approved_by"] = approver
        r["approved_at_utc"] = stamp
        receipt.write_text(json.dumps(r, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"APPROVED {action_id} by {approver} — engine treasury bar now uses the ±0.06 dossier threshold for this action")
    return 0


def list_queue() -> int:
    _, rows = _read_csv(DEEP_CSV)
    pending = [r for r in rows if r.get("status") == "drafted_pending_review"]
    for r in pending:
        grounded = sum(1 for s in SECTIONS if r.get(f"{s}_complete") == "yes")
        print(f"pending  {r['action_id']}  {grounded}/7 grounded")
    print(f"{len(pending)} dossier(s) pending review")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=list(BACKENDS), default="codex")
    ap.add_argument("--missing-only", action="store_true",
                    help="only actions with no deep_research_dossiers row (default behavior for cron)")
    ap.add_argument("--overwrite", action="store_true",
                    help="allow replacing rows this pipeline previously wrote (never hand-curated ones)")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--approve", metavar="ACTION_ID", help="mark a reviewed dossier complete")
    ap.add_argument("--approver", default=os.environ.get("USER", "operator"))
    ap.add_argument("--list", action="store_true", help="show the review queue")
    args = ap.parse_args()

    if args.list:
        return list_queue()
    if args.approve:
        return approve(args.approve, args.approver)
    rc = build(args)
    build_readiness_rows()
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
