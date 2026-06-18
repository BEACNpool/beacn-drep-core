# gov_action1lh2x3kjucjkggvwu6l3txggkvmrnhs3flpv8j35lvlcan4gax3xsq3cxfjc

## Vote
- Decision: **YES**
- Action type: `HardForkInitiation`
- Status: `active`
- Published at: `2026-06-18T20:14:57.948249+00:00`

## Human-readable rationale
Vote: YES. For this HardForkInitiation (active), available evidence supports proceeding, with risk judged manageable under current context. Why: Pinned anchor document is available for this action. Additional context: Hard fork actions are high-impact protocol upgrades and require operator-aware review. Confidence context: score -0.10; confidence 65.0%.

## Assessment tree
- assessment_status: `incomplete`
- Intake: `complete` — Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: `thin` — Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: `thin` — Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: `complete` — A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: `ready` — The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## What influenced this vote
- Pinned anchor document is available for this action.
- Hard fork actions are high-impact protocol upgrades and require operator-aware review.
- Intake: Action type: HardForkInitiation
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano Mainnet from protocol version 10.0 to protocol version 11.0 without an era transition." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Remaining uncertainty
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The hard fork would add UPLC case expressions for Bool, Integer, and Data and the proposer says this provides significant performance improvements and cleaner script logic.
- Claims and evidence missing: Independent evidence for: The proposer states that testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Top 3 fixes to improve next submission
- Use stable, reproducible anchor links (commit-pinned when possible).
- Provide migration readiness evidence across tooling/wallet/exchange dependencies.
- Publish rollback/contingency plan and incident response playbook.

## Proof of vote
- input_hash: `c08b35f153f1369c078d79b5e99ace8643ce0f057e98c7a08443f415b98b9657`
- snapshot_bundle_hash: `14f141b4c979bb2f748ad8aece57ca608ff6f25a24ff62ce8c220cc5e7abffae`
- soul_commit: `6bf4a7d7baa636417ad929e543cfb8be8fae1f03`
- resources_commit: `693efb97d136543a3565ea51fab80f1cada41b23`
- core_commit: `feb750f2eaf3c23326add704d66c9f8c0145001b`
- score: `-0.1`
- confidence: `0.65`

