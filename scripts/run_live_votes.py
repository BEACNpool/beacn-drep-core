#!/usr/bin/env python3
"""Daily auto-voter for the BEACN automated DRep (fully agentic, anti-churn).

Per doctrine the DRep is fully agentic: it submits whatever the deterministic
engine recommends (YES / NO / ABSTAIN) and revises an existing on-chain vote
when the latest recommendation differs. No mandatory operator-review gate.

Two layers protect each vote:
  * vote_policy (deterministic debounce): decides CAST / REVISE / HOLD / NOOP
    from the recommendation history (persistence) + a score hysteresis band, so
    a recommendation parked on a threshold cannot churn the public vote.
  * the signing adapter (fail-closed): enforces all 8 gates (fresh data, votable
    recommendation, replay, published+reachable rationale anchor, action active,
    vote-only tx, fee + per-run caps) and submits only with live=True AND
    BEACN_VOTING_LIVE=1.

Safety knobs: BEACN_AUTO_DIRECTIONS (default "YES,NO,ABSTAIN") narrows which
recommendations may auto-submit; vote-policy thresholds live in
registries/vote_policy.json; BEACN_AUTOVOTE_DISABLED=1 is the kill-switch
(honored by ops/run_daily_vote.sh).

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
from beacn_drep import vote_policy  # noqa: E402
from beacn_drep.adapters.cardano_cli_adapter import (  # noqa: E402
    DREP_KEY_HASH, _relay_query, decode_gov_action_id, prepare_vote,
)

OUT = ROOT / "data" / "output"
AUTO = {x.strip().upper() for x in os.environ.get("BEACN_AUTO_DIRECTIONS", "YES,NO,ABSTAIN").split(",") if x.strip()}


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


def gov_state_scan() -> dict[tuple[str, int], str | None]:
    """One gov-state query -> {(txId, ix): this DRep's vote or None} for every
    currently ACTIVE proposal. Actions absent from this map are expired/ratified
    and are not votable, so the runner skips them entirely."""
    try:
        gs = json.loads(_relay_query(["conway", "query", "gov-state", "--mainnet"]))
    except Exception:
        return {}
    key = f"keyHash-{DREP_KEY_HASH}"
    active: dict[tuple[str, int], str | None] = {}
    for p in gs.get("proposals", []):
        aid = p.get("actionId", {})
        active[(aid.get("txId"), int(aid.get("govActionIx", -1)))] = (p.get("dRepVotes") or {}).get(key)
    return active


def main() -> int:
    live = "--live" in sys.argv
    cfg = vote_policy.load_config()
    ledger = vote_policy.load_ledger()
    active = gov_state_scan()

    voted = 0
    skipped_inactive = 0
    report = []
    for d in latest_runs():
        rat = json.loads((d / "rationale.json").read_text())
        action_id = rat.get("action_id")
        try:
            txix = decode_gov_action_id(action_id)
        except Exception:
            continue
        if txix not in active:
            skipped_inactive += 1   # expired/ratified — not votable
            continue
        onchain_vote = active[txix]
        rec = (rat.get("recommendation") or "").upper()
        score = rat.get("score", 0.0)
        run_id = d.name

        # Record this run into the debounce ledger before deciding.
        vote_policy.record(ledger, action_id, rec, score, run_id, cap=cfg["history_cap"])
        decision = vote_policy.decide(
            recommendation=rec,
            score=score,
            confidence=rat.get("confidence", 0.0),
            directional_threshold=rat.get("directional_threshold", 0.12),
            onchain_vote=onchain_vote,
            history=ledger.get(action_id, []),
            cfg=cfg,
        )

        entry = {
            "action_id": action_id,
            "recommendation": rec,
            "onchain_vote": onchain_vote,
            "policy": decision.action,
            "policy_reason": decision.reason,
        }

        if decision.action in ("CAST", "REVISE") and rec in AUTO:
            # Gate 8 (per-run vote cap) reads this env var; without it the
            # MAX_VOTES_PER_RUN limit is never enforced on the live path.
            os.environ["BEACN_VOTES_THIS_RUN"] = str(voted)
            shadow = prepare_vote(d, live=False)
            gates_ok = bool(shadow.get("gates")) and all(shadow["gates"].values())
            entry["gates_ok"] = gates_ok
            if not gates_ok:
                entry["status"] = "blocked_by_gate"
                entry["reasons"] = shadow.get("reasons")
            elif live:
                res = prepare_vote(d, live=True)
                entry["status"] = res.get("status")
                entry["submitted"] = res.get("submitted")
                entry["transaction_hash"] = res.get("transaction_hash")
                if res.get("reasons"):
                    entry["reasons"] = res.get("reasons")
                if res.get("submitted"):
                    voted += 1
            else:
                entry["status"] = f"would_{decision.action.lower()} (shadow; gates green)"
        elif decision.action in ("CAST", "REVISE"):
            entry["status"] = f"skipped (recommendation {rec} not in auto-set {sorted(AUTO)})"
        else:
            entry["status"] = decision.action  # HOLD / NOOP / SKIP
        report.append(entry)

    vote_policy.save_ledger(ledger)
    print(json.dumps(
        {"live": live, "auto_directions": sorted(AUTO), "submitted": voted,
         "active_evaluated": len(report), "skipped_inactive": skipped_inactive,
         "policy_config": cfg, "runs": report},
        indent=2, default=str,
    ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
