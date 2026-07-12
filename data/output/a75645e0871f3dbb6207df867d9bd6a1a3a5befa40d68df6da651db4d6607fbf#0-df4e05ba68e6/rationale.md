# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.0` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal did not meet the evidence threshold for a directional vote. The action clearly states a proposed Net Change Limit of 500,000,000 ada for Cardano Treasury withdrawals during Epochs 613-713, but several material claims behind that change were asserted rather than independently supported.

The proposal asks DReps to agree to a new Treasury Net Change Limit for the period from Epoch 613, beginning February 13, 2026, through the close of Epoch 713, on or about July 3, 2027. It says the limit would cap only lovelace removed from the Treasury by enacted Treasury Withdrawals, that inflows would not increase the cap, and that withdrawals already debited during the period would count toward the 500,000,000 ada limit. It also makes clear that this Info Action has no direct on-chain effect and does not itself authorize any Treasury Withdrawal.

The strongest supported case for Yes is that the core request and accounting rules are clear, the anchor document is pinned and replayable, and the action is presented as a governance signal rather than a direct spend. The weaker parts are also material: the claim that this supersedes the prior 350,000,000 ada limit, the claim that room under that prior limit is becoming constrained through mid-2027, and the threshold interpretation for recording DRep agreement were not backed by enough independent evidence in the review. The risk review was also thin, with execution risk unknown and missing mitigation or independent assurance evidence.

This ABSTAIN is a conservative, evidence-based hold, not active opposition. A directional vote would be unblocked by replayable independent evidence showing how this action supersedes the prior limit, evidence that the existing 350,000,000 ada limit is becoming practically constrained, and clearer mitigation or assurance around the governance and execution risks.

## Review Tree
- overall_status: `blocked`

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
- finding: Stated amount: not stated in document
- finding: Deliverables: Set a Net Change Limit of 500,000,000 ada for the Cardano Treasury for Epochs 613-713, Record DRep agreement when Yes votes exceed 50% of active voting stake, Clarify that the action has no direct on-chain effect and does not authorize any Treasury Withdrawal
- finding: Deadline/expiry: Period begins at the start of Epoch 613 (February 13, 2026) and ends at the close of Epoch 713 (on or about July 3, 2027)
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713, on or about July 3, 2027.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only lovelace removed from the Cardano Treasury by enacted Treasury Withdrawals recorded on the Cardano ledger.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returned Treasury-funded amounts, do not count toward or increase the limit.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the period count toward the 500,000,000 ada limit and are not reset, reversed, reopened, or reauthorized by this action.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal supersedes any prior Net Change Limit for the same Epochs 613-713 period, including the previously agreed 350,000,000 ada limit referenced in the motivation.
- missing: Independent evidence for: The proposal supersedes any prior Net Change Limit for the same Epochs 613-713 period, including the previously agreed 350,000,000 ada limit referenced in the motivation.
- missing: Independent evidence for: The existing 350,000,000 ada Net Change Limit has served as a useful fiscal guardrail, but practical room under it is becoming constrained through mid-2027.
- missing: Independent evidence for: The action records DRep agreement when Yes votes exceed 50% of active voting stake, identified as the TREASURY-01a threshold for agreeing a Net Change Limit.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal supersedes any prior Net Change Limit for the same Epochs 613-713 period, including the previously agreed 350,000,000 ada limit referenced in the motivation." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: evidence is too thin for a directional vote while 1 blocker(s) remain open.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: freshness gate failed
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Data freshness check failed: data is 91633s old, max allowed is 21600s
- Intake: Action type: InfoAction
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce reliable recommendation with stale data.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- All scoring suspended until fresh data is available.
- Claims and evidence missing: Independent evidence for: The proposal supersedes any prior Net Change Limit for the same Epochs 613-713 period, including the previously agreed 350,000,000 ada limit referenced in the motivation.
- Claims and evidence missing: Independent evidence for: The existing 350,000,000 ada Net Change Limit has served as a useful fiscal guardrail, but practical room under it is becoming constrained through mid-2027.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: freshness gate failed
- Synthesis status is blocked.

## Reproducibility
- input_hash: `df4e05ba68e67c8d82673aca9c217a4fa7671295f35844e8cee0612ae61fb434`
- snapshot_bundle_hash: `eb928163c0167360c6ea85b3e1d4c72177d656977fa97ac1040dd166be6318fc`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `eec0908e48c56be13e86e06ac5d9440d0cac813a`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `91633`
- uncertainty_band: `LOW`
- evidence_depth_score: `1`
- decision_probs: `{"ABSTAIN": 0.32, "NO": 0.34, "YES": 0.34}`

- **DATA STALE**: age exceeded threshold

