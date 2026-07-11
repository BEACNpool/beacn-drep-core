# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#9
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a high-impact treasury withdrawal and the required deep-research dossier was not complete enough to support a directional vote.

The action requested 1,684,050 ada for Tx3 by TxPipe, described as an open API layer for Cardano dApp protocols. The proposal says the funding would cover 12 additional protocol onboardings over 12 months, developer and agent coverage, an MCP server, protocol skills packaging, agent-first documentation, and related open API work. It also states that the total includes 1,308,000 ada for the work, a 327,000 ada contingency reserve, and a 49,050 ada Intersect administration fee.

Some claims were supported in the proposal, including the budget structure, the 12-month onboarding plan, and the use of Intersect-managed smart contracts with milestone-based disbursement controls, oversight, and a public dashboard. Other claims needed stronger independent evidence before BEACN could rely on them, including that Tx3 provides a standard open-source interface with documentation, multi-language SDKs, and live RPC endpoints, and that Cardano currently lacks a common interface mechanism across protocols.

This is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would be unblocked by a completed deep-research dossier, clearer treasury analysis on sustainability and cost-benefit, independent assurance, and a rollback or remedy path for execution risk. Until those gates pass, BEACN cannot responsibly vote yes or no on spending shared treasury ada.

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
- finding: Requested: Treasury withdrawal to fund Tx3 by TxPipe: Open API Layer for Cardano's dApp Protocols, described as an open standardized interface across Cardano on-chain protocols with developer and AI-agent support.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v for administration on behalf of the vendor TxPipe.
- finding: Stated amount: 1,684,050
- finding: Deliverables: 12 additional protocol onboardings over 12 months, described as 3 per quarter, Full developer and agent coverage for onboarded protocols, MCP server for agents to discover and call published protocols, Protocol skills framework and packaging operations, Agent-first documentation and LLM-structured documentation, Open API layer work package for Cardano protocols
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Tx3 is intended to provide a standard open-source interface for Cardano protocols, including documentation, multi-language SDKs, and live RPC endpoints.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states that Catalyst Fund 14 has already put Tx3's developer layer into production with 5 protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal claims there is currently no common interface mechanism across the Cardano ecosystem, forcing integrators to relearn each protocol and rebuild understanding independently.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal says it will fund 12 additional protocol onboardings, at 3 per quarter, with developer and agent coverage.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal claims the work aligns with Intersect budget Pillar 2 on Adoption & Utility and Pillar 4 on Community & Ecosystem Growth.
- missing: Independent evidence for: Tx3 is intended to provide a standard open-source interface for Cardano protocols, including documentation, multi-language SDKs, and live RPC endpoints.
- missing: Independent evidence for: The proposal claims there is currently no common interface mechanism across the Cardano ecosystem, forcing integrators to relearn each protocol and rebuild understanding independently.
- missing: Independent evidence for: The proposal claims the work aligns with Intersect budget Pillar 2 on Adoption & Utility and Pillar 4 on Community & Ecosystem Growth.
- missing: Independent evidence for: The proposal states TxPipe has received funding through 30 Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Tx3 is intended to provide a standard open-source interface for Cardano protocols, including documentation, multi-language SDKs, and live RPC endpoints." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: Tx3 is intended to provide a standard open-source interface for Cardano protocols, including documentation, multi-language SDKs, and live RPC endpoints.
- Claims and evidence missing: Independent evidence for: The proposal claims there is currently no common interface mechanism across the Cardano ecosystem, forcing integrators to relearn each protocol and rebuild understanding independently.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.

## Reproducibility
- input_hash: `e22354bf0fce66e502300e81008df0cfc7af3de5733ecbb82b3b97cf7d533ee8`
- snapshot_bundle_hash: `bc0991b53b79483a4ff567adbe9e5a7b46f73578555aecec0b8066930504a0d2`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

