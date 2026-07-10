#!/usr/bin/env python3
"""Fail closed when public verdict surfaces disagree with the binding record."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from beacn_drep.llm import message_matches_recommendation  # noqa: E402

PUBLIC = ROOT / "data/output/public"
WEB = Path(os.environ.get("BEACN_WEB_REPO", ROOT.parent / "beacn-drep-web"))
VALID = {"YES", "NO", "ABSTAIN", "NEEDS_MORE_INFO"}


def verdict(value: object) -> str:
    value = str(value or "").upper()
    return {"VOTEYES": "YES", "VOTENO": "NO", "ABSTAIN": "ABSTAIN"}.get(value, value)


def main() -> int:
    errors: list[str] = []
    actions = json.loads((PUBLIC / "actions.json").read_text()).get("items", [])
    expected = {row["action_id"]: verdict(row.get("decision")) for row in actions}
    statements = json.loads((PUBLIC / "statements.json").read_text())

    for aid, decision in expected.items():
        if decision not in VALID:
            errors.append(f"{aid}: invalid index decision {decision!r}")
            continue
        path = PUBLIC / "actions" / f"{aid}.json"
        if not path.exists():
            errors.append(f"{aid}: missing detail artifact")
            continue
        detail = json.loads(path.read_text())
        detail_vote = verdict((detail.get("decision") or {}).get("vote"))
        proof_vote = verdict((detail.get("proof_of_vote") or {}).get("vote"))
        if detail_vote != decision or proof_vote != decision:
            errors.append(f"{aid}: index={decision}, detail={detail_vote}, proof={proof_vote}")
        summary = (detail.get("rationale") or {}).get("summary", "")
        if not summary or not message_matches_recommendation(summary, decision):
            errors.append(f"{aid}: rationale summary contradicts {decision}")
        statement = statements.get(aid) or {}
        if statement:
            if verdict(statement.get("decision")) != decision:
                errors.append(f"{aid}: statement decision contradicts {decision}")
            if not message_matches_recommendation(statement.get("statement", ""), decision):
                errors.append(f"{aid}: statement text contradicts {decision}")
        if detail.get("type") == "TreasuryWithdrawals":
            contract = detail.get("decision_contract") or {}
            if not contract or contract.get("model_vote_influence") != 0:
                errors.append(f"{aid}: treasury decision contract missing or model influence nonzero")

    status_path = WEB / "status.json"
    if status_path.exists():
        for row in json.loads(status_path.read_text()).get("actions", []):
            aid = row.get("cip129_action_id")
            if aid in expected and row.get("recommendation") and verdict(row["recommendation"]) != expected[aid]:
                errors.append(f"{aid}: status recommendation contradicts public decision")
            # our_vote is deliberately excluded: it is historical on-chain state
            # and may differ from a newer recommendation. The UI labels both.

    if errors:
        print("PUBLIC CONSISTENCY FAILURE")
        print("\n".join(f"- {item}" for item in errors))
        return 1
    print(f"public consistency: {len(expected)} decisions agree across index, detail, rationale, statements, and status")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
