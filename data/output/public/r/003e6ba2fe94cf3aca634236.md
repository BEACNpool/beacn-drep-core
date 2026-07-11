# Rationale: gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal gives a clear intent, accounting rule, period, and governance use, which supports signal clarity for an Info Action. However, the central justification for increasing the limit from 350,000,000 ada to 500,000,000 ada is mostly asserted rather than evidenced, so a small cautionary nudge is warranted under treasury stewardship and evidence quality.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s core mechanics were clear, but the evidence did not meet the threshold for a directional vote. This is a conservative, evidence-based hold, not active opposition.

The action asked DReps to agree to a new Net Change Limit for the Cardano Treasury for Epochs 613-713, raising the cap to 500,000,000 ada. The proposal stated that this would cap total Treasury Withdrawals debited during that period, would not count Treasury inflows against the limit, would include withdrawals already debited, and would not itself authorize any Treasury Withdrawal. Those points were supported by the pinned, replayable proposal anchor.

The weaker part was the justification for changing the limit. The proposer asserted that the existing 350,000,000 ada limit was becoming practically constrained, and that the new 500,000,000 ada limit would supersede the prior limit for the same period. Those claims were material, but the review found them thinly supported by independent evidence. The risk review was also thin: execution risk was unknown, and mitigation evidence and independent assurance were missing.

For BEACN to move from ABSTAIN to a directional vote, the review would need stronger replayable evidence that the new limit validly supersedes the prior 350,000,000 ada limit, independent support for why the higher limit is needed, and clearer risk mitigation or assurance. Until then, abstaining avoids overstating confidence while still recognizing that the proposal’s basic requested cap and accounting rules were clearly presented.

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
- finding: Requested: Info action to agree a new Net Change Limit for the Cardano Treasury for Epochs 613-713.
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Set a fixed cap of 500,000,000 ada on total Treasury Withdrawals debited during the specified period., Record DRep agreement to the Net Change Limit if Yes votes exceed 50% of active voting stake., Supersede any prior Net Change Limit for the same period while not authorizing any Treasury Withdrawal.
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for the Cardano Treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed limit applies from the start of Epoch 613 on February 13, 2026 through the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only the cumulative lovelace removed from the Treasury by enacted Treasury Withdrawals recorded on the Cardano ledger during the period.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returns of Treasury-funded amounts, do not count toward or increase the limit.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the period count toward the 500,000,000 ada limit and are not reset, reversed, reopened, or reauthorized by this action.
- finding: Claim (governance, proposer_asserted, high materiality): The proposed 500,000,000 ada limit supersedes any prior Net Change Limit for Epochs 613-713, including the previously agreed 350,000,000 ada limit.
- missing: Independent evidence for: The proposed 500,000,000 ada limit supersedes any prior Net Change Limit for Epochs 613-713, including the previously agreed 350,000,000 ada limit.
- missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada limit is becoming practically constrained and that a higher limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for the Cardano Treasury." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposed 500,000,000 ada limit supersedes any prior Net Change Limit for Epochs 613-713, including the previously agreed 350,000,000 ada limit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for the Cardano Treasury." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal gives a clear intent, accounting rule, period, and governance use, which supports signal clarity for an Info Action. However, the central justification for increasing the limit from 350,000,000 ada to 500,000,000 ada is mostly asserted rather than evidenced, so a small cautionary nudge is warranted under treasury stewardship and evidence quality.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposed 500,000,000 ada limit supersedes any prior Net Change Limit for Epochs 613-713, including the previously agreed 350,000,000 ada limit.
- Claims and evidence missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada limit is becoming practically constrained and that a higher limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `021d41161d9716de87a3e00afe2c7ba2c14a859015d538aa938199ec558afe2d`
- snapshot_bundle_hash: `bd2149be986f2bae65b5c744e43ddb075544a8053bb0d5f6a93b136373a65c5a`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

