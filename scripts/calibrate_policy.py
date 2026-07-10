#!/usr/bin/env python3
"""Measure false-YES/false-NO rates from independently assessed outcomes."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTCOMES = ROOT.parent / "beacn-drep-resources" / "data" / "history" / "governance_outcomes.csv"
PUBLIC = ROOT / "data" / "output" / "public" / "vote_rationale_report.json"
REPORT = ROOT / "data" / "output" / "policy_calibration.json"


def main() -> int:
    with OUTCOMES.open(newline="", encoding="utf-8") as f:
        outcomes = {r["action_id"]: r for r in csv.DictReader(f)
                    if r.get("status") == "independently_verified"}
    decisions = {}
    if PUBLIC.exists():
        for row in json.loads(PUBLIC.read_text(encoding="utf-8")).get("items", []):
            decisions[row.get("action_id")] = row.get("vote")
    paired = [(decisions[aid], row["outcome_label"]) for aid, row in outcomes.items() if aid in decisions]
    false_yes = sum(v == "YES" and o in {"wasteful", "failed"} for v, o in paired)
    false_no = sum(v == "NO" and o in {"beneficial", "delivered"} for v, o in paired)
    report = {
        "schema_version": "policy-calibration-v1",
        "verified_outcomes": len(outcomes),
        "paired_decisions": len(paired),
        "false_yes": false_yes,
        "false_no": false_no,
        "false_yes_rate": round(false_yes / len(paired), 4) if paired else None,
        "false_no_rate": round(false_no / len(paired), 4) if paired else None,
        "status": "calibrated" if len(paired) >= 20 else "insufficient_verified_outcomes",
        "minimum_sample": 20,
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
