# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `+0.0`) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal has clear intent and accounting mechanics, and it states that no withdrawal is authorized, but the assessment status is incomplete and the risk review is thin; the deterministic rules appear to capture the main treasury-stewardship and evidence-quality concerns, so no additional nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal did not meet the evidence threshold for a directional vote. This is a conservative, evidence-based hold, not active opposition to the proposed limit.

The action asked DReps to agree to a new Net Change Limit of 500,000,000 ada for Cardano Treasury withdrawals during Epochs 613-713, from February 13, 2026 to about July 3, 2027. It does not directly withdraw treasury funds, name a recipient, or authorize any payment. The proposal says the limit would apply to cumulative Treasury Withdrawals debited during that period and would supersede any prior limit for the same period.

Several core facts were supported by the proposal itself: the 500,000,000 ada limit, the fact that inflows are not counted, the inclusion of already-debited withdrawals during the period, and the lack of direct on-chain effect. However, important claims remained only proposer-asserted or thinly evidenced, including the claim that Yes votes above 50% of active voting stake record DRep agreement under TREASURY-01a, and the claim that the existing 350,000,000 ada limit has become practically constrained. The review also found execution risk unknown, missing mitigation evidence, and missing independent assurance.

A directional vote would be unblocked by replayable independent evidence for the threshold and guardrail interpretation, stronger support for why the current 350,000,000 ada limit is practically constrained, and clearer mitigation or assurance around the identified risk gaps. Until then, abstaining avoids overstating certainty while acknowledging that the proposal’s basic requested limit was clearly stated and reviewable.

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
- finding: Requested: Info action to agree a new Net Change Limit for Cardano Treasury withdrawals for Epochs 613-713.
- finding: Recipient: not stated in document
- finding: Stated amount: no direct treasury withdrawal requested; proposed Net Change Limit is 500,000,000 ada
- finding: Deliverables: Record DRep agreement to a 500,000,000 ada Net Change Limit for Epochs 613-713, Supersede any prior Net Change Limit for the same period, Apply the limit to cumulative Treasury Withdrawals debited during the period
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposed limit caps only ada removed from the Treasury through enacted Treasury Withdrawals and does not count Treasury inflows.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the Epochs 613-713 period count toward the proposed 500,000,000 ada limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal states that Yes votes exceeding 50% of active voting stake record DRep agreement to the Net Change Limit under TREASURY-01a.
- finding: Claim (economic, proposer_asserted, high materiality): The proposer says the existing 350,000,000 ada Net Change Limit has become practically constrained and that a 500,000,000 ada limit preserves room to consider credible withdrawals.
- missing: Independent evidence for: The proposal states that Yes votes exceeding 50% of active voting stake record DRep agreement to the Net Change Limit under TREASURY-01a.
- missing: Independent evidence for: The proposer says the existing 350,000,000 ada Net Change Limit has become practically constrained and that a 500,000,000 ada limit preserves room to consider credible withdrawals.
- missing: Independent evidence for: The proposal says the new Net Change Limit supersedes any prior Net Change Limit for the same Epochs 613-713 period.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Yes votes exceeding 50% of active voting stake record DRep agreement to the Net Change Limit under TREASURY-01a." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: The proposal states that Yes votes exceeding 50% of active voting stake record DRep agreement to the Net Change Limit under TREASURY-01a.
- Claims and evidence missing: Independent evidence for: The proposer says the existing 350,000,000 ada Net Change Limit has become practically constrained and that a 500,000,000 ada limit preserves room to consider credible withdrawals.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `1960ef29c8f605ab2aca54291f509394da6392ef9959705cb4765f3106a0de78`
- snapshot_bundle_hash: `8f7d35a5a64656ba0f9ef257907cd52ad8e23aa5c23b26ea5e39cda5d01c9e10`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

