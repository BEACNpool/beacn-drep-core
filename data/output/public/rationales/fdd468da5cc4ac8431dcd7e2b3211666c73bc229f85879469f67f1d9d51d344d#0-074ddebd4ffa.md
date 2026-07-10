# Rationale: fdd468da5cc4ac8431dcd7e2b3211666c73bc229f85879469f67f1d9d51d344d#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `-0.07` + doctrine-LLM nudge `-0.02`) | Confidence: `0.5` | Readiness: `0.5`
> Reasoning layer (precomputed): Hard fork doctrine requires high evidence quality, upgrade path clarity, ecosystem readiness, and a concrete risk register. The claims show meaningful technical rationale and some independently verifiable references, but the assessment marks risk review as thin and the document itself relies on asserted testing and audit summaries while acknowledging ratification depends on future stake pool readiness verification and that reversion is only available through disaster recovery.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was missing DRep distribution data and did not have a complete independently pinned readiness packet for a high-impact hard fork. This is a conservative, evidence-based hold, not a rejection of the upgrade.

The action requested an intra-era Cardano mainnet hard fork from protocol version 10.0 to 11.0, named the van Rossem hard fork, while staying in the Conway era. The proposal described new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153; broader availability of Plutus built-ins across Plutus V1, V2, and V3; UPLC case expressions for Bool, Integer, and Data; VRF key hash uniqueness and other ledger rule changes; and improved PPView mismatch diagnostics in cardano-node.

Several core technical claims were supported or independently verifiable, including the protocol version upgrade, the linked CIP-based Plutus primitives, the absence of new or deprecated protocol parameters, and the stated recovery path through CIP-0135 disaster recovery. However, important claims still relied on proposer assertions or thin evidence, including the claimed performance and logic benefits of UPLC case expressions, the no-regression testing summary, security audit assurances, and mitigation evidence for execution risk.

The gates that kept BEACN from a directional vote were the missing DRep distribution data, thin claims-and-evidence status, thin risk review, missing mitigation evidence, missing independent assurance, and the lack of a complete readiness packet covering version guardrails, testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning. A YES or NO vote would require those materials to be pinned, replayable, and independently reviewable.

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
- finding: Requested: Initiate an intra-era Cardano mainnet hard fork to protocol version 11.0, named the van Rossem hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Upgrade Cardano mainnet protocol to major version 11 and minor version 0 while remaining in the Conway era., Make new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153 available., Make all Plutus built-in functions consistently available across Plutus V1, V2, and V3., Add UPLC case expressions for Bool, Integer, and Data., Enforce VRF key hash uniqueness and other ledger predicate/rule changes., Improve PPView mismatch diagnostics in cardano-node.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal upgrades Cardano mainnet from protocol version 10.0 to protocol version 11.0 without an era transition.
- finding: Claim (technical, independently_verifiable, high materiality): The hard fork introduces new Plutus primitives defined by CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal says all Plutus built-ins, including newly introduced ones, will become available across Plutus V1, V2, and V3.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says UPLC case expressions over Bool, Integer, and Data will improve script performance and produce cleaner script logic.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says testing reports show no behavioral regressions, complete specification and implementation conformance for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- finding: Claim (technical, independently_verifiable, high materiality): The proposal links a Cardano Node 11.0.1 performance report and says it shows no regressions for standard value, Plutus, and voting benchmarks, plus acceptable baseline performance for the new Plutus primitives and case expressions.
- missing: Independent evidence for: The proposal says UPLC case expressions over Bool, Integer, and Data will improve script performance and produce cleaner script logic.
- missing: Independent evidence for: The proposal says testing reports show no behavioral regressions, complete specification and implementation conformance for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- missing: Independent evidence for: The proposal says security audits have been undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
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
- finding: Strongest YES: the proposal substantiates "The proposal upgrades Cardano mainnet from protocol version 10.0 to protocol version 11.0 without an era transition." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal upgrades Cardano mainnet from protocol version 10.0 to protocol version 11.0 without an era transition." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): Hard fork doctrine requires high evidence quality, upgrade path clarity, ecosystem readiness, and a concrete risk register. The claims show meaningful technical rationale and some independently verifiable references, but the assessment marks risk review as thin and the document itself relies on asserted testing and audit summaries while acknowledging ratification depends on future stake pool readiness verification and that reversion is only available through disaster recovery.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- No DRep distribution available.
- Protocol action lacks a complete independently pinned readiness packet: version_guardrails_pass, testnet_results_pass, spo_readiness_pass, exchange_readiness_pass, dapp_readiness_pass, security_review_pass, constitutional_alignment_pass, rollback_or_containment_plan
- Claims and evidence missing: Independent evidence for: The proposal says UPLC case expressions over Bool, Integer, and Data will improve script performance and produce cleaner script logic.
- Claims and evidence missing: Independent evidence for: The proposal says testing reports show no behavioral regressions, complete specification and implementation conformance for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `074ddebd4ffaeddfb589784a39b8a7c2ee2f3606e2a4607e7c0a447ee33578fd`
- snapshot_bundle_hash: `7f3980328826979466d0a79bd43c6d3358bd5fe18f319f9fdf412ce8bb9379c3`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.445, "NO": 0.2775, "YES": 0.2775}`

