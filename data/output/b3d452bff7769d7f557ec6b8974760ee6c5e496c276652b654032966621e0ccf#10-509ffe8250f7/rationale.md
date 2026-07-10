# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was missing baseline evidence needed to responsibly support or oppose a treasury withdrawal. This is a conservative, evidence-based hold, not a judgment that the work is bad or that the proposer should not be funded.

The action requested 540,750 ada for Year 2 maintenance and enhancement of UTxO RPC by TxPipe, covering part-time maintainer work, SDK and specification maintenance, community support, and AI-friendly documentation resources. The proposal stated that this total includes 420,000 ada for work, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. It also described UTxO RPC as an open Protocol Buffers interface with SDKs across several languages, and said the project has adoption by Amaru, Dingo, and the Haskell Cardano node.

The review found some claims well-supported in the proposal itself, especially the requested total and its stated components. It also noted governance claims that were presented as independently verifiable, including Intersect budget-process support, Net Change Limit compliance, and the use of treasury management smart contracts. But key claims still lacked independent evidence in the review record, including the adoption claims and the claim that more than 10 repositories are maintained under Apache 2.0.

The abstain was driven by failed or incomplete review gates: the intake was blocked because `treasury_amount_lovelace` was missing for a treasury withdrawal, treasury analysis lacked a line-item budget and milestone-gated disbursement evidence, risk review lacked mitigation evidence and independent assurance, and the overall dossier was missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. A directional vote would require those missing baseline fields, a complete proposal summary, replayable public evidence for material adoption and maintenance claims, a clear budget analysis, and enough risk and feasibility evidence for delegators to audit the recommendation.

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
- finding: Requested: Fund UTxO RPC maintenance and enhancement by TxPipe for Year 2, including part-time maintainer work, SDK/spec maintenance, community support, and AI-friendly documentation resources.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address on behalf of TxPipe as vendor
- finding: Stated amount: 540750
- finding: Deliverables: Maintain the protobuf specification, including protocol compatibility, versioning, and documentation., Maintain official SDKs with dependency updates, performance improvements, and bug fixes., Provide community support through issue triage, external contribution review, ecosystem-feedback-driven enhancements, and public communication., Upgrade UTxO RPC compatibility with AI-driven development workflows through AI-friendly documentation and integration resources.
- finding: Deadline/expiry: 12 months after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is described as an open interface specification for UTxO-based blockchains using Protocol Buffers and SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- finding: Claim (technical, proposer_asserted, medium materiality): The project is said to maintain more than 10 repositories covering the core specification, language SDKs, documentation, and provider integrations under Apache 2.0.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (governance, independently_verifiable, high materiality): The proposer states the withdrawal does not breach the applicable 350M Net Change Limit for Epoch 613 to Epoch 713 at submission.
- missing: Independent evidence for: The proposer states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- missing: Independent evidence for: The project is said to maintain more than 10 repositories covering the core specification, language SDKs, documentation, and provider integrations under Apache 2.0.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development on schedule.
- missing: Independent evidence for: The document says prior Intersect 2025 maintenance funding for Pallas, Dolos, and UTxO RPC is being delivered on schedule.
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
- finding: Financial confidence: 0.67
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: The proposer states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- Claims and evidence missing: Independent evidence for: The project is said to maintain more than 10 repositories covering the core specification, language SDKs, documentation, and provider integrations under Apache 2.0.
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
- input_hash: `509ffe8250f7d7d847bd31c8d6076f52bf6f974020df66633d48f027dda9c412`
- snapshot_bundle_hash: `25300740021a03d8e3abe69a8d71ef6f4b0603c8deaac7f090f0a54b218e05bb`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

