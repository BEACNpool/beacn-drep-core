# Rationale: fdd468da5cc4ac8431dcd7e2b3211666c73bc229f85879469f67f1d9d51d344d#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `-0.01` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5` | Readiness: `0.6`
> Reasoning layer (precomputed): Hard fork doctrine requires high evidence quality, bounded execution risk, compatibility readiness, and a concrete risk register. The claims include useful technical detail, external references, and readiness conditions, but several high-materiality readiness, testing, audit, and guardrail claims are asserted rather than evidenced inside the document, and the deterministic assessment marks risk review as thin. A small cautionary negative nudge is warranted without overriding the engine.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because this is a high-impact hard fork and the review did not find a complete, independently pinned readiness packet for mainnet activation.

The action asked to initiate the van Rossem hard fork, upgrading Cardano mainnet from protocol version 10.0 to 11.0 while staying in the Conway era. The proposal says this would add new Plutus primitives, make built-in functions available consistently across Plutus V1, V2, and V3, add UPLC case expressions, and tighten several ledger and node rules. Some core claims were supported or independently verifiable, including the basic protocol-version upgrade, the listed CIPs for new Plutus primitives, the cited node performance report, and the permanent nature of the ledger-rule change.

The hold comes from the evidence gaps around readiness and risk. Several material claims were still proposer-asserted rather than independently evidenced inside the reviewed packet, including the claimed performance benefits of UPLC case expressions, the no-regression testing claims, security audit claims, constitutional guardrail alignment, and broad operational readiness. The risk review was also thin, with missing mitigation evidence and independent assurance.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the upgrade’s goals. A directional vote would need a complete independently pinned readiness packet covering guardrails, testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning.

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
- finding: Requested: Initiate a Cardano mainnet intra-era hard fork to Protocol Version 11 minor 0, called the van Rossem hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Upgrade Cardano mainnet protocol from version 10.0 to 11.0 while remaining in the Conway era., Make new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153 available., Make all Plutus built-in functions available consistently across Plutus V1, V2, and V3., Add UPLC case expressions for Bool, Integer, and Data., Promote or tighten ledger and node rules including VRF key hash uniqueness, reference input rules, Constitutional Committee voting restriction handling, withdrawal predicate validation, and PPView mismatch reporting.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal would upgrade Cardano mainnet to protocol version 11.0 through an intra-era hard fork that remains in the Conway era.
- finding: Claim (technical, independently_verifiable, high materiality): The hard fork would introduce new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153.
- finding: Claim (technical, supported_in_proposal, high materiality): The upgrade would make all Plutus built-in functions available across Plutus V1, V2, and V3, expanding capabilities for existing V1 and V2 scripts.
- finding: Claim (technical, proposer_asserted, medium materiality): UPLC case expressions over Bool, Integer, and Data are claimed to provide significant performance improvements and cleaner script logic.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal claims testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions.
- finding: Claim (technical, independently_verifiable, high materiality): A linked Cardano Node 11.0.1 performance report is cited as showing no regressions for standard value, Plutus, and voting benchmarks and acceptable baseline performance for new primitives and case expressions.
- missing: Independent evidence for: UPLC case expressions over Bool, Integer, and Data are claimed to provide significant performance improvements and cleaner script logic.
- missing: Independent evidence for: The proposal claims testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions.
- missing: Independent evidence for: The proposal states security audits were undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
- missing: Independent evidence for: The proposal states it is consistent with all eight relevant Cardano Constitution hard fork guardrails, while noting none can be checked by the automated guardrails script and HARDFORK-04 requires attention before ratification.
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
- finding: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet to protocol version 11.0 through an intra-era hard fork that remains in the Conway era." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "UPLC case expressions over Bool, Integer, and Data are claimed to provide significant performance improvements and cleaner script logic." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet to protocol version 11.0 through an intra-era hard fork that remains in the Conway era." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: Hard fork doctrine requires high evidence quality, bounded execution risk, compatibility readiness, and a concrete risk register. The claims include useful technical detail, external references, and readiness conditions, but several high-materiality readiness, testing, audit, and guardrail claims are asserted rather than evidenced inside the document, and the deterministic assessment marks risk review as thin. A small cautionary negative nudge is warranted without overriding the engine.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Protocol action lacks a complete independently pinned readiness packet: version_guardrails_pass, testnet_results_pass, spo_readiness_pass, exchange_readiness_pass, dapp_readiness_pass, security_review_pass, constitutional_alignment_pass, rollback_or_containment_plan
- Claims and evidence missing: Independent evidence for: UPLC case expressions over Bool, Integer, and Data are claimed to provide significant performance improvements and cleaner script logic.
- Claims and evidence missing: Independent evidence for: The proposal claims testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `541844bdf7263b889ce2a6f66722e4ed95b121ce9266ff7bcf511448b7f8a7da`
- snapshot_bundle_hash: `6128fc91cf3e70abcae529e5b9fdb8f480ac2ec7bf3c91d7ffaa9f01576cdc50`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `7`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.445, "NO": 0.2775, "YES": 0.2775}`

