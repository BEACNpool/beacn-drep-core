# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#9
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline treasury evidence: the required `treasury_amount_lovelace` field was missing for a treasury withdrawal. For a proposal that would draw shared ADA from the treasury, BEACN treats that as a conservative, evidence-based hold rather than a directional yes or no.

The action requested 1,684,050 ada to fund Tx3 by TxPipe over 12 months as an open API layer for Cardano dApp protocols. The proposal described standardized protocol interfaces, documentation, auto-generated SDKs, live JSON-RPC endpoints, agent-first documentation, protocol skills packaging, an MCP server, and 12 additional protocol onboardings. The proposer’s budget breakdown was supported in the proposal: 1,308,000 ada for work, 327,000 ada contingency, and a 49,050 ada Intersect administration fee. The review also found independent support that TxPipe has 5 protocols live on the Tx3 Protocol Registry, that the proposal passed the 2026 Intersect Budget Process Hydra Voting threshold, and that Intersect described treasury smart-contract administration and oversight.

The hold was driven by gaps in the review record. Some important claims were still only proposer-asserted or lacked independent evidence, including the technical claim that Tx3 can describe each protocol once and generate documentation, SDKs, and JSON-RPC endpoints, and the adoption claim that Cardano lacks a common interface mechanism. The treasury review was incomplete because sustainability path and cost-benefit clarity were missing. The risk review also lacked independent assurance and a rollback or remedy path.

This ABSTAIN is not a rejection of the idea or the team’s claims. It means BEACN could not responsibly vote yes or no without pretending certainty. A directional vote would be unblocked by a complete treasury withdrawal baseline, especially the missing `treasury_amount_lovelace` field, plus independent evidence for the core technical and ecosystem claims, clearer cost-benefit and sustainability analysis, and risk evidence covering assurance and remedies.

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
- finding: Requested: Treasury withdrawal to fund Tx3 by TxPipe as an open API layer for Cardano dApp protocols.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 1,684,050
- finding: Deliverables: Open standardized interface across Cardano on-chain protocols, Documentation, auto-generated SDKs in multiple languages, and live JSON-RPC endpoints from verified interface definitions, Agent-first documentation, protocol skills packaging operations, and an MCP server for agents, 12 additional protocol onboardings over 12 months, three per quarter
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Tx3 is presented as a framework that describes each protocol once with a verified interface definition and generates documentation, multi-language SDKs, and live JSON-RPC endpoints.
- finding: Claim (adoption, independently_verifiable, medium materiality): Through Catalyst Fund 14, TxPipe has put the developer layer into production with 5 protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal funds 12 additional protocol onboardings, three per quarter, with developer and agent coverage plus development of an MCP server and skill framework.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer claims there is currently no common interface mechanism across the Cardano ecosystem, increasing integration costs and limiting composability.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: Tx3 is presented as a framework that describes each protocol once with a verified interface definition and generates documentation, multi-language SDKs, and live JSON-RPC endpoints.
- missing: Independent evidence for: The proposer claims there is currently no common interface mechanism across the Cardano ecosystem, increasing integration costs and limiting composability.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.62
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Tx3 is presented as a framework that describes each protocol once with a verified interface definition and generates documentation, multi-language SDKs, and live JSON-RPC endpoints." — so cost or precedent may outweigh the benefit.
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
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: Tx3 is presented as a framework that describes each protocol once with a verified interface definition and generates documentation, multi-language SDKs, and live JSON-RPC endpoints.
- Claims and evidence missing: Independent evidence for: The proposer claims there is currently no common interface mechanism across the Cardano ecosystem, increasing integration costs and limiting composability.
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
- input_hash: `9601d2c84157429a32f0d24c09b6668e974c092a1e4fd52a233756a9309f1daa`
- snapshot_bundle_hash: `6cab28ec501924991faff3dfe7413dda60186d1cee1c10828b004baef1c0ac24`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

