"""Vote-time truth ledger — what the engine believed at the moment a vote was cast.

Every submitted vote appends one entry here, frozen forever. The public exporter republishes
each action's `proof_of_vote` from the LATEST engine run, so every re-score on fresh evidence
silently rewrote the "proof" of a vote cast weeks earlier — the score, confidence, hashes, and
commits shown as vote-time truth were actually today's. This file is the fix: append-only,
written once per submission by the live-vote path, and never touched by later engine runs.

Keyed by CANONICAL action id (see ids.py) -> list of entries in submission order. Entries are
immutable once written; a re-vote (revision) appends a new entry rather than editing the old one.
"""
from __future__ import annotations

import json
from pathlib import Path

from .config import OUTPUT_DIR
from .ids import canonical_action_id

SNAPSHOTS_PATH = OUTPUT_DIR / "vote_time_snapshots.json"


def load_snapshots(path: Path | None = None) -> dict[str, list[dict]]:
    p = path or SNAPSHOTS_PATH
    if not p.exists():
        return {}
    try:
        raw = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return raw if isinstance(raw, dict) else {}


def latest_snapshot(snapshots: dict[str, list[dict]], action_id: str) -> dict | None:
    """The most recent frozen entry for an action — the vote currently standing on-chain.

    Entries are appended in submission order; reconstructed (backfilled) entries may lack a
    `submitted_at`, so list position is the tiebreaker.
    """
    entries = snapshots.get(canonical_action_id(action_id)) or []
    if not entries:
        return None
    return max(enumerate(entries), key=lambda ie: (ie[1].get("submitted_at") or "", ie[0]))[1]


def append_snapshot(action_id: str, entry: dict, path: Path | None = None) -> bool:
    """Append one frozen entry; existing entries are never modified or removed.

    Idempotent on (action_id, tx_hash): re-running a backfill or re-reading a receipt
    cannot duplicate an entry. Returns True if the entry was written.
    """
    p = path or SNAPSHOTS_PATH
    key = canonical_action_id(action_id)
    snapshots = load_snapshots(p)
    existing = snapshots.setdefault(key, [])
    if entry.get("tx_hash") and any(e.get("tx_hash") == entry["tx_hash"] for e in existing):
        return False
    existing.append(entry)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(snapshots, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return True


def record_submission(run_dir: Path, receipt: dict, path: Path | None = None) -> dict | None:
    """Freeze the vote-time truth for a just-submitted vote. Called by the live-vote path
    immediately after the receipt is written, while the run's rationale.json still IS the
    decision that was cast."""
    rationale = json.loads((Path(run_dir) / "rationale.json").read_text(encoding="utf-8"))
    rec = (receipt.get("recommendation") or rationale.get("recommendation") or "").upper()
    entry = {
        "tx_hash": receipt.get("transaction_hash"),
        "vote": rec,
        "recommendation": rec,
        "score": rationale.get("score"),
        "confidence": rationale.get("confidence"),
        "submitted_at": receipt.get("submitted_at"),
        "run_id": Path(run_dir).name,
        "input_hash": rationale.get("input_hash"),
        "snapshot_bundle_hash": rationale.get("snapshot_bundle_hash"),
        "soul_commit": rationale.get("soul_commit"),
        "resources_commit": rationale.get("resource_registry_commit"),
        "rationale_anchor_hash": rationale.get("rationale_anchor_hash"),
        "frozen": True,
    }
    action_id = rationale.get("action_id") or receipt.get("action_id") or ""
    return entry if append_snapshot(action_id, entry, path) else None
