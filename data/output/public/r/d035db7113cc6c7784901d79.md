# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `-0.02`) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The action has clear intent and useful accounting definitions, but it materially raises a treasury guardrail while key justifications such as constrained remaining room and the constitutional ability to supersede a prior limit are mostly asserted rather than evidenced in the document.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal raises the Treasury Net Change Limit from 350,000,000 ada to 500,000,000 ada, but the key justification for why that increase is needed was mostly asserted rather than independently evidenced.

The action asked DReps to agree to a fixed 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713. It does not authorize any Treasury Withdrawal, name a recipient, or approve any spending by itself. The proposal clearly states that only enacted Treasury withdrawals debited on-chain count toward the cap, that Treasury inflows do not increase the limit, and that withdrawals already debited in the period count toward the same 500,000,000 ada total.

Several core mechanics were well supported by the proposal document, including the amount, the time period, the accounting treatment, and the fact that this is an InfoAction with no direct on-chain spending effect. The weaker part was the policy case: the claims that the existing 350,000,000 ada limit is becoming constrained, and that raising it preserves room for credible withdrawals while maintaining an appropriate guardrail, were not backed by enough independent evidence. The review also found thin risk evidence, with missing mitigation evidence and independent assurance.

This ABSTAIN is a conservative, evidence-based hold, not active opposition. A directional vote would be unblocked by stronger public evidence showing the current limit is practically constrained, why 500,000,000 ada is the right replacement guardrail for Epochs 613-713, and what mitigations or independent assurance address the governance and execution risks of raising the limit.

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
- finding: Stated amount: none; the document states this action does not authorize any Treasury Withdrawal
- finding: Deliverables: Set a fixed Net Change Limit of 500,000,000 ada for Treasury Withdrawals during Epochs 613-713., Record DRep agreement that the new limit supersedes any prior Net Change Limit for the same period., Count all Treasury Withdrawals already debited during the period toward the 500,000,000 ada limit.
- finding: Deadline/expiry: Period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (technical, supported_in_proposal, high materiality): The limit caps only the cumulative amount debited from the Cardano Treasury through enacted Treasury Withdrawals recorded on the Cardano ledger during the period.
- finding: Claim (economic, supported_in_proposal, high materiality): Treasury inflows, including reserve allocations, protocol allocations, transaction-fee allocations, refunds, and returns of Treasury-funded amounts, do not count toward or increase the limit.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the period count toward the 500,000,000 ada limit and are not reset, reversed, reopened, or re-authorized by this action.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal says the existing 350,000,000 ada Net Change Limit has been useful but that practical room under it is becoming constrained.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal says increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals while maintaining a fixed guardrail and simple accounting.
- missing: Independent evidence for: The proposal says the existing 350,000,000 ada Net Change Limit has been useful but that practical room under it is becoming constrained.
- missing: Independent evidence for: The proposal says increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals while maintaining a fixed guardrail and simple accounting.
- missing: Independent evidence for: The proposal asserts that Yes votes exceeding 50% of active voting stake are sufficient for DReps to agree a Net Change Limit under TREASURY-01a.
- missing: Independent evidence for: The proposal asserts that nothing in the Constitution limits DReps to a single Net Change Limit or prevents a newly agreed limit from applying to the same period.
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
- finding: Strongest NO: a material claim is unsupported — "The proposal says the existing 350,000,000 ada Net Change Limit has been useful but that practical room under it is becoming constrained." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The action has clear intent and useful accounting definitions, but it materially raises a treasury guardrail while key justifications such as constrained remaining room and the constitutional ability to supersede a prior limit are mostly asserted rather than evidenced in the document.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal says the existing 350,000,000 ada Net Change Limit has been useful but that practical room under it is becoming constrained.
- Claims and evidence missing: Independent evidence for: The proposal says increasing the limit to 500,000,000 ada preserves DReps' ability to consider credible Treasury Withdrawals while maintaining a fixed guardrail and simple accounting.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `24b029f06dcbdaee286bf208be9a39a1e6c689cf6ce3e29ecce7ac4fd0d31078`
- snapshot_bundle_hash: `6be63481cb09eb1d317d2a59d4b0694b49ea847a66208e8e5e33eeaa5039b412`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `a650e5f55d3662a45d71b3a19d5301fd64c2bbee`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

