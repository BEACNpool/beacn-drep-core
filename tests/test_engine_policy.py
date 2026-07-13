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


class CanonicalActionIdTests(unittest.TestCase):
    """One action, one id — the same proposal must never get two verdicts.

    Regression (2026-07-12): a governance action arrives under BOTH the CIP-129 "<tx>#<ix>" id
    and the legacy bech32 "gov_action1…" id. The engine scored each spelling separately, and the
    evidence packets (decision_support/*.csv) are keyed by ONE spelling — so the other spelling
    saw no evidence and fell to NEEDS_MORE_INFO. In the same run, at the same minute, "Eternl:
    Path to Sustainability - v2" scored YES (+0.2055) under tx#idx and NEEDS_MORE_INFO (-0.16)
    under bech32. The vote runner resolves bech32 gov-state against run dirs, so it read the
    evidence-less verdict — and a live on-chain NO was cast off it.
    """

    ETERNL_TX = "fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0"
    ETERNL_BECH = "gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse"

    def test_bech32_and_cip129_collapse_to_one_id(self):
        from beacn_drep.ids import canonical_action_id, same_action
        self.assertEqual(canonical_action_id(self.ETERNL_TX), self.ETERNL_TX)
        self.assertTrue(
            same_action(self.ETERNL_BECH, self.ETERNL_TX),
            "the two spellings of one action must canonicalise to the same id",
        )

    def test_canonical_form_is_cip129(self):
        from beacn_drep.ids import canonical_action_id
        out = canonical_action_id(self.ETERNL_BECH)
        self.assertRegex(out, r"^[0-9a-f]{64}#\d+$")

    def test_undecodable_id_is_returned_unchanged_not_guessed(self):
        # Merging two DISTINCT actions is far worse than failing to merge two spellings of one.
        from beacn_drep.ids import canonical_action_id
        self.assertEqual(canonical_action_id("gov_action1notrealbech32"), "gov_action1notrealbech32")
        self.assertEqual(canonical_action_id(""), "")


class AdapterActionIdDecodeTests(unittest.TestCase):
    """The adapter must accept every spelling of an action id that the pipeline can hand it.

    On 2026-07-12 it accepted only bech32. Policy approved four votes, every adapter gate passed,
    and all four then died at `invalid bech32 string` because the ids were already in canonical
    `<tx>#<index>` form. Zero votes were cast and the failure looked like a policy hold.
    """

    def test_both_spellings_decode_to_the_same_action(self):
        from beacn_drep.adapters.cardano_cli_adapter import decode_gov_action_id
        bech = "gov_action10dp9wzmgt2nqshyrghufff4sfhcxedhmzluly5k0azguatnsthwqqs84cjf"
        tx, idx = decode_gov_action_id(bech)
        self.assertEqual(decode_gov_action_id(f"{tx}#{idx}"), (tx, idx))

    def test_canonical_form_decodes(self):
        from beacn_drep.adapters.cardano_cli_adapter import decode_gov_action_id
        tx = "b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf"
        self.assertEqual(decode_gov_action_id(f"{tx}#2"), (tx, 2))

    def test_malformed_id_raises_rather_than_resolving_to_another_action(self):
        # Voting on the WRONG governance action is the worst failure this system has. A malformed
        # id must fail loudly, never get coerced into some neighbouring action.
        from beacn_drep.adapters.cardano_cli_adapter import decode_gov_action_id
        for bad in ("deadbeef#0", "z" * 64 + "#0",
                    "b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#x"):
            with self.assertRaises(ValueError):
                decode_gov_action_id(bad)


class MilestoneSelfClaimTests(unittest.TestCase):
    """A proposal's claim about itself must not outrank BEACN's verified finding against it.

    `milestone_payment_gates` is extracted from the proposal's own document and grants the largest
    single delivery weight (0.20). It was granting that credit even where independent research had
    VERIFIED `output_priced = no` — payment not tied to deliverables. Eleven proposals asking
    67,649,589 ADA were holding unearned delivery confidence on the strength of a sentence.
    """

    def _dims(self, output_priced, evidence_status="independently_verified"):
        from beacn_drep import engine as E
        return E._treasury_dimensions(
            action={"action_id": "x#0", "action_type": "TreasuryWithdrawals",
                    "treasury_amount_lovelace": "1000000000"},
            value_row={"evidence_status": evidence_status, "output_priced": output_priced,
                       "critical_infrastructure": "yes"},
            financial_row={"milestone_payment_gates": "yes"},
            risk_row=None, readiness_row=None, deep_complete=True,
        )

    def test_verified_not_output_priced_forfeits_the_self_claimed_milestone_credit(self):
        with_claim = self._dims("unknown")["delivery_confidence"]
        refuted = self._dims("no")["delivery_confidence"]
        self.assertAlmostEqual(with_claim - refuted, 0.20, places=4)

    def test_unknown_never_costs_the_proposer(self):
        # An "unknown" is BEACN's own research gap. It must never be charged to the proposal —
        # that would be missing evidence becoming negative evidence, which doctrine forbids.
        self.assertEqual(self._dims("unknown")["delivery_confidence"],
                         self._dims("yes")["delivery_confidence"])

    def test_credit_is_kept_when_the_evidence_is_not_independent(self):
        # Only an INDEPENDENTLY verified contrary finding may strip the credit.
        self.assertEqual(self._dims("no", evidence_status="proposal_only")["delivery_confidence"],
                         self._dims("unknown", evidence_status="proposal_only")["delivery_confidence"])
