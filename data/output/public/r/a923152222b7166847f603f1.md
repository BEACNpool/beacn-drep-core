# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4825` | Readiness: `0.5`
> Reasoning layer (precomputed): The proposal is clear about the intended accounting rule and emphasizes that it does not directly authorize withdrawals, which supports governance clarity; however, the core need for raising the limit from 350,000,000 ada to 500,000,000 ada is asserted rather than evidenced in the supplied claims, so a small cautionary nudge is warranted for treasury stewardship.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was missing DRep distribution data, so the system did not have enough confidence to make a directional vote. This is a conservative, evidence-based hold, not an objection to the idea of a Treasury limit.

The action asks DReps to agree to a new 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals from the start of Epoch 613 on February 13, 2026 through the close of Epoch 713 on or about July 3, 2027. The proposal says this would supersede any prior limit for the same period, that withdrawals already debited during the period would count toward the cap, and that the action itself has no direct on-chain effect and does not authorize any Treasury Withdrawal.

Several core details were well supported by the proposal document: the 500,000,000 ada limit, the time window, the accounting rule that only Treasury outflows count, the treatment of already debited withdrawals, and the fact that this is an InfoAction rather than a direct withdrawal. But important justification claims were not independently evidenced in the supplied review, including the claim that the existing 350,000,000 ada limit has become practically constrained and the claim that raising it to 500,000,000 ada preserves DReps’ ability to consider credible withdrawals while keeping a fixed guardrail.

The review gates were mixed. The anchor document was pinned and replayable, and the strongest YES case cleared the basic evidence gates on what the proposal would do. However, claims and evidence were thin, execution risk was unknown, mitigation evidence and independent assurance were missing, and a flag score reduced confidence. A directional vote would be unblocked by DRep distribution data, independent evidence for the need to raise the limit, and stronger risk mitigation or assurance evidence.

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
- finding: Stated amount: none requested; proposes a 500,000,000 ada net change limit
- finding: Deliverables: Record DReps' agreement to a 500,000,000 ada fixed cap on total Treasury Withdrawals debited during Epochs 613-713, Supersede any prior Net Change Limit for the same period, Clarify that prior withdrawals already debited during the period count toward the limit
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed limit applies from the start of Epoch 613 on February 13, 2026 through the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (technical, supported_in_proposal, high materiality): The Net Change Limit caps only amounts removed from the Treasury by enacted Treasury Withdrawals recorded on the Cardano ledger, and does not count Treasury inflows.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the period count toward the proposed 500,000,000 ada limit and are not reset, reversed, reopened, or reauthorized by this action.
- finding: Claim (governance, supported_in_proposal, high materiality): The document says this action has no direct on-chain effect and does not authorize any Treasury Withdrawal.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained as its window runs into mid-2027.
- missing: Independent evidence for: The proposer states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained as its window runs into mid-2027.
- missing: Independent evidence for: The proposer claims that increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed fiscal guardrail.
- missing: Independent evidence for: The document states that Yes votes exceeding 50% of active voting stake are the TREASURY-01a threshold for agreeing a Net Change Limit.
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
- finding: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained as its window runs into mid-2027." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal sets a new Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal is clear about the intended accounting rule and emphasizes that it does not directly authorize withdrawals, which supports governance clarity; however, the core need for raising the limit from 350,000,000 ada to 500,000,000 ada is asserted rather than evidenced in the supplied claims, so a small cautionary nudge is warranted for treasury stewardship.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- No DRep distribution available.
- Claims and evidence missing: Independent evidence for: The proposer states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained as its window runs into mid-2027.
- Claims and evidence missing: Independent evidence for: The proposer claims that increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals on their merits while retaining a fixed fiscal guardrail.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `635afb8f808b3f90044ebbea661b2ca817a0a0d80ea8b4aa837f40d6d07672c9`
- snapshot_bundle_hash: `936f109633afda585d9dbbb68c6da07df2113872ad5c710c258862809283b319`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

