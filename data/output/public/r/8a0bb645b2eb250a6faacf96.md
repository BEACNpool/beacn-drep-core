# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


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
- finding: Requested: Reimburse the lost deposit for the Ikigai Info governance action, plus additional ADA intended to compensate for lost staking rewards.
- finding: Recipient: Ikigai Info governance action submitter; specific recipient address not stated in document
- finding: Stated amount: 103000
- finding: Deliverables: Instant on-chain distribution as part of governance action enactment
- finding: Deadline/expiry: Period of delivery is stated as instant upon enactment on-chain
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA from the treasury to reimburse a 100,000 ADA lost governance action deposit plus 3,000 ADA for estimated lost staking rewards.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer says the original Ikigai Info governance action was a symbolic action thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer says a Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (governance, independently_verifiable, medium materiality): The document includes an external reference to an AdaStat governance action page for the Ikigai action.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer says there was significant community sentiment that the Ikigai deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- finding: Claim (governance, proposer_asserted, low materiality): The proposer says no entity-based budget submission included this reimbursement after treasury withdrawals became available following the Plomin hard fork.
- missing: Independent evidence for: The proposer says the original Ikigai Info governance action was a symbolic action thanking contributors and expressing hope for Cardano's future.
- missing: Independent evidence for: The proposer says a Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The proposer says there was significant community sentiment that the Ikigai deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- missing: Independent evidence for: The proposer asserts the recipient has not previously received treasury funds.
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
- finding: Six-month treasury flow regime: unsustainable
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury to reimburse a 100,000 ADA lost governance action deposit plus 3,000 ADA for estimated lost staking rewards." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer says the original Ikigai Info governance action was a symbolic action thanking contributors and expressing hope for Cardano's future." — so cost or precedent may outweigh the benefit.
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
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 103000
- Risk review: Execution risk: low
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury to reimburse a 100,000 ADA lost governance action deposit plus 3,000 ADA for estimated lost staking rewards." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: The proposer says the original Ikigai Info governance action was a symbolic action thanking contributors and expressing hope for Cardano's future.
- Claims and evidence missing: Independent evidence for: The proposer says a Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.
- Missing dossier section: budget analysis
- Missing dossier section: feasibility assessment
- Missing dossier section: alternatives analysis
- Missing dossier section: failure-mode analysis
- Missing dossier section: community impact analysis

## Reproducibility
- input_hash: `4db62802019d031174521f0ed15a4742abcc9cb25226b0ccc6ff3b33f1535856`
- snapshot_bundle_hash: `db87001e820f642b0d59a12e1d4915d8c9e37fdedcc41dfec30111fba366af78`
- soul_commit: `6bf4a7d7baa636417ad929e543cfb8be8fae1f03`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `693efb97d136543a3565ea51fab80f1cada41b23`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `340`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

