# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (base + flags + capped margin; LLM lean `+0.0` recorded, not added) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal has clear intent, fixed accounting rules, and states that it does not itself authorize spending, which supports governance clarity; however, the key need for a higher limit is asserted rather than evidenced, and the assessment notes a thin risk review, so the mechanical score should not be nudged toward spending or opposition.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal did not meet the evidence threshold for a directional vote. This is a conservative hold, not active opposition: the core request was clear, but some material claims and risk evidence were too thin to support a confident Yes or No.

The action asked DReps to agree to a new 500,000,000 ada Net Change Limit for total Cardano Treasury withdrawals debited during Epochs 613-713, ending around July 3, 2027. The proposal says this would supersede any prior Net Change Limit for the same period and would record DRep agreement if Yes votes exceed 50% of active voting stake. It is an InfoAction, so it has no direct on-chain effect and does not itself authorize any Treasury Withdrawal.

Several important claims were well-supported by the proposal anchor: the 500,000,000 ada limit, the Epochs 613-713 period, the fact that the cap applies only to Treasury withdrawals and not inflows, and that withdrawals already debited in the period would count toward the limit. However, independent evidence was missing for the claim that this proposal can supersede a prior Net Change Limit for the same period, and for the claim that the existing 350,000,000 ada limit is becoming practically constrained. The risk review was also thin, with execution risk unknown and missing mitigation evidence and independent assurance.

A directional vote would be unblocked by replayable independent evidence supporting the supersession claim, evidence for the practical constraint under the current 350,000,000 ada limit, and clearer risk mitigation or assurance. Because those gaps remain, BEACN abstained to avoid overstating certainty.

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
- finding: Stated amount: not stated in document
- finding: Deliverables: Set a 500,000,000 ada Net Change Limit for total Treasury Withdrawals debited during Epochs 613-713, Supersede any prior Net Change Limit for the same period, Record DRep agreement when Yes votes exceed 50% of active voting stake
- finding: Deadline/expiry: Period ends at the close of Epoch 713, on or about July 3, 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The limit caps only total lovelace removed from the Treasury by enacted Treasury Withdrawals recorded on the Cardano ledger and does not count Treasury inflows.
- finding: Claim (economic, supported_in_proposal, high materiality): All Treasury Withdrawals already debited during the period count toward the proposed 500,000,000 ada limit.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- finding: Claim (economic, proposer_asserted, medium materiality): The document says the existing 350,000,000 ada Net Change Limit has been useful but practical remaining room under it is becoming constrained.
- missing: Independent evidence for: The proposal supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- missing: Independent evidence for: The document says the existing 350,000,000 ada Net Change Limit has been useful but practical remaining room under it is becoming constrained.
- missing: Independent evidence for: The proposer asserts that nothing in the Constitution limits DReps to a single Net Change Limit or prevents a newly agreed Net Change Limit from applying to the period.
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
- finding: Strongest NO: a material claim is unsupported — "The proposal supersedes any prior Net Change Limit for the same Epochs 613-713 period." — so cost or precedent may outweigh the benefit.
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
- Claims and evidence missing: Independent evidence for: The proposal supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- Claims and evidence missing: Independent evidence for: The document says the existing 350,000,000 ada Net Change Limit has been useful but practical remaining room under it is becoming constrained.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `0609034519bb58cb2d1913ef76bb8825aeb0b8f6748117231a773ad0867b0de5`
- snapshot_bundle_hash: `4285b5c7fb9bda19dabc7675dcf2a0f5453011da120120e8d275e521429efc44`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

