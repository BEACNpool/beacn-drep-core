# Rationale: gov_action1h4ygjv0hjfj3lmafcm76rpdzcm8vsvj9k5wejn3npyxwxm3fesnqqw9kxxz
Recommendation: **ABSTAIN**
Score: `0.04` (raw `0.01` + doctrine-LLM nudge `+0.03`) | Confidence: `0.56` | Readiness: `0.0`
> Reasoning layer (codex-offline-review): Doctrine-aware offline lean for a info action: 8 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).

## Plain-language explanation (codex-offline-review)
BEACN records ABSTAIN on Cardano Blockchain Ecosystem Budget: Amaru Node Development 2025. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: Cardano Blockchain Ecosystem Budget: Amaru Node Development 2025. The strongest grounded claim is: Amaru is an open-source project implementing a new fully interoperable block-producing node for Cardano.

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
- finding: Requested: Cardano Blockchain Ecosystem Budget: Amaru Node Development 2025
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: Amaru is an open-source project implementing a new fully interoperable block-producing node for Cardano., It aims to improve the network's overall accessibility and robustness without compromising its safety and security., Amaru provides another perspective and solution for stake pool operators and developers alike, prioritizing a modular approach, a seamless user experience, and low hardware requirements., Additionally, the project is implemented mainly in Rust, which is well-equipped for high assurance to attract new contributors to the core maintenance of the ecosystem.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, independently_verifiable, low materiality): Amaru is an open-source project implementing a new fully interoperable block-producing node for Cardano.
- finding: Claim (other, independently_verifiable, high materiality): It aims to improve the network's overall accessibility and robustness without compromising its safety and security.
- finding: Claim (other, independently_verifiable, low materiality): Amaru provides another perspective and solution for stake pool operators and developers alike, prioritizing a modular approach, a seamless user experience, and low hardware requirements.
- finding: Claim (adoption, independently_verifiable, low materiality): Additionally, the project is implemented mainly in Rust, which is well-equipped for high assurance to attract new contributors to the core maintenance of the ecosystem.
- finding: Claim (other, independently_verifiable, low materiality): Who we are Amaru is a multi-entity effort that currently sits under PRAGMA: a member-based, not-for-profit open-source association for blockchain software projects.
- finding: Claim (other, independently_verifiable, low materiality): Five members with equal power currently drive PRAGMA's strategy and operations: Blink Labs, Cardano Foundation, dcSpark, Sundae Labs, and TxPipe.
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
- finding: Strongest YES: the proposal substantiates "Amaru is an open-source project implementing a new fully interoperable block-producing node for Cardano." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Amaru is an open-source project implementing a new fully interoperable block-producing node for Cardano." and clears the evidence gates.
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
- input_hash: `3c7dda68dd2677f536c3eccc5dc05676a842ef2c6f2dbebbed8f8df4ba4c8d6c`
- snapshot_bundle_hash: `a2edab01a2d0c98580e9ca8e258b98773660128ed4d27c7ceebff3ba6e89289c`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `577`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.46, "NO": 0.23, "YES": 0.31}`

