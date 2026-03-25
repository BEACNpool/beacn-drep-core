#!/usr/bin/env python3
"""Export governance data from db-sync PostgreSQL to beacn-drep-resources CSVs.

Primary data source. Falls back to SQLite exporter if PostgreSQL is unavailable.
Produces identical CSV schemas to export_proposals_to_resources.py.
"""
import csv
import json
import hashlib
import sys
from pathlib import Path
from datetime import datetime, timezone

try:
    import psycopg2
    import psycopg2.extras
except ImportError:
    print("psycopg2 not installed. Install with: pip install psycopg2-binary --break-system-packages", file=sys.stderr)
    sys.exit(1)

from ..config import (
    DBSYNC_HOST, DBSYNC_PORT, DBSYNC_DB, DBSYNC_USER, DBSYNC_PASS,
    RESOURCES_REPO,
)

OUT = RESOURCES_REPO / "data" / "input" / "governance"


def _connect():
    if not DBSYNC_HOST:
        raise RuntimeError("BEACN_DBSYNC_HOST not set")
    return psycopg2.connect(
        host=DBSYNC_HOST,
        port=DBSYNC_PORT,
        dbname=DBSYNC_DB,
        user=DBSYNC_USER,
        password=DBSYNC_PASS,
    )


def _q(conn, sql, params=None):
    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(sql, params or ())
        return cur.fetchall()


def _write_csv(path: Path, rows: list[dict], columns: list[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columns)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in columns})


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _safe(val):
    """Convert db value to string safely."""
    if val is None:
        return ""
    if isinstance(val, memoryview):
        return bytes(val).hex()
    if isinstance(val, bytes):
        return val.hex()
    return str(val)


