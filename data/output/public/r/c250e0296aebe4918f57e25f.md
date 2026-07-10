# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sj72rg72
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has relatively concrete deliverables, governance process references, NCL assertions, and oversight mechanics, but several core value claims about ecosystem need, AI-agent demand, and integration impact remain largely proposer-asserted, while the ask is large for software and documentation work under BEACN's post-AI cost caution. A small negative nudge is justified for treasury stewardship and evidence quality without overriding the deterministic assessment.

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Withdraw 1,684,050 ada for Tx3 by TxPipe: Open API Layer for Cardano's dApp P. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Tx3 by TxPipe, described as an open API layer for Cardano dApp protocols. It asks the treasury for 1,684,050 ADA. The strongest grounded claim is: The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee.

A material claim remains proposer-asserted or thinly supported: Tx3 is intended to provide a standard, open-source interface to Cardano protocols, including documentation, multi-language SDKs, and live RPC endpoints. Reason code: VERIFIED_NCL_REQUIRED.

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
- finding: Requested: Treasury withdrawal to fund Tx3 by TxPipe, described as an open API layer for Cardano dApp protocols.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor TxPipe
- finding: Stated amount: 1,684,050
- finding: Deliverables: Open, standardized interface across Cardano's leading on-chain protocols, 12 additional protocol onboardings over 12 months, with 3 per quarter, Full developer and agent coverage for onboarded protocols, MCP server for agents to discover and call published protocols, Skill framework and agent-first documentation, Documentation, auto-generated SDKs in multiple languages, and live JSON-RPC endpoints
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Tx3 is intended to provide a standard, open-source interface to Cardano protocols, including documentation, multi-language SDKs, and live RPC endpoints.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn protocols, rebuild understanding independently, and face higher integration costs.
- finding: Claim (adoption, independently_verifiable, high materiality): TxPipe says Catalyst Fund 14 has already put the Tx3 developer layer into production with 5 protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal funds 12 additional protocol onboardings, at a rate of 3 per quarter, with developer and agent coverage.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal claims protocols such as Strike Finance, Indigo Protocol, VyFinance, Bodega Market, and Fluid Tokens are already accessible through Tx3.
- missing: Independent evidence for: Tx3 is intended to provide a standard, open-source interface to Cardano protocols, including documentation, multi-language SDKs, and live RPC endpoints.
- missing: Independent evidence for: The proposal states that there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn protocols, rebuild understanding independently, and face higher integration costs.
- missing: Independent evidence for: TxPipe is reported to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 successfully delivered and 4 under development and on schedule, plus Intersect 2025 open-source maintenance funding for Pallas, Dolos, and UTxO RPC.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Tx3 is intended to provide a standard, open-source interface to Cardano protocols, including documentation, multi-language SDKs, and live RPC endpoints." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has relatively concrete deliverables, governance process references, NCL assertions, and oversight mechanics, but several core value claims about ecosystem need, AI-agent demand, and integration impact remain largely proposer-asserted, while the ask is large for software and documentation work under BEACN's post-AI cost caution. A small negative nudge is justified for treasury stewardship and evidence quality without overriding the deterministic assessment.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Tx3 is intended to provide a standard, open-source interface to Cardano protocols, including documentation, multi-language SDKs, and live RPC endpoints.
- Claims and evidence missing: Independent evidence for: The proposal states that there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn protocols, rebuild understanding independently, and face higher integration costs.
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
- snapshot_bundle_hash: `7bb8e6624d2c0f054ffeb7679e5af4f19592dc217feef20d8b48737d95e44c03`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

