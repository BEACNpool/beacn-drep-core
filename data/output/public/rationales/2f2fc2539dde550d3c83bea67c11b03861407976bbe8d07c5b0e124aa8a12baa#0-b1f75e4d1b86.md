# Rationale: 2f2fc2539dde550d3c83bea67c11b03861407976bbe8d07c5b0e124aa8a12baa#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on Amaru Treasury Withdrawal 2026. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Amaru Treasury Withdrawal 2026. The strongest grounded claim is: Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security.

A material claim remains proposer-asserted or thinly supported: This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025. Open blockers: treasury_amount_lovelace is missing for a treasury withdrawal. BEACN's own independent diligence is also incomplete — before this vote could move to YES, BEACN's published review still needs complete proposal summary; budget analysis; feasibility assessment. Reason code: MISSING_BASELINE_EVIDENCE.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 614
- finding: Expires after epoch: 621
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Amaru Treasury Withdrawal 2026
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security., Amaru provides another perspective and solution for stake pool operators and developers alike, prioritizing low hardware requirements and a seamless user experience., The project is implemented primarily in Rust and aims to attract new contributors to the ecosystem's core maintenance., This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security.
- finding: Claim (economic, supported_in_proposal, low materiality): Amaru provides another perspective and solution for stake pool operators and developers alike, prioritizing low hardware requirements and a seamless user experience.
- finding: Claim (economic, proposer_asserted, low materiality): The project is implemented primarily in Rust and aims to attract new contributors to the ecosystem's core maintenance.
- finding: Claim (economic, proposer_asserted, high materiality): This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025.
- finding: Claim (economic, supported_in_proposal, low materiality): Before we dive further into the details and cost breakdown, here is a high-level view of the ask, some assumptions we are making, and the general direction of this withdrawal request.
- finding: Claim (economic, proposer_asserted, low materiality): 2025 Retrospective We provide a full retrospective of our 2025 roadmap in annex of this document.
- missing: Independent evidence for: This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025.
- missing: Independent evidence for: Duration & Milestones This proposal spans over 12 months , from January to December 2026, throughout which there will be several deliveries, demos, and workshops.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: not specified
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security." though 8 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: not specified
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security." though 8 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025.
- Claims and evidence missing: Independent evidence for: Duration & Milestones This proposal spans over 12 months , from January to December 2026, throughout which there will be several deliveries, demos, and workshops.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `b1f75e4d1b86e20d750e3e6ac2ed7ad9ecfe449e8bd3d92ac3d4671526673803`
- snapshot_bundle_hash: `7e6e04f7a80ebb0fa49a157eb89c5e0b6e399274a59927c0812e88c11411e46b`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `11`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

