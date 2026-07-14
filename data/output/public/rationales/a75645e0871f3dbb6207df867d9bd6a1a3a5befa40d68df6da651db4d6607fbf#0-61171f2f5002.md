# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal gives clear accounting mechanics and governance intent, which supports signal quality, but the key justification for raising the cap is largely asserted rather than evidenced and directly implicates treasury stewardship. A small cautionary nudge is warranted because the doctrine prioritizes downside protection and evidence quality over plausible ecosystem spending flexibility.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s core mechanics were clear, but the evidence did not meet the threshold for a directional vote on raising the Treasury net change limit.

The action asked DReps to agree to a 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713, from February 13, 2026 to about July 3, 2027. It did not request a direct Treasury withdrawal and would have no direct on-chain effect. The proposal clearly supported the amount, the accounting method, the exclusion of Treasury inflows, and the fact that already-debited withdrawals during the period would count toward the cumulative limit.

The weaker part was the justification and assurance around the change. The claim that the new limit supersedes any prior limit for the same period lacked independent evidence. The claim that the existing 350,000,000 ada limit is becoming practically constrained was also proposer-asserted rather than independently evidenced. The risk review was thin, with execution risk unknown and missing mitigation evidence or independent assurance.

This abstention is a conservative, evidence-based hold, not active opposition. A directional vote would be unblocked by stronger replayable evidence showing that the prior limit is being superseded as claimed, independent support for why the current limit is insufficient, and clearer mitigation or assurance around the governance and execution risks.

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
- finding: Stated amount: 500,000,000 ada net change limit; no direct treasury withdrawal requested
- finding: Deliverables: Record DRep agreement to a 500,000,000 ada cap on total Treasury withdrawals debited during Epochs 613-713, Supersede any prior Net Change Limit for the same period, Apply the cumulative-sum accounting method in lovelace and exclude Treasury inflows
- finding: Deadline/expiry: Period begins at start of Epoch 613 on February 13, 2026 and ends at close of Epoch 713 on or about July 3, 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Epochs 613-713.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposed limit caps only total lovelace removed from the Cardano Treasury through enacted Treasury Withdrawals during the period and does not count Treasury inflows.
- finding: Claim (governance, proposer_asserted, high materiality): The proposed limit supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the period count toward the proposed 500,000,000 ada cumulative limit and remain valid.
- finding: Claim (governance, supported_in_proposal, high materiality): The action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer states that the existing 350,000,000 ada Net Change Limit has been useful but that practical room under it is becoming constrained.
- missing: Independent evidence for: The proposed limit supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- missing: Independent evidence for: The proposer states that the existing 350,000,000 ada Net Change Limit has been useful but that practical room under it is becoming constrained.
- missing: Independent evidence for: The proposer states that increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals while keeping a fixed fiscal guardrail.
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
- finding: Strongest NO: a material claim is unsupported — "The proposed limit supersedes any prior Net Change Limit for the same Epochs 613-713 period." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal gives clear accounting mechanics and governance intent, which supports signal quality, but the key justification for raising the cap is largely asserted rather than evidenced and directly implicates treasury stewardship. A small cautionary nudge is warranted because the doctrine prioritizes downside protection and evidence quality over plausible ecosystem spending flexibility.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposed limit supersedes any prior Net Change Limit for the same Epochs 613-713 period.
- Claims and evidence missing: Independent evidence for: The proposer states that the existing 350,000,000 ada Net Change Limit has been useful but that practical room under it is becoming constrained.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `61171f2f5002e20d30a965d44082e06b28694f7aa748ea3b9d64c8443944ac52`
- snapshot_bundle_hash: `a62078c87dbb186ecb874f13cccb45e42feaf06937f107ca167ab44b5d800946`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

