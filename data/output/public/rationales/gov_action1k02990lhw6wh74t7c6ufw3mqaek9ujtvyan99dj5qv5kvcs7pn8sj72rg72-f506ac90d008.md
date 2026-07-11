# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sj72rg72
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show plausible public-benefit ecosystem growth and several independently checkable governance and NCL references, while the deterministic assessment has already marked claims, treasury analysis, and risk review complete. No additional doctrine-based nudge is justified beyond the engine because the high-level ecosystem and AI-agent benefits remain partly proposer-asserted and the large treasury spend is already covered by the mechanical review.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the project.

The action asks to withdraw 1,684,050 ada to fund Tx3 by TxPipe over 12 months, described as an open API layer for Cardano dApp protocols. The proposal says the funding would support a standardized protocol interface, documentation, auto-generated SDKs, live JSON-RPC endpoints, agent-facing documentation, protocol skills packaging, an MCP server, and 12 additional protocol onboardings at 3 per quarter.

Several core claims were supported well enough for review: the budget structure was stated in the proposal, the Tx3 framework was described clearly, the anchor document was pinned and replayable, TxPipe’s existing production work through Catalyst Fund 14 and 5 live registry protocols was independently verifiable, and the proposal stated it had passed the required 67% Intersect Budget Process Hydra Voting threshold. But other material claims remained unsupported by independent evidence, including the claim that Cardano currently lacks a common interface mechanism across protocols and the claim that AI-agent on-chain workflows create specific transaction risks requiring shared auditable intent interfaces.

The review gates showed enough substance to take the proposal seriously, but not enough to cast a YES or NO on a treasury withdrawal. Treasury actions require elevated scrutiny because they spend shared ada and create precedent. The remaining evidence needed to unblock a directional vote is public, independently verifiable confirmation of the applicable Net Change Limit, plus stronger support for the missing treasury and risk evidence: sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path.

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
- finding: Requested: Fund Tx3 by TxPipe, described as an open API layer for Cardano dApp protocols with developer and AI-agent-facing infrastructure.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe as vendor
- finding: Stated amount: 1,684,050
- finding: Deliverables: Open, standardized interface across Cardano on-chain protocols, Documentation, auto-generated SDKs in multiple languages, and live JSON-RPC endpoints, Agent-first documentation, Protocol skills packaging operations, MCP server for agents to discover and call published protocols, 12 additional protocol onboardings, 3 per quarter, with developer and agent coverage
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months to deliver an open standardized interface across Cardano protocols.
- finding: Claim (technical, supported_in_proposal, high materiality): Tx3 is described as a framework where each protocol is defined once and the framework generates documentation, multi-language SDKs, and live JSON-RPC endpoints.
- finding: Claim (adoption, independently_verifiable, high materiality): TxPipe has already put the developer layer into production through Catalyst Fund 14 with 5 protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal will fund 12 additional protocol onboardings, at 3 per quarter, with full developer and agent coverage.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states that there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and making composability impractical.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal claims AI-agent on-chain workflows create risk because hallucinated blockchain transactions can move assets irreversibly, so shared auditable intent interfaces are needed.
- missing: Independent evidence for: The proposal states that there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and making composability impractical.
- missing: Independent evidence for: The proposal claims AI-agent on-chain workflows create risk because hallucinated blockchain transactions can move assets irreversibly, so shared auditable intent interfaces are needed.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule, plus 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC that is being delivered on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months to deliver an open standardized interface across Cardano protocols." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and making composability impractical." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months to deliver an open standardized interface across Cardano protocols." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal states that there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and making composability impractical.
- Claims and evidence missing: Independent evidence for: The proposal claims AI-agent on-chain workflows create risk because hallucinated blockchain transactions can move assets irreversibly, so shared auditable intent interfaces are needed.
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
- snapshot_bundle_hash: `66af02984c7f3ce185a6e1c8f399202729941c8def610bbef319c85e2464cbcf`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

