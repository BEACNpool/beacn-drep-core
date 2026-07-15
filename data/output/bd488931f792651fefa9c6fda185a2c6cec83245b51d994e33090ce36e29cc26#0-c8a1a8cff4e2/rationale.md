# Rationale: bd488931f792651fefa9c6fda185a2c6cec83245b51d994e33090ce36e29cc26#0
Recommendation: **ABSTAIN**
Score: `0.01` (raw `0.01` + doctrine-LLM nudge `+0.03`) | Confidence: `0.5725` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a info action: 8 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
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
- finding: Snapshot freshness source: deep_research_dossiers.csv
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
- input_hash: `c8a1a8cff4e2d1298711265a3a299315bf2a5c1d563861c8c58f7e1b24cbd662`
- snapshot_bundle_hash: `0951036eba6aff872c59f2aea577cb3dabbf6d932432b5c428632157063eeb6d`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4631, "NO": 0.2584, "YES": 0.2784}`

