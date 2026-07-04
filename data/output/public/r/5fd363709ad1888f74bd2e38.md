# Rationale: gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
Recommendation: **ABSTAIN**
Score: `-0.07` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4375` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal has clear intent and specifies accounting mechanics, which supports governance clarity, but the core justification for increasing the treasury guardrail is asserted rather than evidenced in the extracted claims. Under a treasury-stewardship-first standard, that thin evidentiary basis justifies only a small cautionary negative nudge rather than a stronger directional judgment.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s basic terms were clear, but the evidence did not meet the threshold for a directional vote. This is a conservative, evidence-based hold, not active opposition.

The action asked DReps to agree to a 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals from Epoch 613 through Epoch 713. It did not request a direct Treasury withdrawal. The proposal clearly supported several important points: the size of the cap, the period covered, that Treasury inflows would not count against the cap, that prior withdrawals during the period would count, and that the info action itself has no direct on-chain effect.

The weaker parts were the claims used to justify the change. The proposal asserted that the new limit would supersede any prior limit for the same period, and that the existing 350,000,000 ada guardrail is becoming constrained, but those points lacked independent supporting evidence in the review. The risk review was also thin, with missing mitigation evidence and independent assurance.

A YES vote would require stronger replayable evidence for the supersession claim, the need to raise the limit from 350,000,000 ada to 500,000,000 ada, and the relevant risk mitigations. Without that, BEACN held at ABSTAIN because the proposal was understandable but not evidenced strongly enough to justify approval or rejection.

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: not required
- finding: Requested: Info action to agree a new Net Change Limit for Cardano Treasury withdrawals for Epochs 613-713, superseding any prior Net Change Limit for the same period.
- finding: Recipient: Cardano DReps / governance process
- finding: Stated amount: 500,000,000 ada net change limit; no direct treasury withdrawal requested
- finding: Deliverables: Record DRep agreement to a 500,000,000 ada Net Change Limit for Epochs 613-713, Apply the limit as a fixed cap on total Treasury Withdrawals debited during the period, Exclude Treasury inflows from the calculation, Count prior Treasury Withdrawals already debited during the period toward the limit
- finding: Deadline/expiry: Period begins at the start of Epoch 613 (February 13, 2026) and ends at the close of Epoch 713, on or about July 3, 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed limit is a cap on total ada removed from the Treasury through enacted Treasury Withdrawals during the period and does not count Treasury inflows.
- finding: Claim (governance, proposer_asserted, high materiality): The proposed Net Change Limit supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- finding: Claim (economic, supported_in_proposal, high materiality): All Treasury Withdrawals already debited during the period beginning at Epoch 613 count toward the proposed 500,000,000 ada limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The info action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (economic, proposer_asserted, high materiality): The existing 350,000,000 ada Net Change Limit for Epochs 613-713 has served as a useful fiscal guardrail but practical room under it is becoming constrained.
- missing: Independent evidence for: The proposed Net Change Limit supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- missing: Independent evidence for: The existing 350,000,000 ada Net Change Limit for Epochs 613-713 has served as a useful fiscal guardrail but practical room under it is becoming constrained.
- missing: Independent evidence for: Raising the limit to 500,000,000 ada would preserve DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed guardrail and simple accounting.
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
- finding: Strongest NO: a material claim is unsupported — "The proposed Net Change Limit supersedes any prior Net Change Limit for the same Epochs 613-713 period." — so cost or precedent may outweigh the benefit.
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
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has clear intent and specifies accounting mechanics, which supports governance clarity, but the core justification for increasing the treasury guardrail is asserted rather than evidenced in the extracted claims. Under a treasury-stewardship-first standard, that thin evidentiary basis justifies only a small cautionary negative nudge rather than a stronger directional judgment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposed Net Change Limit supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- Claims and evidence missing: Independent evidence for: The existing 350,000,000 ada Net Change Limit for Epochs 613-713 has served as a useful fiscal guardrail but practical room under it is becoming constrained.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `c281086b6de1e098e567fd56e8e01d7d5e2af9e11f23a472e1f5fd6d2daacf19`
- snapshot_bundle_hash: `cf8e16ef3fb3de86645049ae132861c8d6ebd1f5e4510062439923ca6f984fb6`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `959`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4294, "NO": 0.3553, "YES": 0.2153}`

