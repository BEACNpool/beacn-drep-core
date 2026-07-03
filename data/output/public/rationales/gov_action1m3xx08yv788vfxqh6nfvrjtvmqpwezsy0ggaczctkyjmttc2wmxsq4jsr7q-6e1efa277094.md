# Rationale: gov_action1m3xx08yv788vfxqh6nfvrjtvmqpwezsy0ggaczctkyjmttc2wmxsq4jsr7q
Recommendation: **ABSTAIN**
Score: `0.04` (raw `0.01` + doctrine-LLM nudge `+0.03`) | Confidence: `0.56` | Readiness: `0.0`
> Reasoning layer (codex-offline-review): Doctrine-aware offline lean for a info action: 8 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).

## Plain-language explanation (codex-offline-review)
BEACN records ABSTAIN on Net Change Limit (Epoch 613 to Epoch 713). This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: Net Change Limit (Epoch 613 to Epoch 713). The strongest grounded claim is: The Cardano Constitution requires the establishment of a Net Change Limit (NCL), which defines the maximum amount of lovelace that can be withdrawn from the treasury during an outlined period of time.

Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 605
- finding: Expires after epoch: 612
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: not required
- finding: Requested: Net Change Limit (Epoch 613 to Epoch 713)
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: The Cardano Constitution requires the establishment of a Net Change Limit (NCL), which defines the maximum amount of lovelace that can be withdrawn from the treasury during an outlined period of time., This governance action serves as an opportunity for all governance stakeholders to formally express their positions regarding the proposed Net Change Limit, ensuring transparency, accountability, and alignment across the ecosystem., The Net Change Limit will begin at the start of Epoch 613 (13 February 2026) and conclude at the end of Epoch 713 (3 July 2027)., The Net Change Limit will be 350,000,000,000,000 lovelace (350M ada).
- finding: Deadline/expiry: not stated in document
- finding: Claim (governance, independently_verifiable, high materiality): The Cardano Constitution requires the establishment of a Net Change Limit (NCL), which defines the maximum amount of lovelace that can be withdrawn from the treasury during an outlined period of time.
- finding: Claim (governance, independently_verifiable, medium materiality): This governance action serves as an opportunity for all governance stakeholders to formally express their positions regarding the proposed Net Change Limit, ensuring transparency, accountability, and alignment across the ecosystem.
- finding: Claim (other, independently_verifiable, low materiality): The Net Change Limit will begin at the start of Epoch 613 (13 February 2026) and conclude at the end of Epoch 713 (3 July 2027).
- finding: Claim (economic, independently_verifiable, low materiality): The Net Change Limit will be 350,000,000,000,000 lovelace (350M ada).
- finding: Claim (governance, independently_verifiable, high materiality): Prior to the submission of any treasury withdrawal, a Net Change Limit must be formally agreed upon by delegated representatives (Article IV Section 3 of the Constitution).
- finding: Claim (governance, independently_verifiable, high materiality): Failure to establish a Net Change Limit shall render any such treasury withdrawal action unconstitutional and, therefore, inapplicable.
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
- finding: Strongest YES: the proposal substantiates "The Cardano Constitution requires the establishment of a Net Change Limit (NCL), which defines the maximum amount of lovelace that can be withdrawn from the treasury during an outlined period of time." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The Cardano Constitution requires the establishment of a Net Change Limit (NCL), which defines the maximum amount of lovelace that can be withdrawn from the treasury during an outlined period of time." and clears the evidence gates.
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
- input_hash: `6e1efa27709483f2b836c52156c5d29d9b6d963268537479f24dcddf827a6f6f`
- snapshot_bundle_hash: `405af97b23260b69b79eae63da2452856d5a8ea0db33b3f877d91dc74942c0e0`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `b97265e867768077aac16ceb31ccfe1be639d187`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `803`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.46, "NO": 0.23, "YES": 0.31}`

