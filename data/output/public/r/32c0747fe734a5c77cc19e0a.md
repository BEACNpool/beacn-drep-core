# Rationale: gov_action1lh2x3kjucjkggvwu6l3txggkvmrnhs3flpv8j35lvlcan4gax3xsq3cxfjc
Recommendation: **YES**
Score: `-0.1` (raw `-0.07` + doctrine-LLM nudge `-0.03`) | Confidence: `0.65` | Readiness: `0.0`
> Reasoning layer (precomputed): Under the hard fork doctrine, this action deserves highest scrutiny; the claims include meaningful technical benefits and some checkable references, but the supplied claims also show unresolved stake pool readiness, thin in-document audit/testing detail, and only a limited reversion path for a permanent ledger-rule change.

## Plain-language explanation (codex-offline-review)
BEACN records YES on Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork). The deterministic gates found enough evidence and no decisive blocker.

The action is a HardForkInitiation. The cached anchor describes the request as: Initiate an intra-era hard fork of Cardano Mainnet to Protocol Version 11.0, called the van Rossem hard fork.. The recorded treasury amount is none. The strongest grounded claim is: The hard fork will upgrade Cardano Mainnet from protocol version 10.0 to 11.0 without an era transition.

A material weak point is that this claim remains proposer-asserted or thinly supported: Native UPLC case expressions for Bool, Integer, and Data will improve script performance and produce cleaner script logic.

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
- finding: Requested: Initiate an intra-era hard fork of Cardano Mainnet to Protocol Version 11.0, called the van Rossem hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: none
- finding: Deliverables: Upgrade Cardano mainnet protocol to major version 11 and minor version 0 while remaining in the Conway era., Make new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153 available., Make all Plutus built-in functions available consistently across Plutus V1, V2, and V3., Add UPLC case expressions for Bool, Integer, and Data., Promote or tighten ledger predicates including VRF key hash uniqueness, reference input rules, Constitutional Committee voting restriction, withdrawals validation, and PPView mismatch reporting.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The hard fork will upgrade Cardano Mainnet from protocol version 10.0 to 11.0 without an era transition.
- finding: Claim (technical, supported_in_proposal, high materiality): At least 85% of stake pools by active stake should have upgraded to a node version capable of supporting protocol version 11 before ratification.
- finding: Claim (technical, independently_verifiable, high materiality): The upgrade introduces new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153.
- finding: Claim (technical, supported_in_proposal, high materiality): All Plutus built-in functions, including newly introduced ones, will become available across Plutus V1, V2, and V3.
- finding: Claim (technical, proposer_asserted, medium materiality): Native UPLC case expressions for Bool, Integer, and Data will improve script performance and produce cleaner script logic.
- finding: Claim (technical, proposer_asserted, high materiality): Testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- missing: Independent evidence for: Native UPLC case expressions for Bool, Integer, and Data will improve script performance and produce cleaner script logic.
- missing: Independent evidence for: Testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- missing: Independent evidence for: Security audits have been undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
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
- finding: Strongest YES: the proposal substantiates "The hard fork will upgrade Cardano Mainnet from protocol version 10.0 to 11.0 without an era transition." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Native UPLC case expressions for Bool, Integer, and Data will improve script performance and produce cleaner script logic." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The hard fork will upgrade Cardano Mainnet from protocol version 10.0 to 11.0 without an era transition." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): Under the hard fork doctrine, this action deserves highest scrutiny; the claims include meaningful technical benefits and some checkable references, but the supplied claims also show unresolved stake pool readiness, thin in-document audit/testing detail, and only a limited reversion path for a permanent ledger-rule change.
- Action-type policy: a clean hard-fork initiation may proceed despite thin generic risk fields; missing risk detail remains explicit uncertainty.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Native UPLC case expressions for Bool, Integer, and Data will improve script performance and produce cleaner script logic.
- Claims and evidence missing: Independent evidence for: Testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `14eb5395e65feff716012906acde5a6a06301209f407b3639732bba88c82e1ea`
- snapshot_bundle_hash: `9749aa4172b961e72389f3618a892c2b0c5711a346490f8a73e50d8be2206cb6`
- soul_commit: `6bf4a7d7baa636417ad929e543cfb8be8fae1f03`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `20e0915ebc437140b55ee25e28adbae01e97032d`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `268`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.2388, "NO": 0.3588, "YES": 0.4025}`

