"""Tests for the bounded, doctrine-aware LLM lean (Stage 1.5).

Contract under test:
  * hard gates run BEFORE any LLM influence and cannot be overridden;
  * the score adjustment is clamped to ±LLM_SCORE_ADJUST_CAP;
  * a nudge that crosses a directional boundary is flagged llm_assisted with
    reason code LLM_ASSISTED_DIRECTIONAL and preserves the raw score.
"""
import unittest

from beacn_drep import llm
from beacn_drep.config import LLM_SCORE_ADJUST_CAP
from beacn_drep.engine import _score_action

WEIGHTS = {
    "weights": {
        "anchor_present_bonus": 0.05,
        "treasury_base_penalty": -0.10,
        "parameter_change_base_penalty": -0.05,
        "hardfork_base_penalty": -0.12,
        "flag_score_divisor": 30.0,
        "flag_penalty_cap": 0.35,
        "drep_margin_cap": 0.10,
    }
}
FRESH = {"is_stale": False, "snapshot_age_seconds": 1, "freshness_source": "test"}
ASSESS = {"sections": [], "overall_status": "ready", "blocking_questions": []}


def near_threshold_info_action() -> dict:
    # raw score = anchor (0.05) + high DRep ratification support (0.06) = 0.11,
    # which sits just below the 0.12 non-treasury directional threshold.
    return {
        "action_id": "gov_info_near",
        "action_type": "InfoAction",
        "status": "active",
        "anchor_url": "ipfs://x",
        "anchor_hash": "ab" * 32,
        "flag_score": "0",
        "drep_yes_pct": "65",
        "drep_no_pct": "0",
        "drep_abstain_pct": "0",
        "treasury_amount_lovelace": "",
    }


def score(action, *, lean, missing=None, freshness=None, deep_row=None):
    return _score_action(
        action, [], freshness or FRESH, missing or [], True, ASSESS,
        None, None, None, deep_row, {}, {}, WEIGHTS, lean,
    )


class LeanTests(unittest.TestCase):
    def test_adjustment_is_clamped_to_cap(self):
        lean = {"available": True, "score_adjustment": 0.9, "direction": "YES", "source": "test"}
        result = score(near_threshold_info_action(), lean=lean)
        self.assertEqual(result["llm_score_adjustment"], round(LLM_SCORE_ADJUST_CAP, 4))

    def test_positive_lean_tips_near_threshold_action_to_yes(self):
        lean = {"available": True, "score_adjustment": LLM_SCORE_ADJUST_CAP,
                "direction": "YES", "source": "test", "rationale": "doctrine-aligned"}
        result = score(near_threshold_info_action(), lean=lean)
        self.assertEqual(result["recommendation"], "YES")
        self.assertTrue(result["llm_assisted"])
        self.assertEqual(result["llm_assisted_reason_code"], "LLM_ASSISTED_DIRECTIONAL")
        self.assertEqual(result["raw_score"], 0.11)

    def test_no_lean_leaves_near_threshold_action_abstaining(self):
        result = score(near_threshold_info_action(), lean=None)
        self.assertEqual(result["recommendation"], "ABSTAIN")
        self.assertEqual(result["llm_score_adjustment"], 0.0)
        self.assertFalse(result["llm_assisted"])

    def test_stale_gate_dominates_lean(self):
        lean = {"available": True, "score_adjustment": 0.05, "direction": "YES", "source": "test"}
        result = score(near_threshold_info_action(), lean=lean,
                       freshness={"is_stale": True, "snapshot_age_seconds": 999999,
                                  "max_allowed_seconds": 21600})
        self.assertEqual(result["recommendation"], "ABSTAIN")
        self.assertEqual(result["abstain_reason_code"], "STALE_DATA")

    def test_treasury_dossier_gate_dominates_lean(self):
        action = near_threshold_info_action()
        action["action_type"] = "TreasuryWithdrawals"
        action["treasury_amount_lovelace"] = "1000000000"
        lean = {"available": True, "score_adjustment": 0.05, "direction": "YES", "source": "test"}
        result = score(action, lean=lean, deep_row={"dossier_complete": "no"})
        self.assertEqual(result["recommendation"], "NEEDS_MORE_INFO")
        self.assertEqual(result["needs_more_info_reason_code"], "DEEP_RESEARCH_REQUIRED")

    def test_offline_lean_is_deterministic_and_bounded(self):
        action = near_threshold_info_action()
        claims = {"available": True, "claims": [
            {"claim": "audited", "category": "technical",
             "support": "independently_verifiable", "materiality": "high"}]}
        a = llm._offline_assess_lean(action, claims, ASSESS, "# doctrine", "info")
        b = llm._offline_assess_lean(action, claims, ASSESS, "# doctrine", "info")
        self.assertTrue(a["available"])
        self.assertEqual(a["score_adjustment"], b["score_adjustment"])  # deterministic
        self.assertLessEqual(abs(a["score_adjustment"]), LLM_SCORE_ADJUST_CAP)  # bounded


if __name__ == "__main__":
    unittest.main()


class MessageVerdictGuardTests(unittest.TestCase):
    def test_stale_abstain_message_rejected_for_no_vote(self) -> None:
        from beacn_drep.llm import message_matches_recommendation
        text = "BEACN's autonomous DRep is recording ABSTAIN on this action, and the reason is procedural."
        self.assertFalse(message_matches_recommendation(text, "NO"))
        self.assertTrue(message_matches_recommendation(text, "ABSTAIN"))

    def test_matching_and_unnamed_messages_accepted(self) -> None:
        from beacn_drep.llm import message_matches_recommendation
        self.assertTrue(message_matches_recommendation("BEACN records NO on Example.", "NO"))
        self.assertTrue(message_matches_recommendation("BEACN votes YES on Example.", "YES"))
        self.assertTrue(message_matches_recommendation("This proposal funds tooling.", "NO"))
        self.assertFalse(message_matches_recommendation("BEACN records NO on Example.", "YES"))
