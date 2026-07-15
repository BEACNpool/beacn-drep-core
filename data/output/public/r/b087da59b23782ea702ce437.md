# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The document clearly states intent and accounting mechanics for an Info action, but the core justification for raising the Treasury guardrail is mostly asserted rather than evidenced, and the deterministic assessment flags risk review as thin and overall status as incomplete. Under the doctrine, a cautious negative nudge is warranted because treasury stewardship and evidence quality weigh more heavily than preserving spending flexibility.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s core request was clear, but the evidence threshold for a directional vote was not met. This is a conservative, evidence-based hold, not active opposition.

The action asked DReps to record agreement to a new Net Change Limit of 500,000,000 ada for Cardano Treasury withdrawals during Epochs 613 through 713, ending around July 3, 2027. The proposal says this limit would cap only withdrawals recorded on-chain, count withdrawals already debited during the period, supersede the prior 350,000,000 ada limit, and have no direct on-chain effect or authority to approve any Treasury withdrawal.

Several basic claims were well-supported by the pinned proposal document: the amount, the period, the accounting mechanics, and the fact that this Info action does not itself authorize spending. However, important parts of the case were mostly asserted rather than independently evidenced, especially the claim that the existing 350,000,000 ada guardrail is becoming practically constrained before mid-2027 and the claim about superseding the prior limit. The review also found the claims-and-evidence section thin, with execution risk unknown and missing mitigation evidence and independent assurance.

The strongest case for voting yes is that the proposal clearly defines a 500,000,000 ada Treasury withdrawal cap and explains how it would work. The strongest reason to hold back is that Treasury stewardship requires stronger public evidence when raising a fiscal guardrail. A directional vote would be unblocked by independent, replayable evidence supporting the need to raise the limit, clearer support for how the prior limit is superseded, and a stronger risk review with mitigation evidence and independent assurance.

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
- finding: Requested: Record DRep agreement to a new Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Recipient: not stated in document
- finding: Stated amount: 500,000,000
- finding: Deliverables: Set a fixed cap of 500,000,000 ada on total Treasury withdrawals debited during Epochs 613-713., Supersede any prior Net Change Limit for the same period., Count all Treasury withdrawals already debited during the period toward the limit., Clarify that the Info action has no direct on-chain effect and does not authorize any Treasury withdrawal.
- finding: Deadline/expiry: close of Epoch 713, on or about July 3, 2027
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal sets a new Net Change Limit of 500,000,000 ada for the Cardano Treasury for Epochs 613 through 713.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only Treasury withdrawals debited from the Cardano Treasury and recorded on the Cardano ledger, while Treasury inflows do not count or increase the limit.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury withdrawals already debited during the period count toward the 500,000,000 ada cumulative limit and remain valid.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal states that it supersedes any prior Net Change Limit for the same period, including the previously agreed 350,000,000 ada limit.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer asserts that the existing 350,000,000 ada Net Change Limit has served as a useful fiscal guardrail but is becoming practically constrained before mid-2027.
- missing: Independent evidence for: The proposal states that it supersedes any prior Net Change Limit for the same period, including the previously agreed 350,000,000 ada limit.
- missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has served as a useful fiscal guardrail but is becoming practically constrained before mid-2027.
- missing: Independent evidence for: The proposal states that agreeing the new limit preserves DReps' ability to consider credible Treasury withdrawals on their merits while retaining a fixed guardrail.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada for the Cardano Treasury for Epochs 613 through 713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that it supersedes any prior Net Change Limit for the same period, including the previously agreed 350,000,000 ada limit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada for the Cardano Treasury for Epochs 613 through 713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The document clearly states intent and accounting mechanics for an Info action, but the core justification for raising the Treasury guardrail is mostly asserted rather than evidenced, and the deterministic assessment flags risk review as thin and overall status as incomplete. Under the doctrine, a cautious negative nudge is warranted because treasury stewardship and evidence quality weigh more heavily than preserving spending flexibility.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that it supersedes any prior Net Change Limit for the same period, including the previously agreed 350,000,000 ada limit.
- Claims and evidence missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has served as a useful fiscal guardrail but is becoming practically constrained before mid-2027.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `9b4ceddaedfe67413177d49d433dc2f0601a9cb4cf37db7331490585418d5e88`
- snapshot_bundle_hash: `b90cebada62a60f46e377ab1e378f2503e4f874dfc75a969ac1ed0c2b3353a12`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `afd630a34be9d7440e2fac020ac552cde501098f`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

