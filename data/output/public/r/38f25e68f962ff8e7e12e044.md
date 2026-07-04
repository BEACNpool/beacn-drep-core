# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NO**
Score: `-0.4833` (raw `-0.4533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.64` | Readiness: `0.8`
> Reasoning layer (precomputed): The request has a plausible restitution purpose, but the supplied claims remain thin on the key treasury questions identified by the assessment: no budget analysis, feasibility assessment, alternatives analysis, failure-mode analysis, or community impact analysis is provided, and several high-materiality claims are proposer-asserted rather than evidenced in the document. Under a blocked assessment and incomplete treasury analysis, the bounded lean should modestly favor caution rather than spending.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury reimbursement depends on a key claim that was not independently evidenced: that the original 100,000 ADA deposit was lost because of a Cardano node bug involving an unregistered stake key. For a treasury withdrawal, especially one that could set a reimbursement precedent, BEACN requires stronger public evidence before spending shared ADA.

The action requested 103,000 ADA from the treasury for the Ikigai Info governance action submitter: 100,000 ADA to replace the original deposit and 3,000 ADA for estimated lost staking rewards. The proposer also said the prior Ikigai action was symbolic, that there was significant community support for reimbursing the submitter, that the reimbursement had appeared in an earlier Cardano in Oceania budget action that was not approved, that the recipient had not previously received treasury funds, and that the request was within the Net Change Limit.

Some parts were clear from the proposal itself. The requested amount, purpose, recipient, immediate on-chain payment, and the symbolic nature of the referenced Ikigai action were supported in the proposal, and the anchor document was available and replayable. But several material claims remained only proposer-asserted, including the cause of the unrecovered deposit and the level of community sentiment. The review also found the treasury diligence incomplete: missing budget analysis, feasibility assessment, alternatives analysis, failure-mode analysis, and community impact analysis.

The strongest case for YES was that the proposal clearly identified a one-time reimbursement amount and purpose, with low execution risk. BEACN still voted NO because five review blockers remained open, the claims-and-evidence record was thin, the synthesis gate was blocked, and treasury actions require elevated scrutiny.

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
- finding: Requested: Treasury withdrawal to reimburse the lost deposit for the Ikigai Info governance action and compensate estimated lost staking rewards.
- finding: Recipient: Ikigai Info governance action submitter
- finding: Stated amount: 103000
- finding: Deliverables: Immediate on-chain distribution of funds to the intended recipient upon enactment
- finding: Deadline/expiry: instantly performed as part of the governance action's enactment on-chain
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA from the treasury, consisting of the original 100,000 ADA deposit plus 3,000 ADA for estimated lost staking rewards.
- finding: Claim (technical, proposer_asserted, high materiality): The submitter of the September 2024 'Cardanoの生きがい - Ikigai -' Info governance action was unable to recover a 100,000 ADA deposit because of a Cardano node bug involving an unregistered stake key.
- finding: Claim (governance, supported_in_proposal, medium materiality): The referenced Ikigai governance action was symbolic and asked the community whether they agreed with a statement of thanks and hope for Cardano's future.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer states there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included this reimbursement in a budget Info governance action, but that governance action was not approved.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal states that the recipient has not previously received funds from the treasury.
- missing: Independent evidence for: The submitter of the September 2024 'Cardanoの生きがい - Ikigai -' Info governance action was unable to recover a 100,000 ADA deposit because of a Cardano node bug involving an unregistered stake key.
- missing: Independent evidence for: The proposer states there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- missing: Independent evidence for: The Cardano in Oceania initiative included this reimbursement in a budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: The proposal states that the recipient has not previously received funds from the treasury.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury, consisting of the original 100,000 ADA deposit plus 3,000 ADA for estimated lost staking rewards." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The submitter of the September 2024 'Cardanoの生きがい - Ikigai -' Info governance action was unable to recover a 100,000 ADA deposit because of a Cardano node bug involving an unregistered stake key." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury, consisting of the original 100,000 ADA deposit plus 3,000 ADA for estimated lost staking rewards." though 5 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The request has a plausible restitution purpose, but the supplied claims remain thin on the key treasury questions identified by the assessment: no budget analysis, feasibility assessment, alternatives analysis, failure-mode analysis, or community impact analysis is provided, and several high-materiality claims are proposer-asserted rather than evidenced in the document. Under a blocked assessment and incomplete treasury analysis, the bounded lean should modestly favor caution rather than spending.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The submitter of the September 2024 'Cardanoの生きがい - Ikigai -' Info governance action was unable to recover a 100,000 ADA deposit because of a Cardano node bug involving an unregistered stake key.
- Claims and evidence missing: Independent evidence for: The proposer states there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `f4b2e7c25d43463d0057d0414ec2351c661d08db36ad07eaf7fa2630bb13c7d6`
- snapshot_bundle_hash: `b3f240bfe60f29f0e8fcda0e88186e29a604843fff5644761c8947352d3bd8f0`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `32`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

