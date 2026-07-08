# Rationale: gov_action1lh2x3kjucjkggvwu6l3txggkvmrnhs3flpv8j35lvlcan4gax3xsq3cxfjc
Recommendation: **YES**
Score: `-0.04` (raw `-0.01` + doctrine-LLM nudge `-0.03`) | Confidence: `0.51` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal includes meaningful technical detail and checkable references, but the deterministic assessment marks risk review as thin and the document leaves a critical readiness condition unresolved until ratification. Under highest-scrutiny hard fork doctrine, incomplete risk and migration evidence justifies a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted YES because the proposal had a pinned, replayable anchor and substantiated the core hard-fork request: upgrading Cardano mainnet from protocol version 10.0 to 11.0 without leaving the Conway era.

The action requested an intra-era hard fork to Protocol Version 11.0, the “van Rossem” hard fork. Its stated deliverables include enabling new Plutus primitives from several CIPs, making Plutus built-in functions consistently available across Plutus V1, V2, and V3, adding UPLC case expressions for Bool, Integer, and Data, and revising several ledger and node validation, diagnostics, and security rules. The proposer also stated that at least 85% of active stake should be on a compatible node version before ratification.

The review found several important claims well-supported or independently checkable, including the protocol version upgrade itself, the cited CIP-based Plutus primitives, consistent availability of Plutus built-ins across Plutus versions, the node performance report, the 85% stake-pool readiness condition, and the permanence of the hard fork with disaster recovery handled through CIP-0135. Other claims remained thinner: the performance and simplification benefits of UPLC case expressions, the full testing-regression claims, and the security-audit claims were treated as proposer assertions rather than fully independently evidenced in the review.

Because this is a high-impact hard fork, BEACN applied extra caution. The risk review was thin, with missing mitigation evidence and missing independent assurance, and readiness depended on a condition to be checked before ratification. Even so, there were no decisive blockers. Under BEACN’s policy, a clean hard-fork initiation can proceed despite incomplete generic risk fields when the core request and evidence gates are satisfied, so the final vote was YES with explicit residual uncertainty.

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
- finding: Stated amount: none
- finding: Deliverables: Upgrade Cardano mainnet to protocol major version 11 and minor version 0 while remaining in the Conway era., Make new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138 and CIP-0153 available., Make all Plutus built-in functions consistently available across Plutus V1, V2 and V3., Support case expressions for Bool, Integer and Data in Untyped Plutus Core., Promote or revise several ledger and node validation, diagnostics and security rules including VRF key hash uniqueness and PPView mismatch reporting.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal would upgrade Cardano mainnet from protocol version 10.0 to protocol version 11.0 without an era transition.
- finding: Claim (technical, independently_verifiable, high materiality): The upgrade introduces new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138 and CIP-0153.
- finding: Claim (technical, supported_in_proposal, high materiality): The upgrade will make all Plutus built-in functions available consistently across Plutus V1, V2 and V3.
- finding: Claim (technical, proposer_asserted, high materiality): The upgrade adds UPLC case expressions over Bool, Integer and Data, which the proposer says will improve performance and simplify script logic.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer says testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2 and V3.
- finding: Claim (technical, independently_verifiable, high materiality): A linked Cardano Node 11.0.1 performance report is cited as showing no regressions for standard value, Plutus and voting benchmarks and acceptable baseline performance for new Plutus features.
- missing: Independent evidence for: The upgrade adds UPLC case expressions over Bool, Integer and Data, which the proposer says will improve performance and simplify script logic.
- missing: Independent evidence for: The proposer says testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2 and V3.
- missing: Independent evidence for: The proposer says security audits were undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
- missing: Independent evidence for: The proposer states the action is consistent with all eight relevant hard fork guardrails, while noting none can be checked by the automated guardrails script.
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
- finding: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet from protocol version 10.0 to protocol version 11.0 without an era transition." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The upgrade adds UPLC case expressions over Bool, Integer and Data, which the proposer says will improve performance and simplify script logic." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet from protocol version 10.0 to protocol version 11.0 without an era transition." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal includes meaningful technical detail and checkable references, but the deterministic assessment marks risk review as thin and the document leaves a critical readiness condition unresolved until ratification. Under highest-scrutiny hard fork doctrine, incomplete risk and migration evidence justifies a small cautionary nudge rather than a positive adjustment.
- Action-type policy: a clean hard-fork initiation may proceed despite thin generic risk fields; missing risk detail remains explicit uncertainty.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Claims and evidence missing: Independent evidence for: The upgrade adds UPLC case expressions over Bool, Integer and Data, which the proposer says will improve performance and simplify script logic.
- Claims and evidence missing: Independent evidence for: The proposer says testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2 and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `29e8f7e0d9844fc6000296a8494f08c2f450fd3f4bc0869fa1b5f117b05b6417`
- snapshot_bundle_hash: `7ae58409c5555a83ca789bc5dca92b1f8a7f466c56a36fe448652af87d35a107`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.2562, "NO": 0.3163, "YES": 0.4275}`

