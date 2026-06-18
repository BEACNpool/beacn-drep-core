#!/usr/bin/env python3
"""Daily auto-voter for the BEACN automated DRep (fully agentic).

Per doctrine the DRep is fully agentic: it submits whatever the deterministic
engine recommends (YES / NO / ABSTAIN), and revises an existing on-chain vote
when the latest recommendation differs. No mandatory operator-review gate.

The underlying adapter still fails closed: it submits only with live=True AND
BEACN_VOTING_LIVE=1 and only after all 8 gates pass (fresh data, votable
recommendation, replay, published+reachable rationale anchor, action active
[unvoted, or a recommendation revision], vote-only tx, fee + per-run caps).

Safety knobs: BEACN_AUTO_DIRECTIONS (default "YES,NO,ABSTAIN") narrows which
recommendations may auto-submit; BEACN_AUTOVOTE_DISABLED=1 is the kill-switch
(honored by ops/run_daily_vote.sh).

  PYTHONPATH=src python3 scripts/run_live_votes.py            # shadow (no submit)
  BEACN_VOTING_LIVE=1 PYTHONPATH=src python3 scripts/run_live_votes.py --live
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from beacn_drep.adapters.cardano_cli_adapter import prepare_vote  # noqa: E402

OUT = ROOT / "data" / "output"
AUTO = {x.strip().upper() for x in os.environ.get("BEACN_AUTO_DIRECTIONS", "YES,NO,ABSTAIN").split(",") if x.strip()}


def latest_runs() -> list[Path]:
    selected: dict[str, Path] = {}
    for d in OUT.iterdir():
        rj = d / "rationale.json"
        if not d.is_dir() or d.name == "public" or not rj.exists():
            continue
        try:
            action_id = json.loads(rj.read_text()).get("action_id")
        except Exception:
            continue
        if not action_id:
            continue
        cur = selected.get(action_id)
        if cur is None or rj.stat().st_mtime_ns > (cur / "rationale.json").stat().st_mtime_ns:
            selected[action_id] = d
    return list(selected.values())


def main() -> int:
    live = "--live" in sys.argv
    voted = 0
    report = []
    for d in latest_runs():
        os.environ["BEACN_VOTES_THIS_RUN"] = str(voted)
        rec = (json.loads((d / "rationale.json").read_text()).get("recommendation") or "").upper()
        shadow = prepare_vote(d, live=False)
        gates_ok = bool(shadow.get("gates")) and all(shadow["gates"].values())
        # Revisions (changing an existing on-chain vote when the recommendation
        # changed) are permitted under the fully-agentic policy; flagged for audit.
        is_revision = "revision" in str(shadow.get("action_live_reason", "")).lower()
        entry = {
            "action_id": shadow.get("action_id"),
            "recommendation": rec,
            "gates_ok": gates_ok,
            "revision": is_revision,
        }
        if gates_ok and rec in AUTO:
            if live:
                res = prepare_vote(d, live=True)
                entry["status"] = res.get("status")
                entry["submitted"] = res.get("submitted")
                entry["transaction_hash"] = res.get("transaction_hash")
                if res.get("submitted"):
                    voted += 1
            else:
                entry["status"] = "would_submit (shadow)"
        elif gates_ok and rec not in AUTO:
            entry["status"] = f"skipped (recommendation {rec} not in auto-set {sorted(AUTO)})"
        else:
            entry["status"] = "skip"
            entry["reasons"] = shadow.get("reasons")
        report.append(entry)

    print(json.dumps(
        {"live": live, "auto_directions": sorted(AUTO), "submitted": voted, "runs": report},
        indent=2, default=str,
    ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
