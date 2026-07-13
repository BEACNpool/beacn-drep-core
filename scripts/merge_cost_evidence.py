#!/usr/bin/env python3
"""Merge independent cost-comparable research into the existing value-evidence packets.

Why this exists: benefit and delivery were independently verified for the open treasury asks, but
`cost_compared_to_market` and `output_priced` came back "unknown" on 18 of 24 packets. The engine's
cost floor (0.40) therefore could not be met, so a dozen proposals with strong verified benefit sat
at NEEDS_MORE_INFO — BEACN knew what the work was worth but not whether the price was fair, and
correctly refused to vote either way.

Rules, in order of importance:

  1. FILL ONLY. A field already carrying a directional value ("yes"/"no") from the earlier
     independent pass is NEVER overwritten by this merge. New research adds knowledge; it does not
     get to relitigate a verified finding. Only "unknown" (or absent) fields are filled.

  2. NEVER MANUFACTURE A NO. A researcher's "unknown" is written as "unknown". Under doctrine
     missing evidence can never become negative evidence, and the cheapest way to break that rule
     would be to quietly treat "we couldn't find comparables" as "the price is bad".

  3. SOURCES OR IT DIDN'T HAPPEN. A directional value with no public https source is demoted to
     "unknown" here, and pin_value_evidence_sources.py then FETCHES and SHA-256 hashes every URL
     that survives — an invented, dead, or auth-walled citation cannot become evidence.

Run: merge_cost_evidence.py [--dry-run]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

WORKSPACE = Path(__file__).resolve().parents[2]
PACKETS = WORKSPACE / "beacn-drep-resources/data/input/governance/decision_support/value_evidence"
RESULTS = Path("/tmp/claude-1000/cost")

FIELDS = ("cost_compared_to_market", "output_priced", "material_duplication")
VALID = {"yes", "no", "unknown"}

# Every source needs the snapshot path the pinner will fetch it into. Same scheme the original
# packet writer used, so old and new sources are indistinguishable downstream.
SNAP_REL = "data/input/governance/decision_support/value_evidence/snapshots"


def snapshot_path(action_id: str, url: str) -> str:
    host = (urlparse(url).hostname or "x").replace(".", "-")
    digest = hashlib.sha256(url.encode()).hexdigest()[:10]
    aid = re.sub(r"[^0-9a-zA-Z]", "", action_id)[:12]
    return f"{SNAP_REL}/{aid}-{host}-{digest}.snap"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    filled = skipped_verified = demoted = 0
    touched: list[str] = []

    for res_path in sorted(RESULTS.glob("*.json")):
        try:
            res = json.loads(res_path.read_text())
        except Exception as e:
            print(f"  SKIP  {res_path.name}: unreadable ({e})")
            continue

        # Researchers cache scratch downloads (a forum thread, a Koios dump) into their working
        # directory. Those are not results and must never be mistaken for one — anything without a
        # dict shape and an action_id is ignored rather than half-parsed.
        if not isinstance(res, dict) or not res.get("action_id"):
            print(f"  SKIP  {res_path.name}: not a result file")
            continue
        aid = res["action_id"]

        packet_path = PACKETS / f"{aid}.json"
        if not packet_path.exists():
            print(f"  SKIP  {aid[:20]}..: no existing packet to merge into")
            continue

        packet = json.loads(packet_path.read_text())
        fields = packet.setdefault("fields", {})
        changes = []

        for name in FIELDS:
            item = res.get(name) or {}
            value = str(item.get("value") or "unknown").lower()
            if value not in VALID:
                value = "unknown"

            sources = [{"url": s["url"], "snapshot_path": snapshot_path(aid, s["url"])}
                       for s in (item.get("sources") or [])
                       if str(s.get("url", "")).startswith("https://")]

            # A directional claim with no public source cannot be checked, so it is not evidence.
            if value != "unknown" and not sources:
                demoted += 1
                changes.append(f"{name}: {value} -> unknown (no public source)")
                value = "unknown"

            existing = fields.get(name) or {}
            existing_value = str(existing.get("value") or "unknown").lower()

            # A RETRACTION always lands. When a researcher withdraws its own claim — "I found two
            # independent domains, and corroborating it is what killed my finding" — refusing the
            # downgrade because the old value was "already directional" would pin a claim its own
            # author has disowned. Withdrawing evidence can only ever remove a reason to act; it can
            # never manufacture one. Blocking this was, briefly, holding `material_duplication: yes`
            # and `cost_compared_to_market: no` against a 25,400,000 ADA proposal on evidence the
            # researcher had already retracted as an FX illusion.
            if value == "unknown" and existing_value in ("yes", "no"):
                fields[name] = {"value": "unknown", "sources": []}
                demoted += 1
                changes.append(f"{name}: {existing_value} -> unknown (RETRACTED by researcher)")
                continue

            # Rule 1: never let a later pass silently flip a directional finding to its opposite.
            if existing_value in ("yes", "no"):
                if value != "unknown" and value != existing_value:
                    # Two independent passes reached opposite conclusions. Keeping the older value
                    # is the conservative move — it can only ever deny a bonus, never manufacture a
                    # YES — but quietly discarding the disagreement would hide exactly the kind of
                    # thing a reader of this record deserves to see. Put it ON the packet.
                    packet.setdefault("evidence_conflicts", [])
                    conflict = {
                        "field": name,
                        "retained_value": existing_value,
                        "conflicting_value": value,
                        "conflicting_sources": [s.get("url") for s in sources],
                        "resolution": ("retained the earlier independently verified value; the newer "
                                       "finding is recorded but not applied, because a later pass must "
                                       "not silently overturn a verified field"),
                    }
                    if conflict not in packet["evidence_conflicts"]:
                        packet["evidence_conflicts"].append(conflict)
                        changes.append(f"{name}: CONFLICT recorded (kept '{existing_value}', new pass said '{value}')")
                    print(f"  KEEP  {aid[:16]}.. {name}: existing '{existing_value}' kept "
                          f"(new research said '{value}' — conflict recorded, not overwritten)")
                skipped_verified += 1
                continue

            if value == "unknown":
                continue                       # nothing learned; leave the honest unknown alone

            fields[name] = {"value": value, "sources": sources}
            filled += 1
            changes.append(f"{name}: unknown -> {value} ({len(sources)} sources)")

        if changes:
            touched.append(aid)
            title = (res.get("title_as_read_from_csv") or "")[:40]
            print(f"  {aid[:16]}..  {title}")
            for c in changes:
                print(f"      {c}")
            if not args.dry_run:
                # Force a re-pin: the new sources are unhashed until the fetcher runs.
                packet["pinned_at_utc"] = None
                packet_path.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n")

    verb = "would fill" if args.dry_run else "filled"
    print(f"\n{verb} {filled} fields across {len(touched)} packets; "
          f"{skipped_verified} already-verified fields left untouched; "
          f"{demoted} unsourced claims demoted to unknown")
    if not args.dry_run and touched:
        print("\nNEXT: run scripts/pin_value_evidence_sources.py — it fetches and SHA-256 hashes "
              "every new URL. Any citation that does not resolve is dropped and its field demoted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
