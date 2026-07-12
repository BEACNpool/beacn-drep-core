import unittest

from beacn_drep.engine import (_build_assessment, _score_action, _treasury_dimensions,
                               _treasury_merit_recommendation, _ncl_spent_lovelace,
                               NCL_VERIFIED_STATUSES)


class NclCapacityWindowTests(unittest.TestCase):
    """Spend charged against the NCL must be measured over the NCL's OWN period.

    Regression (2026-07-12): the engine charged a rolling 73-epoch window against the NCL, which
    swept in withdrawals enacted BEFORE the period began (those belong to the PREVIOUS NCL). At
    epoch 642 that read 638.5M ADA against a 300M NCL -> available == 0 -> the engine FORCED a
    directional NO on every treasury proposal, including "Eternl: Path to Sustainability - v2",
    which the portfolio had ranked #1 and fundable. True in-period spend was 291.4M, leaving 8.6M.

    A forced NO on a phantom overspend is the worst failure available to this system: it is
    directional (castable on-chain) and it votes down meritorious work for a reason that is false.
    """

    NCL = 300_000_000_000_000          # 300M ADA
    IN_PERIOD = 291_435_336_000_000    # true spend within epochs 613-713 at epoch 642
    ROLLING_73E = 638_466_843_000_000  # rolling window — includes the PREVIOUS NCL period

    def test_prefers_in_period_spend_over_rolling_window(self):
        spent = _ncl_spent_lovelace(
            {"withdrawals_in_period_lovelace": self.IN_PERIOD},
            {"withdrawals_73e_lovelace": self.ROLLING_73E},
        )
        self.assertEqual(spent, self.IN_PERIOD)

    def test_real_capacity_remains_so_a_fundable_proposal_is_not_force_voted_no(self):
        spent = _ncl_spent_lovelace(
            {"withdrawals_in_period_lovelace": self.IN_PERIOD},
            {"withdrawals_73e_lovelace": self.ROLLING_73E},
        )
        available = self.NCL - spent
        self.assertGreater(available, 0, "capacity must not be phantom-depleted")
        # Eternl asks 2.35M ADA and must fit inside the real remaining capacity.
        self.assertGreater(available, 2_350_000_000_000)

    def test_rolling_window_alone_would_have_forced_the_bad_no(self):
        # Guards the claim above: with only the rolling figure, capacity really does go to zero.
        spent = _ncl_spent_lovelace({}, {"withdrawals_73e_lovelace": self.ROLLING_73E})
        self.assertEqual(spent, self.ROLLING_73E)
        self.assertLessEqual(self.NCL - spent, 0)

    def test_falls_back_to_rolling_window_only_when_in_period_absent(self):
        self.assertEqual(
            _ncl_spent_lovelace({"withdrawals_in_period_lovelace": 0},
                                {"withdrawals_73e_lovelace": self.ROLLING_73E}),
            self.ROLLING_73E,
        )

    def test_info_action_ncl_counts_as_verified(self):
        # Info actions can never be enacted, so demanding "verified_on_chain" made the treasury
        # gate unsatisfiable and froze all funding permanently.
        self.assertIn("verified_onchain_info_action", NCL_VERIFIED_STATUSES)


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
    protocol_row: dict | None = None,
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
                },
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
        protocol_row=protocol_row,
    )


