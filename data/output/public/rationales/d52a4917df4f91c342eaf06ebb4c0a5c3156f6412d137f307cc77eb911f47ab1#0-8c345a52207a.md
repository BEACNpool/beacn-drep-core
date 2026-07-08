# Rationale: d52a4917df4f91c342eaf06ebb4c0a5c3156f6412d137f307cc77eb911f47ab1#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was missing baseline evidence needed to responsibly judge a treasury withdrawal. This is a conservative, evidence-based hold, not a rejection of the reimbursement request itself.

The proposal asked for 103,000 ADA to reimburse the Ikigai Info governance action submitter for an unrecovered 100,000 ADA governance action deposit, plus 3,000 ADA in estimated lost staking rewards, with funds distributed directly on-chain if enacted. The proposal supported the basic claim that this is the amount being requested and why, and it provided a pinned, replayable proposal anchor. It also referenced an external AdaStat page for the original governance action.

However, several important claims were still only proposer assertions or lacked independent evidence in the review. These included the claim that a Cardano node bug allowed an unregistered stake key to be used and prevented deposit recovery, the description of the original Ikigai action as symbolic, the level of community sentiment for reimbursement, and the claim that the recipient had not previously received treasury funds. The review also found missing or incomplete treasury, feasibility, risk, alternatives, failure-mode, and community-impact analysis.

For BEACN to move from ABSTAIN to a directional vote, the missing treasury withdrawal baseline would need to be complete, including the required `treasury_amount_lovelace` field, a complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, community impact analysis, and independent evidence for the key technical and governance claims. Since those blockers remained open, BEACN held its vote at ABSTAIN.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 636
- finding: Expires after epoch: 643
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
- finding: Requested: Reimburse the submitter of the Ikigai Info governance action for an unrecovered governance action deposit plus estimated lost staking rewards.
- finding: Recipient: Ikigai Info governance action submitter
- finding: Stated amount: 103,000
- finding: Deliverables: Instant on-chain distribution to the intended recipient upon enactment
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests a treasury withdrawal of 103,000 ADA to reimburse a lost 100,000 ADA governance action deposit plus 3,000 ADA for estimated lost staking rewards.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer states that the original Ikigai Info governance action was a symbolic action thanking contributors to Cardano governance and expressing hope for the future.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer states that a Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing recovery of the 100,000 ADA deposit.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer states that there was significant community sentiment at the time that the Ikigai deposit should be reimbursed.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal references an external AdaStat governance action page for the original Ikigai governance action.
- finding: Claim (governance, proposer_asserted, low materiality): The proposer states that the Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that action was not approved.
- missing: Independent evidence for: The proposer states that the original Ikigai Info governance action was a symbolic action thanking contributors to Cardano governance and expressing hope for the future.
- missing: Independent evidence for: The proposer states that a Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing recovery of the 100,000 ADA deposit.
- missing: Independent evidence for: The proposer states that there was significant community sentiment at the time that the Ikigai deposit should be reimbursed.
- missing: Independent evidence for: The proposer states that the recipient has not previously received treasury funds.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: unknown
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: not confirmed
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests a treasury withdrawal of 103,000 ADA to reimburse a lost 100,000 ADA governance action deposit plus 3,000 ADA for estimated lost staking rewards." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that the original Ikigai Info governance action was a symbolic action thanking contributors to Cardano governance and expressing hope for the future." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests a treasury withdrawal of 103,000 ADA to reimburse a lost 100,000 ADA governance action deposit plus 3,000 ADA for estimated lost staking rewards." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: The proposer states that the original Ikigai Info governance action was a symbolic action thanking contributors to Cardano governance and expressing hope for the future.
- Claims and evidence missing: Independent evidence for: The proposer states that a Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing recovery of the 100,000 ADA deposit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `8c345a52207a9df238976f8b0328b480ebe3239848f1e9b5f24fdc8e979fcb6b`
- snapshot_bundle_hash: `cb273c51f13db9db41316322a051ddaab4e6da4e0315b44ccba431aa78f5afa5`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

