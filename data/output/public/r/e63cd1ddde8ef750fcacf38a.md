# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The document provides clear intent, accounting mechanics, and states that the action does not itself authorize spending, which supports governance clarity. However, the key justification for increasing the cap from 350,000,000 ada to 500,000,000 ada is mostly asserted rather than evidenced, so treasury stewardship and evidence quality justify a small cautionary negative nudge.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s main request is clear, but the evidence did not meet the threshold for a confident directional vote. This is a conservative, evidence-based hold, not active opposition.

The action asks DReps to agree to a new Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713. It does not request a treasury withdrawal and states that it has no direct on-chain effect. The proposal clearly explains that only Treasury Withdrawals debited from the Treasury and recorded on-chain during the period count toward the limit, that inflows do not increase the limit, and that withdrawals already debited since Epoch 613 count against it.

The well-supported parts are the basic mechanics: the amount, the epoch range, the accounting treatment, and the fact that this action does not itself authorize spending. The weaker parts are the justification for raising the limit from the existing 350,000,000 ada to 500,000,000 ada, the claim that practical room under the existing limit is becoming constrained, and the claim that this action supersedes the prior limit. Those points were mostly asserted rather than independently evidenced.

The review found a pinned, replayable anchor document and a credible strongest-YES case, but confidence was reduced by a flag score, thin claims-and-evidence status, unknown execution risk, and missing mitigation or independent assurance evidence. A directional vote would be unblocked by independent evidence showing why the current 350,000,000 ada limit is constrained, support for the supersession claim, and clearer risk mitigation or assurance for the proposed change.

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
- finding: Requested: Info action to agree a new Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Recipient: not stated in document
- finding: Stated amount: 500,000,000 ada net change limit; no treasury withdrawal requested
- finding: Deliverables: Set a fixed cap on total ada removed from the Treasury through Treasury Withdrawals during the period., Apply the limit from the start of Epoch 613 through the close of Epoch 713., Count Treasury Withdrawals already debited during the period toward the limit., Supersede any prior Net Change Limit for the same period., Record DRep agreement if Yes votes exceed 50% of active voting stake.
- finding: Deadline/expiry: Close of Epoch 713, stated as on or about July 3, 2027
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal sets a new Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed limit caps only Treasury Withdrawals debited from the Cardano Treasury and recorded on the Cardano ledger during the period.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returned Treasury-funded amounts, do not count toward or increase the proposed limit.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the period beginning at Epoch 613 count toward the 500,000,000 ada cumulative limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that it has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal states that it supersedes any prior Net Change Limit for the same Epochs 613-713 period, including the existing 350,000,000 ada limit.
- missing: Independent evidence for: The proposal states that it supersedes any prior Net Change Limit for the same Epochs 613-713 period, including the existing 350,000,000 ada limit.
- missing: Independent evidence for: The proposer asserts that practical room under the existing 350,000,000 ada limit is becoming constrained.
- missing: Independent evidence for: The proposer asserts that a 500,000,000 ada limit preserves DRep ability to consider credible Treasury Withdrawals on their merits while retaining a clear fixed fiscal guardrail.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a new Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that it supersedes any prior Net Change Limit for the same Epochs 613-713 period, including the existing 350,000,000 ada limit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a new Cardano Treasury Net Change Limit of 500,000,000 ada for Epochs 613-713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The document provides clear intent, accounting mechanics, and states that the action does not itself authorize spending, which supports governance clarity. However, the key justification for increasing the cap from 350,000,000 ada to 500,000,000 ada is mostly asserted rather than evidenced, so treasury stewardship and evidence quality justify a small cautionary negative nudge.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that it supersedes any prior Net Change Limit for the same Epochs 613-713 period, including the existing 350,000,000 ada limit.
- Claims and evidence missing: Independent evidence for: The proposer asserts that practical room under the existing 350,000,000 ada limit is becoming constrained.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `4cbb04ea256de936dcc7c66b7bd674b2b2c39fd378bc816e5f94c645ac8e7410`
- snapshot_bundle_hash: `2da31df1546f18701e03b548da3d6ec57024c9f22145b0ccd8e0658f390696fc`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

