# Rationale: gov_action1lh2x3kjucjkggvwu6l3txggkvmrnhs3flpv8j35lvlcan4gax3xsq3cxfjc
Recommendation: **YES**
Score: `-0.03` (raw `-0.01` + doctrine-LLM nudge `-0.02`) | Confidence: `0.5075` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal provides meaningful technical detail, external references, readiness conditions, and some performance and audit assertions, but hard forks receive highest scrutiny and the deterministic assessment still marks risk review as thin. The document does not present a concrete risk register with mitigations beyond the general disaster recovery and cost-model-disable path, so a small cautionary nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted YES because the core request was clear and reviewable: this action initiates the Cardano mainnet hard fork to Protocol Version 11.0, the “van Rossem” hard fork, while staying within the Conway era. The proposal had a pinned, replayable anchor document, and the main upgrade claim cleared the evidence gates.

The action requests a protocol upgrade from version 10.0 to 11.0. The proposer says it would add new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153; make Plutus built-ins available consistently across Plutus V1, V2, and V3; add UPLC case expressions for Bool, Integer, and Data; tighten or promote several ledger validation checks; and improve Cardano node PPView mismatch reporting. The review found strong support for the basic hard fork scope, the new primitives, the cross-version Plutus availability claim, the absence of new protocol parameters, and the stated readiness condition that at least 85% of active stake pools should be on a capable node version before ratification.

BEACN also noted important limits in the evidence. Some claims were still mainly proposer assertions, including that the new UPLC case expressions will improve script performance and produce cleaner logic, that testing showed no behavioral regressions and full conformance, and that security audits covered Plutus BLS primitives and execution costs. The risk review was thin: execution risk was marked unknown, and the review lacked detailed mitigation evidence or independent assurance beyond the general CIP-0135 disaster recovery path and the possibility of disabling Plutus primitive use through companion cost model settings.

Even with those uncertainties, there were no decisive blockers. BEACN treated this as a high-impact hard fork requiring extra caution, but the action-type policy allows a clean hard-fork initiation to proceed when the core upgrade is well anchored and reviewable. The YES vote reflects support for moving forward, while openly preserving the uncertainty around thin risk documentation and several claims that were not independently evidenced in the review.

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
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Initiate an intra-era Cardano mainnet hard fork to Protocol Version 11.0, named the van Rossem hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Upgrade Cardano mainnet protocol from version 10.0 to 11.0 while remaining in the Conway era., Make new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153 available., Make all Plutus built-in functions available consistently across Plutus V1, V2, and V3., Add UPLC case expressions for Bool, Integer, and Data., Promote or tighten several ledger validation checks and improve Cardano node PPView mismatch reporting.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal would upgrade Cardano mainnet to protocol version 11.0 through an intra-era hard fork while remaining in the Conway era.
- finding: Claim (technical, independently_verifiable, high materiality): The upgrade introduces new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153, including modular exponentiation, dropList, BLS12-381 multi-scalar multiplication, Array, and Value built-ins.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal says all Plutus built-in functions, including newly introduced ones, will become available across Plutus V1, V2, and V3.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says UPLC case expressions over Bool, Integer, and Data will improve script performance and produce cleaner script logic.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2, and V3.
- finding: Claim (technical, independently_verifiable, high materiality): The proposal links a Cardano Node 11.0.1 performance report and says it shows no regressions for standard value, Plutus, and voting benchmarks, with acceptable baseline performance for new primitives and case expressions.
- missing: Independent evidence for: The proposal says UPLC case expressions over Bool, Integer, and Data will improve script performance and produce cleaner script logic.
- missing: Independent evidence for: The proposal says testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2, and V3.
- missing: Independent evidence for: The proposal says security audits were undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
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
- finding: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet to protocol version 11.0 through an intra-era hard fork while remaining in the Conway era." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says UPLC case expressions over Bool, Integer, and Data will improve script performance and produce cleaner script logic." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet to protocol version 11.0 through an intra-era hard fork while remaining in the Conway era." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal provides meaningful technical detail, external references, readiness conditions, and some performance and audit assertions, but hard forks receive highest scrutiny and the deterministic assessment still marks risk review as thin. The document does not present a concrete risk register with mitigations beyond the general disaster recovery and cost-model-disable path, so a small cautionary nudge is justified.
- Action-type policy: a clean hard-fork initiation may proceed despite thin generic risk fields; missing risk detail remains explicit uncertainty.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Claims and evidence missing: Independent evidence for: The proposal says UPLC case expressions over Bool, Integer, and Data will improve script performance and produce cleaner script logic.
- Claims and evidence missing: Independent evidence for: The proposal says testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2, and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `b722a208df8a3434e590b472c74908865c6fa81a9636d049abff78877a5e20e0`
- snapshot_bundle_hash: `29fdd66a808f44a8b6e1e26598714e0f5de962b0c804e5e7a3162fb62bec0b85`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.2566, "NO": 0.3066, "YES": 0.4369}`

