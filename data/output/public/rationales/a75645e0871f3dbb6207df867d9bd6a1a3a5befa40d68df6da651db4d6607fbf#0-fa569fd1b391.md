# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (base + flags + capped margin; LLM lean `+0.0` recorded, not added) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal gives clear intent, period, accounting mechanics, and governance use for a signaling action, while the main justification for increasing the cap is asserted rather than evidenced; the deterministic assessment already captures the incomplete/thin review posture, so no additional advisory nudge is warranted.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal did not meet the evidence threshold for a directional vote. The action clearly describes a 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals, but the key justification for raising the limit was not independently supported enough for BEACN to vote yes or no with confidence.

The proposal asked DReps to record agreement to a new Treasury Net Change Limit for Epochs 613 through 713, ending around July 3, 2027. It would supersede any prior limit for the same period and count Treasury Withdrawals already debited during the period toward the new 500,000,000 ada cap. The proposal also states that this is an Info action only: it has no direct on-chain effect and does not itself authorize any Treasury Withdrawal.

Several factual claims were well-supported by the proposal anchor, including the amount of the limit, the epoch range, the treatment of already-debited withdrawals, and the fact that the cap applies only to cumulative lovelace removed from the Treasury through enacted Treasury Withdrawals. However, the proposal’s central policy claims were thinner: BEACN did not have independent evidence that the existing 350,000,000 ada limit had become practically constrained, or that raising it to 500,000,000 ada would preserve useful flexibility while still maintaining an appropriate fiscal guardrail.

This abstention is a conservative, evidence-based hold, not active opposition. A directional vote would be unblocked by stronger independent evidence for the need to raise the limit, clearer mitigation evidence for the risks, and independent assurance around the fiscal and governance effects of the proposed change.

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
- finding: Requested: Info action to agree a new Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Record DRep agreement to a 500,000,000 ada Net Change Limit for Epochs 613-713., Supersede any prior Net Change Limit for the same period., Define that prior Treasury Withdrawals already debited during the period count toward the limit.
- finding: Deadline/expiry: Close of Epoch 713, on or about July 3, 2027.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for the Cardano Treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed limit applies from the start of Epoch 613 on February 13, 2026 through the close of Epoch 713, on or about July 3, 2027.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only the cumulative lovelace removed from the Treasury through enacted Treasury Withdrawals recorded on the Cardano ledger during the period.
- finding: Claim (technical, supported_in_proposal, medium materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returns of Treasury-funded amounts, do not count toward or increase the limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that Treasury Withdrawals already debited during the period count toward the 500,000,000 ada limit and remain valid.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that this Info action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained while still serving as a useful fiscal guardrail.
- missing: Independent evidence for: The proposal asserts that agreeing a higher 500,000,000 ada limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed fiscal guardrail.
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
- finding: Strongest NO: a material claim is unsupported — "The proposer asserts that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained while still serving as a useful fiscal guardrail." — so cost or precedent may outweigh the benefit.
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
- No additional inference.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained while still serving as a useful fiscal guardrail.
- Claims and evidence missing: Independent evidence for: The proposal asserts that agreeing a higher 500,000,000 ada limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed fiscal guardrail.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `fa569fd1b391a060792e127f055e2f2fe0b5672baaca72418bde888eba50fbe5`
- snapshot_bundle_hash: `4c6e3efa8e6989b156ca08f322edfecec34b5bf55305d5408cda6bf2c796ef1e`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `8349c00bf634786b09e40136f9b870b28102b9dd`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

