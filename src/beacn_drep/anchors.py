"""Load the cached proposal (anchor) document text for a governance action.

The upstream exporter fetches each action's anchor document and pins a local copy
under the resources repo, recording the path in
`data/input/governance/anchor_documents_index.csv`. The deterministic engine only
ever treated the anchor as a boolean (`fetched: yes/no`) and never opened the file.
This module reads the actual text so the reasoning layer can extract real claims.

It is intentionally dependency-free and never raises: a missing index, missing file,
or decode error returns `(None, meta)` and the pipeline degrades to its
deterministic, anchor-unread behaviour.
"""
from __future__ import annotations

import csv
from pathlib import Path

from .config import RESOURCES_REPO

# Anchor bodies can be large; cap how much text we hand to the model to keep
# token cost bounded. Proposal metadata documents are almost always far smaller.
MAX_ANCHOR_CHARS = 60_000

_INDEX = RESOURCES_REPO / "data" / "input" / "governance" / "anchor_documents_index.csv"
_OK_STATUSES = {"ok", "ok_cached"}


def _index_row(action_id: str) -> dict | None:
    if not _INDEX.exists():
        return None
    with _INDEX.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("action_id") == action_id:
                return row
    return None


def load_anchor_text(action_id: str) -> tuple[str | None, dict]:
    """Return (text, meta) for the action's pinned anchor document.

    `text` is None when the anchor was never fetched, the file is missing, or it
    cannot be decoded. `meta` always carries the diagnostic fields so callers can
    record *why* claim extraction had nothing to read.
    """
    meta: dict = {"action_id": action_id, "anchor_read": False, "reason": None}

    row = _index_row(action_id)
    if row is None:
        meta["reason"] = "no anchor_documents_index row for this action"
        return None, meta

    meta["fetch_status"] = row.get("fetch_status")
    meta["anchor_url"] = row.get("anchor_url")
    meta["file_sha256"] = row.get("file_sha256")

    if (row.get("fetch_status") or "").strip() not in _OK_STATUSES:
        meta["reason"] = f"anchor fetch_status is '{row.get('fetch_status')}'"
        return None, meta

    rel = (row.get("file_path") or "").strip()
    if not rel:
        meta["reason"] = "anchor index row has no file_path"
        return None, meta

    path = RESOURCES_REPO / rel
    if not path.exists():
        meta["reason"] = f"pinned anchor file missing: {rel}"
        return None, meta

    try:
        raw = path.read_bytes()
    except Exception as e:  # noqa: BLE001 - never fail the pipeline on a read error
        meta["reason"] = f"could not read anchor file: {e}"
        return None, meta

    text = raw.decode("utf-8", errors="replace").strip()
    if not text:
        meta["reason"] = "anchor file is empty after decode"
        return None, meta

    meta["anchor_read"] = True
    meta["file_path"] = rel
    meta["content_chars"] = len(text)
    if len(text) > MAX_ANCHOR_CHARS:
        text = text[:MAX_ANCHOR_CHARS]
        meta["truncated_to_chars"] = MAX_ANCHOR_CHARS

    return text, meta
