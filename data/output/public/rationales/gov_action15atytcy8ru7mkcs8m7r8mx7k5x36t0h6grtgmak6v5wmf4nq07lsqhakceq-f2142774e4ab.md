# Rationale: gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
Recommendation: **ABSTAIN**
Score: `-0.06` (raw `-0.05` + doctrine-LLM nudge `-0.01`) | Confidence: `0.485` | Readiness: `0.6`
> Reasoning layer (precomputed): A small cautionary nudge is warranted because the proposal raises a treasury guardrail by 150,000,000 ada and several material justifications, including constrained practical room and constitutional interpretation, are mostly asserted rather than evidenced in the document. The action does improve governance clarity and says it does not directly authorize withdrawals, so the adjustment should remain small.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal did not meet the evidence threshold for a directional vote. The action clearly states a new 500,000,000 ada Net Change Limit for Treasury withdrawals during Epochs 613-713, but several important reasons for increasing the guardrail were asserted rather than independently supported.

The proposal asks DReps to record agreement, through an Info action, to replace any prior Net Change Limit for the same period with a 500,000,000 ada cap. It does not directly authorize any Treasury Withdrawal, does not request a withdrawal amount, and says all Treasury withdrawals already debited during the period would count toward the cap. It also says Treasury inflows, refunds, and returns would not increase the limit.

The strongest supported claims were the mechanics of the proposal: the amount, the epoch range, the cumulative lovelace accounting method, the inclusion of already-debited withdrawals, and the fact that this Info action has no direct on-chain effect. The weaker claims were the justification for the increase: that the existing 350,000,000 ada limit is becoming practically constrained before mid-2027, and that a 500,000,000 ada limit preserves DReps’ ability to consider credible withdrawals while keeping a fixed guardrail. Those claims were material, but not independently evidenced in the review.

This is a conservative, evidence-based hold, not active opposition. A directional vote would be unblocked by independent evidence showing that the current 350,000,000 ada limit is practically constrained, that the higher 500,000,000 ada limit is needed for credible Treasury governance during the period, and stronger mitigation or assurance evidence for the governance and execution risks of raising the guardrail.

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
- finding: Requested: Agree a new Net Change Limit for the Cardano Treasury for Epochs 613-713 through an Info action with no direct on-chain effect and no authorization of any Treasury Withdrawal.
- finding: Recipient: not stated in document
- finding: Stated amount: 500,000,000 ada net cap on total Treasury Withdrawals during the period; no withdrawal amount requested
- finding: Deliverables: Record DReps' agreement to a 500,000,000 ada Net Change Limit for Epochs 613-713, Supersede any prior Net Change Limit for the same period, Count all Treasury Withdrawals already debited during the period toward the limit, Apply a cumulative lovelace accounting method that excludes Treasury inflows
- finding: Deadline/expiry: period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for the Cardano Treasury during Epochs 613-713.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only the cumulative lovelace removed from the Treasury through enacted Treasury Withdrawals recorded on the Cardano ledger during the period.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returns of Treasury-funded amounts, do not count toward or increase the limit.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the Epoch 613-713 period count toward the 500,000,000 ada limit and remain valid.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that this Info action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer asserts that the existing 350,000,000 ada Net Change Limit has served as a useful fiscal guardrail but is becoming practically constrained before mid-2027.
- missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has served as a useful fiscal guardrail but is becoming practically constrained before mid-2027.
- missing: Independent evidence for: The proposer claims the 500,000,000 ada limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed guardrail and simple accounting.
- missing: Independent evidence for: The proposal states that Yes votes exceeding 50% of active voting stake record DRep agreement to the Net Change Limit under threshold TREASURY-01a.
- missing: Independent evidence for: The proposer claims nothing in the Constitution limits DReps to a single Net Change Limit or prevents a newly agreed Net Change Limit from applying to the same period.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for the Cardano Treasury during Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer asserts that the existing 350,000,000 ada Net Change Limit has served as a useful fiscal guardrail but is becoming practically constrained before mid-2027." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for the Cardano Treasury during Epochs 613-713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.010 (clamped to ±0.05): A small cautionary nudge is warranted because the proposal raises a treasury guardrail by 150,000,000 ada and several material justifications, including constrained practical room and constitutional interpretation, are mostly asserted rather than evidenced in the document. The action does improve governance clarity and says it does not directly authorize withdrawals, so the adjustment should remain small.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has served as a useful fiscal guardrail but is becoming practically constrained before mid-2027.
- Claims and evidence missing: Independent evidence for: The proposer claims the 500,000,000 ada limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed guardrail and simple accounting.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `f2142774e4ab8351c3f904026267d004b8f6201115ca5d10ea3ae192fc6c4303`
- snapshot_bundle_hash: `e74661091da8f75c56ad744b9c578ac9a487ec5b5f7d8e7f0bfa7eb201345eb5`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4413, "NO": 0.3394, "YES": 0.2194}`

