# Rationale: gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
Recommendation: **ABSTAIN**
Score: `-0.07` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4875` | Readiness: `0.6`
> Reasoning layer (precomputed): The action improves governance clarity by defining the cap and accounting method, but its central justification for increasing the limit is mostly asserted rather than evidenced, and the deterministic assessment marks risk review as thin and overall status as incomplete. A small cautionary nudge is warranted because treasury stewardship and evidence quality carry more weight than preserving spending flexibility.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s core mechanics were clear, but the evidence did not meet the threshold for a directional vote. This is a conservative, evidence-based hold, not active opposition to the Net Change Limit.

The action asked DReps to record agreement to a 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713, from February 13, 2026 to about July 3, 2027. It did not request a direct treasury withdrawal. The proposal said the cap would count enacted Treasury Withdrawals debited during the period, exclude Treasury inflows, supersede any prior limit for the same period, and replace the existing 350,000,000 ada limit.

The review found strong support in the proposal itself for the 500,000,000 ada limit, the accounting method, and the statement that this InfoAction has no direct on-chain effect and does not authorize spending. However, several important governance claims were still only proposer assertions, including that a Yes vote above 50% of active voting stake records DRep agreement under TREASURY-01a, and that the new limit supersedes the prior 350,000,000 ada limit. The risk review was also thin, with execution risk unknown and missing mitigation evidence or independent assurance.

A directional vote would be unblocked by replayable independent evidence for the TREASURY-01a ratification threshold claim, evidence that the 500,000,000 ada limit validly supersedes the prior limit for the same period, and stronger risk review materials showing mitigation and independent assurance. Until then, BEACN abstained to avoid overstating certainty.

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
- finding: Requested: Info action to record DRep agreement to a Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Recipient: not stated in document
- finding: Stated amount: No direct treasury withdrawal requested; proposed Net Change Limit is 500,000,000 ada.
- finding: Deliverables: Set or signal agreement to a 500,000,000 ada cap on total Treasury Withdrawals debited during Epochs 613-713., Supersede any prior Net Change Limit for the same period., Count already debited Treasury Withdrawals during the period toward the cap.
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Epochs 613-713.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposed limit caps total lovelace removed from the Cardano Treasury through enacted Treasury Withdrawals during the period and does not count Treasury inflows.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal says it has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal says a Yes vote exceeding 50% of active voting stake records DRep agreement to the Net Change Limit under TREASURY-01a.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal states that the new 500,000,000 ada limit supersedes any prior Net Change Limit for the same period, including the existing 350,000,000 ada limit.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer claims the existing 350,000,000 ada limit has been a useful fiscal guardrail but practical room under it is becoming constrained.
- missing: Independent evidence for: The proposal says a Yes vote exceeding 50% of active voting stake records DRep agreement to the Net Change Limit under TREASURY-01a.
- missing: Independent evidence for: The proposal states that the new 500,000,000 ada limit supersedes any prior Net Change Limit for the same period, including the existing 350,000,000 ada limit.
- missing: Independent evidence for: The proposer claims the existing 350,000,000 ada limit has been a useful fiscal guardrail but practical room under it is becoming constrained.
- missing: Independent evidence for: The proposer claims the higher limit preserves DRep ability to consider credible Treasury Withdrawals on their merits while retaining a clear fixed guardrail.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says a Yes vote exceeding 50% of active voting stake records DRep agreement to the Net Change Limit under TREASURY-01a." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Epochs 613-713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The action improves governance clarity by defining the cap and accounting method, but its central justification for increasing the limit is mostly asserted rather than evidenced, and the deterministic assessment marks risk review as thin and overall status as incomplete. A small cautionary nudge is warranted because treasury stewardship and evidence quality carry more weight than preserving spending flexibility.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal says a Yes vote exceeding 50% of active voting stake records DRep agreement to the Net Change Limit under TREASURY-01a.
- Claims and evidence missing: Independent evidence for: The proposal states that the new 500,000,000 ada limit supersedes any prior Net Change Limit for the same period, including the existing 350,000,000 ada limit.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `069136195703bce815f904629413172fb600230fbf85c67a4b579e3ddecfbaa1`
- snapshot_bundle_hash: `0eaeee4c7f1a5bf148d7328a34b089519b70303feed4cd4af4b734b2099b1c1e`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4419, "NO": 0.3491, "YES": 0.2091}`

