# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4825` | Readiness: `0.5`
> Reasoning layer (precomputed): The claims provide clear intent and accounting mechanics, and the action does not directly authorize spending, but several high-materiality governance and constitutional assertions depend on external verification while the deterministic assessment marks risk review as thin and overall status incomplete. A small cautionary nudge is warranted because raising a treasury guardrail affects downside protection even though the proposal preserves per-withdrawal discretion.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because a key review input was missing: no DRep distribution was available, so the system could not confidently turn the evidence review into a directional vote.

The action asked DReps to agree to a new Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613 through 713, from February 13, 2026 to about July 3, 2027. It did not request a direct treasury withdrawal. The proposal said this cap would apply to total ada removed through enacted Treasury Withdrawals during that period, would supersede any prior Net Change Limit for the same period, and would count withdrawals already debited during the period toward the limit.

Several core mechanics were well-supported by the proposal itself: the 500,000,000 ada limit, the fact that only treasury debits from enacted withdrawals count against it, the exclusion of treasury inflows from the cap, and the statement that this Info action has no direct on-chain spending effect. However, some material claims were not independently supported in the review, including the claim that the existing 350,000,000 ada limit is becoming practically constrained before mid-2027 and the claim that the Constitution allows DReps to set a new Net Change Limit for the same period.

This ABSTAIN is a conservative, evidence-based hold. A directional vote would be unblocked by the missing DRep distribution, stronger independent evidence for the unsupported fiscal and constitutional claims, and better mitigation or assurance evidence for the thin risk review.

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
- finding: Stated amount: 500,000,000 ada net change limit; no direct treasury withdrawal requested
- finding: Deliverables: Record DReps' agreement to a 500,000,000 ada fixed cap on total ada removed from the Treasury through Treasury Withdrawals during Epochs 613-713, Supersede any prior Net Change Limit for the same period, Clarify that all Treasury Withdrawals already debited during the period count toward the limit
- finding: Deadline/expiry: Period begins at the start of Epoch 613, February 13, 2026, and ends at the close of Epoch 713, on or about July 3, 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets the Net Change Limit for the Cardano Treasury during Epochs 613-713 at 500,000,000 ada, equal to 500,000,000,000,000 lovelace.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only the cumulative amount debited from the Cardano Treasury by enacted Treasury Withdrawals recorded on the Cardano ledger during the period.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returns of Treasury-funded amounts, do not count toward or increase the Net Change Limit.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the Epochs 613-713 period count toward the 500,000,000 ada limit and are not reset, reversed, reopened, or reauthorized by this action.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that this Info action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer asserts that the existing 350,000,000 ada Net Change Limit has been a useful fiscal guardrail but is becoming practically constrained before mid-2027.
- missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has been a useful fiscal guardrail but is becoming practically constrained before mid-2027.
- missing: Independent evidence for: The proposer asserts that the Constitution does not limit DReps to a single Net Change Limit or prevent a newly agreed Net Change Limit from applying to the period.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets the Net Change Limit for the Cardano Treasury during Epochs 613-713 at 500,000,000 ada, equal to 500,000,000,000,000 lovelace." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer asserts that the existing 350,000,000 ada Net Change Limit has been a useful fiscal guardrail but is becoming practically constrained before mid-2027." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets the Net Change Limit for the Cardano Treasury during Epochs 613-713 at 500,000,000 ada, equal to 500,000,000,000,000 lovelace." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The claims provide clear intent and accounting mechanics, and the action does not directly authorize spending, but several high-materiality governance and constitutional assertions depend on external verification while the deterministic assessment marks risk review as thin and overall status incomplete. A small cautionary nudge is warranted because raising a treasury guardrail affects downside protection even though the proposal preserves per-withdrawal discretion.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- No DRep distribution available.
- Claims and evidence missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has been a useful fiscal guardrail but is becoming practically constrained before mid-2027.
- Claims and evidence missing: Independent evidence for: The proposer asserts that the Constitution does not limit DReps to a single Net Change Limit or prevent a newly agreed Net Change Limit from applying to the period.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `f83933cec24c217817bf82471f225496064af49e4e855b8bf9adf7e8c9ba45c3`
- snapshot_bundle_hash: `83afdf74ecfda431d2403ed5cb7f7d34b3165365c8ebcc215677444d433574ff`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

