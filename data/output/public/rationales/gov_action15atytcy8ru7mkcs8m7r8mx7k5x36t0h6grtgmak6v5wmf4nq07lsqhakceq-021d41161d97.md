# Rationale: gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
Recommendation: **ABSTAIN**
Score: `-0.07` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4875` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal has clear intent and accounting mechanics, and it preserves per-withdrawal discretion, which supports governance clarity. However, the material justification for raising the guardrail from 350,000,000 ada to 500,000,000 ada rests mainly on an asserted constraint rather than quantified Treasury demand or demonstrated need, so a small cautionary nudge is warranted for treasury stewardship and evidence quality.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s core mechanics were clear, but the evidence did not meet the threshold for a directional vote. This is a conservative, evidence-based hold, not active opposition.

The action asked DReps to record agreement, through an InfoAction, to a 500,000,000 ada Net Change Limit for the Cardano Treasury from Epoch 613, beginning February 13, 2026, through Epoch 713, ending on or about July 3, 2027. It does not directly authorize any Treasury Withdrawal. The proposal says the limit would apply only to ledger-recorded Treasury Withdrawals, that withdrawals already debited during the period would count toward it, and that Treasury inflows or returned funds would not increase the limit. Those accounting mechanics were supported in the proposal.

The main weakness was evidence quality around the need and effect of raising the limit from the previously agreed 350,000,000 ada to 500,000,000 ada. The proposer asserted that the existing limit has been useful but is becoming constrained, and asserted that the new limit supersedes any prior limit for the same period. Those points were not independently supported in the supplied review. The risk review was also thin, with execution risk unknown and missing mitigation evidence or independent assurance.

The review gates found a pinned and replayable proposal anchor, and the strongest YES case was that the proposal clearly sets a new 500,000,000 ada limit and preserves DRep discretion over each future withdrawal. But confidence was reduced by a flag score, thin evidence status, and unsupported material claims. A directional vote would need independent evidence for the practical need to raise the limit, stronger support for the superseding effect over the prior 350,000,000 ada limit, and clearer risk mitigation or assurance.

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
- finding: Requested: Record DRep agreement to a new Net Change Limit for the Cardano Treasury for Epochs 613-713 through an InfoAction with no direct on-chain effect and no authorization of any Treasury Withdrawal.
- finding: Recipient: not stated in document
- finding: Stated amount: none requested; proposed Net Change Limit is 500,000,000 ada
- finding: Deliverables: Set a 500,000,000 ada Net Change Limit for Epochs 613-713, Supersede any prior Net Change Limit for the same period, Count all Treasury Withdrawals already debited during the period toward the limit, Use cumulative ledger-recorded Treasury Withdrawals in lovelace for limit accounting, Record DRep agreement if Yes votes exceed 50% of active voting stake
- finding: Deadline/expiry: period begins at the start of Epoch 613 (February 13, 2026) and ends at the close of Epoch 713 (on or about July 3, 2027)
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal sets a new Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed Net Change Limit caps only the total lovelace removed from the Treasury by enacted Treasury Withdrawals recorded on the Cardano ledger during the period.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returned Treasury-funded amounts, do not count toward or increase the proposed limit.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the Epochs 613-713 period count toward the proposed 500,000,000 ada limit.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal states that the new limit supersedes any prior Net Change Limit for the same period, including a previously agreed 350,000,000 ada limit.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer asserts that the existing 350,000,000 ada limit has been useful but that practical room under it is becoming constrained.
- missing: Independent evidence for: The proposal states that the new limit supersedes any prior Net Change Limit for the same period, including a previously agreed 350,000,000 ada limit.
- missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada limit has been useful but that practical room under it is becoming constrained.
- missing: Independent evidence for: The proposal asserts that nothing in the Constitution limits DReps to a single Net Change Limit or prevents a newly agreed Net Change Limit from applying to the same period.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a new Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that the new limit supersedes any prior Net Change Limit for the same period, including a previously agreed 350,000,000 ada limit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a new Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has clear intent and accounting mechanics, and it preserves per-withdrawal discretion, which supports governance clarity. However, the material justification for raising the guardrail from 350,000,000 ada to 500,000,000 ada rests mainly on an asserted constraint rather than quantified Treasury demand or demonstrated need, so a small cautionary nudge is warranted for treasury stewardship and evidence quality.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that the new limit supersedes any prior Net Change Limit for the same period, including a previously agreed 350,000,000 ada limit.
- Claims and evidence missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada limit has been useful but that practical room under it is becoming constrained.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `021d41161d9716de87a3e00afe2c7ba2c14a859015d538aa938199ec558afe2d`
- snapshot_bundle_hash: `721371b04a929c2b19f0ba32f657b386d594635f7b987ffb18f8482d26df6295`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4419, "NO": 0.3491, "YES": 0.2091}`

