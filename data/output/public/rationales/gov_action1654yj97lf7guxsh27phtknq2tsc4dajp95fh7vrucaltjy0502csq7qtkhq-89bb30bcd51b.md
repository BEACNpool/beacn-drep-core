# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NO**
Score: `-0.4833` (raw `-0.4533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.64` | Readiness: `0.8`
> Reasoning layer (precomputed): The deterministic assessment is already blocked for missing budget, feasibility, alternatives, failure-mode, and community-impact analysis, and the extracted claims show the central loss, bug cause, recipient history, and NCL compliance are mostly proposer assertions. A small negative nudge is warranted for treasury stewardship and evidence quality, especially because the request spends treasury funds without documented verification of the unrecovered deposit or reward calculation in the supplied document.

## Plain-language explanation (precomputed)
BEACN voted NO because the proposal asks to spend treasury funds, but key evidence and analysis needed for treasury stewardship were missing. The request may be sympathetic, but the review found that several material claims remained unsupported and five decisive review blockers were still open.

The action requested 103,000 ADA to reimburse the Ikigai Info governance action submitter: 100,000 ADA for an unrecovered deposit and 3,000 ADA for estimated lost staking rewards at 2% per year. The proposer said the original Info action was submitted in September 2024 after Chang, that it was symbolic, that a Cardano node bug allowed an unregistered stake key and prevented recovery of the deposit, and that there was community sentiment in favor of reimbursement. The amount requested was supported in the proposal, and the action would pay the intended recipient directly on-chain if enacted.

However, the review found the evidence base was thin. Independent evidence was missing for the prior action’s timing and for the core technical claim that a node bug caused the deposit to become unrecoverable. Other important claims, including recipient history and Net Change Limit compliance, were mostly proposer assertions. The review also noted that this is a treasury withdrawal, which requires a higher bar because it spends shared ADA and can set precedent.

Several gates failed or remained incomplete: missing budget analysis, feasibility assessment, alternatives analysis, failure-mode analysis, and community impact analysis. Risk execution was judged low, and milestone gating was not required because this was a one-time reimbursement, but the treasury diligence dossier was incomplete and independent assurance was missing. On the supplied record, BEACN therefore voted NO rather than approving a treasury payment without enough verifiable evidence and completed analysis.

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
- finding: Requested: Reimburse the lost deposit for the Ikigai Info governance action, plus compensation for lost staking rewards.
- finding: Recipient: the Ikigai Info governance action submitter
- finding: Stated amount: 103,000 ADA
- finding: Deliverables: On-chain treasury withdrawal directly to the intended recipient upon enactment
- finding: Deadline/expiry: instantly performed as part of the governance action's enactment on-chain
- finding: Claim (governance, proposer_asserted, medium materiality): An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork.
- finding: Claim (governance, proposer_asserted, low materiality): The Ikigai Info governance action was symbolic and asked the community whether they agreed with a statement thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug permitted an unregistered stake key to be used in the governance action, causing the submitter to be unable to recover a 100,000 ADA deposit.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal states there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested withdrawal is 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards at 2% per annum.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork.
- missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, causing the submitter to be unable to recover a 100,000 ADA deposit.
- missing: Independent evidence for: The proposal states there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- missing: Independent evidence for: The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
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
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "The requested withdrawal is 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards at 2% per annum." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork." — so cost or precedent may outweigh the benefit.
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
- Treasury profile: one-time reimbursement — milestone-gating expectations do not apply.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 103000
- Risk review: Execution risk: low
- Counterargument pass: Strongest YES: the proposal substantiates "The requested withdrawal is 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards at 2% per annum." though 5 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The deterministic assessment is already blocked for missing budget, feasibility, alternatives, failure-mode, and community-impact analysis, and the extracted claims show the central loss, bug cause, recipient history, and NCL compliance are mostly proposer assertions. A small negative nudge is warranted for treasury stewardship and evidence quality, especially because the request spends treasury funds without documented verification of the unrecovered deposit or reward calculation in the supplied document.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork.
- Claims and evidence missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, causing the submitter to be unable to recover a 100,000 ADA deposit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `89bb30bcd51bd2c9bf465f193178aedaf232edaa0a9293d8de3f6f7c960cb921`
- snapshot_bundle_hash: `a90b371789cf2110f98adc2af930a00f3b64ae5fb53c0114a1d657fdf5ad1c58`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

