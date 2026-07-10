# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because a required baseline field for a treasury withdrawal, `treasury_amount_lovelace`, was missing. Even though the proposal text says it requests 540,750 ada, the review found the treasury intake blocked because the required on-chain amount field was not available for the assessment tree.

The proposal asked to fund Year 2 maintenance and enhancements for UTxO RPC by TxPipe over 12 months, including maintenance of the protobuf specification, official SDKs, community support, and AI-friendly documentation and integration resources. The proposer claimed the total request was 540,750 ada, made up of 525,000 ada for maintenance and enhancement plus a 15,750 ada Intersect administration fee. The proposal also described governance process support, oversight through Intersect and third parties, milestone-based disbursement controls, and treasury smart contract administration.

Several claims were supported in the proposal or marked independently verifiable, including the requested budget breakdown, the technical description of UTxO RPC, the Intersect budget-process threshold, the Net Change Limit statement, and the treasury administration structure. But some material claims still lacked independent evidence in the review, including adoption by Amaru, Dingo, and the Haskell Cardano node, and TxPipe’s stated Catalyst delivery record. The treasury analysis was also incomplete because sustainability path and cost-benefit clarity were missing, and the risk review lacked independent assurance and a rollback or remedy path.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the project’s usefulness. A directional vote would require the missing `treasury_amount_lovelace` field for the treasury withdrawal, plus stronger independent evidence for the adoption and delivery-record claims, clearer cost-benefit and sustainability analysis, and stronger assurance and remedy details for execution risk.

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
- finding: Requested: Fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2, including part-time maintenance and enhancements over 12 months.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v; submitted by Intersect on behalf of the vendor TxPipe.
- finding: Stated amount: 540,750
- finding: Deliverables: Maintain the protobuf specification, including protocol compatibility, versioning, and documentation., Maintain official SDKs, including dependency updates, performance improvements, and bug fixing., Provide community support, including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication., Upgrade UTxO RPC compatibility with AI-driven development workflows through AI-friendly documentation and integration resources.
- finding: Deadline/expiry: 12 months; new grant period begins after closure of the existing contract.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement plus a 15,750 ADA Intersect budget administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The motivation section describes the core grant as 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time maintainer at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is described as an open interface specification for UTxO-based blockchains using Protocol Buffers and SDKs for Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface.
- finding: Claim (technical, independently_verifiable, medium materiality): The project is described as maintaining 10+ repositories across the core specification, SDKs, documentation, and provider integrations under the Apache 2.0 license.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and therefore advanced to on-chain Treasury Withdrawal submission.
- missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface.
- missing: Independent evidence for: The proposal states that TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement plus a 15,750 ADA Intersect budget administration fee." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement plus a 15,750 ADA Intersect budget administration fee." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface.
- Claims and evidence missing: Independent evidence for: The proposal states that TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development on schedule.
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
- input_hash: `e33036de34058fbef9f34bfef493fbc8657af5cf284a645a449eb6570bf92adb`
- snapshot_bundle_hash: `d0175a504d82621415f88c92662cda1fc6434aa62eadc088cb0b5a5e16a30df4`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

