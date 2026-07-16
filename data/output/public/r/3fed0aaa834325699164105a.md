# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (base + flags + capped margin; LLM lean `-0.01` recorded, not added) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal has clear intent and accounting mechanics, but several high-materiality governance claims, including superseding the prior limit and constitutional interpretation, are mostly asserted rather than evidenced within the document; a small cautionary nudge is justified for an Info action with real treasury coordination effects.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s core request was clear, but key governance claims did not meet the evidence threshold for a directional vote.

The action asked DReps to agree to a new Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713, running from February 13, 2026 to about July 3, 2027. The proposal says this limit would cap total Treasury withdrawals enacted during that period, would not count Treasury inflows, and would include withdrawals already debited during the period. It also states that the Info action itself has no direct on-chain effect and does not authorize any Treasury withdrawal.

Several important claims were well-supported in the proposal, especially the amount, the accounting mechanics, and the fact that this is an Info action rather than a direct withdrawal. However, higher-materiality governance claims were not supported strongly enough by independent evidence, including that the new 500,000,000 ada limit supersedes the prior 350,000,000 ada limit, and that Yes votes above 50% of active voting stake record DRep agreement under threshold TREASURY-01a. The review also found the claims-and-evidence status thin, with risk review thin and missing mitigation evidence and independent assurance.

This ABSTAIN is a conservative, evidence-based hold, not active opposition. A directional vote would be unblocked by replayable independent evidence for the superseding effect, clearer support for the claimed voting threshold, and stronger mitigation or assurance evidence for the governance and execution risks.

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
- finding: Stated amount: not stated in document
- finding: Deliverables: Set a 500,000,000 ada net change limit for total Treasury withdrawals during Epochs 613-713., Record DRep agreement that this limit supersedes any prior Net Change Limit for the same period.
- finding: Deadline/expiry: Period begins at start of Epoch 613 on February 13, 2026 and ends at close of Epoch 713 on or about July 3, 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets the Cardano Treasury Net Change Limit for Epochs 613-713 at 500,000,000 ada, equal to 500,000,000,000,000 lovelace.
- finding: Claim (economic, supported_in_proposal, high materiality): The limit caps the cumulative amount removed from the Treasury through enacted Treasury Withdrawals during the period and does not count Treasury inflows.
- finding: Claim (governance, proposer_asserted, high materiality): The proposed 500,000,000 ada limit supersedes a previously agreed 350,000,000 ada Net Change Limit for the same period.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the Epochs 613-713 period count toward the proposed 500,000,000 ada limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The Info action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (governance, proposer_asserted, medium materiality): Yes votes exceeding 50% of active voting stake record DRep agreement to the Net Change Limit under threshold TREASURY-01a.
- missing: Independent evidence for: The proposed 500,000,000 ada limit supersedes a previously agreed 350,000,000 ada Net Change Limit for the same period.
- missing: Independent evidence for: Yes votes exceeding 50% of active voting stake record DRep agreement to the Net Change Limit under threshold TREASURY-01a.
- missing: Independent evidence for: The existing 350,000,000 ada limit has been useful but is becoming practically constrained through mid-2027.
- missing: Independent evidence for: Nothing in the Constitution limits DReps to a single Net Change Limit or prevents a newly agreed Net Change Limit from applying to the period.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets the Cardano Treasury Net Change Limit for Epochs 613-713 at 500,000,000 ada, equal to 500,000,000,000,000 lovelace." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposed 500,000,000 ada limit supersedes a previously agreed 350,000,000 ada Net Change Limit for the same period." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets the Cardano Treasury Net Change Limit for Epochs 613-713 at 500,000,000 ada, equal to 500,000,000,000,000 lovelace." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.010 (display cap ±0.05) and had zero influence on the binding score: The proposal has clear intent and accounting mechanics, but several high-materiality governance claims, including superseding the prior limit and constitutional interpretation, are mostly asserted rather than evidenced within the document; a small cautionary nudge is justified for an Info action with real treasury coordination effects.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposed 500,000,000 ada limit supersedes a previously agreed 350,000,000 ada Net Change Limit for the same period.
- Claims and evidence missing: Independent evidence for: Yes votes exceeding 50% of active voting stake record DRep agreement to the Net Change Limit under threshold TREASURY-01a.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `19581b9204f8a4508431661bd90eac85fb4e4acf2de6589a5fc19b172b9aaca1`
- snapshot_bundle_hash: `3de4c5785d6848f14e55b6fe661c7f90c3cf3cb6cc932161f9155dd0d155cbe7`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

