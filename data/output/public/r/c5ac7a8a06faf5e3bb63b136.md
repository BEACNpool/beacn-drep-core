# Rationale: d52a4917df4f91c342eaf06ebb4c0a5c3156f6412d137f307cc77eb911f47ab1#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and the review did not have a complete deep-research dossier with independent evidence for the key claim: that a Cardano node bug prevented recovery of the 100,000 ADA governance action deposit.

The action asks the treasury to pay 103,000 ADA to the Ikigai Info governance action submitter: 100,000 ADA for the unrecovered deposit and 3,000 ADA for estimated lost staking rewards at 2% per year. The proposer says the original Info action, “Cardanoの生きがい - Ikigai -,” was submitted in September 2024 after the Chang hard fork, and that the action was symbolic, thanking contributors and expressing hope for Cardano’s future. The review found the existence and timing of that Info action supported in the proposal, and the request amount was clearly stated.

However, several material claims remained only proposer-asserted or lacked independent support. Most importantly, the review did not have independent evidence that a node bug allowed an unregistered stake key to be used and made the deposit unrecoverable. It also lacked independent evidence that the Cardano in Oceania initiative previously included this reimbursement in a budget Info action that was not approved. The risk review found medium execution risk, with mitigation evidence and independent assurance still missing.

This is a conservative, evidence-based hold. A directional vote would be unblocked by a completed treasury deep-research dossier, replayable public evidence for the claimed node bug and deposit-recovery failure, independent support for the prior Cardano in Oceania reimbursement claim, and clearer treasury/risk analysis addressing mitigation and assurance.

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
- finding: Snapshot freshness source: governance_actions_all.csv
- finding: Deep research dossier: required
- finding: Requested: Reimburse the Ikigai Info governance action submitter for an unrecovered governance action deposit plus estimated lost staking rewards.
- finding: Recipient: Ikigai Info governance action submitter
- finding: Stated amount: 103,000
- finding: Deliverables: On-chain treasury withdrawal directly to the intended recipient upon enactment
- finding: Deadline/expiry: Instantly performed as part of the governance action's enactment on-chain
- finding: Claim (governance, supported_in_proposal, medium materiality): An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork.
- finding: Claim (governance, proposer_asserted, low materiality): The Ikigai Info governance action was symbolic and asked the community to agree with a statement thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug permitted use of an unregistered stake key in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards at 2% per annum.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
- finding: Claim (economic, proposer_asserted, medium materiality): The recipient of the reimbursement has not previously received treasury funds.
- missing: Independent evidence for: A Cardano node bug permitted use of an unregistered stake key in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: The recipient of the reimbursement has not previously received treasury funds.
- missing: Independent evidence for: The requested amount does not exceed the current Net Change Limit.
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
- finding: Strongest NO: a material claim is unsupported — "A Cardano node bug permitted use of an unregistered stake key in the governance action, preventing the submitter from recovering the 100,000 ADA deposit." — so cost or precedent may outweigh the benefit.
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
- Claims and evidence missing: Independent evidence for: A Cardano node bug permitted use of an unregistered stake key in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- Claims and evidence missing: Independent evidence for: The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
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
- input_hash: `dfe89011d8d3c892ed7d11fdea480190e5206cfd34731a4d9d99564aa22a6e4a`
- snapshot_bundle_hash: `fb07b084f5b87e2608003d434756df9c7ce6cbb434d20319afcd715ea7fb8f40`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `82a02efa3be4dedf61fea1548ca03635163347a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `22`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

