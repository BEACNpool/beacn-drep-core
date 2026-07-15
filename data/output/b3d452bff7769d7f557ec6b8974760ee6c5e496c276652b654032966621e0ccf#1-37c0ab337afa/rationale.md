# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1359` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.754` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show a concrete open-source infrastructure maintenance scope, named oversight and disbursement controls, public audit references, and independently checkable process/NCL claims. The nudge remains small because several core technical benefit and adoption claims are still largely proposer asserted or only externally checkable rather than verified within the document.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal depends on a required Net Change Limit check that was not pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Dolos or TxPipe.

The action requests 540,750 ada for Year 2 maintenance of Dolos by TxPipe, sent through the 2026 Treasury Reserve Smart Contract stake address administered by Intersect. The proposal says this includes 525,000 ada for maintenance and enhancement plus a 15,750 ada Intersect administration fee. It describes 12 months of part-time maintenance work, including dependency updates, protocol compatibility, performance improvements, bug fixing, documentation, issue triage, contribution review, developer communication, and AI-friendly integration resources.

Several parts were supported well enough for review: the proposal anchor was pinned and replayable, the requested amount was clear, the budget-process support and audit references were presented, and the proposal described oversight, milestone-based disbursement controls, and a public dashboard. Other important claims were still thin or not independently verified in the supplied record, including Dolos’s technical role as a lightweight Rust data node, its network and query-interface claims, the sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path.

Because this is a treasury withdrawal, BEACN applies a higher bar: spending shared ada requires replayable public evidence, not just proposer assertions. A directional vote would be unblocked by pinned, independently verifiable Net Change Limit evidence from public chain data, plus stronger independent evidence for the key technical benefit claims and clearer treasury-risk information.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 540.8k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect for the vendor TxPipe.
- finding: Stated amount: 540750
- finding: Deliverables: WP1 - Dolos Maintenance and Enhancement, Part-time maintainer for Dolos over 12 months, Essential maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, external contribution review, ecosystem-feedback-driven enhancements, and public developer communication, AI-friendly documentation and integration resources
- finding: Deadline/expiry: 12 months; new grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect budget administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The motivation states the underlying maintenance grant is 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Dolos maintainer for 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without running a traditional full node.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C Unix socket compatible with existing tooling.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal reports Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal states the maintainer will handle dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, documentation, issue triage, contribution review, community communication, and AI-friendly documentation and integration resources.
- missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without running a traditional full node.
- missing: Independent evidence for: The proposal says Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C Unix socket compatible with existing tooling.
- missing: Independent evidence for: The proposal asserts Dolos aligns with Pillar 2 focus area A.3 for Developer Experience and open-source maintenance incentives.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.68
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect budget administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without running a traditional full node." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 540750
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect budget administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show a concrete open-source infrastructure maintenance scope, named oversight and disbursement controls, public audit references, and independently checkable process/NCL claims. The nudge remains small because several core technical benefit and adoption claims are still largely proposer asserted or only externally checkable rather than verified within the document.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without running a traditional full node.
- Claims and evidence missing: Independent evidence for: The proposal says Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C Unix socket compatible with existing tooling.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `37c0ab337afaaa5d3dd0dd14d1801af16bd54942b563e1572d8e233d160e8626`
- snapshot_bundle_hash: `757a8a378d0ff9b6915e452e0c2049f82b12432b50fcb8563b2cefc77df890e8`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5085, "NO": 0.1099, "YES": 0.3816}`

