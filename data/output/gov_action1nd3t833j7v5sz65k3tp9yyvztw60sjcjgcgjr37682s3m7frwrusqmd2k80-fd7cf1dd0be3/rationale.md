# Rationale: gov_action1nd3t833j7v5sz65k3tp9yyvztw60sjcjgcgjr37682s3m7frwrusqmd2k80
Recommendation: **ABSTAIN**
Score: `0.04` (raw `0.01` + doctrine-LLM nudge `+0.03`) | Confidence: `0.58` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a info action: 8 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on 2025 Net Change Limit. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: 2025 Net Change Limit. The strongest grounded claim is: The Cardano Constitution requires the establishment of a Net Change Limit, which defines the maximum amount of lovelace that can be withdrawn from the treasury during an outlined period of time.

Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 547
- finding: Expires after epoch: 554
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: not required
- finding: Requested: 2025 Net Change Limit
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: The Cardano Constitution requires the establishment of a Net Change Limit, which defines the maximum amount of lovelace that can be withdrawn from the treasury during an outlined period of time., This governance action serves as an opportunity for all governance stakeholders to formally express their positions regarding the proposed Net Change Limit, ensuring transparency, accountability, and alignment across the ecosystem., This Net Change Limit facilitates a yearly budget cycle for the Cardano community., The 2025 Net Change Limit will begin at the start of Epoch 532 and continue for 72 epochs, finishing at the conclusion of Epoch 604 in December 2025.
- finding: Deadline/expiry: not stated in document
- finding: Claim (governance, independently_verifiable, high materiality): The Cardano Constitution requires the establishment of a Net Change Limit, which defines the maximum amount of lovelace that can be withdrawn from the treasury during an outlined period of time.
- finding: Claim (governance, independently_verifiable, medium materiality): This governance action serves as an opportunity for all governance stakeholders to formally express their positions regarding the proposed Net Change Limit, ensuring transparency, accountability, and alignment across the ecosystem.
- finding: Claim (economic, independently_verifiable, high materiality): This Net Change Limit facilitates a yearly budget cycle for the Cardano community.
- finding: Claim (other, independently_verifiable, low materiality): The 2025 Net Change Limit will begin at the start of Epoch 532 and continue for 72 epochs, finishing at the conclusion of Epoch 604 in December 2025.
- finding: Claim (economic, independently_verifiable, high materiality): Prior to the submission of any budget request, a Net Change Limit must be formally agreed upon by delegate representatives (Article IV Section 3 of the Constitution).
- finding: Claim (economic, independently_verifiable, high materiality): Failure to establish a Net Change Limit shall render any such budget request unconstitutional and, therefore, inapplicable.
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
- finding: Strongest YES: the proposal substantiates "The Cardano Constitution requires the establishment of a Net Change Limit, which defines the maximum amount of lovelace that can be withdrawn from the treasury during an outlined period of time." and clears the evidence gates.
- finding: Strongest NO: weak controls, unclear delivery, or governance precedent could outweigh the benefit of InfoAction.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The Cardano Constitution requires the establishment of a Net Change Limit, which defines the maximum amount of lovelace that can be withdrawn from the treasury during an outlined period of time." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by +0.030 (clamped to ±0.05): Doctrine-aware offline lean for a info action: 8 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `fd7cf1dd0be36be860f12cd52dab11d9373e7668801e237727b5f4bf2e583ca3`
- snapshot_bundle_hash: `fdb7b0b3fb4fb1229c3156d305a1114f45b3d0071288cbccdcbb3baac60a8f6f`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `969`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.465, "NO": 0.2275, "YES": 0.3075}`

