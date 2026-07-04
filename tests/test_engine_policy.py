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


    def test_stale_treasury_flow_does_not_penalize(self) -> None:
        # An out-of-date fee-flow snapshot must not apply the regime penalty.
        from beacn_drep.engine import _treasury_flow_stale, _mainnet_epoch_now
        stale, epoch, lag = _treasury_flow_stale({"current_epoch": 621})
        self.assertTrue(stale)
        self.assertGreater(lag, 6)
        fresh, _, lag2 = _treasury_flow_stale({"current_epoch": _mainnet_epoch_now()})
        self.assertFalse(fresh)
        self.assertLessEqual(lag2, 6)

        action = base_action("TreasuryWithdrawals")
        action["treasury_amount_lovelace"] = "1000000000"
        soft = {"dossier_gate": {"mode": "soft", "incomplete_penalty": -0.10}}
        stale_flow = {"current_epoch": 621, "treasury_fee_inflow_6m_lovelace": "1",
                      "treasury_withdrawals_6m_lovelace": "999999999999"}
        result = _score_action(
            action, [],
            {"is_stale": False, "snapshot_age_seconds": 1, "freshness_source": "test"},
            [], True, {"sections": [], "overall_status": "ready", "blocking_questions": []},
            None, None, None, {"dossier_complete": "no"}, stale_flow, soft,
            {"weights": {"treasury_base_penalty": -0.10, "anchor_present_bonus": 0.05,
                         "treasury_flow_unsustainable_penalty": -0.10, "flag_score_divisor": 30.0,
                         "drep_margin_cap": 0.10}},
        )
        self.assertTrue(any("stale" in u.lower() for u in result["uncertainty"]))

    def test_confidence_is_capped_and_evidence_based(self) -> None:
        # A big penalty stack must NOT inflate confidence (old bug: 0.55+|score| -> 1.0).
        action = base_action("TreasuryWithdrawals")
        action["treasury_amount_lovelace"] = "103000000000"
        action["flag_score"] = "7"
        soft = {"dossier_gate": {"mode": "soft", "incomplete_penalty": -0.10}}
        result = _score_action(
            action, [{"flag": "a"}, {"flag": "b"}],
            {"is_stale": False, "snapshot_age_seconds": 1, "freshness_source": "test"},
            [], True, {"sections": [], "overall_status": "blocked", "blocking_questions": ["x"]},
            None, None, None, {"dossier_complete": "no"},
            {"current_epoch": 9999, "treasury_inflow_total_6m_lovelace": "100",
             "treasury_withdrawals_6m_lovelace": "999999"},
            soft,
            {"weights": {"treasury_base_penalty": -0.10, "anchor_present_bonus": 0.05,
                         "treasury_flow_unsustainable_penalty": -0.10, "flag_score_divisor": 30.0,
                         "drep_margin_cap": 0.10}},
        )
        self.assertLessEqual(result["confidence"], 0.90)
        self.assertLess(result["confidence"], 0.75)  # thin evidence can't read as near-certain

    def test_true_inflow_preferred_over_fee_inflow(self) -> None:
        from beacn_drep.engine import _treasury_flow_amounts
        inflow, outflow, basis = _treasury_flow_amounts({
            "treasury_inflow_total_6m_lovelace": "158838297854652",
            "treasury_fee_inflow_6m_lovelace": "302047240294",
            "treasury_withdrawals_6m_lovelace": "361435336000000",
        })
        self.assertEqual(inflow, 158838297854652.0)
        self.assertIn("total inflow", basis)
        legacy_inflow, _, legacy_basis = _treasury_flow_amounts({
            "treasury_fee_inflow_6m_lovelace": "302047240294",
            "treasury_withdrawals_6m_lovelace": "361435336000000",
        })
        self.assertEqual(legacy_inflow, 302047240294.0)
        self.assertIn("legacy", legacy_basis)

    def test_reimbursement_profile_skips_milestone_penalty(self) -> None:
        from beacn_drep.engine import _treasury_profile
        reimb = base_action("TreasuryWithdrawals")
        reimb["metadata_title"] = "Reimburse Ikigai Info Governance Action Deposit"
        self.assertEqual(_treasury_profile(reimb), "reimbursement")
        general = base_action("TreasuryWithdrawals")
        general["metadata_title"] = "Fund a new DeFi integration"
        self.assertEqual(_treasury_profile(general), "general")

        reimb["treasury_amount_lovelace"] = "103000000000"
        soft = {"dossier_gate": {"mode": "soft", "incomplete_penalty": -0.10}}
        weights = {"weights": {"treasury_base_penalty": -0.10, "anchor_present_bonus": 0.05,
                               "flag_score_divisor": 30.0, "drep_margin_cap": 0.10}}
        financial = {"milestone_payment_gates": "no"}
        fresh = {"is_stale": False, "snapshot_age_seconds": 1, "freshness_source": "test"}
        empty_assessment = {"sections": [], "overall_status": "ready", "blocking_questions": []}
        r_reimb = _score_action(reimb, [], fresh, [], True, empty_assessment,
                                None, financial, None, {"dossier_complete": "no"}, {}, soft, weights)
        general["treasury_amount_lovelace"] = "103000000000"
        r_general = _score_action(general, [], fresh, [], True, empty_assessment,
                                  None, financial, None, {"dossier_complete": "no"}, {}, soft, weights)
        # Same inputs except the title: the reimbursement must not carry the -0.15
        # no-milestones penalty that the general spend does.
        self.assertAlmostEqual(r_reimb["raw_score"] - r_general["raw_score"], 0.15, places=4)
        self.assertTrue(any("reimbursement" in f.lower() for f in r_reimb["facts"]))


if __name__ == "__main__":
    unittest.main()
