# Rationale: gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `+0.0`) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The claims show clear intent, defined accounting mechanics, and an explicit statement that the action does not authorize spending, which aligns with governance clarity for Info actions. However, the main justification that room under the prior limit is becoming constrained is asserted rather than evidenced, and the constitutional interpretation is not substantiated inside the document beyond a reference, so the deterministic assessment appears to capture the relevant caution.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal did not meet the evidence threshold for a directional vote. This is a conservative, evidence-based hold, not active opposition to the idea of changing the Treasury Net Change Limit.

The action asked DReps to record agreement to a 500,000,000 ada cap on total Treasury withdrawals debited from Epoch 613 through Epoch 713, replacing any prior limit for the same period and counting withdrawals already debited during that window. The proposal also stated that the action has no direct on-chain effect and does not itself authorize any Treasury withdrawal. Those core mechanics were supported by the pinned, replayable proposal anchor.

The proposer also claimed that the existing 350,000,000 ada limit has been a useful guardrail but is becoming constrained, and that the higher limit would preserve DReps’ ability to assess credible withdrawals while keeping a fixed cap. Those claims were not independently supported in the review. The review also found the claims-and-evidence record thin, with execution risk unknown and missing mitigation evidence and independent assurance.

A YES case exists: the proposal clearly establishes the requested 500,000,000 ada limit and passes the basic evidence gates for what the action would do. But BEACN’s rule threshold was not met because some material claims remained unsupported. A directional vote would need independent evidence that the current 350,000,000 ada limit is actually becoming constrained, plus clearer risk mitigation or independent assurance for the proposed higher guardrail.

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
- finding: Stated amount: not stated in document
- finding: Deliverables: Set a fixed cap of 500,000,000 ada on total Treasury Withdrawals debited during the period from Epoch 613 through Epoch 713., Supersede any prior Net Change Limit for the same period., Count all Treasury Withdrawals already debited during the period toward the limit., Record DRep agreement if Yes votes exceed 50% of active voting stake.
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal sets a new Net Change Limit of 500,000,000 ada for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed limit caps only lovelace removed from the Treasury through enacted Treasury Withdrawals recorded on the Cardano ledger.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returns of Treasury-funded amounts, do not count toward or increase the limit.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the period count toward the proposed 500,000,000 ada limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer states that an existing 350,000,000 ada Net Change Limit for Epochs 613-713 has served as a useful fiscal guardrail but is becoming constrained.
- missing: Independent evidence for: The proposer states that an existing 350,000,000 ada Net Change Limit for Epochs 613-713 has served as a useful fiscal guardrail but is becoming constrained.
- missing: Independent evidence for: The proposer states that the new limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed guardrail.
- missing: Independent evidence for: The proposer states that nothing in the Constitution limits DReps to a single Net Change Limit or prevents a newly agreed Net Change Limit from applying to the period.
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
- finding: Strongest NO: a material claim is unsupported — "The proposer states that an existing 350,000,000 ada Net Change Limit for Epochs 613-713 has served as a useful fiscal guardrail but is becoming constrained." — so cost or precedent may outweigh the benefit.
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
- No additional inference.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer states that an existing 350,000,000 ada Net Change Limit for Epochs 613-713 has served as a useful fiscal guardrail but is becoming constrained.
- Claims and evidence missing: Independent evidence for: The proposer states that the new limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed guardrail.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `021d41161d9716de87a3e00afe2c7ba2c14a859015d538aa938199ec558afe2d`
- snapshot_bundle_hash: `6066fea471df80968ae91834940b45734062c8046c78d3f3b0f50d6c202c5c27`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

