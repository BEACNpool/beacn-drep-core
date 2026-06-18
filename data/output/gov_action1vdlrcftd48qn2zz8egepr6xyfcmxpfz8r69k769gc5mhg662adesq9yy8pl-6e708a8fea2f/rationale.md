# Rationale: gov_action1vdlrcftd48qn2zz8egepr6xyfcmxpfz8r69k769gc5mhg662adesq9yy8pl
Recommendation: **ABSTAIN**
Score: `0.01` | Confidence: `0.53` | Readiness: `0.0`

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
- input_hash: `6e708a8fea2f4844d62036af71dfc4b9b5a85c37c775bb3ce2a88868bab6b66a`
- snapshot_bundle_hash: `444712c6c4c27c815b95ece6a9f4e0be10898ed5e7aed9f60a4ca04dd5c0c8f4`
- soul_commit: `6bf4a7d7baa636417ad929e543cfb8be8fae1f03`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `c2d37d96622e9918a7eb9e4cc72da2044797ae72`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `8`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4525, "NO": 0.2638, "YES": 0.2838}`

