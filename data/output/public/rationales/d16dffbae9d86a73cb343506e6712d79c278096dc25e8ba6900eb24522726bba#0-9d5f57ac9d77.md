# Rationale: d16dffbae9d86a73cb343506e6712d79c278096dc25e8ba6900eb24522726bba#0
Recommendation: **ABSTAIN**
Score: `-0.05` (raw `-0.05` + doctrine-LLM nudge `+0.005`) | Confidence: `0.4325` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a info action: 6 well-supported claim(s), 1 unsupported high-materiality claim(s). Net bounded adjustment +0.005 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on 2025 Net Change Limit Extension. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: 2025 Net Change Limit Extension. The strongest grounded claim is: The Cardano Community adopted the 2025 Net Change Limit (NCL) on 24 April 2025, which defined the maximum amount of lovelace that could be withdrawn from the Cardano Treasury from the start of Epoch 532 until the conclusion of Epoch 604.

A material claim remains proposer-asserted or thinly supported: We seek to have this Governance Action adopted so that the management of the Cardano Treasury will not be disrupted by the expiration of the current NCL. Reason code: DREP_DISTRIBUTION_MISSING.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 597
- finding: Expires after epoch: 604
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: 2025 Net Change Limit Extension
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: The Cardano Community adopted the 2025 Net Change Limit (NCL) on 24 April 2025, which defined the maximum amount of lovelace that could be withdrawn from the Cardano Treasury from the start of Epoch 532 until the conclusion of Epoch 604., Because the Cardano Constitution does not allow withdrawals from the Treasury that would violate the established NCL, this "2025 Net Change Limit Extension" serves the purpose of extending the previously established Net Change Limit for an additional eight..., We seek to have this Governance Action adopted so that the management of the Cardano Treasury will not be disrupted by the expiration of the current NCL., Withdrawals from the Cardano Blockchain Treasury that would cause the Treasury balance to violate the applicable NCL are not permitted under Article IV, Section 3 of the Cardano Constitution and the Treasury Guardrails.
- finding: Deadline/expiry: not stated in document
- finding: Claim (adoption, supported_in_proposal, high materiality): The Cardano Community adopted the 2025 Net Change Limit (NCL) on 24 April 2025, which defined the maximum amount of lovelace that could be withdrawn from the Cardano Treasury from the start of Epoch 532 until the conclusion of Epoch 604.
- finding: Claim (governance, supported_in_proposal, high materiality): Because the Cardano Constitution does not allow withdrawals from the Treasury that would violate the established NCL, this "2025 Net Change Limit Extension" serves the purpose of extending the previously established Net Change Limit for an additional eight...
- finding: Claim (governance, proposer_asserted, high materiality): We seek to have this Governance Action adopted so that the management of the Cardano Treasury will not be disrupted by the expiration of the current NCL.
- finding: Claim (governance, supported_in_proposal, high materiality): Withdrawals from the Cardano Blockchain Treasury that would cause the Treasury balance to violate the applicable NCL are not permitted under Article IV, Section 3 of the Cardano Constitution and the Treasury Guardrails.
- finding: Claim (governance, supported_in_proposal, high materiality): Because the "2025 Net Change Limit" explicitly states that its term ends at the close of Epoch 604, any Treasury Withdrawal Governance Action (TWGA) that relies on that NCL must be both ratified and enacted before that point.
- finding: Claim (governance, supported_in_proposal, high materiality): Given the one-epoch enactment delay for Treasury Withdrawals, where a Governance Action that is ratified at one Epoch boundary is only enacted and paid out at the next Epoch boundary, the last Epoch in which such a TWGA may validly be ratified is Epoch 603...
- missing: Independent evidence for: We seek to have this Governance Action adopted so that the management of the Cardano Treasury will not be disrupted by the expiration of the current NCL.
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
- finding: Strongest YES: the proposal substantiates "The Cardano Community adopted the 2025 Net Change Limit (NCL) on 24 April 2025, which defined the maximum amount of lovelace that could be withdrawn from the Cardano Treasury from the start of Epoch 532 until the conclusion of Epoch 604." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "We seek to have this Governance Action adopted so that the management of the Cardano Treasury will not be disrupted by the expiration of the current NCL." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The Cardano Community adopted the 2025 Net Change Limit (NCL) on 24 April 2025, which defined the maximum amount of lovelace that could be withdrawn from the Cardano Treasury from the start of Epoch 532 until the conclusion of Epoch 604." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by +0.005 (clamped to ±0.05): Doctrine-aware offline lean for a info action: 6 well-supported claim(s), 1 unsupported high-materiality claim(s). Net bounded adjustment +0.005 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- No DRep distribution available.
- Claims and evidence missing: Independent evidence for: We seek to have this Governance Action adopted so that the management of the Cardano Treasury will not be disrupted by the expiration of the current NCL.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `9d5f57ac9d77539780d1200baf646fc69f4b5a02b03ce218ef06b5a4b4c4d421`
- snapshot_bundle_hash: `196661fee89972c25f67cde0bed528f5a491eb5842ffc8655998c552ef2de268`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `13`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4281, "NO": 0.3359, "YES": 0.2359}`

