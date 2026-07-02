# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NO**
Score: `-0.6333` (raw `-0.6033` + doctrine-LLM nudge `-0.03`) | Confidence: `1.0` | Readiness: `0.8`
> Reasoning layer (precomputed): The claim set contains a clear reimbursement purpose and a checkable reference, but the core justification depends on proposer assertions about the node bug, unrecoverable deposit, recipient history, community sentiment, and NCL adherence, while the deterministic assessment reports missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. Under a treasury withdrawal standard, this evidence quality does not justify a positive nudge and supports a small cautionary adjustment.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Reimburse Ikigai Info Governance Action Deposit.. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Reimburse the submitter of the Ikigai Info governance action for an unrecovered governance action deposit plus estimated lost staking rewards.. The recorded treasury amount is 103000. The strongest grounded claim is: The proposal requests 103,000 ADA from the treasury to reimburse a lost 100,000 ADA Info governance action deposit plus 3,000 ADA for estimated lost staking rewards.

A material weak point is that this claim remains proposer-asserted or thinly supported: The proposer states that the original Ikigai Info governance action was symbolic and asked the community whether it agreed with a statement of thanks and hope for Cardano's future. The blocking questions are: missing budget analysis; missing feasibility assessment; missing alternatives analysis.

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
- finding: Requested: Reimburse the submitter of the Ikigai Info governance action for an unrecovered governance action deposit plus estimated lost staking rewards.
- finding: Recipient: not stated in document
- finding: Stated amount: 103000
- finding: Deliverables: Instant on-chain distribution of funds to the intended recipient as part of governance action enactment
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA from the treasury to reimburse a lost 100,000 ADA Info governance action deposit plus 3,000 ADA for estimated lost staking rewards.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer states that the original Ikigai Info governance action was symbolic and asked the community whether it agreed with a statement of thanks and hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer states that a Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal references an external Adastat governance page for the Ikigai action.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer states there was significant community sentiment at the time that the Ikigai deposit should be reimbursed.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer states that the Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: The proposer states that the original Ikigai Info governance action was symbolic and asked the community whether it agreed with a statement of thanks and hope for Cardano's future.
- missing: Independent evidence for: The proposer states that a Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The proposer states there was significant community sentiment at the time that the Ikigai deposit should be reimbursed.
- missing: Independent evidence for: The proposer states that the Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury to reimburse a lost 100,000 ADA Info governance action deposit plus 3,000 ADA for estimated lost staking rewards." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that the original Ikigai Info governance action was symbolic and asked the community whether it agreed with a statement of thanks and hope for Cardano's future." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the treasury to reimburse a lost 100,000 ADA Info governance action deposit plus 3,000 ADA for estimated lost staking rewards." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claim set contains a clear reimbursement purpose and a checkable reference, but the core justification depends on proposer assertions about the node bug, unrecoverable deposit, recipient history, community sentiment, and NCL adherence, while the deterministic assessment reports missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. Under a treasury withdrawal standard, this evidence quality does not justify a positive nudge and supports a small cautionary adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow signal is in unsustainable regime (advisory penalty applied).
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: The proposer states that the original Ikigai Info governance action was symbolic and asked the community whether it agreed with a statement of thanks and hope for Cardano's future.
- Claims and evidence missing: Independent evidence for: The proposer states that a Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `7d6fdcfab9d4761da6037c15f0f3d51936aeb35fef855ccff30f69b35c3015c9`
- snapshot_bundle_hash: `0f4894f0b9e220d2e3ba1b65a93c8541976ffb9ec5360b3e60e4e36cb40bf737`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4fbc4829bb6142608e4d32087d1ed0565eaf5b12`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `5891`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1518, "NO": 0.8093, "YES": 0.0389}`

