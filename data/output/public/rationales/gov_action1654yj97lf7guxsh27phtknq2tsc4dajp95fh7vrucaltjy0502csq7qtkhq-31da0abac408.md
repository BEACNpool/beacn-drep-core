# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and the review did not yet have the completed deep-research dossier needed to justify a directional vote.

The action asks for 103,000 ADA from the treasury to reimburse the Ikigai Info governance action submitter: 100,000 ADA for an unrecovered governance action deposit and 3,000 ADA for estimated lost staking rewards. The proposal says the funds would be distributed on-chain to the intended recipient upon enactment, but the document did not state a specific recipient address or identity, and no deadline was provided.

The review found that the requested amount itself was clearly stated and supported in the proposal, and the proposal anchor was pinned and replayable. Execution risk was assessed as low. However, several important claims were still only proposer-asserted or thinly evidenced, including the reason the deposit could not be recovered, the claimed Cardano node bug involving an unregistered stake key, the history and purpose of the original Ikigai Info action, prior community sentiment, and whether the recipient had not previously received treasury funds.

This is a conservative, evidence-based hold. A directional vote would require the missing dossier gates to be completed, especially independent evidence for the unrecovered deposit and node-bug claim, a clear budget analysis, feasibility assessment, alternatives analysis, failure-mode analysis, community impact analysis, independent assurance, and dependency map. Until those are available, BEACN cannot responsibly treat this treasury request as ready for a YES or NO vote.

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
- finding: Requested: Reimburse the submitter of the Ikigai Info governance action for an unrecovered governance action deposit and estimated lost staking rewards.
- finding: Recipient: Ikigai Info governance action submitter; specific address or identity not stated in document
- finding: Stated amount: 103000
- finding: Deliverables: Instant on-chain distribution of funds to the intended recipient upon enactment
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA from the treasury to reimburse a 100,000 ADA lost deposit plus 3,000 ADA for estimated lost staking rewards.
- finding: Claim (governance, proposer_asserted, medium materiality): The original Ikigai Info governance action was submitted in September 2024 as a symbolic action thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): The submitter was unable to recover the 100,000 ADA deposit because a Cardano node bug permitted use of an unregistered stake key in the governance action.
- finding: Claim (governance, proposer_asserted, medium materiality): The document says there was significant community sentiment at the time that the Ikigai Info governance action deposit should be reimbursed.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal says Cardano in Oceania included the reimbursement in a budget Info governance action, but that governance action was not approved.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal claims the requested amount does not exceed the current Net Change Limit.
- missing: Independent evidence for: The original Ikigai Info governance action was submitted in September 2024 as a symbolic action thanking contributors and expressing hope for Cardano's future.
- missing: Independent evidence for: The submitter was unable to recover the 100,000 ADA deposit because a Cardano node bug permitted use of an unregistered stake key in the governance action.
- missing: Independent evidence for: The document says there was significant community sentiment at the time that the Ikigai Info governance action deposit should be reimbursed.
- missing: Independent evidence for: The proposal says Cardano in Oceania included the reimbursement in a budget Info governance action, but that governance action was not approved.
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
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury to reimburse a 100,000 ADA lost deposit plus 3,000 ADA for estimated lost staking rewards." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The original Ikigai Info governance action was submitted in September 2024 as a symbolic action thanking contributors and expressing hope for Cardano's future." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury to reimburse a 100,000 ADA lost deposit plus 3,000 ADA for estimated lost staking rewards." though 5 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: The original Ikigai Info governance action was submitted in September 2024 as a symbolic action thanking contributors and expressing hope for Cardano's future.
- Claims and evidence missing: Independent evidence for: The submitter was unable to recover the 100,000 ADA deposit because a Cardano node bug permitted use of an unregistered stake key in the governance action.
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
- input_hash: `31da0abac4087cd2084307bf3e78123feadd69854728aac48c5d7887b96d8f2f`
- snapshot_bundle_hash: `2269bb3df928f9998094fdeac7bf46b9049bb434215adc5f834c139bde840dda`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

