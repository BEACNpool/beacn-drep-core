# Rationale: 9b62b3c632f329016a968ac25211825bb4f84b12461121c7da3aa11df92370f9#0
Recommendation: **ABSTAIN**
Score: `0.01` (base + flags + capped margin; LLM lean `+0.03` recorded, not added) | Confidence: `0.5725` | Readiness: `0.0`
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
- finding: Snapshot freshness source: deep_research_dossiers.csv
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
- Advisory model lean was +0.030 (display cap ±0.05) and had zero influence on the binding score: Doctrine-aware offline lean for a info action: 8 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).
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
- input_hash: `e4869d2a4c22ead4627fa4c273ab7bfa162afacfbe9983fbfcb7d74198617c03`
- snapshot_bundle_hash: `0919eff270152a98d1eff9a420428205424d1b9fd5460dda26e76c9b72c8ee87`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `646629824e42aafea23488c5eeef5362c697d560`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `5`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4631, "NO": 0.2584, "YES": 0.2784}`

