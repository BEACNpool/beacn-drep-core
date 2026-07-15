# Rationale: 2f2fc2539dde550d3c83bea67c11b03861407976bbe8d07c5b0e124aa8a12baa#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (binding treasury composite; advisory raw signal `0.0`; LLM lean `+0.0` recorded, not added) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Amaru Treasury Withdrawal 2026. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Amaru Treasury Withdrawal 2026. It asks the treasury for 10.14M ADA. The strongest grounded claim is: Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security.

A material claim remains proposer-asserted or thinly supported: This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025. BEACN's own independent diligence is also incomplete — before this vote could move to YES, BEACN's published review still needs complete proposal summary; budget analysis; feasibility assessment. Reason code: DEEP_RESEARCH_REQUIRED.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 614
- finding: Expires after epoch: 621
- finding: Treasury request: 10.14M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Amaru Treasury Withdrawal 2026
- finding: Recipient: not stated in document
- finding: Stated amount: 10.14M ADA
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
- finding: Requested ADA: 10.14M ADA
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
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 10.14M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Amaru is an open-source project building a new, fully interoperable block-producing node that improves the overall accessibility and robustness of the Cardano network without compromising its safety and security." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional voting is blocked until dossier quality gates pass.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Dossier completeness not confirmed for this treasury proposal.
- Claims and evidence missing: Independent evidence for: This is our second treasury withdrawal proposal, following a successful budget and treasury withdrawal in mid-2025.
- Claims and evidence missing: Independent evidence for: Duration & Milestones This proposal spans over 12 months , from January to December 2026, throughout which there will be several deliveries, demos, and workshops.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.
- Missing dossier section: complete proposal summary
- Missing dossier section: budget analysis
- Missing dossier section: feasibility assessment
- Missing dossier section: risk analysis
- Missing dossier section: alternatives analysis
- Missing dossier section: failure-mode analysis
- Missing dossier section: community impact analysis

## Reproducibility
- input_hash: `6a6d3bafab8cb7976b421ae0a766ed2c281038cdfca92d0dbc27a8d1f0885e5e`
- snapshot_bundle_hash: `1087ba33bccd83ac1bb17a4e08e672b67ee1c8131c44915534da467616453c46`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `3e3c343fc0dd14a03a92aad1216ba6620b3d0185`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

