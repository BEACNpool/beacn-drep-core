# Rationale: gov_action1lh2x3kjucjkggvwu6l3txggkvmrnhs3flpv8j35lvlcan4gax3xsq3cxfjc
Recommendation: **YES**
Score: `-0.04` (raw `-0.01` + doctrine-LLM nudge `-0.03`) | Confidence: `0.59` | Readiness: `0.0`
> Reasoning layer (precomputed): A small negative nudge is justified because hard forks receive highest scrutiny and the supplied claims leave important readiness and risk evidence only partly evidenced: the 85% SPO readiness condition is explicitly pending, security audits and testing results are asserted without detailed reports in the anchor text, and the deterministic assessment flags the risk review as thin. The document does provide meaningful technical specificity and external references, so the adjustment should remain small rather than strongly negative.

## Plain-language explanation (codex-offline-review)
BEACN records YES on Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork). The deterministic gates found enough evidence and no decisive blocker.

The action is a HardForkInitiation. The cached anchor describes the request as: Initiate a hard fork upgrading Cardano Mainnet to protocol version 11.0, called the 'van Rossem' hard fork.. The strongest grounded claim is: The hard fork will upgrade Cardano Mainnet from protocol version 10.0 to protocol version 11.0 while remaining in the Conway era and not changing transaction shape.

A material weak point is that this claim remains proposer-asserted or thinly supported: The proposal claims native UPLC case expressions over Bool, Integer and Data will improve performance and produce cleaner script logic.

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
- finding: Requested: Initiate a hard fork upgrading Cardano Mainnet to protocol version 11.0, called the 'van Rossem' hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Upgrade Cardano mainnet protocol to major version 11 and minor version 0 while remaining in the Conway era., Make new Plutus primitives available as defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138 and CIP-0153., Make all Plutus built-in functions available consistently across Plutus V1, V2 and V3., Add UPLC case expressions for Bool, Integer and Data., Enforce or tighten several ledger and node validation, diagnostic, and security rules.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The hard fork will upgrade Cardano Mainnet from protocol version 10.0 to protocol version 11.0 while remaining in the Conway era and not changing transaction shape.
- finding: Claim (technical, independently_verifiable, high materiality): The upgrade introduces new Plutus primitives for modular exponentiation, dropList, BLS12-381 multi-scalar multiplication, Array operations, and native Value handling, with the referenced CIPs identifying the primitives.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal states that all Plutus built-ins, including newly introduced ones, will become available across Plutus V1, V2 and V3.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal claims native UPLC case expressions over Bool, Integer and Data will improve performance and produce cleaner script logic.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal claims the upgrade tightens ledger and node behavior by enforcing VRF key hash uniqueness, revising Plutus V1/V2 reference input rules, promoting Constitutional Committee voting restrictions to ledger predicates, rewriting withdrawal validation, and improving PPView mismatch diagnostics.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2 and V3.
- missing: Independent evidence for: The proposal claims native UPLC case expressions over Bool, Integer and Data will improve performance and produce cleaner script logic.
- missing: Independent evidence for: The proposal states that testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2 and V3.
- missing: Independent evidence for: The proposal states that security audits have been undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
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
- finding: Strongest YES: the proposal substantiates "The hard fork will upgrade Cardano Mainnet from protocol version 10.0 to protocol version 11.0 while remaining in the Conway era and not changing transaction shape." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal claims native UPLC case expressions over Bool, Integer and Data will improve performance and produce cleaner script logic." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The hard fork will upgrade Cardano Mainnet from protocol version 10.0 to protocol version 11.0 while remaining in the Conway era and not changing transaction shape." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small negative nudge is justified because hard forks receive highest scrutiny and the supplied claims leave important readiness and risk evidence only partly evidenced: the 85% SPO readiness condition is explicitly pending, security audits and testing results are asserted without detailed reports in the anchor text, and the deterministic assessment flags the risk review as thin. The document does provide meaningful technical specificity and external references, so the adjustment should remain small rather than strongly negative.
- Action-type policy: a clean hard-fork initiation may proceed despite thin generic risk fields; missing risk detail remains explicit uncertainty.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Claims and evidence missing: Independent evidence for: The proposal claims native UPLC case expressions over Bool, Integer and Data will improve performance and produce cleaner script logic.
- Claims and evidence missing: Independent evidence for: The proposal states that testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2 and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `8b789b4e50b6232c5e3e7be7432354f9ae6f51fa8a717ea1bb828bdfcf9184f7`
- snapshot_bundle_hash: `bd0cc9819c666dcbe0af3e27eb7eb60b54555b6266ac8bab281b2cf7845a62c2`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `569`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.2463, "NO": 0.3063, "YES": 0.4475}`

