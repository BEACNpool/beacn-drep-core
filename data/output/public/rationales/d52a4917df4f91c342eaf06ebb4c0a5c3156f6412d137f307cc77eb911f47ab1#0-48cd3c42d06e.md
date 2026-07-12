# Rationale: d52a4917df4f91c342eaf06ebb4c0a5c3156f6412d137f307cc77eb911f47ab1#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and the review did not have enough independent evidence or completed risk analysis to justify a directional vote.

The proposal asks the Cardano treasury to pay 103,000 ADA to the Ikigai Info governance action submitter: 100,000 ADA to reimburse the original lost deposit, plus 3,000 ADA for claimed lost staking rewards. The proposer says the original Ikigai Info action was submitted in September 2024 shortly after Chang, was symbolic in nature, and that a Cardano node bug allowed an unregistered stake key to be used, preventing recovery of the deposit. The proposal also says there was community sentiment in favor of reimbursement, that a prior Cardano in Oceania budget action included this reimbursement but was not approved, and that the recipient has not previously received treasury funds.

Some parts were supported well enough for intake: the proposal anchor was pinned and replayable, the requested amount was clear, the on-chain distribution would be auditable, and the existence of the September 2024 Ikigai Info action was substantiated. But the central reason for reimbursement was not independently evidenced in the review: the claimed node bug and its link to the unrecoverable 100,000 ADA deposit remained unsupported beyond proposer assertion. The review also found thin claims-and-evidence status overall.

This is a conservative, evidence-based hold. The review gates for a treasury action were not complete: treasury analysis was incomplete, risk review lacked mitigation evidence and independent assurance, and synthesis was blocked by missing risk analysis, missing alternatives analysis, and missing failure-mode analysis. A directional vote would be unblocked by a completed deep-research dossier with independent evidence for the node-bug claim, clearer risk and failure-mode analysis, alternatives analysis, and treasury-specific support such as mitigation evidence and independent assurance.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 636
- finding: Expires after epoch: 643
- finding: Treasury request: 103.0k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to reimburse the lost deposit for the Ikigai Info governance action, plus compensation for staking rewards.
- finding: Recipient: the Ikigai Info governance action submitter
- finding: Stated amount: 103,000
- finding: Deliverables: Instant on-chain distribution of funds to the intended recipient upon enactment
- finding: Deadline/expiry: not stated in document
- finding: Claim (governance, supported_in_proposal, medium materiality): An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork.
- finding: Claim (governance, proposer_asserted, low materiality): The Ikigai Info governance action was symbolic and asked whether the community agreed with a statement of thanks and hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug allowed an unregistered stake key to be used for the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards calculated at 2% per year.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal states there were significant community sentiments at the time that the Ikigai Info governance action deposit should be reimbursed.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included this reimbursement in a budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: A Cardano node bug allowed an unregistered stake key to be used for the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The proposal states there were significant community sentiments at the time that the Ikigai Info governance action deposit should be reimbursed.
- missing: Independent evidence for: The Cardano in Oceania initiative included this reimbursement in a budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: The recipient has not previously received funds from the treasury.
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 103000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: not confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: low
- finding: Governance risk: medium
- finding: Technical risk: low
- finding: Treasury exposure risk: low
- finding: Mitigation evidence: not confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: not confirmed
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork." though 3 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "A Cardano node bug allowed an unregistered stake key to be used for the governance action, preventing the submitter from recovering the 100,000 ADA deposit." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 103000
- Risk review: Execution risk: low
- Counterargument pass: Strongest YES: the proposal substantiates "An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork." though 3 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: A Cardano node bug allowed an unregistered stake key to be used for the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- Claims and evidence missing: Independent evidence for: The proposal states there were significant community sentiments at the time that the Ikigai Info governance action deposit should be reimbursed.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Synthesis missing: missing risk analysis
- Synthesis missing: missing alternatives analysis
- Synthesis status is blocked.

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.
- Missing dossier section: risk analysis
- Missing dossier section: alternatives analysis
- Missing dossier section: failure-mode analysis

## Reproducibility
- input_hash: `48cd3c42d06e09a9fbc51057c0657d04a2f55f6239efcc0c68beb26d8505854d`
- snapshot_bundle_hash: `14db6e966060728c8a20228b1f5c76bdb3ee229205451fdf59cf6b959ff6388d`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

