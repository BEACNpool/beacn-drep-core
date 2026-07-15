# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (base + flags + capped margin; LLM lean `+0.0` recorded, not added) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal has clear intent and describes a simple accounting rule, but several high-materiality constitutional and threshold assertions are stated rather than demonstrated in the document; the deterministic assessment already marks the review incomplete with thin risk review, so no additional advisory nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal did not meet the evidence threshold for a directional vote. The core request was clear, but key justification claims were not independently supported enough for BEACN to vote Yes or No with confidence.

The action asked DReps to agree to a new 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713, replacing any prior limit for that same period and counting withdrawals already debited during the period toward the cap. The proposal stated that this InfoAction has no direct on-chain effect and does not authorize any Treasury Withdrawal. It also clearly supported the basic mechanics of the limit: the cap applies only to lovelace removed from the Treasury by enacted Treasury Withdrawal governance actions, while inflows and returned funds do not increase the limit.

The strongest case for Yes is that the proposal’s anchor was pinned and replayable, and the basic 500,000,000 ada limit was substantiated. The weakness is that important rationale remained thin: there was missing independent evidence that the existing 350,000,000 ada limit had become practically constrained, and missing independent evidence that raising the cap would preserve DReps’ ability to consider credible withdrawals while retaining a fixed fiscal guardrail. The risk review was also thin, with mitigation evidence and independent assurance missing, and execution risk marked unknown.

This ABSTAIN is a conservative, evidence-based hold, not active opposition. A directional vote would be unblocked by stronger independent evidence for why the current 350,000,000 ada limit is insufficient, why 500,000,000 ada is the appropriate replacement guardrail, and what mitigation or assurance exists around the governance and execution risks of changing the limit for the same period.

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
- finding: Requested: Agree a new Net Change Limit for Cardano Treasury withdrawals for Epochs 613-713.
- finding: Recipient: Cardano Treasury governance process / DReps
- finding: Stated amount: 500,000,000 ada cap on total Treasury withdrawals during the period; no direct withdrawal amount requested
- finding: Deliverables: Record DReps' agreement to a 500,000,000 ada Net Change Limit for Epochs 613-713, Supersede any prior Net Change Limit for the same period, Count all Treasury withdrawals already debited during the period toward the limit
- finding: Deadline/expiry: Period begins at start of Epoch 613 on February 13, 2026 and ends at close of Epoch 713 on or about July 3, 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Epochs 613-713.
- finding: Claim (governance, supported_in_proposal, high materiality): The Net Change Limit caps only lovelace removed from the Cardano Treasury by enacted Treasury Withdrawal governance actions recorded on the ledger.
- finding: Claim (economic, supported_in_proposal, medium materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returns of Treasury-funded amounts, do not count toward or increase the limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained as its window runs into mid-2027.
- finding: Claim (governance, proposer_asserted, high materiality): The proposer states that increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals while retaining a fixed fiscal guardrail.
- missing: Independent evidence for: The proposer states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained as its window runs into mid-2027.
- missing: Independent evidence for: The proposer states that increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals while retaining a fixed fiscal guardrail.
- missing: Independent evidence for: The proposer states that Yes votes exceeding 50% of active voting stake are sufficient to record agreement to the Net Change Limit under TREASURY-01a.
- missing: Independent evidence for: The proposer asserts that nothing in the Constitution limits DReps to a single Net Change Limit or prevents a newly agreed limit from applying to the same period.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained as its window runs into mid-2027." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Epochs 613-713." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: The proposer states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained as its window runs into mid-2027.
- Claims and evidence missing: Independent evidence for: The proposer states that increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals while retaining a fixed fiscal guardrail.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `778eb05f5a59c5f3ae0e33e1160462a9444fb39b43316eed6e115f0a0089629f`
- snapshot_bundle_hash: `0e8570683edfd187b4566d488e77df260d1e839340fe9316dc386ab9e8659942`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `d68b33ee7989803aaecd7edc03d77c134a98a7f1`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

