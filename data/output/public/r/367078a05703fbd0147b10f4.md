# Rationale: gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
Recommendation: **ABSTAIN**
Score: `-0.07` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4875` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal has clear intent and accounting mechanics, and it preserves discretion over later Treasury Withdrawals, but several important justifications for increasing the cap from 350,000,000 ada to 500,000,000 ada are asserted rather than evidenced in the extracted claims. Given the doctrine's preference for treasury stewardship and evidence quality, a small cautionary negative nudge is warranted without treating the Info action as a direct spend authorization.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s core mechanics were clear, but the evidence did not meet the threshold for a directional Yes or No. This is a conservative, evidence-based hold, not active opposition.

The action asked DReps to record agreement to a new Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613 through 713, from February 13, 2026 to about July 3, 2027. It would not directly authorize any treasury withdrawal. The proposal clearly supported several accounting details: the cap applies only to withdrawals debited on ledger, withdrawals already made during the period count toward the cap, and treasury inflows do not increase or count against the limit.

The weaker part was the justification for raising the limit from the existing 350,000,000 ada to 500,000,000 ada. The proposer asserted that the current limit has been useful but is becoming constrained before mid-2027, and that raising it would preserve DRep discretion while keeping a fiscal guardrail. Those claims were not backed by independent evidence in the review. The risk review was also thin, with execution risk unknown and missing mitigation evidence or independent assurance.

A directional vote would be unblocked by replayable public evidence showing why the 350,000,000 ada limit is becoming constrained, why 500,000,000 ada is the appropriate new cap, and what mitigations or assurances address the governance and execution risks. Until then, ABSTAIN best reflects BEACN’s evidence standard.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: active
- finding: Proposed epoch: 640
- finding: Expires after epoch: 647
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Info action to record DRep agreement to a new Net Change Limit for the Cardano Treasury for Epochs 613-713.
- finding: Recipient: not stated in document
- finding: Stated amount: No direct treasury withdrawal; proposed Net Change Limit is 500,000,000 ada.
- finding: Deliverables: Set a fixed cap of 500,000,000 ada on total Treasury Withdrawals debited during Epochs 613-713., Apply the limit from the start of Epoch 613 on February 13, 2026 through the close of Epoch 713 on or about July 3, 2027., Count all Treasury Withdrawals already debited during the period toward the limit., Exclude Treasury inflows from increasing or counting against the limit., Record DRep agreement if Yes votes exceed 50% of active voting stake.
- finding: Deadline/expiry: Period ends at the close of Epoch 713, on or about July 3, 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (governance, supported_in_proposal, high materiality): The period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713, on or about July 3, 2027.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only lovelace removed from the Treasury through enacted Treasury Withdrawals recorded on the Cardano ledger.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returned Treasury-funded amounts, are not counted and do not increase the limit.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the period count toward the 500,000,000 ada cumulative limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has been useful but is becoming constrained before mid-2027.
- missing: Independent evidence for: The proposer asserts that raising the limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed fiscal guardrail.
- missing: Independent evidence for: The proposal states that agreement occurs when Yes votes exceed 50% of active voting stake under TREASURY-01a.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer asserts that the existing 350,000,000 ada Net Change Limit has been useful but is becoming constrained before mid-2027." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Flag score present (3), reducing confidence.
- Intake: Action type: InfoAction
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has clear intent and accounting mechanics, and it preserves discretion over later Treasury Withdrawals, but several important justifications for increasing the cap from 350,000,000 ada to 500,000,000 ada are asserted rather than evidenced in the extracted claims. Given the doctrine's preference for treasury stewardship and evidence quality, a small cautionary negative nudge is warranted without treating the Info action as a direct spend authorization.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has been useful but is becoming constrained before mid-2027.
- Claims and evidence missing: Independent evidence for: The proposer asserts that raising the limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed fiscal guardrail.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `4ced793ea4eb16d22e17ace750c3fca2ef2bedae851520abe94777ece259170b`
- snapshot_bundle_hash: `f0f7695baca661681aefb2f87b93dd51941ca6c88da71ebe4af7a844e996068b`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `30`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4419, "NO": 0.3491, "YES": 0.2091}`

