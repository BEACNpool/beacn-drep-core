#!/usr/bin/env python3
"""Query governance actions from the resources CSV snapshot."""
import argparse
import csv
import json
from pathlib import Path

from ..config import RESOURCES_REPO

CSV_PATH = RESOURCES_REPO / "data" / "input" / "governance" / "governance_actions_all.csv"


def _load_rows():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--status")
    ap.add_argument("--type")
    ap.add_argument("--action-id")
    ap.add_argument("--search")
    ap.add_argument("--limit", type=int, default=50)
    ap.add_argument("--format", choices=["json", "table"], default="table")
    args = ap.parse_args()

    rows = _load_rows()
    out = []
    for r in rows:
        if args.status and (r.get("status", "").lower() != args.status.lower()):
            continue
        if args.type and args.type.lower() not in (r.get("action_type", "").lower()):
            continue
        if args.action_id and args.action_id not in r.get("action_id", ""):
            continue
        if args.search:
            hay = " ".join([r.get("action_id", ""), r.get("action_type", ""), r.get("anchor_url", ""), r.get("proposer_address", "")]).lower()
            if args.search.lower() not in hay:
                continue
        out.append(r)
        if len(out) >= args.limit:
            break

    if args.format == "json":
        print(json.dumps(out, indent=2))
        return

    print(f"results={len(out)}")
    for r in out:
        print(f"{r.get('action_id')} | {r.get('action_type')} | {r.get('status')} | epoch={r.get('proposed_epoch')} | flag={r.get('flag_score')}")


if __name__ == "__main__":
    main()
