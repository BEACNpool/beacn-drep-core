# Rationale: fdd468da5cc4ac8431dcd7e2b3211666c73bc229f85879469f67f1d9d51d344d#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `-0.01` + doctrine-LLM nudge `-0.02`) | Confidence: `0.5` | Readiness: `0.6`
> Reasoning layer (precomputed): Hard fork doctrine requires highest scrutiny, implementation readiness, migration readiness, and a concrete risk register. The claims include useful references and a clear 85% SPO readiness condition, but several high-materiality readiness, testing, and audit claims are asserted rather than evidenced in the supplied document, and the deterministic assessment marks risk review as thin and overall status incomplete. A small cautionary nudge is warranted without overriding the engine's gates.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the hard fork is a high-impact protocol change and the supplied evidence did not meet BEACN’s threshold for a directional vote. This is a conservative, evidence-based hold, not an objection to the upgrade itself.

The action requested an intra-era hard fork on Cardano mainnet from protocol version 10.0 to 11.0, the “van Rossem” hard fork, while remaining in the Conway era. The proposal says this would add new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153, make Plutus built-ins consistently available across Plutus V1, V2, and V3, support additional UPLC case expressions, and promote or revise several ledger and node checks. The core claim that the action upgrades mainnet to protocol version 11.0 was supported, and the pinned anchor document made the proposal reviewable.

The review also found important gaps. Several material readiness, testing, and audit claims were asserted rather than independently evidenced in the supplied material, including the claim that transaction shape is unchanged and ecosystem upgrade effort is minimized, and the claim that testing showed no behavioral regressions and complete conformance for new rules and Plutus behavior. The risk review was also thin: execution risk was marked unknown, mitigation evidence and independent assurance were missing, and the readiness packet was incomplete across areas such as testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning.

A directional vote would be unblocked by a complete independently pinned readiness packet, including clear evidence for implementation readiness, migration readiness, testing results, security review, constitutional alignment, and concrete mitigation or containment plans. Until those claims are tied to replayable public evidence, abstaining avoids overstating certainty on a permanent, operator-sensitive protocol upgrade.

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
- finding: Snapshot freshness source: governance_actions_all.csv
- finding: Deep research dossier: not required
- finding: Requested: Initiate an intra-era hard fork on Cardano mainnet to Protocol Version 11.0, called the 'van Rossem' hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Upgrade Cardano mainnet protocol to major version 11 and minor version 0 while remaining in the Conway era., Make new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153 available., Make all Plutus built-in functions consistently available across Plutus V1, V2, and V3., Support UPLC case expressions for Bool, Integer, and Data., Promote or revise ledger and node checks including VRF key hash uniqueness, reference input rules, Constitutional Committee voting restriction, withdrawals validation, and PPView mismatch reporting.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal would upgrade Cardano mainnet from protocol version 10.0 to protocol version 11.0 through an intra-era hard fork while remaining in the Conway era.
- finding: Claim (technical, independently_verifiable, high materiality): The hard fork would make new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153 available across Plutus V1, V2, and V3.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal asserts that transaction shape is unchanged and ecosystem upgrade effort is minimized because the change is intra-era.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer states that testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- finding: Claim (technical, independently_verifiable, high materiality): A referenced Cardano Node 11.0.1 performance report is said to show no regressions for standard value, Plutus, and voting benchmarks and acceptable baseline performance for new Plutus primitives and case expressions.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that security audits were undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
- missing: Independent evidence for: The proposal asserts that transaction shape is unchanged and ecosystem upgrade effort is minimized because the change is intra-era.
- missing: Independent evidence for: The proposer states that testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- missing: Independent evidence for: The proposal states that security audits were undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
- missing: Independent evidence for: The submission was recommended by Intersect's Hard Fork Working Group on 2026-06-15 and endorsed by Intersect's Technical Steering Committee on 2026-06-16.
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
- finding: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet from protocol version 10.0 to protocol version 11.0 through an intra-era hard fork while remaining in the Conway era." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal asserts that transaction shape is unchanged and ecosystem upgrade effort is minimized because the change is intra-era." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet from protocol version 10.0 to protocol version 11.0 through an intra-era hard fork while remaining in the Conway era." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: Hard fork doctrine requires highest scrutiny, implementation readiness, migration readiness, and a concrete risk register. The claims include useful references and a clear 85% SPO readiness condition, but several high-materiality readiness, testing, and audit claims are asserted rather than evidenced in the supplied document, and the deterministic assessment marks risk review as thin and overall status incomplete. A small cautionary nudge is warranted without overriding the engine's gates.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Protocol action lacks a complete independently pinned readiness packet: version_guardrails_pass, testnet_results_pass, spo_readiness_pass, exchange_readiness_pass, dapp_readiness_pass, security_review_pass, constitutional_alignment_pass, rollback_or_containment_plan
- Claims and evidence missing: Independent evidence for: The proposal asserts that transaction shape is unchanged and ecosystem upgrade effort is minimized because the change is intra-era.
- Claims and evidence missing: Independent evidence for: The proposer states that testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `7265d3f55255bb2522a4e18ead8e5d81f657eb21f681bef7ccfc9da45991dc5b`
- snapshot_bundle_hash: `ead5cb349a090c35f682b25848861ed9833e2fea660491a9e0103ac3cb79e16b`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `82a02efa3be4dedf61fea1548ca03635163347a8`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `22`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.445, "NO": 0.2775, "YES": 0.2775}`

