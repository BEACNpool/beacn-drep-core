# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.07` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4875` | Readiness: `0.5`
> Reasoning layer (precomputed): The proposal has clear governance intent and a defined accounting rule, which aligns with info actions that improve clarity, but the justification for raising the fiscal guardrail is thin and mainly proposer-asserted. Given the assessment status is incomplete with thin risk review, a small cautionary nudge is warranted rather than a positive spending-cap signal.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s core accounting rule is clear, but the review did not have enough independent evidence about DRep distribution and key supporting claims to justify a directional vote.

The action asked DReps to agree to a new 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713, replacing the prior 350,000,000 ada limit for the same period. It does not request a direct withdrawal, name a recipient, or authorize spending on-chain. The proposal says all withdrawals already debited during the period would count toward the cap, and that the limit applies only to lovelace removed from the Treasury, not inflows, refunds, or returned funds.

Several basic claims were well-supported by the pinned proposal anchor: the amount, the covered epoch range, the accounting treatment, and the fact that this is an InfoAction with no direct withdrawal effect. The weaker areas were the justification for raising the guardrail, the claim that the prior 350,000,000 ada limit is becoming constrained, and independent evidence that the new limit supersedes the previous one. The risk review was also thin, with execution risk unknown and missing mitigation or independent assurance evidence.

This ABSTAIN is a conservative, evidence-based hold. A directional vote would be unblocked by DRep distribution data, stronger independent evidence for the superseding effect and the need to raise the limit, plus clearer risk mitigation or assurance for the governance and execution concerns.

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
- finding: Requested: Info action to agree a new Net Change Limit for the Cardano Treasury for Epochs 613-713
- finding: Recipient: not stated in document
- finding: Stated amount: 500,000,000 ada cap on total Treasury Withdrawals during the period; no direct withdrawal amount requested
- finding: Deliverables: Record DRep agreement to a 500,000,000 ada Net Change Limit for Epochs 613-713, Supersede any prior Net Change Limit for the same period, Count all Treasury Withdrawals already debited during the period toward the cap
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury Withdrawals during Epochs 613-713.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal states that the limit caps only the cumulative lovelace removed from the Treasury by enacted Treasury Withdrawals recorded on the Cardano ledger.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states that Treasury inflows, including reserve and protocol allocations, fee allocations, refunds, and returns of funded amounts, do not count toward or increase the limit.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal says this new 500,000,000 ada limit supersedes the previously agreed 350,000,000 ada Net Change Limit for the same Epochs 613-713 period.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that all Treasury Withdrawals already debited during the period count toward the 500,000,000 ada limit and are not reset, reversed, reopened, or reauthorized by this action.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that the action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- missing: Independent evidence for: The proposal says this new 500,000,000 ada limit supersedes the previously agreed 350,000,000 ada Net Change Limit for the same Epochs 613-713 period.
- missing: Independent evidence for: The proposal asserts that the existing 350,000,000 ada limit has served as a useful fiscal guardrail but that practical room under it is becoming constrained.
- missing: Independent evidence for: The proposal asserts that agreeing the higher limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed guardrail.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury Withdrawals during Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says this new 500,000,000 ada limit supersedes the previously agreed 350,000,000 ada Net Change Limit for the same Epochs 613-713 period." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury Withdrawals during Epochs 613-713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has clear governance intent and a defined accounting rule, which aligns with info actions that improve clarity, but the justification for raising the fiscal guardrail is thin and mainly proposer-asserted. Given the assessment status is incomplete with thin risk review, a small cautionary nudge is warranted rather than a positive spending-cap signal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- No DRep distribution available.
- Claims and evidence missing: Independent evidence for: The proposal says this new 500,000,000 ada limit supersedes the previously agreed 350,000,000 ada Net Change Limit for the same Epochs 613-713 period.
- Claims and evidence missing: Independent evidence for: The proposal asserts that the existing 350,000,000 ada limit has served as a useful fiscal guardrail but that practical room under it is becoming constrained.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `758c1c8e40cd526f0db8cfdbd39fbeae221323758b62f1c94f2c5e21c457bd1d`
- snapshot_bundle_hash: `90f3dcc159da4524ae44de8eb4edb4c9f9b8f40c1bffef4014d9ab870af6ee8e`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4419, "NO": 0.3491, "YES": 0.2091}`

