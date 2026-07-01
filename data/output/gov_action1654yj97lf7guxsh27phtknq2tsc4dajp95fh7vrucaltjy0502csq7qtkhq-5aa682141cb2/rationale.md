# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NO**
Score: `-0.5333` (raw `-0.5033` + doctrine-LLM nudge `-0.03`) | Confidence: `1.0` | Readiness: `0.8`
> Reasoning layer (precomputed): The claims describe a sympathetic reimbursement request, but the material basis for spending treasury funds depends on asserted facts about the node bug, unrecoverable deposit, recipient history, NCL compliance, and community sentiment, while the deterministic assessment already identifies thin evidence and missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. Under a blocked treasury assessment, evidence quality does not justify a positive nudge and supports a small cautionary negative adjustment.

## Plain-language explanation (precomputed)
BEACN's autonomous DRep is recording ABSTAIN on this action, and the reason is procedural rather than a verdict on the proposal's merits. BEACN's on-chain governance data snapshot is currently about eight hours old, which is beyond the six-hour freshness limit its policy requires before it will cast a directional vote. When data is this stale BEACN holds rather than risk voting on an out-of-date picture of the proposal, the treasury, and the wider vote distribution. The request is narrow and sympathetic: 103,000 ADA to reimburse an early governance participant whose 100,000 ADA Info-action deposit was stranded by a documented Cardano node bug shortly after the Chang hard fork, plus 3,000 ADA for lost staking rewards. The core fact — that a node defect prevented recovery of the deposit — is independently checkable on-chain and is the strongest part of the case; the 2%-per-annum staking top-up is a reasonable but proposer-set figure. The amount is small relative to other live treasury actions and there is no ongoing delivery risk. Once BEACN's snapshot is current and the deep-research record confirms the bug and the recipient address, this is the kind of low-risk, well-bounded reimbursement on which it could reach a directional vote.

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to reimburse the Ikigai Info governance action deposit and claimed lost staking rewards.
- finding: Recipient: Ikigai Info governance action submitter / intended recipient; exact address not stated in document
- finding: Stated amount: 103,000
- finding: Deliverables: Instant on-chain distribution of reimbursement upon governance action enactment
- finding: Deadline/expiry: Period of delivery is instant as part of on-chain enactment
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA from the treasury to reimburse a lost 100,000 ADA governance action deposit plus 3,000 ADA for claimed lost staking rewards.
- finding: Claim (governance, proposer_asserted, medium materiality): The original Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork and was symbolic in nature.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer says there was significant community sentiment at the time that the deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that action was not approved.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal states there are no costs or expenses associated with the withdrawal beyond the reimbursement amount.
- missing: Independent evidence for: The original Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork and was symbolic in nature.
- missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The proposer says there was significant community sentiment at the time that the deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- missing: Independent evidence for: The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that action was not approved.
- missing: budget analysis
- missing: feasibility assessment
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 103000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: unknown (stale snapshot)
- finding: Financial confidence: 0.70
- missing: milestone-gated disbursement
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: low
- finding: Governance risk: low
- finding: Technical risk: low
- finding: Treasury exposure risk: low
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury to reimburse a lost 100,000 ADA governance action deposit plus 3,000 ADA for claimed lost staking rewards." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The original Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork and was symbolic in nature." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 103000
- Risk review: Execution risk: low
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury to reimburse a lost 100,000 ADA governance action deposit plus 3,000 ADA for claimed lost staking rewards." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims describe a sympathetic reimbursement request, but the material basis for spending treasury funds depends on asserted facts about the node bug, unrecoverable deposit, recipient history, NCL compliance, and community sentiment, while the deterministic assessment already identifies thin evidence and missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. Under a blocked treasury assessment, evidence quality does not justify a positive nudge and supports a small cautionary negative adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~19 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: The original Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork and was symbolic in nature.
- Claims and evidence missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `5aa682141cb2612360647bd7876ed6571bfe07e362b798b13f8c5a6525ad4d12`
- snapshot_bundle_hash: `3905606f27d9721eda2f1fc484dae49ce72a2500889eaadf71be644e17e38253`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `715`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1518, "NO": 0.8093, "YES": 0.0389}`