def main():
    conn = _connect()
    now = datetime.now(timezone.utc)

    # -- Get current tip for freshness metadata --
    tip = _q(conn, "SELECT block_no, slot_no, time FROM block ORDER BY id DESC LIMIT 1")
    tip_info = tip[0] if tip else {}

    # -- Governance actions --
    # NOTE: db-sync schema varies by version. This targets 13.6+/14.x.
    # Adjust column names if your db-sync version differs.
    proposals_sql = """
        SELECT
            gap.id AS gap_id,
            encode(tx.hash, 'hex') || '#' || gap.index::text AS action_id,
            encode(tx.hash, 'hex') AS tx_hash,
            gap.index AS cert_index,
            gap.type::text AS action_type,
            CASE
                WHEN gap.enacted_epoch IS NOT NULL THEN 'enacted'
                WHEN gap.ratified_epoch IS NOT NULL THEN 'ratified'
                WHEN gap.dropped_epoch IS NOT NULL THEN 'dropped'
                WHEN gap.expired_epoch IS NOT NULL THEN 'expired'
                ELSE 'active'
            END AS status,
            COALESCE(b.epoch_no, 0) AS proposed_epoch,
            gap.expiration AS expiration_epoch,
            gap.deposit::bigint AS deposit_lovelace,
            encode(sa.hash_raw, 'hex') AS return_address,
            va.url AS anchor_url,
            encode(va.data_hash, 'hex') AS anchor_hash,
            '' AS proposer_address,
            COALESCE((
                SELECT SUM(tw.amount)::bigint
                FROM treasury_withdrawal tw
                WHERE tw.gov_action_proposal_id = gap.id
            ), 0) AS treasury_amount_lovelace,
            0.0 AS drep_yes_pct,
            0.0 AS drep_no_pct,
            0.0 AS drep_abstain_pct,
            0.0 AS spo_yes_pct,
            0.0 AS spo_no_pct,
            0.0 AS spo_abstain_pct,
            0 AS cc_yes,
            0 AS cc_no,
            0 AS cc_abstain,
            0 AS flag_score,
            b.time AS first_seen,
            b.time AS last_updated
        FROM gov_action_proposal gap
        JOIN tx ON tx.id = gap.tx_id
        JOIN block b ON b.id = tx.block_id
        LEFT JOIN voting_anchor va ON va.id = gap.voting_anchor_id
        LEFT JOIN stake_address sa ON sa.id = gap.return_address
        ORDER BY gap.id DESC
    """

    try:
        raw_proposals = _q(conn, proposals_sql)
    except Exception as e:
        # If the schema doesn't match, try a simpler query
        print(f"WARNING: Complex query failed ({e}), trying simplified query...", file=sys.stderr)
        raw_proposals = _q(conn, """
            SELECT
                gap.id AS gap_id,
                encode(tx.hash, 'hex') || '#' || gap.index::text AS action_id,
                encode(tx.hash, 'hex') AS tx_hash,
                gap.index AS cert_index,
                gap.type::text AS action_type,
                'active' AS status,
                0 AS proposed_epoch,
                gap.expiration AS expiration_epoch,
                gap.deposit::bigint AS deposit_lovelace,
                '' AS return_address,
                va.url AS anchor_url,
                encode(va.data_hash, 'hex') AS anchor_hash,
                '' AS proposer_address,
                0 AS treasury_amount_lovelace,
                0.0 AS drep_yes_pct, 0.0 AS drep_no_pct, 0.0 AS drep_abstain_pct,
                0.0 AS spo_yes_pct, 0.0 AS spo_no_pct, 0.0 AS spo_abstain_pct,
                0 AS cc_yes, 0 AS cc_no, 0 AS cc_abstain,
                0 AS flag_score,
                NOW() AS first_seen, NOW() AS last_updated
            FROM gov_action_proposal gap
            JOIN tx ON tx.id = gap.tx_id
            LEFT JOIN voting_anchor va ON va.id = gap.voting_anchor_id
            ORDER BY gap.id DESC
        """)

    # Compute DRep vote percentages per action
    votes_sql = """
        SELECT
            vp.gov_action_proposal_id,
            vp.vote::text AS vote,
            COUNT(*) AS cnt
        FROM voting_procedure vp
        WHERE vp.voter_role = 'DRep'
        GROUP BY vp.gov_action_proposal_id, vp.vote
    """
    try:
        vote_rows = _q(conn, votes_sql)
        vote_map: dict[int, dict[str, int]] = {}
        for vr in vote_rows:
            gid = vr["gov_action_proposal_id"]
            vote_map.setdefault(gid, {}).setdefault(vr["vote"], 0)
            vote_map[gid][vr["vote"]] += vr["cnt"]
    except Exception:
        vote_map = {}

    proposals = []
    for r in raw_proposals:
        row = {k: _safe(v) for k, v in r.items()}
        gid = int(r.get("gap_id")) if r.get("gap_id") is not None else None
        counts = vote_map.get(gid, {}) if gid is not None else {}
        y = int(counts.get("Yes", 0))
        n = int(counts.get("No", 0))
        a = int(counts.get("Abstain", 0))
        total = y + n + a
        if total > 0:
            row["drep_yes_pct"] = f"{(y / total) * 100:.4f}"
            row["drep_no_pct"] = f"{(n / total) * 100:.4f}"
            row["drep_abstain_pct"] = f"{(a / total) * 100:.4f}"
        proposals.append(row)

    # -- Treasury recipients --
    treasury_rows = []
    try:
        tw_sql = """
            SELECT
                encode(tx.hash, 'hex') || '#' || gap.index::text AS action_id,
                encode(sa.hash_raw, 'hex') AS stake_address,
                tw.amount::bigint AS amount_lovelace
            FROM treasury_withdrawal tw
            JOIN gov_action_proposal gap ON gap.id = tw.gov_action_proposal_id
            JOIN tx ON tx.id = gap.tx_id
            JOIN stake_address sa ON sa.id = tw.stake_address_id
        """
        for r in _q(conn, tw_sql):
            treasury_rows.append({k: _safe(v) for k, v in r.items()})
    except Exception as e:
        print(f"WARNING: treasury query failed: {e}", file=sys.stderr)

    # -- Write CSVs --
    actions_cols = [
        "action_id", "tx_hash", "cert_index", "action_type", "status",
        "proposed_epoch", "expiration_epoch", "deposit_lovelace", "return_address",
        "anchor_url", "anchor_hash", "proposer_address", "treasury_amount_lovelace",
        "drep_yes_pct", "drep_no_pct", "drep_abstain_pct",
        "spo_yes_pct", "spo_no_pct", "spo_abstain_pct",
        "cc_yes", "cc_no", "cc_abstain",
        "flag_score", "first_seen", "last_updated",
    ]

    active = [r for r in proposals if (r.get("status") or "").lower() == "active"]

    _write_csv(OUT / "governance_actions_all.csv", proposals, actions_cols)
    _write_csv(OUT / "governance_actions_active.csv", active, actions_cols)
    _write_csv(OUT / "governance_treasury_recipients.csv", treasury_rows, ["action_id", "stake_address", "amount_lovelace"])

    # Flags: not available from db-sync directly, preserve existing file if present
    flags_path = OUT / "governance_action_flags.csv"
    if not flags_path.exists():
        _write_csv(flags_path, [], ["action_id", "flag", "severity", "detail"])

    # Poll runs: not applicable for PostgreSQL source, write empty if missing
    poll_path = OUT / "governance_poll_runs.csv"
    if not poll_path.exists():
        _write_csv(poll_path, [], ["id", "timestamp", "source", "proposals_found", "new_proposals", "errors"])

    # -- Manifest --
    manifest = {
        "generated_at_utc": now.isoformat(),
        "source": "postgresql_dbsync",
        "source_host": DBSYNC_HOST,
        "source_db": DBSYNC_DB,
        "tip": {
            "block_no": _safe(tip_info.get("block_no")),
            "slot_no": _safe(tip_info.get("slot_no")),
            "time": _safe(tip_info.get("time")),
        },
        "totals": {
            "actions_all": len(proposals),
            "actions_active": len(active),
            "treasury_rows": len(treasury_rows),
        },
        "outputs": [],
    }

    for p in [
        OUT / "governance_actions_all.csv",
        OUT / "governance_actions_active.csv",
        OUT / "governance_treasury_recipients.csv",
        flags_path,
        poll_path,
    ]:
        if p.exists():
            manifest["outputs"].append({"path": str(p.relative_to(RESOURCES_REPO)), "sha256": _sha256(p)})

    (OUT / "governance_export_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    conn.close()
    print(json.dumps(manifest["totals"]))


if __name__ == "__main__":
    main()
