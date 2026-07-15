#!/usr/bin/env python3
"""One-off backfill of data/output/vote_time_snapshots.json for votes cast before the
ledger existed.

Every entry is reconstructed from three immutable-or-near-immutable sources and marked
"reconstructed": true so nobody mistakes it for a snapshot written at submission time:

  * beacn-drep-resources data/input/governance/onchain_vote_anchors.json — the chain's own
    record of each cast vote (tx hash, direction, rationale anchor hash/url);
  * data/output/public/r/<anchor_hash[:24]>.md — the anchored rationale bytes the vote
    committed to on-chain; its header carries the vote-time recommendation/score/confidence;
  * the vote_receipt.json written at submission (matched by transaction_hash), whose run
    dir's rationale.json still holds the vote-time input/bundle hashes and repo commits.

A vote with no surviving receipt still gets an entry (the chain + anchored rationale are
enough to freeze direction/score/confidence); the receipt-only fields stay null.

Idempotent: append_snapshot dedupes on (action_id, tx_hash), so re-running is safe.

  PYTHONPATH=src python3 scripts/backfill_vote_time_snapshots.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from beacn_drep.config import RESOURCES_REPO  # noqa: E402
from beacn_drep.vote_snapshots import SNAPSHOTS_PATH, append_snapshot, load_snapshots  # noqa: E402

RUNS = ROOT / "data" / "output"
R_DIR = RUNS / "public" / "r"
ANCHORS = RESOURCES_REPO / "data" / "input" / "governance" / "onchain_vote_anchors.json"

_REC = re.compile(r"Recommendation:\s*\*\*(\w+)\*\*")
_SCORE = re.compile(r"Score:\s*`(-?[\d.]+)`")
_CONF = re.compile(r"Confidence:\s*`(-?[\d.]+)`")


def _anchored_header(anchor_hash: str) -> dict:
    """Vote-time verdict/score/confidence from the anchored rationale's header lines."""
    path = R_DIR / f"{anchor_hash[:24]}.md"
    if not path.exists():
        return {}
    head = path.read_text(encoding="utf-8")[:800]
    rec = _REC.search(head)
    score = _SCORE.search(head)
    conf = _CONF.search(head)
    return {
        "recommendation": rec.group(1).upper() if rec else None,
        "score": float(score.group(1)) if score else None,
        "confidence": float(conf.group(1)) if conf else None,
    }


def _receipts_by_tx() -> dict[str, tuple[Path, dict]]:
    out: dict[str, tuple[Path, dict]] = {}
    for path in RUNS.glob("*/vote_receipt.json"):
        try:
            receipt = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        tx = receipt.get("transaction_hash")
        if tx and receipt.get("submitted"):
            out[tx] = (path.parent, receipt)
    return out


def main() -> int:
    anchors = json.loads(ANCHORS.read_text(encoding="utf-8")).get("anchors") or {}
    receipts = _receipts_by_tx()

    written = 0
    skipped = 0
    for aid, row in sorted(anchors.items()):
        tx_hash = row.get("transaction_hash")
        header = _anchored_header(row.get("anchor_hash") or "")
        run_dir, receipt = receipts.get(tx_hash, (None, {}))
        rationale = {}
        if run_dir and (run_dir / "rationale.json").exists():
            rationale = json.loads((run_dir / "rationale.json").read_text(encoding="utf-8"))

        entry = {
            "tx_hash": tx_hash,
            "vote": (row.get("vote") or "").upper() or None,
            "recommendation": header.get("recommendation") or rationale.get("recommendation"),
            "score": header.get("score") if header.get("score") is not None else rationale.get("score"),
            "confidence": header.get("confidence") if header.get("confidence") is not None else rationale.get("confidence"),
            "submitted_at": receipt.get("submitted_at"),
            "run_id": run_dir.name if run_dir else None,
            "input_hash": rationale.get("input_hash"),
            "snapshot_bundle_hash": rationale.get("snapshot_bundle_hash"),
            "soul_commit": rationale.get("soul_commit"),
            "resources_commit": rationale.get("resource_registry_commit"),
            "rationale_anchor_hash": row.get("anchor_hash"),
            "frozen": True,
            "reconstructed": True,
        }
        if append_snapshot(aid, entry):
            written += 1
            src = "anchor+receipt" if run_dir else "anchor only"
            print(f"backfilled {aid[:32]}..  {entry['vote']:<8} score {entry['score']}  ({src})")
        else:
            skipped += 1

    total = sum(len(v) for v in load_snapshots().values())
    print(f"done: {written} written, {skipped} already present, "
          f"{total} total entries in {SNAPSHOTS_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
