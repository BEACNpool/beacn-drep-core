# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because a required baseline field for a treasury withdrawal was missing: `treasury_amount_lovelace`. Even though the proposal describes a 540,750 ada request, the review record’s treasury analysis could not complete the required baseline evidence check for the on-chain treasury amount, so BEACN treated this as a conservative evidence-based hold.

The action requested funding for Year 2 of UTxO RPC by TxPipe: 12 months of part-time maintenance and enhancement, including protobuf specification work, official SDK maintenance, community support, AI-friendly documentation, and Intersect administration. The proposer claimed the budget includes 525,000 ada for maintenance and enhancement plus a 15,750 ada Intersect administration fee, for 540,750 ada total. The proposal also supported several technical and governance claims, including the existence of open-source UTxO RPC repositories, SDKs across multiple languages, Intersect budget-process support, Net Change Limit compliance, and a treasury management framework.

Some claims were still too thin for a directional vote. The review lacked independent evidence for the claim that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, and for the claim about TxPipe’s Catalyst delivery record. The treasury review was also incomplete because it lacked a sustainability path and clear cost-benefit analysis, and the risk review lacked independent assurance and a rollback or remedy path.

This ABSTAIN is not a rejection of UTxO RPC or TxPipe. It is a conservative hold because BEACN could not produce a responsible recommendation without complete baseline evidence for the treasury withdrawal. A directional vote would require the missing `treasury_amount_lovelace` field, stronger independent evidence for the adoption and delivery-record claims, clearer treasury cost-benefit and sustainability analysis, and better assurance around execution risk and remedies.

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
- finding: Requested: Fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2, including 12 months of part-time maintenance and enhancement plus Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with Intersect submitting on behalf of the vendor TxPipe
- finding: Stated amount: 540,750
- finding: Deliverables: Maintenance of the protobuf specification, including protocol compatibility, versioning, and documentation, Maintenance of official SDKs, including dependency updates, performance improvements, and bug fixing, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months, beginning after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget summary lists 525,000 ADA for UTxO RPC maintenance and enhancement, 15,750 ADA for the Intersect administration fee, and 540,750 ADA total.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC defines common methods, data structures, and communication patterns using Protocol Buffers and provides SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations, and is open source under Apache 2.0.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation and audited results.
- missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem.
- Claims and evidence missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- input_hash: `8332c0054e9c8d5519bfd3e854aaf6463624e8ba01a52fe9f36c87327aeb9fdd`
- snapshot_bundle_hash: `f95de565593a306ca31566a3002b5fc6774a04e644d596a68b978d359f76e65a`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

