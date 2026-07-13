# Rationale: a75645e0871f3dbb6207df867d9bd6a1a3a5befa40d68df6da651db4d6607fbf#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `+0.0`) | Confidence: `0.4825` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal has clear intent, accounting mechanics, and governance use, and it explicitly states that it does not authorize spending; however, the core justification that remaining room is constrained and that 500,000,000 ada is the appropriate guardrail is mostly proposer-asserted, so the deterministic assessment appears to capture the main evidence limitations without needing an additional nudge.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the proposal did not meet the rule threshold for a directional vote: the core mechanics were reviewable, but important claims about why the higher Treasury limit is needed were not independently supported.

The action asks DReps to record agreement to a 500,000,000 ada Net Change Limit for Cardano Treasury withdrawals during Epochs 613-713, from February 13, 2026 to about July 3, 2027. It does not request a Treasury withdrawal, name a recipient, or directly authorize spending. The proposal says withdrawals already debited during the period would count toward the limit, and that the action would supersede any prior Net Change Limit for the same period.

The review found several claims well-supported in the proposal itself: the size of the limit, the epoch range, the fact that the cap applies only to cumulative lovelace removed from the Treasury by enacted withdrawals, and the statement that this Info action has no direct on-chain effect. However, the case for raising the limit was thinner. The claims that the existing 350,000,000 ada limit has become practically constrained, and that raising it to 500,000,000 ada preserves useful DRep discretion while maintaining a fiscal guardrail, were treated as proposer assertions without independent evidence.

This ABSTAIN is a conservative, evidence-based hold, not active opposition. A directional vote would be unblocked by independent evidence showing that the current 350,000,000 ada limit is actually constraining credible Treasury withdrawals, plus clearer mitigation or assurance around the governance and execution risks of raising the limit.

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
- finding: Stated amount: none requested; proposed net change limit is 500,000,000 ada
- finding: Deliverables: Record DRep agreement to a 500,000,000 ada Net Change Limit for the Cardano Treasury for Epochs 613-713, Supersede any prior Net Change Limit for the same period, Count all Treasury Withdrawals already debited during the period toward the limit
- finding: Deadline/expiry: Period begins at start of Epoch 613 on February 13, 2026 and ends at close of Epoch 713 on or about July 3, 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal sets a Net Change Limit of 500,000,000 ada, equal to 500,000,000,000,000 lovelace, for Cardano Treasury withdrawals during Epochs 613-713.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed period begins at the start of Epoch 613 on February 13, 2026 and ends at the close of Epoch 713 on or about July 3, 2027.
- finding: Claim (technical, supported_in_proposal, high materiality): The limit caps only the cumulative lovelace removed from the Treasury by enacted Treasury Withdrawals recorded on the Cardano ledger during the period.
- finding: Claim (economic, supported_in_proposal, medium materiality): Treasury inflows, including reserve and protocol allocations, fee allocations, refunds, and returns of funded amounts, do not count toward or increase the proposed limit.
- finding: Claim (governance, supported_in_proposal, high materiality): Treasury Withdrawals already debited during the period count toward the 500,000,000 ada cumulative limit and are not reset, reversed, reopened, or re-authorized by this action.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained while still serving as a useful fiscal guardrail.
- missing: Independent evidence for: The proposal states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained while still serving as a useful fiscal guardrail.
- missing: Independent evidence for: The proposal states that raising the limit to 500,000,000 ada preserves DRep ability to consider credible Treasury Withdrawals while maintaining a fixed guardrail and simple accounting.
- missing: Independent evidence for: The proposal states that Yes votes exceeding 50% of active voting stake record DRep agreement to the Net Change Limit under TREASURY-01a.
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
- finding: Strongest NO: a material claim is unsupported — "The proposal states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained while still serving as a useful fiscal guardrail." — so cost or precedent may outweigh the benefit.
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
- No additional inference.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that the existing 350,000,000 ada Net Change Limit for Epochs 613-713 has become practically constrained while still serving as a useful fiscal guardrail.
- Claims and evidence missing: Independent evidence for: The proposal states that raising the limit to 500,000,000 ada preserves DRep ability to consider credible Treasury Withdrawals while maintaining a fixed guardrail and simple accounting.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `16cd89bd952060cea9eb6447bcf4b653a4f92f628e6efc8861a344d549275a75`
- snapshot_bundle_hash: `362796a7bc59f925c53f6c14601ed23d4dd1386e031c33b6a78d3efbe3ef4050`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4406, "NO": 0.3297, "YES": 0.2297}`