class EnginePolicyTests(unittest.TestCase):
    def test_clean_hardfork_low_ratification_support_is_agentic_yes(self) -> None:
        result = score_for(base_action("HardForkInitiation"), protocol_row={
            "evidence_status": "independently_verified", "version_guardrails_pass": "yes",
            "testnet_results_pass": "yes", "spo_readiness_pass": "yes",
            "exchange_readiness_pass": "yes", "dapp_readiness_pass": "yes",
            "security_review_pass": "yes", "constitutional_alignment_pass": "yes",
            "rollback_or_containment_plan": "yes", "affirmative_blocker": "no",
        })

        self.assertEqual(result["recommendation"], "YES")
        self.assertFalse(result["operator_review_required"])
        self.assertIsNone(result["operator_review_reason_code"])
        self.assertEqual(result["agentic_high_impact_reason_code"], "HIGH_IMPACT_HARD_FORK")
        self.assertIn("not treated as active opposition", " ".join(result["uncertainty"]))

    def test_committee_liveness_parameter_is_agentic_yes(self) -> None:
        action = base_action("ParameterChange")
        action["metadata_title"] = "Reduce the committeeMinSize parameter from 7 to 5"
        action["param_changes"] = '{"committee_min_size": 5}'

        result = score_for(action, protocol_row={
            "evidence_status": "independently_verified", "constitutional_alignment_pass": "yes",
            "impact_analysis_complete": "yes", "rollback_or_containment_plan": "yes",
            "safety_margin_clear": "yes", "affirmative_blocker": "no",
        })

        self.assertEqual(result["recommendation"], "YES")
        self.assertFalse(result["operator_review_required"])
        self.assertIsNone(result["operator_review_reason_code"])
        self.assertEqual(result["agentic_high_impact_reason_code"], "GOVERNANCE_LIVENESS_PARAMETER")
        self.assertIn("independently verified", " ".join(result["inferences"]))

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

    def test_treasury_soft_gate_cannot_turn_missing_evidence_into_no(self) -> None:
        # Doctrine v1.4: even a legacy soft setting cannot turn missing evidence
        # into a directional treasury vote.
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
        self.assertEqual(result["recommendation"], "NEEDS_MORE_INFO")
        self.assertEqual(result["needs_more_info_reason_code"], "DEEP_RESEARCH_REQUIRED")


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
            None, None, None, {"dossier_complete": "yes"}, stale_flow, soft,
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
                                None, financial, None, {"dossier_complete": "yes"}, {}, soft, weights)
        general["treasury_amount_lovelace"] = "103000000000"
        r_general = _score_action(general, [], fresh, [], True, empty_assessment,
                                  None, financial, None, {"dossier_complete": "yes"}, {}, soft, weights)
        # Same inputs except the title: the reimbursement must not carry the -0.15
        # no-milestones penalty that the general spend does.
        self.assertAlmostEqual(r_reimb["raw_score"] - r_general["raw_score"], 0.15, places=4)
        self.assertTrue(any("reimbursement" in f.lower() for f in r_reimb["facts"]))

    def test_balanced_treasury_yes_requires_verified_benefit_and_controls(self) -> None:
        action = base_action("TreasuryWithdrawals")
        action["treasury_amount_lovelace"] = "1000000000"
        result = _score_action(
            action, [], {"is_stale": False}, [], True,
            {"sections": [], "overall_status": "ready"},
            {"timeline_defined": "yes", "risk_profile_complete": "yes"},
            {"budget_granularity": "yes", "milestone_payment_gates": "yes",
             "clawback_refund_path": "yes", "cost_benefit_clarity": "yes",
             "sustainability_path_clear": "yes"},
            {"execution_risk_level": "low", "governance_risk_level": "low",
             "technical_risk_level": "medium", "treasury_exposure_risk_level": "low",
             "mitigation_evidence_present": "yes", "independent_assurance_present": "yes"},
            {"dossier_complete": "yes"}, {}, {"dossier_gate": {"mode": "hard"}},
            {"weights": {"treasury_base_penalty": -0.10, "anchor_present_bonus": 0.05,
                         "flag_score_divisor": 30.0}}, None,
            {"evidence_status": "independently_verified", "critical_infrastructure": "yes",
             "open_source_public_good": "yes", "measurable_existing_adoption": "yes",
             "ecosystem_leverage": "yes", "credible_prior_delivery": "yes",
             "cost_compared_to_market": "yes", "output_priced": "yes"},
            {"verification_status": "verified_on_chain", "ncl_lovelace": 500_000_000_000_000},
            {"status": "verified", "candidates": [{"action_id": "gov_action_test",
             "funding_eligible": "yes", "rank": 1}]},
        )
        self.assertEqual(result["recommendation"], "YES")
        self.assertGreaterEqual(result["treasury_dimensions"]["benefit"], 0.55)

    def test_balanced_treasury_no_requires_affirmative_waste_evidence(self) -> None:
        action = base_action("TreasuryWithdrawals")
        action["treasury_amount_lovelace"] = "1000000000"
        result = _score_action(
            action, [], {"is_stale": False}, [], True,
            {"sections": [], "overall_status": "ready"}, None,
            {"budget_granularity": "yes", "cost_benefit_clarity": "no"},
            {"execution_risk_level": "high", "governance_risk_level": "medium",
             "technical_risk_level": "medium", "treasury_exposure_risk_level": "high"},
            {"dossier_complete": "yes"}, {}, {"dossier_gate": {"mode": "hard"}},
            {"weights": {"treasury_base_penalty": -0.10, "anchor_present_bonus": 0.05,
                         "flag_score_divisor": 30.0}}, None,
            {"evidence_status": "independently_verified", "material_duplication": "yes",
             "critical_infrastructure": "no", "open_source_public_good": "no"},
            {"verification_status": "verified_on_chain", "ncl_lovelace": 500_000_000_000_000},
            {"status": "verified", "candidates": [{"action_id": "gov_action_test",
             "funding_eligible": "no", "rank": 2}]},
        )
        self.assertEqual(result["recommendation"], "NO")
        self.assertTrue(result["treasury_dimensions"]["affirmative_waste_evidence"])

    def test_established_infrastructure_prices_non_funding_risk_without_special_case(self) -> None:
        dimensions = _treasury_dimensions(
            base_action("TreasuryWithdrawals"),
            {"evidence_status": "independently_verified", "critical_infrastructure": "yes",
             "measurable_existing_adoption": "yes", "ecosystem_leverage": "yes",
             "credible_prior_delivery": "yes", "established_service": "yes",
             "builder_workflow_dependency": "yes", "low_functional_substitutability": "yes",
             "non_funding_disruption_risk": "yes"},
            {"timeline_defined": "yes", "risk_profile_complete": "no"},
            {"budget_granularity": "yes", "clawback_refund_path": "yes",
             "sustainability_path_clear": "yes", "cost_benefit_clarity": "unknown"},
            {"execution_risk_level": "unknown", "governance_risk_level": "medium",
             "technical_risk_level": "unknown", "treasury_exposure_risk_level": "medium",
             "mitigation_evidence_present": "yes", "independent_assurance_present": "no"},
            False,
        )
        self.assertGreaterEqual(dimensions["benefit"], 0.55)
        self.assertGreaterEqual(dimensions["delivery_confidence"], 0.55)
        self.assertEqual(_treasury_merit_recommendation(dimensions)[0], "YES")


if __name__ == "__main__":
    unittest.main()
