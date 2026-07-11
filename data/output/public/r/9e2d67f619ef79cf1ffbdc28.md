# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and the review did not yet have the completed deep-research dossier required before spending shared ADA.

The action requests 103,000 ADA from the Cardano treasury: 100,000 ADA to reimburse an unrecovered governance action deposit, plus 3,000 ADA for estimated missed staking rewards. The proposer says the earlier Ikigai Info action was submitted in September 2024, that a Cardano node bug prevented recovery of the deposit, that community sentiment favored reimbursement, and that the recipient has not previously received treasury funds. The review found the basic request itself well-supported in the proposal, and the proposal anchor was pinned and replayable. Execution risk was assessed as low.

However, several important claims were still unsupported or incomplete. The review did not have independent evidence that a Cardano node bug caused the unrecoverable deposit, or independent evidence for the claimed level of community support. The treasury analysis was incomplete, including missing budget analysis and no milestone-gated disbursement. The synthesis was blocked by missing feasibility, alternatives, failure-mode, and community impact analysis. The recipient identity or address was also not stated in the supplied document.

This is a conservative, evidence-based hold, not a rejection of the reimbursement request. A directional vote would be unblocked by a complete deep-research dossier with replayable public evidence for the node-bug claim, clearer recipient details, stronger claims-and-evidence mapping, and completed budget, feasibility, alternatives, failure-mode, and community impact analyses.

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
- finding: Requested: Reimburse the unrecovered deposit from the earlier Ikigai Info governance action, plus compensation for estimated missed staking rewards.
- finding: Recipient: the Ikigai Info governance action submitter; specific recipient identity/address not stated in document
- finding: Stated amount: 103,000 ADA
- finding: Deliverables: Instant on-chain distribution of the requested treasury withdrawal to the intended recipient upon enactment
- finding: Deadline/expiry: upon governance action enactment on-chain
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA from the Cardano treasury to reimburse a lost 100,000 ADA governance action deposit and add 3,000 ADA for missed staking rewards.
- finding: Claim (governance, independently_verifiable, medium materiality): The earlier Cardanoの生きがい - Ikigai - Info governance action was submitted in September 2024 shortly after the Chang hard fork.
- finding: Claim (governance, proposer_asserted, low materiality): The earlier Ikigai action was symbolic and asked whether the community agreed with a statement of thanks and hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer states there was significant community sentiment at the time that the Ikigai deposit should be reimbursed.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer states that entity-based budget submissions did not include this reimbursement after treasury withdrawals became available following the Plomin hard fork.
- missing: Independent evidence for: A Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The proposer states there was significant community sentiment at the time that the Ikigai deposit should be reimbursed.
- missing: Independent evidence for: The proposer states that entity-based budget submissions did not include this reimbursement after treasury withdrawals became available following the Plomin hard fork.
- missing: Independent evidence for: The Cardano in Oceania initiative included the reimbursement in its budget Info governance action, but that governance action was not approved.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the Cardano treasury to reimburse a lost 100,000 ADA governance action deposit and add 3,000 ADA for missed staking rewards." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "A Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the Cardano treasury to reimburse a lost 100,000 ADA governance action deposit and add 3,000 ADA for missed staking rewards." though 5 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: A Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- Claims and evidence missing: Independent evidence for: The proposer states there was significant community sentiment at the time that the Ikigai deposit should be reimbursed.
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
- snapshot_bundle_hash: `c6dbc71cfd23f5eb22e83f2ea4249aea2df6f60f1f0f80a0c8d9b647a2d6fb8f`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

