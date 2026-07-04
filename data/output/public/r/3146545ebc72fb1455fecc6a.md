# Rationale: gov_action15atytcy8ru7mkcs8m7r8mx7k5x36t0h6grtgmak6v5wmf4nq07lsqhakceq
Recommendation: **ABSTAIN**
Score: `-0.07` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4375` | Readiness: `0.0`
> Reasoning layer (precomputed): The action improves governance clarity by specifying the cap, period, ledger-based accounting, and non-authorization effect, but the central justification for raising the existing limit is thinly supported and the deterministic assessment marks risk review as thin and overall status incomplete. Under treasury stewardship and evidence quality principles, that warrants a small cautionary negative nudge rather than a positive signal.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s core mechanics were clear, but the evidence did not meet the threshold for a directional vote. This is a conservative, evidence-based hold, not active opposition.

The action asked DReps to record agreement to a new 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713, from February 13, 2026 through about July 3, 2027. The proposal was clear that this is an InfoAction with no direct on-chain effect and that it does not authorize any Treasury withdrawal. It also clearly stated that withdrawals already debited during the period would count toward the limit, and that the cap applies only to lovelace removed from the Treasury through enacted Treasury withdrawals.

Several important claims were supported by the proposal itself, including the amount, period, ledger-based accounting, and non-authorization effect. However, the main justification for raising the prior 350,000,000 ada limit was thinner: the claims that room under the existing limit is becoming constrained, and that a 500,000,000 ada limit would preserve DReps’ ability to consider credible withdrawals while keeping a fixed guardrail, were proposer assertions without independent supporting evidence. The review also found the risk review thin, with missing mitigation evidence and independent assurance, and confidence was reduced by a flag score.

BEACN would need replayable independent evidence showing that the current 350,000,000 ada limit is materially constraining credible Treasury withdrawal review, plus clearer mitigation evidence or independent assurance around the governance and execution risks, before moving from abstention to a YES or NO vote.

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
- finding: Requested: Info action to record DRep agreement to a new Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Recipient: not stated in document
- finding: Stated amount: none requested; proposed net change limit is 500,000,000 ada
- finding: Deliverables: Set or signal agreement to a 500,000,000 ada cap on total Treasury withdrawals debited during Epochs 613-713, Supersede any prior Net Change Limit for the same period, Count all Treasury withdrawals already debited during the period toward the limit, Clarify that the action has no direct on-chain effect and does not authorize any Treasury withdrawal
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Epochs 613-713.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed limit caps only lovelace removed from the Cardano Treasury through enacted Treasury Withdrawals recorded on the Cardano ledger during the period.
- finding: Claim (technical, supported_in_proposal, medium materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returned Treasury-funded amounts, do not count toward or increase the proposed limit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states that all Treasury Withdrawals already debited during Epochs 613-713 count toward the 500,000,000 ada cumulative limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that this Info action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer says the existing 350,000,000 ada Net Change Limit has been a useful fiscal guardrail but that practical room under it is becoming constrained.
- missing: Independent evidence for: The proposer says the existing 350,000,000 ada Net Change Limit has been a useful fiscal guardrail but that practical room under it is becoming constrained.
- missing: Independent evidence for: The proposer says increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals on their merits while keeping a fixed guardrail and simple accounting.
- missing: Independent evidence for: The proposal claims nothing in the Constitution limits DReps to a single Net Change Limit or prevents a newly agreed Net Change Limit from applying to the same period.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer says the existing 350,000,000 ada Net Change Limit has been a useful fiscal guardrail but that practical room under it is becoming constrained." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Epochs 613-713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The action improves governance clarity by specifying the cap, period, ledger-based accounting, and non-authorization effect, but the central justification for raising the existing limit is thinly supported and the deterministic assessment marks risk review as thin and overall status incomplete. Under treasury stewardship and evidence quality principles, that warrants a small cautionary negative nudge rather than a positive signal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer says the existing 350,000,000 ada Net Change Limit has been a useful fiscal guardrail but that practical room under it is becoming constrained.
- Claims and evidence missing: Independent evidence for: The proposer says increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals on their merits while keeping a fixed guardrail and simple accounting.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `aedc564753ef33d6f14425969532d5c1b3bc714efd8fb17d64c6e009b5c7bad4`
- snapshot_bundle_hash: `0653cc0481f8fdbabe9c3fd753d0799c530bbe064b156727ba5460ececd6acc7`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1217`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4294, "NO": 0.3553, "YES": 0.2153}`

