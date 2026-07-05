# Rationale: gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
Recommendation: **ABSTAIN**
Score: `-0.07` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4875` | Readiness: `0.6`
> Reasoning layer (precomputed): The document is clear about the mechanics of the limit and its non-withdrawal effect, but the central justification for raising the cap from 350,000,000 ada to 500,000,000 ada rests mainly on asserted constrained room and future flexibility rather than evidence in the proposal. Because the action has treasury coordination effects and the assessment notes thin risk review, a small cautionary nudge is warranted without treating the Info action as an actual withdrawal.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s mechanics were clear, but the evidence did not meet the threshold for a directional vote. This is a conservative, evidence-based hold, not active opposition.

The action asked DReps to record agreement to a 500,000,000 ada Net Change Limit for the Cardano Treasury from Epoch 613 through Epoch 713. It was an InfoAction with no direct on-chain effect and did not authorize any Treasury Withdrawal. The proposal said the limit would apply to Treasury Withdrawals already debited in the period and future enacted withdrawals in the same period, and that it would supersede any prior Net Change Limit for those epochs.

Several core facts were well-supported in the proposal: the 500,000,000 ada amount, the Epoch 613-713 period, the fact that only Treasury outflows count against the limit, and the fact that this action does not itself withdraw funds. However, important parts of the case were thinner. Independent evidence was missing for the claim that this new limit supersedes the prior limit, and for the claim that the existing 350,000,000 ada limit is becoming practically constrained. The risk review was also thin, with mitigation evidence and independent assurance missing.

BEACN would need stronger replayable evidence for the supersession claim, stronger support for why the 350,000,000 ada limit is no longer sufficient, and clearer risk mitigation or independent assurance to move from this hold to a Yes or No vote.

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
- finding: Requested: Agree a new Net Change Limit for the Cardano Treasury for Epochs 613-713 via an Info action with no direct on-chain effect and no authorization of any Treasury Withdrawal.
- finding: Recipient: not stated in document
- finding: Stated amount: none requested; proposed net change limit is 500,000,000 ada
- finding: Deliverables: Record DReps' agreement to a 500,000,000 ada Net Change Limit for Epochs 613-713, Supersede any prior Net Change Limit for the same period, Apply the limit to all Treasury Withdrawals already debited during the period and future enacted Treasury Withdrawals during the period
- finding: Deadline/expiry: period ends at the close of Epoch 713, on or about July 3, 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713, on or about July 3, 2027.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only total lovelace removed from the Treasury by enacted Treasury Withdrawals recorded on the Cardano ledger, and does not count Treasury inflows.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the period count toward the 500,000,000 ada limit and remain valid without being reset, reversed, re-opened, or re-authorized by this action.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal states that this new limit supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer says the existing 350,000,000 ada Net Change Limit has been useful but practical room under it is becoming constrained.
- missing: Independent evidence for: The proposal states that this new limit supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- missing: Independent evidence for: The proposer says the existing 350,000,000 ada Net Change Limit has been useful but practical room under it is becoming constrained.
- missing: Independent evidence for: The proposer says increasing the limit preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed fiscal guardrail.
- missing: Independent evidence for: The proposal states that Yes votes exceeding 50% of active voting stake are sufficient to record DRep agreement to a Net Change Limit under TREASURY-01a.
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
- finding: Strongest NO: a material claim is unsupported — "The proposal states that this new limit supersedes any prior Net Change Limit for the same Epochs 613-713 period." — so cost or precedent may outweigh the benefit.
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
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The document is clear about the mechanics of the limit and its non-withdrawal effect, but the central justification for raising the cap from 350,000,000 ada to 500,000,000 ada rests mainly on asserted constrained room and future flexibility rather than evidence in the proposal. Because the action has treasury coordination effects and the assessment notes thin risk review, a small cautionary nudge is warranted without treating the Info action as an actual withdrawal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that this new limit supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- Claims and evidence missing: Independent evidence for: The proposer says the existing 350,000,000 ada Net Change Limit has been useful but practical room under it is becoming constrained.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `b7c9cd6537eebae2a17a19e67354e82041a786951e70295da10b5b87fedf3df6`
- snapshot_bundle_hash: `ee821eef0071fcac48f13082d5b2bfc6f5a77d6d8dd724a5ae3d136f26ff2477`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4419, "NO": 0.3491, "YES": 0.2091}`

