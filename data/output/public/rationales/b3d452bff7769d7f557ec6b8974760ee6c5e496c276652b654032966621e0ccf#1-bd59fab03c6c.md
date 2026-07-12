# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and the required deep-research dossier was not complete enough to support a directional vote. This is a conservative, evidence-based hold, not a rejection of Dolos or TxPipe.

The action requested 540,750 ada for “Dolos by TxPipe: Maintaining Cardano’s Lightweight Data Node, Year 2,” covering 12 months of part-time maintenance, protocol compatibility work, performance improvements, bug fixing, documentation, community support, AI-friendly integration resources, and Intersect administration. The proposal breaks the amount into 420,000 ada for the grant, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. It also says Dolos has public adoption signals such as commits, releases, stars, forks, and contributors, and that the action passed the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase.

Several important items were supported by the proposal or identified as independently verifiable, including the requested amount, the maintenance scope, the Intersect budget-process status, the Net Change Limit claim, and the treasury-management structure. But key review areas remained incomplete. Independent evidence was still missing for the claim that Dolos provides lightweight chain-data access without full-node overhead, and for the claimed audit, oversight, reporting, and milestone-control arrangements. The treasury review was also missing a line-item budget and sustainability path, the risk review lacked independent assurance and a rollback or remedy path, and synthesis was blocked by missing alternatives and failure-mode analysis.

A directional YES or NO would be unblocked by a completed deep-research dossier with replayable public evidence for the unsupported technical and oversight claims, a line-item budget, a sustainability path, independent assurance, a clear rollback or remedy path, alternatives analysis, and failure-mode analysis. Until those gates pass, BEACN’s vote remains NEEDS_MORE_INFO.

## Review Tree
- overall_status: `blocked`

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
- finding: Deep research dossier: required
- finding: Requested: Fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2, including maintenance and enhancement plus Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months, Essential maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows, Milestone-based disbursement controls and reporting obligations through Intersect oversight
- finding: Deadline/expiry: 12 months; grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is described as a lightweight Cardano data node in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- finding: Claim (technical, supported_in_proposal, medium materiality): Dolos is said to expose five query interfaces, including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros Node-to-Client Unix socket compatible with Cardano-cli, Ogmios, and other tooling.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document reports Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope covers dependency updates, protocol compatibility, performance improvements, bug fixing, documentation, issue triage, external contribution review, ecosystem-feedback enhancements, public communication, and AI-friendly resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- missing: Independent evidence for: Dolos is described as a lightweight Cardano data node in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- missing: Independent evidence for: The proposal states audit and oversight costs are included in overhead, with Intersect and technically capable third parties providing reporting obligations and milestone-based disbursement controls.
- missing: Independent evidence for: The document states TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule, and that 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC is being delivered on schedule.
- missing: alternatives analysis
- missing: failure-mode analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 540750
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: not confirmed
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.55
- missing: line-item budget
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: low
- finding: Governance risk: medium
- finding: Technical risk: low
- finding: Treasury exposure risk: low
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." though 2 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Dolos is described as a lightweight Cardano data node in Rust that provides efficient access to chain data without the overhead of traditional full nodes." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 540750
- Risk review: Execution risk: low
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." though 2 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional voting is blocked until dossier quality gates pass.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Dossier completeness not confirmed for this treasury proposal.
- Claims and evidence missing: Independent evidence for: Dolos is described as a lightweight Cardano data node in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- Claims and evidence missing: Independent evidence for: The proposal states audit and oversight costs are included in overhead, with Intersect and technically capable third parties providing reporting obligations and milestone-based disbursement controls.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: missing alternatives analysis
- Synthesis missing: missing failure-mode analysis
- Synthesis status is blocked.

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.
- Missing dossier section: alternatives analysis
- Missing dossier section: failure-mode analysis

## Reproducibility
- input_hash: `bd59fab03c6c4a4bc69655a3e535ca20b5e909259264b64d3a1a72fb36441a4f`
- snapshot_bundle_hash: `2f0d4f726d05821d3878644b9206459c27f50759637859004932ecd742ea3f64`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

