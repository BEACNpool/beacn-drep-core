# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The document gives clear intent, period, accounting rules, and no-direct-withdrawal framing, but the material justification for raising the cap is mostly asserted and the deterministic assessment marks risk review as thin and overall status incomplete. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive signal.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal did not meet BEACN’s evidence threshold for a directional vote. The action was clear about what it wanted to record, but key governance claims and the risk review were too thin to justify a Yes, while the record did not support treating this as active opposition.

The proposal asked DReps to agree to a 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713, from February 13, 2026 to about July 3, 2027. It stated that this would supersede the existing 350,000,000 ada limit for the same period, that withdrawals already debited during the period would count toward the new limit, and that the action itself has no direct on-chain effect and does not authorize any treasury withdrawal.

Several core facts were supported by the proposal anchor: the 500,000,000 ada limit, the period covered, the no-direct-withdrawal framing, and the rule that only treasury withdrawals count against the limit, not inflows. However, other important claims were only asserted or still needed independent support, including the voting-threshold claim under TREASURY-01a and the claim that the new limit supersedes the prior 350,000,000 ada limit. The proposal also asserted that practical room under the current limit is becoming constrained, but that justification remained mostly asserted.

This abstention is a conservative, evidence-based hold. A directional vote would be unblocked by replayable independent evidence for the governance threshold and supersession claims, plus stronger mitigation or assurance evidence for the risk review. The strongest Yes case is that the requested limit and accounting rules are clearly stated; the strongest hold case is that BEACN should not overstate certainty when material claims are not fully tied to public, verifiable evidence.

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
- finding: Stated amount: no direct withdrawal requested; proposed net change limit is 500,000,000 ada
- finding: Deliverables: Record DRep agreement to a 500,000,000 ada Net Change Limit for Treasury Withdrawals during Epochs 613-713., Supersede any prior Net Change Limit for the same period., Clarify that withdrawals already debited during the period count toward the limit.
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposed limit caps only Treasury Withdrawals debited from the Treasury and does not count Treasury inflows.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that it has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal states that DRep agreement is recorded when Yes votes exceed 50% of active voting stake under TREASURY-01a.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal says the new 500,000,000 ada limit supersedes any prior Net Change Limit for the same period, including the existing 350,000,000 ada limit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states that all Treasury Withdrawals already debited during the period count toward the 500,000,000 ada limit.
- missing: Independent evidence for: The proposal states that DRep agreement is recorded when Yes votes exceed 50% of active voting stake under TREASURY-01a.
- missing: Independent evidence for: The proposal says the new 500,000,000 ada limit supersedes any prior Net Change Limit for the same period, including the existing 350,000,000 ada limit.
- missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has been useful but that practical room under it is becoming constrained.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that DRep agreement is recorded when Yes votes exceed 50% of active voting stake under TREASURY-01a." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The document gives clear intent, period, accounting rules, and no-direct-withdrawal framing, but the material justification for raising the cap is mostly asserted and the deterministic assessment marks risk review as thin and overall status incomplete. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive signal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that DRep agreement is recorded when Yes votes exceed 50% of active voting stake under TREASURY-01a.
- Claims and evidence missing: Independent evidence for: The proposal says the new 500,000,000 ada limit supersedes any prior Net Change Limit for the same period, including the existing 350,000,000 ada limit.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `76c23676bee0f757add9cf64b9b0bf59fe6b7b096e91620651d0a53551971adf`
- snapshot_bundle_hash: `dcf0c10766096dd5caf44ebea6eca5d4e2da31a7bc36459f947bffab4ffde409`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4d394ccfc21657ebcbf2e1dbb3e210682b5ea383`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

