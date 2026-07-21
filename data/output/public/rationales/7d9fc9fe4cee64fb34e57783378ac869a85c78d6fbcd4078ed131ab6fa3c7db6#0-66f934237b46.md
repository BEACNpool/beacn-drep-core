# Rationale: 7d9fc9fe4cee64fb34e57783378ac869a85c78d6fbcd4078ed131ab6fa3c7db6#0
Recommendation: **ABSTAIN**
Score: `0.01` (base + flags + capped margin; LLM lean `+0.03` recorded, not added) | Confidence: `0.5725` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a info action: 8 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on 2025 Cardano NCL. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: 2025 Cardano NCL. The strongest grounded claim is: The Cardano Constitution, at Article IV, Section 3, requires that before withdrawal of Treasury funds, the community must have established a Net Change Limit (NCL).

Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 554
- finding: Expires after epoch: 561
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: 2025 Cardano NCL
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: The Cardano Constitution, at Article IV, Section 3, requires that before withdrawal of Treasury funds, the community must have established a Net Change Limit (NCL)., This means passing a NCL in a formal on-chain governance info action., The NCL represents the maximum amount of ada which may be withdrawn from the Cardano Treasury in a given period., It is a guardrail which, by definition in the Cardano Blockchain Ecosystem Constitution Definitions referenced below, protects the sustainability of the Cardano Treasury by preventing excessive withdrawals.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, independently_verifiable, high materiality): The Cardano Constitution, at Article IV, Section 3, requires that before withdrawal of Treasury funds, the community must have established a Net Change Limit (NCL).
- finding: Claim (governance, independently_verifiable, medium materiality): This means passing a NCL in a formal on-chain governance info action.
- finding: Claim (economic, independently_verifiable, high materiality): The NCL represents the maximum amount of ada which may be withdrawn from the Cardano Treasury in a given period.
- finding: Claim (governance, independently_verifiable, high materiality): It is a guardrail which, by definition in the Cardano Blockchain Ecosystem Constitution Definitions referenced below, protects the sustainability of the Cardano Treasury by preventing excessive withdrawals.
- finding: Claim (economic, independently_verifiable, high materiality): No funds may be withdrawn from the Cardano Treasury without establishing a NCL.
- finding: Claim (adoption, independently_verifiable, high materiality): If the community wishes to use the Treasury to continue to maintain and grow the Cardano ecosystem it’s necessary to establish a NCL.
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
- input_hash: `66f934237b460aaa145224136ea6237325564351b3675587f10b7085a0ebb065`
- snapshot_bundle_hash: `3b3cb8e085d125ac0ccf8935920b00caab6e60a6a3c2a53b4326e9b1ffdf2525`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `199e0465f8eabf20be3ce768498dd41ae56148a9`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `5`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4631, "NO": 0.2584, "YES": 0.2784}`

