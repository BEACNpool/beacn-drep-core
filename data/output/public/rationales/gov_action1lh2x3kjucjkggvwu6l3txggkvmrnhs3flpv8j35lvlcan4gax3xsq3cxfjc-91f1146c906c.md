# Rationale: gov_action1lh2x3kjucjkggvwu6l3txggkvmrnhs3flpv8j35lvlcan4gax3xsq3cxfjc
Recommendation: **YES**
Score: `-0.07` (raw `-0.04` + doctrine-LLM nudge `-0.03`) | Confidence: `0.62` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal gives meaningful technical detail and checkable references, but for a highest-scrutiny hard fork the extracted claims still show important reliance on asserted testing and audit outcomes, a future readiness condition for 85% active stake, and only a thin risk/reversion posture for an effectively permanent ledger-rule change. A small cautionary nudge is justified because the doctrine requires high evidence quality and bounded execution risk for directional support.

## Plain-language explanation (codex-offline-review)
BEACN records YES on Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork). The deterministic gates found enough evidence and no decisive blocker.

The action is a HardForkInitiation. The cached anchor describes the request as: Initiate an intra-era hard fork upgrading Cardano mainnet to protocol version 11.0, named the van Rossem hard fork.. The strongest grounded claim is: The proposal would upgrade Cardano mainnet to protocol version major 11 minor 0 through an intra-era hard fork while remaining in the Conway era.

A material weak point is that this claim remains proposer-asserted or thinly supported: The upgrade adds UPLC case expressions over Bool, Integer, and Data, which the proposer says will improve performance and simplify script logic.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: HardForkInitiation
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: not required
- finding: Requested: Initiate an intra-era hard fork upgrading Cardano mainnet to protocol version 11.0, named the van Rossem hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Cardano mainnet protocol upgraded from version 10.0 to 11.0 while remaining in the Conway era, New Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153 made available, All Plutus built-in functions made consistently available across Plutus V1, V2, and V3, UPLC case expressions for Bool, Integer, and Data supported, Ledger and node enhancements including VRF key hash uniqueness, revised reference input rules, CC voting restriction as a ledger predicate, clearer withdrawal validation, and improved PPView mismatch reporting
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal would upgrade Cardano mainnet to protocol version major 11 minor 0 through an intra-era hard fork while remaining in the Conway era.
- finding: Claim (technical, independently_verifiable, high materiality): The upgrade introduces new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153.
- finding: Claim (technical, supported_in_proposal, high materiality): The upgrade will make all Plutus built-in functions available consistently across Plutus V1, V2, and V3.
- finding: Claim (technical, proposer_asserted, medium materiality): The upgrade adds UPLC case expressions over Bool, Integer, and Data, which the proposer says will improve performance and simplify script logic.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer states that testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- finding: Claim (technical, independently_verifiable, high materiality): The proposal cites a Cardano Node 11.0.1 performance report showing no regressions for standard value, Plutus, and voting benchmarks and acceptable baseline performance for the new primitives and case expressions.
- missing: Independent evidence for: The upgrade adds UPLC case expressions over Bool, Integer, and Data, which the proposer says will improve performance and simplify script logic.
- missing: Independent evidence for: The proposer states that testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- missing: Independent evidence for: Security audits were undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
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
- finding: Flag count: 0
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet to protocol version major 11 minor 0 through an intra-era hard fork while remaining in the Conway era." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The upgrade adds UPLC case expressions over Bool, Integer, and Data, which the proposer says will improve performance and simplify script logic." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Hard fork actions are high-impact protocol upgrades and require operator-aware review.
- Intake: Action type: HardForkInitiation
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet to protocol version major 11 minor 0 through an intra-era hard fork while remaining in the Conway era." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal gives meaningful technical detail and checkable references, but for a highest-scrutiny hard fork the extracted claims still show important reliance on asserted testing and audit outcomes, a future readiness condition for 85% active stake, and only a thin risk/reversion posture for an effectively permanent ledger-rule change. A small cautionary nudge is justified because the doctrine requires high evidence quality and bounded execution risk for directional support.
- Action-type policy: a clean hard-fork initiation may proceed despite thin generic risk fields; missing risk detail remains explicit uncertainty.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Claims and evidence missing: Independent evidence for: The upgrade adds UPLC case expressions over Bool, Integer, and Data, which the proposer says will improve performance and simplify script logic.
- Claims and evidence missing: Independent evidence for: The proposer states that testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `91f1146c906cb3e3cce08d779a7a3dd2e5dce0c71e317a7f4bfd20be2dec5d01`
- snapshot_bundle_hash: `2596b7eba143fcbeb63270863b327224e0d501b699d7b19998f93e0c1a1afcad`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `249`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.2425, "NO": 0.3325, "YES": 0.425}`

