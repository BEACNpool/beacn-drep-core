# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sj72rg72
Recommendation: **NO**
Score: `-0.3733` (raw `-0.3533` + doctrine-LLM nudge `-0.02`) | Confidence: `0.6633` | Readiness: `0.85`
> Reasoning layer (precomputed): A small negative adjustment is warranted because the proposal asks for a large treasury withdrawal while several central benefit claims, including ecosystem-wide interface gaps, AI-agent demand, and TxPipe delivery history, are largely asserted in the anchor rather than evidenced inside it, even though some governance, registry, and oversight claims are externally checkable. The deterministic engine already handles hard gates and treasury-analysis incompleteness, so this is only a modest evidence-quality caution rather than a decisive vote judgment.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and the evidence record was too thin on key benefit, cost-benefit, and risk questions to justify spending 1,684,050 ada.

The proposal requested funding for Tx3 by TxPipe as an open API layer for Cardano dApp protocols over 12 months. It committed to onboarding 12 more protocols, building an MCP server for agents, creating a protocol skills framework and agent-first documentation, and providing documentation, generated SDKs, and live JSON-RPC endpoints. The budget claim itself was well-supported: 1,308,000 ada for work, 327,000 ada contingency, and a 49,050 ada Intersect administration fee. The proposal also had a pinned, replayable anchor and showed governance-process support through the Intersect Budget Process.

The strongest case for YES was that the funding request and some governance and adoption claims were reviewable, including statements about existing protocols and budget-process approval. But several central claims remained mostly proposer-asserted rather than independently evidenced in the review record, including the claim that Tx3’s verified interface model can generate the promised outputs, that Cardano lacks a common interface mechanism in a way that makes composability impractical, and that AI-agent demand requires this shared interface layer.

The treasury review also carried elevated scrutiny because this action spends shared ada. The dossier was incomplete, treasury sustainability and cost-benefit clarity were missing, execution risk was unknown, and the risk review lacked independent assurance and a rollback or remedy path. With those gaps, BEACN judged that the cost and precedent risk outweighed the supported evidence, so the evidence-based vote was NO.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.68M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Fund Tx3 by TxPipe as an open API layer for Cardano dApp protocols, including developer and agent-facing infrastructure.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe
- finding: Stated amount: 1,684,050
- finding: Deliverables: Deliver an open, standardized interface across Cardano's leading on-chain protocols over 12 months, Onboard 12 additional protocols, 3 per quarter, with full developer and agent coverage, Develop an MCP server for agents to discover and call published protocols, Develop a protocol skills framework and agent-first documentation, Provide documentation, auto-generated SDKs in multiple languages, and live JSON-RPC endpoints
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Tx3 is described as a framework where each protocol is specified once with a verified interface definition that generates documentation, multi-language SDKs, and live JSON-RPC endpoints.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states that Catalyst Fund 14 already put Tx3's developer layer into production with 5 protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to 12 additional protocol onboardings, at 3 per quarter, with developer and agent coverage.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states that protocols such as Strike Finance, Indigo Protocol, VyFinance, Bodega Market, and Fluid Tokens are already accessible through Tx3.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer claims there is no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and making cross-protocol composability impractical.
- missing: Independent evidence for: Tx3 is described as a framework where each protocol is specified once with a verified interface definition that generates documentation, multi-language SDKs, and live JSON-RPC endpoints.
- missing: Independent evidence for: The proposer claims there is no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and making cross-protocol composability impractical.
- missing: Independent evidence for: The proposer claims AI agents require discoverable, auditable, deterministic shared interfaces for Cardano protocols because hallucinated on-chain transactions can irreversibly move real assets.
- missing: Independent evidence for: The proposal states TxPipe has received funding through 30 Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule, plus Intersect 2025 funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1684050
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.67
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Tx3 is described as a framework where each protocol is specified once with a verified interface definition that generates documentation, multi-language SDKs, and live JSON-RPC endpoints." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1684050
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): A small negative adjustment is warranted because the proposal asks for a large treasury withdrawal while several central benefit claims, including ecosystem-wide interface gaps, AI-agent demand, and TxPipe delivery history, are largely asserted in the anchor rather than evidenced inside it, even though some governance, registry, and oversight claims are externally checkable. The deterministic engine already handles hard gates and treasury-analysis incompleteness, so this is only a modest evidence-quality caution rather than a decisive vote judgment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Tx3 is described as a framework where each protocol is specified once with a verified interface definition that generates documentation, multi-language SDKs, and live JSON-RPC endpoints.
- Claims and evidence missing: Independent evidence for: The proposer claims there is no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and making cross-protocol composability impractical.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `13c0f582778f01cb8a76a21fc7c7ec8eeb93cc4f0bf988044285d0d7736c9338`
- snapshot_bundle_hash: `a6661b58f00e9dde2964d64191d18f8b1df5f8368a682ebaab93c699f7dfea88`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `31`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2033, "NO": 0.7538, "YES": 0.0429}`

