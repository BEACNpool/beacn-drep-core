#!/usr/bin/env python3
"""Write the BEACN DRep web status feed — the bot's check-in.

Run on every cron tick (whether or not anything is voted on). Queries the live
chain through the relay, summarizes the open governance actions and this DRep's
vote status on each, and writes `status.json` into the beacn-drep-web clone.
The landing page renders that file, so the website itself is the heartbeat.

  PYTHONPATH=src python3 scripts/update_web_status.py
"""
from __future__ import annotations

import json
import os
import sys
import csv
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from beacn_drep.adapters.cardano_cli_adapter import _relay_query, DREP_KEY_HASH  # noqa: E402

WEB = Path(os.environ.get("BEACN_WEB_REPO", Path.home() / ".openclaw/workspace/beacn-drep-web"))
DREP_ID = "drep1yg3fzjm63hjg37k3rtdt7wx0mgmn303lwv2s50xxkjzsv5qfhynxg"
WORKSPACE = Path(os.environ.get("BEACN_WORKSPACE", ROOT.parent))
RESOURCES = WORKSPACE / "beacn-drep-resources"
GOVERNANCE_ALL = RESOURCES / "data/input/governance/governance_actions_all.csv"
PUBLIC_ACTIONS_INDEX = ROOT / "data/output/public/actions.json"


def _load_latest_scores() -> dict[str, dict]:
    """cip129 action_id -> the deciding numbers from the latest engine run, so the
    public status feed shows the weighted score behind each recommendation."""
    runs_dir = ROOT / "data" / "output"
    latest: dict[str, tuple[int, dict]] = {}
    for run_dir in runs_dir.iterdir():
        rationale_path = run_dir / "rationale.json"
        if not run_dir.is_dir() or not rationale_path.exists():
            continue
        try:
            rationale = json.loads(rationale_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        action_id = rationale.get("action_id")
        if not action_id:
            continue
        mtime = rationale_path.stat().st_mtime_ns
        if action_id not in latest or mtime > latest[action_id][0]:
            latest[action_id] = (mtime, rationale)
    return {
        aid: {
            "score": r.get("score"),
            "raw_score": r.get("raw_score"),
            "llm_score_adjustment": r.get("llm_score_adjustment"),
            "directional_threshold": r.get("directional_threshold"),
            "confidence": r.get("confidence"),
        }
        for aid, (_, r) in latest.items()
    }


def _load_action_metadata() -> dict[str, dict]:
    metadata: dict[str, dict] = {}
    decisions: dict[str, str | None] = {}
    try:
        public = json.loads(PUBLIC_ACTIONS_INDEX.read_text(encoding="utf-8"))
        for item in public.get("items", []):
            decisions[item.get("action_id", "")] = item.get("decision")
    except FileNotFoundError:
        pass

    try:
        with GOVERNANCE_ALL.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                key = f"{row.get('tx_hash')}#{row.get('cert_index')}"
                action_id = row.get("action_id", "")
                metadata[key] = {
                    "cip129_action_id": action_id,
                    "title": row.get("metadata_title", ""),
                    "recommendation": decisions.get(action_id),
                }
    except FileNotFoundError:
        pass
    return metadata


def main() -> int:
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    tip = json.loads(_relay_query(["conway", "query", "tip", "--mainnet"]))
    gov = json.loads(_relay_query(["conway", "query", "gov-state", "--mainnet"]))
    epoch = int(tip["epoch"])
    voted_key = f"keyHash-{DREP_KEY_HASH}"

    actions = []
    metadata = _load_action_metadata()
    scores = _load_latest_scores()
    open_count = 0
    voted_count = 0
    for p in gov.get("proposals", []):
        aid = p.get("actionId", {})
        action_key = f'{aid.get("txId")}#{aid.get("govActionIx")}'
        meta = metadata.get(action_key, {})
        exp = p.get("expiresAfter")
        is_open = exp is None or int(exp) >= epoch
        our_vote = (p.get("dRepVotes") or {}).get(voted_key)  # 'VoteYes'/'VoteNo'/'Abstain' or None
        if is_open:
            open_count += 1
        if our_vote is not None:
            voted_count += 1
        score_info = scores.get(meta.get("cip129_action_id") or "", {})
        actions.append({
            "action_id": action_key,
            "cip129_action_id": meta.get("cip129_action_id") if is_open else None,
            "title": meta.get("title", ""),
            "type": (p.get("proposalProcedure", {}).get("govAction", {}) or {}).get("tag"),
            "proposed_in_epoch": p.get("proposedIn"),
            "expires_after_epoch": exp,
            "status": "open" if is_open else "closed",
            "recommendation": meta.get("recommendation"),
            "our_vote": our_vote,
            "score": score_info.get("score"),
            "raw_score": score_info.get("raw_score"),
            "llm_score_adjustment": score_info.get("llm_score_adjustment"),
            "directional_threshold": score_info.get("directional_threshold"),
            "confidence": score_info.get("confidence"),
            "anchor_url": (p.get("proposalProcedure", {}).get("anchor", {}) or {}).get("url"),
        })
    actions.sort(key=lambda a: (a["status"] != "open", -(a["expires_after_epoch"] or 0)))

    # Mode from ground truth: if this DRep has votes on-chain it is live, whatever
    # the local environment says. BEACN_VOTING_LIVE only *adds* live intent (e.g.
    # freshly enabled before the first vote lands); it can never mask cast votes.
    mode = "live" if (voted_count > 0 or os.environ.get("BEACN_VOTING_LIVE") == "1") else "shadow"

    status = {
        "generated_at": now,
        "drep_id": DREP_ID,
        "mode": mode,
        "last_check": {
            "at": now,
            "epoch": epoch,
            "open_actions": open_count,
            "actions_with_our_vote": voted_count,
            "summary": (f"Last checked at epoch {epoch}. {open_count} open governance "
                        f"action(s); this DRep has voted on {voted_count}. Mode: {mode}."),
        },
        "actions": actions[:50],
        "note": "Generated by the BEACN DRep bot on each check. A live feed may replace this later.",
    }
    out = WEB / "status.json"
    out.write_text(json.dumps(status, indent=2) + "\n")
    print(f"wrote {out}: epoch {epoch}, {open_count} open, {voted_count} voted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
