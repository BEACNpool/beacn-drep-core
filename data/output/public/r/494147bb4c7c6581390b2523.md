# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NO**
Score: `-0.4833` (raw `-0.4533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.64` | Readiness: `0.8`
> Reasoning layer (precomputed): The request has a plausible restitution purpose, but the deterministic assessment identifies thin evidence and missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. Under BEACN doctrine, treasury stewardship and evidence quality should dominate public-benefit or sentiment-based arguments, so the bounded lean is a small cautionary negative rather than a spending-positive nudge.

## Plain-language explanation (precomputed)
BEACN voted NO because the proposal asks the treasury for 103,000 ADA, but the key justification for reimbursement was not independently supported: that a Cardano node bug caused the original submitter to lose a 100,000 ADA governance action deposit.

The request was a one-time treasury withdrawal to reimburse the lost Ikigai Info governance action deposit, plus 3,000 ADA in estimated lost staking rewards. The proposal did support the basic amount requested and explained that the original Ikigai Info action was symbolic, thanking contributors to Cardano governance and expressing hope for the future. It also stated that there were no extra costs beyond the reimbursement and no expected refund back to the treasury.

Several important claims remained only proposer assertions. BEACN did not have independent evidence for the claimed node-bug cause of the unrecoverable deposit, or for the claimed significant community sentiment in favor of reimbursement. The recipient was also not stated in the document. Because this was a treasury withdrawal, BEACN applied elevated scrutiny: spending shared ADA creates precedent, even when execution risk is low and milestone gating is not relevant for a one-time reimbursement.

The review found the anchor document available and the requested amount clear, but the evidence record was thin and the synthesis remained blocked. The decisive open issues were missing budget analysis, feasibility assessment, alternatives analysis, failure-mode analysis, and community impact analysis. With those blockers still open, BEACN judged that the cost and precedent risk outweighed the supported case for reimbursement.

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
- finding: Requested: Treasury withdrawal to reimburse the lost deposit for the Ikigai Info governance action, plus estimated lost staking rewards.
- finding: Recipient: not stated in document
- finding: Stated amount: 103000
- finding: Deliverables: Instant on-chain distribution to the intended recipient upon governance action enactment
- finding: Deadline/expiry: upon enactment on-chain
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA from the treasury, consisting of a 100,000 ADA lost governance action deposit plus 3,000 ADA for staking rewards at 2% per annum.
- finding: Claim (technical, proposer_asserted, high materiality): The Ikigai Info governance action submitter was unable to recover a 100,000 ADA deposit because a Cardano node bug permitted an unregistered stake key to be used in the governance action.
- finding: Claim (governance, supported_in_proposal, medium materiality): The original Ikigai Info governance action was a symbolic action thanking contributors to Cardano governance and expressing hope for the future.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal says there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal says the Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
- finding: Claim (economic, supported_in_proposal, medium materiality): The proposal states there are no costs or expenses associated with the withdrawal beyond the reimbursement itself.
- missing: Independent evidence for: The Ikigai Info governance action submitter was unable to recover a 100,000 ADA deposit because a Cardano node bug permitted an unregistered stake key to be used in the governance action.
- missing: Independent evidence for: The proposal says there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed.
- missing: Independent evidence for: The proposal says the Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: The proposal states the recipient has not previously received funds from the treasury.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury, consisting of a 100,000 ADA lost governance action deposit plus 3,000 ADA for staking rewards at 2% per annum." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The Ikigai Info governance action submitter was unable to recover a 100,000 ADA deposit because a Cardano node bug permitted an unregistered stake key to be used in the governance action." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury, consisting of a 100,000 ADA lost governance action deposit plus 3,000 ADA for staking rewards at 2% per annum." though 5 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The request has a plausible restitution purpose, but the deterministic assessment identifies thin evidence and missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. Under BEACN doctrine, treasury stewardship and evidence quality should dominate public-benefit or sentiment-based arguments, so the bounded lean is a small cautionary negative rather than a spending-positive nudge.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The Ikigai Info governance action submitter was unable to recover a 100,000 ADA deposit because a Cardano node bug permitted an unregistered stake key to be used in the governance action.
- Claims and evidence missing: Independent evidence for: The proposal says there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `7e84a0f1bcfd3c3f141df8f5b0fe838ca0506d4cba6560c6bcd3d510c8d235cf`
- snapshot_bundle_hash: `a87916cbe2b98e61aa434a6818fdb7346f58e830fe423425e79082044ecf7f0e`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1218`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

