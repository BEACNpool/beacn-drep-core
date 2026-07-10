#!/usr/bin/env python3
"""Independent dossier verification + agentic approval (doctrine v1.3.0).

Replaces the human --approve gate per owner directive 2026-07-04: the workflow
is fully agentic, and the human role is random spot-checks of the published
record on the website. To earn `dossier_complete: yes` a machine-drafted
dossier must pass BOTH:

  Deterministic gates
    * all 7 sections grounded in the dossier CSV row
    * the pinned anchor's sha256 still matches the drafting receipt
      (the dossier verifies against exactly the document it was drafted from)
    * financial + risk extraction rows exist for the action

  Independent verification pass (separate model call from the drafting call)
    * every FACT in the dossier is re-checked against the same admitted
      material (anchor text, on-chain context, doctrine)
    * >= 90% of facts verified as supported (doctrine threshold)
    * zero material discrepancies (anchor-contradicted or invented specifics)

Everything is recorded: per-fact verdicts, ratios, and prompt/output hashes go
into the dossier receipt (published with the web artifacts), and the CSV row
becomes status `approved_agentic`. A failed verification keeps
`dossier_complete: no` — failure can only preserve the strict posture, never
loosen anything.

Kill switch: BEACN_DOSSIER_AUTOAPPROVE_DISABLED=1 (verification still runs and
records its findings; approval is withheld).

Usage:
  python3 scripts/verify_dossiers.py --backend codex          # all pending
  python3 scripts/verify_dossiers.py --action gov_action1...  # one action
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from beacn_drep import engine as E, llm  # noqa: E402
from beacn_drep.anchors import load_anchor_text  # noqa: E402
import build_deep_research_dossiers as drafting  # noqa: E402

DS = drafting.DS
DOSSIER_DIR = drafting.DOSSIER_DIR
DEEP_CSV = drafting.DEEP_CSV
SECTIONS = drafting.SECTIONS

MIN_SUPPORT_RATIO = 0.90
MAX_MATERIAL_DISCREPANCIES = 0

VERIFY_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "fact_verdicts": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "fact": {"type": "string"},
                    "verdict": {"type": "string", "enum": ["supported", "contradicted", "not_found"]},
                    "note": {"type": "string"},
                },
                "required": ["fact", "verdict", "note"],
            },
        },
        "material_discrepancies": {
            "type": "array",
            "items": {"type": "string"},
            "description": "facts the source material CONTRADICTS, or invented figures/names/commitments",
        },
        "summary": {"type": "string"},
    },
    "required": ["fact_verdicts", "material_discrepancies", "summary"],
}

VERIFY_SYSTEM = (
    "You are an INDEPENDENT auditor for an autonomous Cardano DRep. A separate analyst drafted "
    "a diligence dossier; your only job is to re-check each of its FACT statements against the "
    "supplied source material (the proposal's anchor document, the on-chain context block, and "
    "the doctrine text). You did not write the dossier and you must not defend it.\n"
    "For each fact return exactly one verdict:\n"
    "  supported    — the source material states or directly entails it (numbers must match)\n"
    "  contradicted — the source material says otherwise (ALWAYS a material discrepancy)\n"
    "  not_found    — the source material neither supports nor contradicts it\n"
    "List a material discrepancy for every contradicted fact and for any invented specific "
    "(a figure, name, date, or commitment that appears in the fact but nowhere in the material). "
    "Vague wording or paraphrase is NOT material. Be strict on numbers, quotes, and named "
    "entities; be fair on phrasing."
)


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _extract_facts(dossier_md: str) -> list[str]:
    facts: list[str] = []
    in_facts = False
    for line in dossier_md.splitlines():
        if line.startswith("## "):
            in_facts = line.strip() == "## FACTS (document/on-chain supported)"
            continue
        if in_facts and line.startswith("- "):
            facts.append(line[2:].strip())
    return [f for f in facts if f and f != "(none extracted)"]


def call_codex(prompt: str) -> dict:
    with tempfile.TemporaryDirectory() as td:
        schema_f = Path(td) / "schema.json"
        out_f = Path(td) / "out.json"
        schema_f.write_text(json.dumps(VERIFY_SCHEMA), encoding="utf-8")
        cmd = [
            drafting.CODEX_BIN, "exec", "--skip-git-repo-check", "-s", "read-only",
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


def verify_one(action: dict, row: dict, backend: str, autoapprove: bool) -> tuple[str, dict]:
    """Returns (outcome, verification_record). Outcome: approved_agentic |
    verification_failed | gate_failed | error."""
    aid = action["action_id"]
    record: dict = {
        "verified_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "backend": backend,
        "model": os.environ.get("BEACN_CODEX_MODEL", "gpt-5.5") if backend == "codex" else "claude-cli",
        "thresholds": {"min_fact_support_ratio": MIN_SUPPORT_RATIO,
                       "max_material_discrepancies": MAX_MATERIAL_DISCREPANCIES},
        "gates": {},
    }

    # --- deterministic gates -------------------------------------------------
    grounded_ok = all(row.get(f"{s}_complete") == "yes" for s in SECTIONS)
    record["gates"]["sections_grounded_7of7"] = grounded_ok

    dossier_path = DOSSIER_DIR / f"{aid}.md"
    receipt_path = DOSSIER_DIR / f"{aid}.receipt.json"
    record["gates"]["dossier_and_receipt_present"] = dossier_path.exists() and receipt_path.exists()
    if not (dossier_path.exists() and receipt_path.exists()):
        return "gate_failed", record
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    drafter_identity = (str(receipt.get("backend") or "").lower(),
                        str(receipt.get("model") or "").lower())
    verifier_identity = (str(record["backend"]).lower(), str(record["model"]).lower())
    independent_model = drafter_identity != verifier_identity
    record["gates"]["different_model_from_drafter"] = independent_model
    if not independent_model:
        record["note"] = (
            "Verification must use a different backend/model from dossier drafting; "
            f"both resolved to {verifier_identity}."
        )
        return "gate_failed", record

    anchor_text, _meta = load_anchor_text(aid)
    anchor_match = bool(anchor_text) and _sha(anchor_text) == receipt.get("anchor_sha256")
    record["gates"]["anchor_sha256_matches_draft"] = anchor_match

    _, fin_rows = drafting._read_csv(drafting.FIN_CSV)
    _, risk_rows = drafting._read_csv(drafting.RISK_CSV)
    rows_ok = any(r.get("action_id") == aid for r in fin_rows) and \
        any(r.get("action_id") == aid for r in risk_rows)
    record["gates"]["financial_and_risk_rows_present"] = rows_ok

    if not (grounded_ok and anchor_match and rows_ok):
        return "gate_failed", record

    # --- independent verification pass ---------------------------------------
    facts = _extract_facts(dossier_path.read_text(encoding="utf-8"))
    record["fact_count"] = len(facts)
    if not facts:
        return "gate_failed", record

    doctrine = E._load_doctrine_for(action.get("action_type"))
    # Verify against the drafter's FROZEN inputs where the receipt has them —
    # live ballot counts and flow figures move between draft and verify, and a
    # moved snapshot must not read as a fabricated fact.
    onchain = receipt.get("onchain_context") or drafting._onchain_context(action)
    snapshot_note = "" if receipt.get("onchain_context") else (
        "NOTE: the on-chain context below was re-fetched AFTER drafting; ballot counts and "
        "flow figures are moving snapshots. A differing or absent count is not_found, not "
        "contradicted, and must NOT be listed as a material discrepancy — only figures "
        "misquoted from the anchor document or invented named commitments are material.\n")
    metadata_block = (
        f"Action id: {aid}\n"
        f"Action type: {action.get('action_type')}\n"
        f"Title: {action.get('metadata_title') or '(none)'}\n"
        f"Treasury amount (lovelace): {action.get('treasury_amount_lovelace') or '(none)'}\n"
        f"Proposed epoch: {action.get('proposed_epoch')}  "
        f"Expires after: {action.get('expires_after_epoch') or action.get('expiration_epoch')}\n"
    )
    prompt = (
        VERIFY_SYSTEM
        + "\n\n========================================\n"
        + "SOURCE MATERIAL 0 — ON-CHAIN ACTION METADATA (from the governance export, "
        + "part of the drafter's admitted inputs):\n-----8<-----\n" + metadata_block + "-----8<-----\n\n"
        + "SOURCE MATERIAL 1 — ON-CHAIN CONTEXT:\n-----8<-----\n" + snapshot_note + onchain + "\n-----8<-----\n\n"
        + "SOURCE MATERIAL 2 — DOCTRINE:\n-----8<-----\n"
        + llm._truncate(doctrine.get("text") or "(none)", 6000) + "\n-----8<-----\n\n"
        + "SOURCE MATERIAL 3 — ANCHOR DOCUMENT (verbatim):\n-----8<-----\n"
        + llm._truncate(anchor_text, 48000) + "\n-----8<-----\n\n"
        + "DOSSIER FACTS TO VERIFY:\n"
        + "\n".join(f"{i+1}. {f}" for i, f in enumerate(facts))
        + "\n\nReturn the verification JSON."
    )
    data = BACKENDS[backend](prompt)

    verdicts = data.get("fact_verdicts") or []
    supported = sum(1 for v in verdicts if v.get("verdict") == "supported")
    contradicted = [v for v in verdicts if v.get("verdict") == "contradicted"]
    material = list(data.get("material_discrepancies") or [])
    for v in contradicted:  # a contradiction is always material, whatever the model listed
        if v.get("fact") not in material:
            material.append(f"contradicted: {v.get('fact')}")
    filtered_legacy: list[str] = []
    if not receipt.get("onchain_context"):
        # Legacy dossier drafted before receipts froze the on-chain context: the
        # verifier sees moved ballot/flow snapshots. Deterministically exclude
        # discrepancies about those time-varying figures (recorded, auditable);
        # anchor misquotes and invented commitments always stay material.
        _snapshot_markers = ("ballot", "vote count", "yes=", "no=", "abstain=",
                             "drep_yes", "treasury flow", "inflow", "withdrawals ")
        keep = []
        for m in material:
            if any(k in m.lower() for k in _snapshot_markers):
                filtered_legacy.append(m)
            else:
                keep.append(m)
        material = keep
    ratio = supported / len(verdicts) if verdicts else 0.0

    record.update({
        "verdicts_returned": len(verdicts),
        "supported": supported,
        "contradicted": len(contradicted),
        "not_found": sum(1 for v in verdicts if v.get("verdict") == "not_found"),
        "support_ratio": round(ratio, 4),
        "material_discrepancies": material,
        "filtered_legacy_snapshot_items": filtered_legacy,
        "summary": data.get("summary", ""),
        "fact_verdicts": verdicts,
        "prompt_sha256": _sha(prompt),
        "output_sha256": _sha(json.dumps(data, sort_keys=True)),
    })

    passed = (
        len(verdicts) == len(facts)
        and ratio >= MIN_SUPPORT_RATIO
        and len(material) <= MAX_MATERIAL_DISCREPANCIES
    )
    record["passed"] = passed
    if not passed:
        return "verification_failed", record
    if not autoapprove:
        record["note"] = "verification passed; approval withheld (BEACN_DOSSIER_AUTOAPPROVE_DISABLED=1)"
        return "verification_failed", record
    return "approved_agentic", record


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=list(BACKENDS), default="codex")
    ap.add_argument("--action", help="verify a single action id")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    autoapprove = os.environ.get("BEACN_DOSSIER_AUTOAPPROVE_DISABLED", "0") != "1"
    actions = {a["action_id"]: a for a in E._load_actions()}
    hdr, rows = drafting._read_csv(DEEP_CSV)

    pending = [r for r in rows
               if r.get("status") in ("drafted_pending_review", "verification_failed")
               and r.get("dossier_complete") != "yes"
               and (not args.action or r.get("action_id") == args.action)]
    if args.limit:
        pending = pending[:args.limit]

    ok = failed = errors = 0
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for row in pending:
        aid = row["action_id"]
        action = actions.get(aid)
        if action is None or (action.get("status") or "").lower() != "active":
            continue
        try:
            outcome, record = verify_one(action, row, args.backend, autoapprove)
        except Exception as e:  # noqa: BLE001 - continue with the rest, fail closed
            errors += 1
            print(f"  [verify] ERROR {aid[:24]}..  {type(e).__name__}: {str(e)[:160]}")
            continue

        receipt_path = DOSSIER_DIR / f"{aid}.receipt.json"
        if receipt_path.exists():
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            receipt["verification"] = record
            receipt["review_status"] = outcome
            receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n",
                                    encoding="utf-8")

        if outcome == "approved_agentic":
            row["dossier_complete"] = "yes"
            row["status"] = "approved_agentic"
            row["analyst_notes"] = (row.get("analyst_notes", "") +
                                    f" | AGENTIC APPROVAL {stamp}: {record['supported']}/"
                                    f"{record['fact_count']} facts verified "
                                    f"(ratio {record['support_ratio']}), 0 material discrepancies"
                                    ).strip(" |")
            ok += 1
            print(f"  [verify] APPROVED {aid[:24]}..  {record['supported']}/{record['fact_count']} "
                  f"supported (ratio {record['support_ratio']})")
        else:
            row["status"] = "verification_failed" if outcome != "gate_failed" else "drafted_pending_review"
            failed += 1
            why = "; ".join((record.get("material_discrepancies") or [])[:2]) or \
                json.dumps(record.get("gates", {}))
            print(f"  [verify] HELD {aid[:24]}..  {outcome}: "
                  f"ratio={record.get('support_ratio', 'n/a')} {why[:140]}")

    drafting._write_csv(DEEP_CSV, hdr, rows)
    print(f"verification: approved={ok} held={failed} errors={errors} "
          f"(autoapprove={'on' if autoapprove else 'OFF'})")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
