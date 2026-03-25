#!/usr/bin/env python3
"""Export governance data from cardano-gov SQLite to beacn-drep-resources CSVs.

Fallback source when PostgreSQL db-sync is unavailable.
Produces identical CSV schemas to export_from_postgres.py.
"""
import csv
import json
import hashlib
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

from ..config import SQLITE_DB, RESOURCES_REPO

OUT = RESOURCES_REPO / "data" / "input" / "governance"


def _q(conn, sql):
    conn.row_factory = sqlite3.Row
    return [dict(r) for r in conn.execute(sql).fetchall()]


def _write_csv(path: Path, rows: list[dict], columns: list[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columns)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k) for k in columns})


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if not SQLITE_DB.exists():
        raise SystemExit(f"missing db: {SQLITE_DB}")

    conn = sqlite3.connect(SQLITE_DB)

    proposals = _q(conn, """
        SELECT
          id AS action_id,
          tx_hash,
          cert_index,
          type AS action_type,
          status,
          proposed_epoch,
          expiration_epoch,
          deposit_lovelace,
          return_address,
          anchor_url,
          anchor_hash,
          proposer_address,
          treasury_amount_lovelace,
          drep_yes_pct,
          drep_no_pct,
          drep_abstain_pct,
          spo_yes_pct,
          spo_no_pct,
          spo_abstain_pct,
          cc_yes,
          cc_no,
          cc_abstain,
          flag_score,
          first_seen,
          last_updated
        FROM proposals
        ORDER BY proposed_epoch DESC, action_id DESC
    """)

    active = [r for r in proposals if (r.get("status") or "").lower() == "active"]

    treasury_rows = []
    for r in _q(conn, "SELECT id, treasury_recipients FROM proposals WHERE treasury_recipients IS NOT NULL AND treasury_recipients != ''"):
        try:
            recips = json.loads(r["treasury_recipients"])
        except Exception:
            recips = []
        for item in recips if isinstance(recips, list) else []:
            treasury_rows.append({
                "action_id": r["id"],
                "stake_address": item.get("stake_address"),
                "amount_lovelace": item.get("amount"),
            })

    flags_rows = []
    for r in _q(conn, "SELECT id, flags FROM proposals WHERE flags IS NOT NULL AND flags != ''"):
        try:
            flags = json.loads(r["flags"])
        except Exception:
            flags = []
        for f in flags if isinstance(flags, list) else []:
            flags_rows.append({
                "action_id": r["id"],
                "flag": f.get("flag"),
                "severity": f.get("severity"),
                "detail": f.get("detail"),
            })

    poll_runs = _q(conn, "SELECT id, timestamp, source, proposals_found, new_proposals, errors FROM poll_log ORDER BY id DESC")

    actions_cols = [
        "action_id", "tx_hash", "cert_index", "action_type", "status",
        "proposed_epoch", "expiration_epoch", "deposit_lovelace", "return_address",
        "anchor_url", "anchor_hash", "proposer_address", "treasury_amount_lovelace",
        "drep_yes_pct", "drep_no_pct", "drep_abstain_pct",
        "spo_yes_pct", "spo_no_pct", "spo_abstain_pct",
        "cc_yes", "cc_no", "cc_abstain",
        "flag_score", "first_seen", "last_updated",
    ]
    _write_csv(OUT / "governance_actions_all.csv", proposals, actions_cols)
    _write_csv(OUT / "governance_actions_active.csv", active, actions_cols)
    _write_csv(OUT / "governance_treasury_recipients.csv", treasury_rows, ["action_id", "stake_address", "amount_lovelace"])
    _write_csv(OUT / "governance_action_flags.csv", flags_rows, ["action_id", "flag", "severity", "detail"])
    _write_csv(OUT / "governance_poll_runs.csv", poll_runs, ["id", "timestamp", "source", "proposals_found", "new_proposals", "errors"])

    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": "sqlite_cardano_gov",
        "source_db_path": str(SQLITE_DB),
        "source_db_sha256": _sha256(SQLITE_DB),
        "totals": {
            "actions_all": len(proposals),
            "actions_active": len(active),
            "treasury_rows": len(treasury_rows),
            "flag_rows": len(flags_rows),
            "poll_runs": len(poll_runs),
        },
        "outputs": [],
    }

    for p in [
        OUT / "governance_actions_all.csv",
        OUT / "governance_actions_active.csv",
        OUT / "governance_treasury_recipients.csv",
        OUT / "governance_action_flags.csv",
        OUT / "governance_poll_runs.csv",
    ]:
        manifest["outputs"].append({"path": str(p.relative_to(RESOURCES_REPO)), "sha256": _sha256(p)})

    (OUT / "governance_export_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest["totals"]))


if __name__ == "__main__":
    main()
