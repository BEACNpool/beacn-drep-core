"""Deterministic vote-revision policy — anti-churn for the automated DRep.

Separates two concerns that were previously conflated:

  * the *engine* produces a pure, replayable recommendation from evidence; and
  * this module decides whether that recommendation should be turned into (or
    kept as) an on-chain vote.

The engine recommendation can legitimately wobble across daily runs when a score
sits near a directional threshold (e.g. NO at score -0.13 one day, ABSTAIN at
-0.05 the next). With fully-agentic voting + sub-ADA fees, naively mirroring
every change would churn the public vote on-chain. This module debounces that:

  * a brand-new ABSTAIN casts immediately (safe, conservative default);
  * a brand-new directional (YES/NO) vote waits until the recommendation has
    persisted for `min_persistence_directional_cast` runs OR confidence is high;
  * CHANGING an existing on-chain vote (a revision) requires BOTH the new
    recommendation to persist for `min_persistence_revision` runs AND the score
    to clear the directional threshold by `hysteresis_margin` (a dead-band so a
    score parked on the boundary cannot flip the public vote back and forth).

`decide()` is a pure function (no I/O) so it is fully unit-testable. State lives
in an append-only ledger (`data/output/vote_state.json`): the recommendation
history per action, written each vote run.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .config import CORE_REPO, OUTPUT_DIR

VOTABLE = {"YES", "NO", "ABSTAIN"}
LEDGER_PATH = OUTPUT_DIR / "vote_state.json"
CONFIG_PATH = CORE_REPO / "registries" / "vote_policy.json"

# ABSTAIN reason codes that mean "we are missing evidence", NOT "the evidence says
# this action is neutral". METHODOLOGY.md already holds that missing evidence can never
# *become* a NO. The same asymmetry must apply to retraction: an empty, stale, or
# unfetched evidence file is a fact about BEACN's pipeline, not a finding about the
# proposal, and it must never pull a considered YES/NO vote back off the chain.
#
# Codes NOT listed here (HARD_BLOCKER_PRESENT, RISK_HIGH, RULE_THRESHOLD_UNMET) are
# affirmative findings — those may legitimately revise a live vote to ABSTAIN.
EVIDENCE_ABSENCE_ABSTAIN_CODES = {
    "STALE_DATA",
    "UNKNOWN_ACTION_TYPE",
    "MISSING_BASELINE_EVIDENCE",
    "MISSING_PROTOCOL_READINESS_EVIDENCE",
    "CONTEXT_THIN_ANCHOR_UNPINNED",
    "DREP_DISTRIBUTION_MISSING",
}

DEFAULTS: dict = {
    # consecutive runs the new recommendation must hold before CHANGING a live vote
    "min_persistence_revision": 2,
    # consecutive runs before a FIRST directional (YES/NO) vote is cast
    "min_persistence_directional_cast": 2,
    # score must clear |directional_threshold| by this margin to (re)affirm or
    # leave a directional vote during a revision (dead-band width)
    "hysteresis_margin": 0.04,
    # a sufficiently confident directional may be cast without full persistence
    "min_confidence_directional": 0.60,
    # ledger entries retained per action
    "history_cap": 60,
}

_ONCHAIN_TO_REC = {"VoteYes": "YES", "VoteNo": "NO", "Abstain": "ABSTAIN"}


def map_onchain_vote(vote: str | None) -> str | None:
    """Map a gov-state dRep vote ('VoteYes'/'VoteNo'/'Abstain') to a recommendation."""
    return _ONCHAIN_TO_REC.get(vote or "")


def load_config() -> dict:
    cfg = dict(DEFAULTS)
    if CONFIG_PATH.exists():
        try:
            loaded = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            for key in DEFAULTS:
                if key in loaded:
                    cfg[key] = type(DEFAULTS[key])(loaded[key])
        except Exception:
            pass
    return cfg


# --- ledger (append-only recommendation history per action) ------------------
def load_ledger(path: Path = LEDGER_PATH) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_ledger(ledger: dict, path: Path = LEDGER_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(ledger, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def record(ledger: dict, action_id: str, recommendation: str, score, run_id: str,
           cap: int = DEFAULTS["history_cap"]) -> dict:
    """Append this run's recommendation to the action's history (in place).

    Idempotent per run_id: re-recording the same run replaces its entry rather
    than inflating persistence, so re-running the vote step does not falsely
    debounce-approve a revision.
    """
    history = ledger.setdefault(action_id, [])
    if history and history[-1].get("run_id") == run_id:
        history.pop()
    history.append({
        "recommendation": (recommendation or "").upper(),
        "score": round(float(score or 0.0), 4),
        "run_id": run_id,
    })
    ledger[action_id] = history[-cap:]
    return ledger


def persistence(history: list[dict], recommendation: str) -> int:
    """Count trailing (most-recent) consecutive entries equal to `recommendation`."""
    rec = (recommendation or "").upper()
    n = 0
    for entry in reversed(history):
        if (entry.get("recommendation") or "").upper() == rec:
            n += 1
        else:
            break
    return n


# --- decision (pure) ---------------------------------------------------------
@dataclass
class Decision:
    action: str   # CAST | REVISE | HOLD | NOOP | SKIP
    reason: str


def decide(*, recommendation: str, score, confidence, directional_threshold,
           onchain_vote: str | None, history: list[dict], cfg: dict | None = None,
           abstain_reason_code: str | None = None) -> Decision:
    """Decide what to do with a vote given the engine output and prior state.

    `history` must already include the current run's recommendation (record()
    it before calling), so persistence counts the current run.
    """
    cfg = cfg or DEFAULTS
    rec = (recommendation or "").upper()
    if rec not in VOTABLE:
        return Decision("SKIP", f"recommendation {rec or 'EMPTY'} is not votable")

    onchain_rec = map_onchain_vote(onchain_vote)
    if onchain_rec == rec:
        return Decision("NOOP", f"on-chain vote already {rec}")

    persist = persistence(history, rec)
    thr = abs(float(directional_threshold or 0.12))
    margin = abs(float(score or 0.0)) - thr  # >0: clearly directional; <0: inside dead-band
    h = float(cfg["hysteresis_margin"])

    # Fresh vote (nothing on-chain yet).
    if onchain_rec is None:
        if rec == "ABSTAIN":
            return Decision("CAST", "fresh abstain (conservative default)")
        if persist >= cfg["min_persistence_directional_cast"] or float(confidence or 0.0) >= cfg["min_confidence_directional"]:
            return Decision("CAST", f"fresh {rec}: persist={persist}, confidence={confidence}")
        return Decision("HOLD",
                        f"fresh {rec} not yet stable: persist={persist}/{cfg['min_persistence_directional_cast']}, "
                        f"confidence={confidence}<{cfg['min_confidence_directional']}")

    # Revision: changing an existing on-chain vote — higher bar.

    # Absence of evidence can never retract a cast directional vote. Checked before
    # persistence/hysteresis because it is a hard rule, not a debounce: if the reason we
    # want to abstain is that an evidence file is empty or stale, the honest action is to
    # leave the existing vote standing and fix the pipeline.
    if rec == "ABSTAIN" and onchain_rec in ("YES", "NO"):
        code = (abstain_reason_code or "").upper()
        if code in EVIDENCE_ABSENCE_ABSTAIN_CODES:
            return Decision(
                "HOLD",
                f"revision {onchain_rec}->ABSTAIN refused: abstain is evidence-absence "
                f"({code}); missing evidence must never retract a cast directional vote",
            )

    if persist < cfg["min_persistence_revision"]:
        return Decision("HOLD",
                        f"revision {onchain_rec}->{rec} held: not persistent "
                        f"(persist={persist}/{cfg['min_persistence_revision']})")
    if rec == "ABSTAIN":
        # leaving a directional vote: score must be clearly inside the dead-band
        if margin > -h:
            return Decision("HOLD",
                            f"revision {onchain_rec}->ABSTAIN held: score {score} within hysteresis "
                            f"({h}) of threshold {thr}")
    else:
        # moving to a directional vote: score must clear the threshold by the margin
        if margin < h:
            return Decision("HOLD",
                            f"revision {onchain_rec}->{rec} held: score {score} not clear of threshold "
                            f"{thr} by {h}")
    return Decision("REVISE", f"revision {onchain_rec}->{rec} approved: persist={persist}, margin={round(margin, 4)}")
