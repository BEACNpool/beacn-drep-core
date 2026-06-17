#!/usr/bin/env python3
"""Build an operator intervention queue for active governance actions.

The queue is intentionally local/read-only. It does not query keys, build
transactions, or submit votes. It maps active actions into the intervention
lanes documented in docs/OPERATOR_INTERVENTION_PLAN.md.
"""

from __future__ import annotations

import csv
import json
import os
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT.parent / "beacn-drep-resources"
ACTIVE = RESOURCES / "data" / "input" / "governance" / "governance_actions_active.csv"
OUT = ROOT / "data" / "output"
QUEUE_JSON = OUT / "operator_intervention_queue.json"
QUEUE_MD = OUT / "operator_intervention_queue.md"


def read_active() -> list[dict]:
    with ACTIVE.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def latest_run(action_id: str) -> tuple[Path | None, dict | None]:
    candidates = sorted(
        (
            d for d in OUT.glob(f"{action_id}-*")
            if d.is_dir() and (d / "rationale.json").exists()
        ),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not candidates:
        return None, None
    path = candidates[0]
    return path, json.loads((path / "rationale.json").read_text(encoding="utf-8"))


def latest_submitted_receipt(action_id: str) -> dict | None:
    candidates = sorted(
        (
            p for p in OUT.glob(f"{action_id}-*/vote_receipt.json")
            if p.is_file()
        ),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    for path in candidates:
        try:
            receipt = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if receipt.get("submitted") and (receipt.get("status") or "").lower() == "submitted":
            receipt["run_id"] = path.parent.name
            return receipt
    return None


def current_epoch(actions: list[dict]) -> int | None:
    env = os.environ.get("CARDANO_CURRENT_EPOCH")
    if env:
        try:
            return int(env)
        except ValueError:
            pass
    epochs = []
    for row in actions:
        try:
            epochs.append(int(row.get("proposed_epoch") or ""))
        except ValueError:
            pass
    return max(epochs) if epochs else None


def lane_for(
    action: dict,
    run_dir: Path | None,
    rationale: dict | None,
    receipt: dict | None,
    epoch: int | None,
) -> tuple[str, str]:
    if rationale is None:
        return "NEEDS_DECISION_RUN", "No local rationale run found for this active action."

    rec = (rationale.get("recommendation") or "").upper()
    receipt_rec = ((receipt or {}).get("recommendation") or "").upper()
    if receipt_rec and receipt_rec == rec:
        return "DONE", "Latest submitted vote matches the latest local recommendation."
    if receipt_rec and receipt_rec != rec:
        return "VOTE_REVISION", f"Existing submitted vote is {receipt_rec}; latest recommendation is {rec}."

    freshness = rationale.get("freshness") or {}
    if freshness.get("is_stale"):
        return "DATA_FAILURE", "Governance snapshot is stale; refresh data before voting."

    if rec == "NEEDS_MORE_INFO":
        return "NEEDS_RESEARCH", rationale.get("needs_more_info_reason_code") or "Research dossier incomplete."

    if rec == "ABSTAIN":
        return "POLICY_REVIEW", rationale.get("abstain_reason_code") or "Rule threshold unmet or policy hold."

    if rec in {"YES", "NO"} and not (
        rationale.get("rationale_anchor_url") and rationale.get("rationale_anchor_hash")
    ):
        return "PUBLISH_RATIONALE", "Directional vote exists but published rationale URL/hash is not recorded."

    if epoch is not None:
        try:
            expires = int(action.get("expiration_epoch") or "")
            if expires - epoch <= 1:
                return "EXPIRY_PRESSURE", f"Expires in {expires - epoch} epoch(s); confirm final action."
        except ValueError:
            pass

    return "READY_FOR_SHADOW", "Decision has passed local classification; run replay and shadow signing."


def main() -> int:
    actions = read_active()
    epoch = current_epoch(actions)
    rows = []
    for action in actions:
        run_dir, rationale = latest_run(action["action_id"])
        receipt = latest_submitted_receipt(action["action_id"])
        lane, reason = lane_for(action, run_dir, rationale, receipt, epoch)
        rows.append({
            "lane": lane,
            "reason": reason,
            "action_id": action["action_id"],
            "title": action.get("metadata_title") or "",
            "action_type": action.get("action_type") or "",
            "expires_epoch": action.get("expiration_epoch") or "",
            "recommendation": (rationale or {}).get("recommendation"),
            "operator_review_required": bool((rationale or {}).get("operator_review_required")),
            "run_id": run_dir.name if run_dir else None,
            "submitted_recommendation": (receipt or {}).get("recommendation"),
            "submitted_tx": (receipt or {}).get("transaction_hash"),
            "submitted_at": (receipt or {}).get("submitted_at"),
        })

    order = {
        "VOTE_REVISION": 0,
        "DATA_FAILURE": 0,
        "EXPIRY_PRESSURE": 1,
        "PUBLISH_RATIONALE": 3,
        "POLICY_REVIEW": 4,
        "NEEDS_RESEARCH": 5,
        "NEEDS_DECISION_RUN": 6,
        "READY_FOR_SHADOW": 7,
        "DONE": 99,
    }
    rows.sort(key=lambda r: (order.get(r["lane"], 98), int(r["expires_epoch"] or 9999), r["title"]))
    active_rows = [r for r in rows if r["lane"] != "DONE"]

    output = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "current_epoch": epoch,
        "counts": {lane: sum(1 for r in rows if r["lane"] == lane) for lane in sorted({r["lane"] for r in rows})},
        "items": active_rows,
        "done": [r for r in rows if r["lane"] == "DONE"],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    QUEUE_JSON.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Operator Intervention Queue",
        "",
        f"- generated_at: `{output['generated_at']}`",
        f"- current_epoch: `{epoch if epoch is not None else 'unknown'}`",
        "",
        "## Counts",
        "",
    ]
    for lane, count in sorted(output["counts"].items()):
        lines.append(f"- {lane}: {count}")
    lines.extend(["", "## Items", ""])
    for row in rows:
        if row["lane"] == "DONE":
            continue
        lines.extend([
            f"### {row['lane']} — {row['title'] or row['action_id']}",
            f"- action_id: `{row['action_id']}`",
            f"- type: `{row['action_type']}`",
            f"- expires_epoch: `{row['expires_epoch']}`",
            f"- recommendation: `{row['recommendation']}`",
            f"- run_id: `{row['run_id']}`",
            f"- submitted_recommendation: `{row['submitted_recommendation'] or ''}`",
            f"- submitted_tx: `{row['submitted_tx'] or ''}`",
            f"- reason: {row['reason']}",
            "",
        ])
    QUEUE_MD.write_text("\n".join(lines), encoding="utf-8")
    print(str(QUEUE_MD))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
