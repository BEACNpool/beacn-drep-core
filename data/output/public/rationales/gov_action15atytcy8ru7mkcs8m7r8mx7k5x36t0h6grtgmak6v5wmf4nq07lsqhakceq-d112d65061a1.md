# Rationale: gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
Recommendation: **ABSTAIN**
Score: `-0.07` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4875` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal has clear intent and accounting mechanics, but several important justifications for raising the limit, including constrained practical room and constitutional interpretation, rely on assertions or external verification rather than evidence contained in the anchor document; under an incomplete and thin assessment, a small cautionary nudge is warranted.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal did not meet the evidence threshold for a directional vote. The core mechanics of the action were clear, but key reasons for raising the Treasury net change limit were not independently supported enough to justify a Yes or No.

The action asked DReps to record agreement to a new 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713, from February 13, 2026 to about July 3, 2027. It did not request a direct Treasury withdrawal and had no direct on-chain effect. The proposal said the cap would apply only to ada removed through enacted Treasury Withdrawals, that withdrawals already debited during the period would count toward the limit, and that prior limits for the same period would be superseded.

Several claims were well-supported in the proposal, including the 500,000,000 ada limit, the fact that this was an InfoAction, and the accounting rule that already-debited Treasury Withdrawals count toward the cap. But important justification claims were thin: the claim that the existing 350,000,000 ada limit is becoming constrained, and the claim that increasing the cap preserves DReps’ ability to consider credible withdrawals while maintaining a fiscal guardrail, were treated as proposer assertions rather than independently evidenced conclusions. The risk review was also thin, with execution risk unknown and missing mitigation evidence or independent assurance.

This abstention is a conservative, evidence-based hold, not active opposition. A directional vote would be unblocked by replayable independent evidence showing that practical room under the existing 350,000,000 ada limit is constrained, stronger support for why 500,000,000 ada is the appropriate new guardrail, and clearer mitigation or assurance evidence for the governance and execution risks.

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
- finding: Stated amount: 500,000,000 ada net change limit; no direct treasury withdrawal requested
- finding: Deliverables: Set a fixed cap on total ada removed from the Treasury through Treasury Withdrawals during Epochs 613-713., Supersede any prior Net Change Limit for the same period., Count all Treasury Withdrawals already debited during the period toward the limit., Record DRep agreement if Yes votes exceed 50% of active voting stake.
- finding: Deadline/expiry: Period begins at the start of Epoch 613 (February 13, 2026) and ends at the close of Epoch 713, on or about July 3, 2027.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only lovelace removed from the Cardano Treasury through enacted Treasury Withdrawals recorded on the Cardano ledger.
- finding: Claim (technical, supported_in_proposal, medium materiality): Treasury inflows, including reserves, protocol allocations, transaction-fee allocations, refunds, and returns of Treasury-funded amounts, do not count toward or increase the limit.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the Epochs 613-713 period count toward the 500,000,000 ada cumulative limit.
- finding: Claim (governance, supported_in_proposal, high materiality): This Info action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal says the existing 350,000,000 ada Net Change Limit has been useful but practical room under it is becoming constrained.
- missing: Independent evidence for: The proposal says the existing 350,000,000 ada Net Change Limit has been useful but practical room under it is becoming constrained.
- missing: Independent evidence for: The proposer claims increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals while maintaining a fixed fiscal guardrail.
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
- finding: Strongest NO: a material claim is unsupported — "The proposal says the existing 350,000,000 ada Net Change Limit has been useful but practical room under it is becoming constrained." — so cost or precedent may outweigh the benefit.
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
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has clear intent and accounting mechanics, but several important justifications for raising the limit, including constrained practical room and constitutional interpretation, rely on assertions or external verification rather than evidence contained in the anchor document; under an incomplete and thin assessment, a small cautionary nudge is warranted.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal says the existing 350,000,000 ada Net Change Limit has been useful but practical room under it is becoming constrained.
- Claims and evidence missing: Independent evidence for: The proposer claims increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals while maintaining a fixed fiscal guardrail.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `d112d65061a11c384714158a5494af09789526dbfb9a14e013758b55681302fa`
- snapshot_bundle_hash: `cfaa94f9550441e2f531e29e0b045b5becc03a95f68afd97d4f2ccd4f9fa7d6c`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4419, "NO": 0.3491, "YES": 0.2091}`

