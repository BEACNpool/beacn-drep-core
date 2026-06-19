import unittest

from beacn_drep.engine import _build_assessment, _score_action


def base_action(action_type: str) -> dict:
    return {
        "action_id": "gov_action_test",
        "action_type": action_type,
        "status": "active",
        "proposed_epoch": "637",
        "expiration_epoch": "644",
        "anchor_url": "ipfs://example",
        "anchor_hash": "ab" * 32,
        "flag_score": "0",
        # Ratification support snapshot: low YES early in the vote, with the
        # remaining stake not yet YES. This must not be treated as active NO.
        "drep_yes_pct": "11.38",
        "drep_no_pct": "88.62",
        "drep_abstain_pct": "",
        "treasury_amount_lovelace": "",
    }


def score_for(
    action: dict,
    *,
    readiness_row: dict | None = None,
    risk_row: dict | None = None,
    deep_row: dict | None = None,
) -> dict:
    freshness = {"is_stale": False, "snapshot_age_seconds": 1, "freshness_source": "test"}
    missing = []
    assessment = _build_assessment(
        action,
        freshness,
        missing,
        True,
        readiness_row,
        None,
        risk_row,
        deep_row,
        {},
        {},
        [],
        {
            "available": True,
            "request": {"what": "Test action", "deliverables": ["test"], "deadline": "not stated"},
            "claims": [
                {
                    "claim": "The action is technically scoped.",
                    "category": "technical",
                    "support": "independently_verifiable",
                    "materiality": "high",
                }
            ],
        },
    )
    return _score_action(
        action,
        [],
        freshness,
        missing,
        True,
        assessment,
        readiness_row,
        None,
        risk_row,
        deep_row,
        {},
        {},
        {
            "weights": {
                "anchor_present_bonus": 0.05,
                "treasury_base_penalty": -0.10,
                "parameter_change_base_penalty": -0.05,
                "hardfork_base_penalty": -0.12,
                "flag_score_divisor": 30.0,
                "flag_penalty_cap": 0.35,
                "drep_margin_cap": 0.10,
            }
        },
    )


class EnginePolicyTests(unittest.TestCase):
    def test_clean_hardfork_low_ratification_support_is_agentic_yes(self) -> None:
        result = score_for(base_action("HardForkInitiation"))

        self.assertEqual(result["recommendation"], "YES")
        self.assertFalse(result["operator_review_required"])
        self.assertIsNone(result["operator_review_reason_code"])
        self.assertEqual(result["agentic_high_impact_reason_code"], "HIGH_IMPACT_HARD_FORK")
        self.assertIn("not treated as active opposition", " ".join(result["uncertainty"]))

    def test_committee_liveness_parameter_is_agentic_yes(self) -> None:
        action = base_action("ParameterChange")
        action["metadata_title"] = "Reduce the committeeMinSize parameter from 7 to 5"
        action["param_changes"] = '{"committee_min_size": 5}'

        result = score_for(action)

        self.assertEqual(result["recommendation"], "YES")
        self.assertFalse(result["operator_review_required"])
        self.assertIsNone(result["operator_review_reason_code"])
        self.assertEqual(result["agentic_high_impact_reason_code"], "GOVERNANCE_LIVENESS_PARAMETER")
        self.assertIn("committeeMinSize liveness", " ".join(result["inferences"]))

    def test_generic_parameter_change_does_not_use_liveness_exception(self) -> None:
        action = base_action("ParameterChange")
        action["metadata_title"] = "Increase max block body size"
        action["param_changes"] = '{"max_block_body_size": 98304}'

        result = score_for(action)

        self.assertEqual(result["recommendation"], "ABSTAIN")
        self.assertFalse(result["operator_review_required"])

    def test_hardfork_with_high_unmitigated_flags_still_abstains(self) -> None:
        action = base_action("HardForkInitiation")
        action["flag_score"] = "9"
        result = _score_action(
            action,
            [],
            {"is_stale": False, "snapshot_age_seconds": 1, "freshness_source": "test"},
            [],
            True,
            {"sections": [], "overall_status": "ready"},
            None,
            None,
            None,
            None,
            {},
            {},
            {"weights": {"hardfork_base_penalty": -0.12, "flag_score_divisor": 30.0}},
        )

        self.assertEqual(result["recommendation"], "ABSTAIN")
        self.assertEqual(result["abstain_reason_code"], "RISK_HIGH")

    def test_treasury_without_deep_dossier_needs_more_info(self) -> None:
        # Default (empty doctrine) -> code default is the strict HARD gate.
        action = base_action("TreasuryWithdrawals")
        action["treasury_amount_lovelace"] = "1000000000"
        result = score_for(action, deep_row={"dossier_complete": "no"})

        self.assertEqual(result["recommendation"], "NEEDS_MORE_INFO")
        self.assertEqual(result["needs_more_info_reason_code"], "DEEP_RESEARCH_REQUIRED")

    def test_treasury_soft_gate_votes_directionally_not_nmi(self) -> None:
        # Soul doctrine sets dossier_gate.mode=soft -> judge directionally with a
        # caution penalty instead of holding at NEEDS_MORE_INFO.
        action = base_action("TreasuryWithdrawals")
        action["treasury_amount_lovelace"] = "1000000000"
        soft = {"dossier_gate": {"mode": "soft", "incomplete_penalty": -0.10}}
        result = _score_action(
            action, [],
            {"is_stale": False, "snapshot_age_seconds": 1, "freshness_source": "test"},
            [], True, {"sections": [], "overall_status": "ready", "blocking_questions": []},
            None, None, None, {"dossier_complete": "no"}, {}, soft,
            {"weights": {"treasury_base_penalty": -0.10, "anchor_present_bonus": 0.05,
                         "flag_score_divisor": 30.0, "drep_margin_cap": 0.10}},
        )
        self.assertNotEqual(result["recommendation"], "NEEDS_MORE_INFO")
        self.assertIn(result["recommendation"], ("NO", "ABSTAIN", "YES"))
        self.assertEqual(result["treasury_gate_mode"], "soft")
        self.assertTrue(result["treasury_dossier_incomplete"])


if __name__ == "__main__":
    unittest.main()
