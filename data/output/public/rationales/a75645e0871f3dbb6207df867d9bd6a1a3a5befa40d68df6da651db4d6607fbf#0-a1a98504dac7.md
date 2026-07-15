# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `-0.01`) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The document has clear intent and useful accounting detail for an Info action, but the central justification for raising the limit from 350,000,000 ada to 500,000,000 ada rests mainly on an asserted constraint rather than evidence of treasury capacity, committed obligations, or demand quality. Because this is signaling rather than a direct withdrawal, only a small cautionary negative nudge is warranted.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal’s core request was clear, but the case for raising the Net Change Limit from 350,000,000 ada to 500,000,000 ada did not meet the evidence threshold.

The action asked DReps to signal agreement to a 500,000,000 ada cap on total Treasury Withdrawals debited during Epochs 613-713, from February 13, 2026 to about July 3, 2027. It did not request a direct treasury withdrawal and stated that DReps would still review each future withdrawal separately. The proposal also clearly explained the accounting method: only lovelace removed by enacted Treasury Withdrawals would count, while Treasury inflows would not increase the limit.

Several basic claims were well-supported by the proposal document, including the size of the limit, the time period, the no-direct-withdrawal nature of the action, and the cumulative accounting approach. The weaker point was the justification for the increase: the claim that the existing 350,000,000 ada limit is becoming practically constrained before mid-2027 was asserted, but independent evidence was missing. The review also found thin risk evidence, with missing mitigation evidence and independent assurance.

This ABSTAIN is a conservative, evidence-based hold, not active opposition. A directional vote would be unblocked by stronger independent evidence showing why the current 350,000,000 ada limit is insufficient, how expected treasury demand supports a 500,000,000 ada cap, and what risk mitigations or assurances support the larger limit.

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
- finding: Requested: Info action to agree a new Net Change Limit for Cardano Treasury withdrawals for Epochs 613-713.
- finding: Recipient: not stated in document
- finding: Stated amount: 500,000,000 ada net change limit; no direct treasury withdrawal requested
- finding: Deliverables: Record DReps' agreement to a 500,000,000 ada cap on total Treasury Withdrawals debited during Epochs 613-713, Supersede any prior Net Change Limit for the same period, Apply the cumulative-sum accounting method in lovelace, excluding Treasury inflows
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only lovelace removed from the Treasury by enacted Treasury Withdrawals recorded on the Cardano ledger.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury inflows, including reserve and protocol allocations, transaction-fee allocations, refunds, and returns of Treasury-funded amounts, do not count toward or increase the limit.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the Epochs 613-713 period count toward the 500,000,000 ada cumulative limit.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that this Info action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has been useful but is becoming practically constrained before mid-2027.
- missing: Independent evidence for: The proposal claims that nothing in the Constitution limits DReps to a single Net Change Limit or prevents a newly agreed limit from applying to the same period.
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
- finding: Strongest NO: a material claim is unsupported — "The proposer asserts that the existing 350,000,000 ada Net Change Limit has been useful but is becoming practically constrained before mid-2027." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was -0.010 (display cap ±0.05) and had zero influence on the binding score: The document has clear intent and useful accounting detail for an Info action, but the central justification for raising the limit from 350,000,000 ada to 500,000,000 ada rests mainly on an asserted constraint rather than evidence of treasury capacity, committed obligations, or demand quality. Because this is signaling rather than a direct withdrawal, only a small cautionary negative nudge is warranted.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer asserts that the existing 350,000,000 ada Net Change Limit has been useful but is becoming practically constrained before mid-2027.
- Claims and evidence missing: Independent evidence for: The proposal claims that nothing in the Constitution limits DReps to a single Net Change Limit or prevents a newly agreed limit from applying to the same period.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `a1a98504dac77b5d0db4e78c1bc9b2d2585beaff66d478448a4ba006af701de1`
- snapshot_bundle_hash: `cdcd673d6e7962182ad40072f429912aea36ddd0fca05926c981e69f403a0ab6`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3d9c2c9681f9060eff076f9ca8f4e36a1ddb67a2`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

