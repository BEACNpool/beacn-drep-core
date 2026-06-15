#!/usr/bin/env python3
"""Run the guarded signing adapter over engine output runs.

SHADOW by default: builds + signs nothing is submitted unless --live is passed
AND BEACN_VOTING_LIVE=1 is set in the environment. Prints one JSON report per run.

  python scripts/sign_votes_shadow.py            # shadow over recent runs
  python scripts/sign_votes_shadow.py --run-dir data/output/<run>
  BEACN_VOTING_LIVE=1 python scripts/sign_votes_shadow.py --live   # real votes
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from beacn_drep.adapters.cardano_cli_adapter import prepare_vote  # noqa: E402

OUT = ROOT / "data" / "output"


def main() -> int:
    args = sys.argv[1:]
    live = "--live" in args
    if "--run-dir" in args:
        runs = [Path(args[args.index("--run-dir") + 1])]
    else:
        limit = int(os.environ.get("BEACN_SHADOW_LIMIT", "5"))
        runs = sorted(
            (d for d in OUT.iterdir()
             if d.is_dir() and d.name != "public" and (d / "rationale.json").exists()),
            key=lambda d: d.stat().st_mtime, reverse=True,
        )[:limit]

    voted = 0
    for d in runs:
        os.environ["BEACN_VOTES_THIS_RUN"] = str(voted)
        report = prepare_vote(d, live=live)
        print(json.dumps(report, indent=2, default=str))
        if report.get("submitted"):
            voted += 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
