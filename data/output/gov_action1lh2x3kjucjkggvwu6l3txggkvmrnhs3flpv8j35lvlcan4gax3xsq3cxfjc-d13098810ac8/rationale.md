# Rationale: gov_action1lh2x3kjucjkggvwu6l3txggkvmrnhs3flpv8j35lvlcan4gax3xsq3cxfjc
Recommendation: **YES**
Score: `-0.03` (raw `-0.01` + doctrine-LLM nudge `-0.02`) | Confidence: `0.58` | Readiness: `0.0`
> Reasoning layer (precomputed): The document contains substantial technical detail and references, but the deterministic assessment marks risk review as thin, and the hard fork doctrine requires high evidence quality, upgrade path clarity, compatibility readiness, and concrete mitigations because hard forks have asymmetric downside. The unresolved reliance on pre-ratification SPO readiness verification and mostly asserted testing and audit claims justify a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (codex-offline-review)
BEACN records YES on Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork). The deterministic gates found enough evidence and no decisive blocker.

The action is a HardForkInitiation. The cached anchor describes the request as: Initiate an intra-era Cardano mainnet hard fork to Protocol Version 11.0, named the van Rossem hard fork.. The strongest grounded claim is: The proposal would upgrade Cardano mainnet to protocol version 11.0 through an intra-era hard fork while keeping the ledger in the Conway era.

A material weak point is that this claim remains proposer-asserted or thinly supported: The proposal says native case expressions for Bool, Integer, and Data in UPLC will improve performance and produce cleaner script logic.

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
- finding: Requested: Initiate an intra-era Cardano mainnet hard fork to Protocol Version 11.0, named the van Rossem hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Upgrade Cardano mainnet protocol from version 10.0 to 11.0 while remaining in the Conway era., Enable new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153., Make all Plutus built-in functions consistently available across Plutus V1, V2, and V3., Add UPLC case expressions for Bool, Integer, and Data., Promote or tighten ledger predicates and improve Cardano-node PPView mismatch diagnostics.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal would upgrade Cardano mainnet to protocol version 11.0 through an intra-era hard fork while keeping the ledger in the Conway era.
- finding: Claim (technical, independently_verifiable, high materiality): The hard fork would introduce new Plutus primitives for modular exponentiation, dropList, BLS12-381 multi-scalar multiplication, arrays, and native Value handling, with linked CIP references for each primitive set.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal says all Plutus built-in functions will become available across Plutus V1, V2, and V3, expanding capabilities for existing V1 and V2 scripts.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says native case expressions for Bool, Integer, and Data in UPLC will improve performance and produce cleaner script logic.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says testing reports demonstrate no behavioral regressions, complete specification-to-implementation conformance for new ledger rules, and correct operation of new Plutus features across Plutus V1, V2, and V3.
- finding: Claim (technical, independently_verifiable, high materiality): The proposal links a Cardano Node 11.0.1 performance report and says it shows no regressions for standard value, Plutus, and voting benchmarks, plus acceptable baseline performance for new Plutus primitives and case expressions.
- missing: Independent evidence for: The proposal says native case expressions for Bool, Integer, and Data in UPLC will improve performance and produce cleaner script logic.
- missing: Independent evidence for: The proposal says testing reports demonstrate no behavioral regressions, complete specification-to-implementation conformance for new ledger rules, and correct operation of new Plutus features across Plutus V1, V2, and V3.
- missing: Independent evidence for: The proposal says security audits were undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
- missing: Independent evidence for: The proposal says it is consistent with all eight listed hard fork guardrails, while noting that none can be checked by the automated guardrails script and that HARDFORK-04 depends on stake pool upgrade status before ratification.
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
- finding: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet to protocol version 11.0 through an intra-era hard fork while keeping the ledger in the Conway era." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says native case expressions for Bool, Integer, and Data in UPLC will improve performance and produce cleaner script logic." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet to protocol version 11.0 through an intra-era hard fork while keeping the ledger in the Conway era." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The document contains substantial technical detail and references, but the deterministic assessment marks risk review as thin, and the hard fork doctrine requires high evidence quality, upgrade path clarity, compatibility readiness, and concrete mitigations because hard forks have asymmetric downside. The unresolved reliance on pre-ratification SPO readiness verification and mostly asserted testing and audit claims justify a small cautionary nudge rather than a positive adjustment.
- Action-type policy: a clean hard-fork initiation may proceed despite thin generic risk fields; missing risk detail remains explicit uncertainty.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Claims and evidence missing: Independent evidence for: The proposal says native case expressions for Bool, Integer, and Data in UPLC will improve performance and produce cleaner script logic.
- Claims and evidence missing: Independent evidence for: The proposal says testing reports demonstrate no behavioral regressions, complete specification-to-implementation conformance for new ledger rules, and correct operation of new Plutus features across Plutus V1, V2, and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `d13098810ac8ff48443fd634c4f93883046dd499cd00722114bcdb2385c5232c`
- snapshot_bundle_hash: `439073d8387f274f5305edf73e8773126263aa8f7dc4ec912ffefb09d881961d`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `715`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.2475, "NO": 0.2975, "YES": 0.455}`

