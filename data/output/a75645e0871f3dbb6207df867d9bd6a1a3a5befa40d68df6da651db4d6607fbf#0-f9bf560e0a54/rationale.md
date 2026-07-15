# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (base + flags + capped margin; LLM lean `-0.01` recorded, not added) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal has clear intent and detailed accounting mechanics, which supports governance clarity, but the central fiscal justification for increasing the guardrail from 350,000,000 ada to 500,000,000 ada is mostly proposer-asserted and the assessment notes a thin risk review. A small cautionary nudge is warranted because treasury stewardship and evidence quality matter even for a non-binding Info action with real coordination effects.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s basic request was clear, but the evidence did not meet the threshold for a directional vote. This is a conservative, evidence-based hold, not active opposition.

The action asked DReps to agree to a new Net Change Limit of 500,000,000 ada for Cardano Treasury withdrawals during Epochs 613-713. The proposal said this would cap only Treasury outflows from enacted withdrawals, include any withdrawals already debited in that period, supersede any prior limit for the same period, and have no direct on-chain effect or authorization power by itself. The strongest supported point was that the proposal clearly sets a 500,000,000 ada cap for the stated period and explains the accounting mechanics.

The weaker part was the justification and independent support for key claims. The review found the anchor document was available, pinned, and replayable, but several important claims remained mostly proposer-asserted: that this new limit supersedes the previous 350,000,000 ada limit, that the existing limit has become practically constrained, and that raising the cap to 500,000,000 ada is the right fiscal guardrail. The risk review was also thin, with execution risk unknown and missing mitigation evidence and independent assurance.

An ABSTAIN vote leaves room for a future directional vote if the missing evidence is provided. The clearest unblockers would be independent, replayable support for the supersession of the prior 350,000,000 ada limit, evidence that the existing limit is practically constrained through mid-2027, and stronger risk or mitigation assurance for the proposed increase.

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
- finding: Requested: Info action to agree a new Net Change Limit for Cardano Treasury withdrawals for Epochs 613-713
- finding: Recipient: not stated in document
- finding: Stated amount: 500,000,000
- finding: Deliverables: Set a fixed cap of 500,000,000 ada on total Treasury withdrawals debited during Epochs 613-713, Supersede any prior Net Change Limit for the same period, Record DRep agreement if Yes votes exceed 50% of active voting stake, Clarify that the action has no direct on-chain effect and does not authorize any Treasury Withdrawal
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal sets a new Net Change Limit of 500,000,000 ada for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed limit caps only total lovelace removed from the Treasury through enacted Treasury Withdrawals and does not count Treasury inflows.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the Epoch 613-713 period count toward the proposed 500,000,000 ada cumulative limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that this Info action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal says it supersedes any prior Net Change Limit for the same Epoch 613-713 period, including a previously agreed 350,000,000 ada limit.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer claims the existing 350,000,000 ada limit has become practically constrained while its window runs into mid-2027.
- missing: Independent evidence for: The proposal says it supersedes any prior Net Change Limit for the same Epoch 613-713 period, including a previously agreed 350,000,000 ada limit.
- missing: Independent evidence for: The proposer claims the existing 350,000,000 ada limit has become practically constrained while its window runs into mid-2027.
- missing: Independent evidence for: The proposer claims a 500,000,000 ada limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed fiscal guardrail.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada for Cardano Treasury withdrawals during Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says it supersedes any prior Net Change Limit for the same Epoch 613-713 period, including a previously agreed 350,000,000 ada limit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada for Cardano Treasury withdrawals during Epochs 613-713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.010 (display cap ±0.05) and had zero influence on the binding score: The proposal has clear intent and detailed accounting mechanics, which supports governance clarity, but the central fiscal justification for increasing the guardrail from 350,000,000 ada to 500,000,000 ada is mostly proposer-asserted and the assessment notes a thin risk review. A small cautionary nudge is warranted because treasury stewardship and evidence quality matter even for a non-binding Info action with real coordination effects.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal says it supersedes any prior Net Change Limit for the same Epoch 613-713 period, including a previously agreed 350,000,000 ada limit.
- Claims and evidence missing: Independent evidence for: The proposer claims the existing 350,000,000 ada limit has become practically constrained while its window runs into mid-2027.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `f9bf560e0a543b4a850a2f21efed9af185bd6271b8c3d4a08422b9cca5c7944e`
- snapshot_bundle_hash: `2f2365477f6f8a45e05d096d937c493797ac799e1f0aa8b3d083f04cd5d724bd`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `880436a840989202a38cccce66fd8f1cbf15004d`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

