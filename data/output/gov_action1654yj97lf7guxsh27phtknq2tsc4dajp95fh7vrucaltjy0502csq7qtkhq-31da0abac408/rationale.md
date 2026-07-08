# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NO**
Score: `-0.4833` (raw `-0.4533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.64` | Readiness: `0.8`
> Reasoning layer (precomputed): The claims describe a sympathetic reimbursement request, but the assessment says evidence is thin and treasury analysis is incomplete, with missing budget, feasibility, alternatives, failure-mode, and community impact analysis. Under BEACN doctrine, treasury stewardship and evidence quality outweigh speed or sentiment, so a small cautionary negative nudge is justified without overriding the deterministic blocker.

## Plain-language explanation (precomputed)
BEACN voted NO because the proposal asks the treasury for 103,000 ADA, but the review found that key evidence and treasury diligence were incomplete for a withdrawal that would spend shared funds and set a reimbursement precedent.

The action requested reimbursement of a lost 100,000 ADA governance action deposit for the Ikigai Info submitter, plus 3,000 ADA for estimated lost staking rewards. The proposer claimed the original Ikigai action was symbolic, that a Cardano node bug prevented recovery of the deposit, that there had been significant community sentiment in favor of reimbursement, and that the amount was within the Net Change Limit. The proposal did support the basic payment request and included a pinned, replayable anchor plus an external AdaStat reference, but several important claims remained proposer-asserted rather than independently supported.

The review treated this as a one-time reimbursement, so milestone-gating was not the central issue. Execution risk was considered low, and the strongest YES case was that the requested amount and purpose were clear. But the treasury review still had major open blockers: missing budget analysis, feasibility assessment, alternatives analysis, failure-mode analysis, and community impact analysis. The synthesis was blocked, the treasury analysis was incomplete, and the evidence record was thin.

For BEACN, treasury stewardship requires more than sympathy or a clear payment amount. Because the proposal did not provide enough independent evidence and analysis to justify spending treasury ADA, BEACN voted NO.

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
- finding: Requested: Reimburse the lost deposit for the Ikigai Info governance action, including estimated lost staking rewards.
- finding: Recipient: the Ikigai Info governance action submitter
- finding: Stated amount: 103000
- finding: Deliverables: Instant on-chain distribution of the reimbursement as part of governance action enactment
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA from the treasury to reimburse a 100,000 ADA lost governance action deposit plus 3,000 ADA for estimated staking rewards.
- finding: Claim (governance, proposer_asserted, medium materiality): The original Ikigai Info governance action was symbolic and asked the community whether they agreed with a statement thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): The submitter was unable to recover the 100,000 ADA deposit because a Cardano node bug permitted an unregistered stake key to be used in the governance action.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal says there was significant community sentiment at the time that the Ikigai Info governance action deposit should be reimbursed.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal says the Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that action was not approved.
- finding: Claim (economic, proposer_asserted, medium materiality): The document states there are no costs or expenses associated with the treasury withdrawal beyond the reimbursement amount.
- missing: Independent evidence for: The original Ikigai Info governance action was symbolic and asked the community whether they agreed with a statement thanking contributors and expressing hope for Cardano's future.
- missing: Independent evidence for: The submitter was unable to recover the 100,000 ADA deposit because a Cardano node bug permitted an unregistered stake key to be used in the governance action.
- missing: Independent evidence for: The proposal says there was significant community sentiment at the time that the Ikigai Info governance action deposit should be reimbursed.
- missing: Independent evidence for: The proposal says the Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that action was not approved.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury to reimburse a 100,000 ADA lost governance action deposit plus 3,000 ADA for estimated staking rewards." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The original Ikigai Info governance action was symbolic and asked the community whether they agreed with a statement thanking contributors and expressing hope for Cardano's future." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury to reimburse a 100,000 ADA lost governance action deposit plus 3,000 ADA for estimated staking rewards." though 5 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims describe a sympathetic reimbursement request, but the assessment says evidence is thin and treasury analysis is incomplete, with missing budget, feasibility, alternatives, failure-mode, and community impact analysis. Under BEACN doctrine, treasury stewardship and evidence quality outweigh speed or sentiment, so a small cautionary negative nudge is justified without overriding the deterministic blocker.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The original Ikigai Info governance action was symbolic and asked the community whether they agreed with a statement thanking contributors and expressing hope for Cardano's future.
- Claims and evidence missing: Independent evidence for: The submitter was unable to recover the 100,000 ADA deposit because a Cardano node bug permitted an unregistered stake key to be used in the governance action.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `31da0abac4087cd2084307bf3e78123feadd69854728aac48c5d7887b96d8f2f`
- snapshot_bundle_hash: `105152fe668db68b04266383959d8e1cd666b553b9badc67faac9941a9500d7a`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

