# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#9
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline evidence for a treasury withdrawal: the required `treasury_amount_lovelace` field was missing, so the action could not be fully audited in BEACN’s evidence tree.

The proposal requested 1,684,050 ada for Tx3 by TxPipe, described as an open API layer for Cardano dApp protocols. The requested work included 12 additional protocol onboardings over 12 months, an MCP server, skill framework, agent-first documentation, protocol skills packaging, multi-language SDKs, and live JSON-RPC endpoints. The proposal’s budget structure was supported in the proposal: 1,308,000 ada, a 327,000 ada contingency reserve, and a 49,050 ada Intersect administration fee. The review also treated the proposal anchor as pinned and replayable, and noted proposer claims about Intersect budget-process support, the net change limit, and milestone-based controls.

Several important claims were still not strong enough for a directional vote. The review found missing independent evidence for the technical claim that Tx3 lets each protocol be defined once and then used to generate documentation, SDKs, and JSON-RPC endpoints. It also found missing independent evidence for the claim that Cardano currently lacks a common interface mechanism across protocols. Treasury analysis was incomplete because the review lacked a sustainability path and clear cost-benefit case, and risk review was incomplete because it lacked independent assurance and a rollback or remedy path.

This abstention is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would require the missing treasury withdrawal amount field in lovelace, stronger independent evidence for the key technical and ecosystem claims, clearer cost-benefit and sustainability analysis, and a defined assurance and remedy path for execution risk.

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
- finding: Requested: Withdraw treasury funds for Tx3 by TxPipe, an open API layer for Cardano dApp protocols with developer and agent-facing infrastructure.
- finding: Recipient: Intersect treasury reserve smart contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, for TxPipe/vendor project administration by Intersect
- finding: Stated amount: 1,684,050
- finding: Deliverables: Open API Layer for Cardano Protocols, 12 additional protocol onboardings over 12 months, MCP server, skill framework, agent-first documentation, protocol skills packaging operations, multi-language SDKs and live JSON-RPC endpoints for published protocols
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total budget of 1,684,050 ADA including a 49,050 ADA Intersect administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Tx3 is described as a framework where each protocol is defined once and then used to produce documentation, auto-generated SDKs in multiple languages, and live JSON-RPC endpoints.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal says Catalyst Fund 14 already put the Tx3 developer layer into production with 5 protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, supported_in_proposal, high materiality): The requested work includes onboarding 12 additional protocols at a rate of 3 per quarter with developer and agent coverage.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal asserts that there is currently no common interface mechanism across the Cardano ecosystem, forcing integrators to relearn each protocol from scratch.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal claims Tx3 will reduce dependence on centralized or official protocol frontends by exposing standardized open-source interfaces.
- missing: Independent evidence for: Tx3 is described as a framework where each protocol is defined once and then used to produce documentation, auto-generated SDKs in multiple languages, and live JSON-RPC endpoints.
- missing: Independent evidence for: The proposal asserts that there is currently no common interface mechanism across the Cardano ecosystem, forcing integrators to relearn each protocol from scratch.
- missing: Independent evidence for: The proposal claims Tx3 will reduce dependence on centralized or official protocol frontends by exposing standardized open-source interfaces.
- missing: Independent evidence for: The proposal says TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total budget of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Tx3 is described as a framework where each protocol is defined once and then used to produce documentation, auto-generated SDKs in multiple languages, and live JSON-RPC endpoints." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total budget of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: Tx3 is described as a framework where each protocol is defined once and then used to produce documentation, auto-generated SDKs in multiple languages, and live JSON-RPC endpoints.
- Claims and evidence missing: Independent evidence for: The proposal asserts that there is currently no common interface mechanism across the Cardano ecosystem, forcing integrators to relearn each protocol from scratch.
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
- input_hash: `53d0ec73fc2aecceee8747c5bd94e6ad0a0c21186af79993dcd58dfb0922d3bc`
- snapshot_bundle_hash: `693002a43402696e0ce0a706b0c8523eee93a6830b3f0c4ce9201a14d0e41bee`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

