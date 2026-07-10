# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline evidence for a treasury withdrawal, especially the missing `treasury_amount_lovelace` field. This is a conservative, evidence-based hold, not a judgment that the Dolos maintenance work is bad or unnecessary.

The action requested 540,750 ada for Year 2 maintenance of Dolos by TxPipe, submitted by Intersect on behalf of the vendor. The proposal describes a 12-month maintenance scope covering part-time maintainer work, dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, documentation, community support, external contribution review, and AI-friendly integration resources. It also states the budget is made up of 420,000 ada, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee.

Several claims were supported in the proposal, including the budget structure, the maintenance scope, the listed Dolos interfaces, the Intersect Budget Process support threshold, the Net Change Limit statement, and the use of treasury management smart contracts with milestone controls and public auditability. But other important claims were not independently supported in the review, including the technical claim that Dolos provides lightweight chain data access without full-node overhead, and the claim about TxPipe’s Project Catalyst delivery history.

Because this is a treasury action, BEACN requires a higher evidence bar before voting yes or no. The intake and synthesis gates were blocked, claims-and-evidence was thin, treasury analysis was incomplete, and risk review lacked independent assurance and a rollback or remedy path. A directional vote would be unblocked by a complete treasury withdrawal baseline, including the missing `treasury_amount_lovelace`, plus stronger independent evidence for the unsupported technical and delivery-history claims, clearer sustainability and cost-benefit analysis, and a defined remedy path if execution falls short.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Fund Dolos by TxPipe for Year 2 maintenance of Cardano's lightweight data node, submitted by Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with project-specific contract address addr1x9d6k9z6t6fvsetj2djmerargk475lef9gfvshy4rwh4h7jm4v295h5jepjhy5m9hj86x3dtafljj2sjepwf2xa0t0aq048cay stated for later transfer.
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months., Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation., Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication., AI-friendly documentation and integration resources for AI-driven development workflows.
- finding: Deadline/expiry: 12-month grant period beginning after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve, with a budget summary totaling 540,750 ADA including a 15,750 ADA Intersect administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- finding: Claim (technical, supported_in_proposal, medium materiality): Dolos exposes five query interfaces, including Mini-Blockfrost HTTP, UTxO-RPC gRPC, Mini-Kupo, and an Ouroboros Node-to-Client Unix socket compatible with Cardano-cli, Ogmios, and other tooling.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope covers dependency updates, protocol compatibility, performance improvements, bug fixes, documentation, issue triage, review of external contributions, ecosystem-driven enhancements, public communication, and AI-friendly documentation and integration resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- missing: Independent evidence for: The document states TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- missing: Independent evidence for: The document states TxPipe received 2025 Intersect open-source maintenance funding for Pallas, Dolos, and UTxO RPC and that all are being delivered on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.66
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve, with a budget summary totaling 540,750 ADA including a 15,750 ADA Intersect administration fee." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve, with a budget summary totaling 540,750 ADA including a 15,750 ADA Intersect administration fee." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- Claims and evidence missing: Independent evidence for: The document states TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `2554d9178db589936d9ac8017f5e5e9ab5d21bc130cae8761d21639607b453a5`
- snapshot_bundle_hash: `d84f849962fb5c2df6dacd264d2c4c183bfcf82f449ea465f4322dd5d75a4eb5`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

