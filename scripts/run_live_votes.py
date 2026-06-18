#!/usr/bin/env python3
"""Daily gated auto-voter for the BEACN automated DRep.

Conservative by policy: only **ABSTAIN** recommendations are broadcast
automatically. Directional (YES/NO) decisions that pass every gate are HELD for
operator review rather than auto-submitted, because a directional mainnet vote
is high-consequence and the engine's directional logic is still stabilizing.

The widenable set is BEACN_AUTO_DIRECTIONS (default "ABSTAIN"). Even then, the
underlying adapter fails closed: it submits only with live=True AND
BEACN_VOTING_LIVE=1 and only after all 8 gates pass (fresh data, votable
recommendation, replay, published+reachable rationale anchor, action still
active and unvoted by this DRep, vote-only tx, fee + per-run caps).

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
AUTO = {x.strip().upper() for x in os.environ.get("BEACN_AUTO_DIRECTIONS", "ABSTAIN").split(",") if x.strip()}


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
        # The adapter intentionally allows REVISING an existing on-chain vote when
        # the recommendation changed. Changing a vote already on the public record
        # is at least as consequential as a fresh directional vote, so never do it
        # automatically — only cast brand-new votes on unvoted actions.
        is_revision = "revision" in str(shadow.get("action_live_reason", "")).lower()
        entry = {
            "action_id": shadow.get("action_id"),
            "recommendation": rec,
            "gates_ok": gates_ok,
        }
        if gates_ok and rec in AUTO and not is_revision:
            if live:
                res = prepare_vote(d, live=True)
                entry["status"] = res.get("status")
                entry["submitted"] = res.get("submitted")
                entry["transaction_hash"] = res.get("transaction_hash")
                if res.get("submitted"):
                    voted += 1
            else:
                entry["status"] = "would_submit (shadow)"
        elif gates_ok and is_revision:
            entry["status"] = f"HELD_FOR_REVIEW (vote revision — {shadow.get('action_live_reason')})"
        elif gates_ok and rec not in AUTO:
            entry["status"] = "HELD_FOR_REVIEW (directional — not auto-submitted)"
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
