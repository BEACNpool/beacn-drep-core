# Rationale: gov_action1vdlrcftd48qn2zz8egepr6xyfcmxpfz8r69k769gc5mhg662adesq9yy8pl
Recommendation: **ABSTAIN**
Score: `0.04` (raw `0.01` + doctrine-LLM nudge `+0.03`) | Confidence: `0.56` | Readiness: `0.0`
> Reasoning layer (codex-offline-review): Doctrine-aware offline lean for a info action: 7 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).

## Plain-language explanation (codex-offline-review)
BEACN records ABSTAIN on Set a 300 million ADA Net Change Limit for Epochs 563–635. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: Set a 300 million ADA Net Change Limit for Epochs 563–635. The strongest grounded claim is: The Cardano Constitution, at Article IV, Section 3, requires that before withdrawal of Treasury funds, the community must have established a Net Change Limit (NCL).

Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 556
- finding: Expires after epoch: 563
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: not required
- finding: Requested: Set a 300 million ADA Net Change Limit for Epochs 563–635
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: The Cardano Constitution, at Article IV, Section 3, requires that before withdrawal of Treasury funds, the community must have established a Net Change Limit (NCL)., This means passing a NCL in a formal on-chain governance info action., The NCL represents the maximum amount of ada which may be withdrawn from the Cardano Treasury in a given period., We believe that the NCL covering the period from the start of epoch 563 to the end of epoch 635 should be 300M ADA.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The Cardano Constitution, at Article IV, Section 3, requires that before withdrawal of Treasury funds, the community must have established a Net Change Limit (NCL).
- finding: Claim (governance, independently_verifiable, medium materiality): This means passing a NCL in a formal on-chain governance info action.
- finding: Claim (economic, supported_in_proposal, high materiality): The NCL represents the maximum amount of ada which may be withdrawn from the Cardano Treasury in a given period.
- finding: Claim (economic, proposer_asserted, low materiality): We believe that the NCL covering the period from the start of epoch 563 to the end of epoch 635 should be 300M ADA.
- finding: Claim (other, supported_in_proposal, low materiality): Existing and pending NCLs only cover periods through the end of 2025.
- finding: Claim (economic, supported_in_proposal, high materiality): However, many current and upcoming budget proposals are structured around 12-month timelines, extending into 2026.
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
- finding: Strongest YES: the proposal substantiates "The Cardano Constitution, at Article IV, Section 3, requires that before withdrawal of Treasury funds, the community must have established a Net Change Limit (NCL)." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The Cardano Constitution, at Article IV, Section 3, requires that before withdrawal of Treasury funds, the community must have established a Net Change Limit (NCL)." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by +0.030 (clamped to ±0.05): Doctrine-aware offline lean for a info action: 7 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).
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
- input_hash: `35b18468508d30fdf42a6d8e5e3f2b335aecd8079b7e22232cbe4b40db73339b`
- snapshot_bundle_hash: `23f98617e2fa3c9b1660db842ae486c62a4d6f494170a334915d0179a89d042b`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `247`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.46, "NO": 0.23, "YES": 0.31}`

