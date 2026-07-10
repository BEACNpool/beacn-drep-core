# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sj72rg72
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has clear public-benefit alignment and some independently checkable governance and oversight references, but several high-value technical and adoption claims remain largely proposer-asserted while the ask is large; BEACN doctrine favors caution on treasury stewardship and evidence quality when spending upside is plausible but not fully verified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the idea.

The action requests 1,684,050 ada for Tx3 by TxPipe, submitted by Intersect on behalf of TxPipe as vendor. The proposal says this includes 1,308,000 ada of project funding, a 327,000 ada contingency reserve, and a 49,050 ada Intersect administration fee. The requested work includes an open API layer for Cardano protocols, 12 additional protocol onboardings over 12 months, an MCP server, protocol skills packaging, agent-facing documentation, auto-generated SDKs, and live JSON-RPC endpoints.

Several governance and budget claims were well-supported in the review: the proposal anchor was pinned and replayable, the amount breakdown was substantiated, the proposal cited Intersect budget-process support, stated that the withdrawal did not breach the 350M ada Net Change Limit, and described oversight, milestone controls, and public auditability. But several important technical and adoption claims remained thin or proposer-asserted, including the claim that Tx3 provides a verified interface definition that generates documentation, SDKs, and endpoints, and the claim that Cardano lacks a common interface mechanism in a way that materially raises integration cost.

Because this is a treasury withdrawal, BEACN applies elevated scrutiny. The review found stressed treasury-flow conditions, unknown execution risk, missing independent assurance, no clear rollback or remedy path, and missing sustainability and cost-benefit clarity. The evidence that would unblock a directional vote is independent, public-chain verification of the applicable Net Change Limit, plus stronger replayable evidence for the central technical claims and clearer treasury-risk mitigations.

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
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Tx3 by TxPipe: Open API Layer for Cardano's dApp Protocols, including an open standardized interface, additional protocol onboardings, MCP server, skill framework, and agent-facing documentation.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe as vendor
- finding: Stated amount: 1,684,050
- finding: Deliverables: Open API Layer for Cardano Protocols, 12 additional protocol onboardings over 12 months, described as 3 per quarter, MCP server for agents to discover and call published protocols, Protocol skills packaging operations, Agent-first documentation and LLM-structured documentation, Auto-generated SDKs in multiple languages and live JSON-RPC endpoints for registry protocols
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Tx3 is presented as a framework where each protocol is described once with a verified interface definition that produces documentation, multi-language SDKs, and live JSON-RPC endpoints.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal says Catalyst Fund 14 has already put the Tx3 developer layer into production with 5 protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to fund 12 additional protocol onboardings, 3 per quarter, with full developer and agent coverage.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposer argues that Cardano currently lacks a common interface mechanism across ecosystem protocols, increasing integration cost and limiting composability.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposer argues that AI-agent-driven on-chain activity requires shared, auditable interfaces because hallucinated on-chain transactions can move real assets irreversibly.
- missing: Independent evidence for: Tx3 is presented as a framework where each protocol is described once with a verified interface definition that produces documentation, multi-language SDKs, and live JSON-RPC endpoints.
- missing: Independent evidence for: The proposer argues that Cardano currently lacks a common interface mechanism across ecosystem protocols, increasing integration cost and limiting composability.
- missing: Independent evidence for: The proposer argues that AI-agent-driven on-chain activity requires shared, auditable interfaces because hallucinated on-chain transactions can move real assets irreversibly.
- missing: Independent evidence for: The proposal states TxPipe has received funding through 30 Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1684050
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Tx3 is presented as a framework where each protocol is described once with a verified interface definition that produces documentation, multi-language SDKs, and live JSON-RPC endpoints." — so cost or precedent may outweigh the benefit.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1684050
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal has clear public-benefit alignment and some independently checkable governance and oversight references, but several high-value technical and adoption claims remain largely proposer-asserted while the ask is large; BEACN doctrine favors caution on treasury stewardship and evidence quality when spending upside is plausible but not fully verified.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Tx3 is presented as a framework where each protocol is described once with a verified interface definition that produces documentation, multi-language SDKs, and live JSON-RPC endpoints.
- Claims and evidence missing: Independent evidence for: The proposer argues that Cardano currently lacks a common interface mechanism across ecosystem protocols, increasing integration cost and limiting composability.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `f506ac90d0086750c41146410d2151ceb8b2fb82bc05b935909ace209ce32a2e`
- snapshot_bundle_hash: `c2e3f845fbbd1f6d788cdea6fd47df990427ed9cce2c654c6c22e28bef9e73b5`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

