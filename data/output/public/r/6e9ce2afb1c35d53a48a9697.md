# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.077` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7392` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the proposal identifies concrete maintenance deliverables for established open-source developer infrastructure, includes governance-process and on-chain-verifiable references, and describes custody and oversight controls; the adjustment remains small because several high-materiality adoption and delivery-history claims are proposer asserted rather than evidenced inside the document.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work itself.

The proposal asks for 540,750 ada to fund Year 2 maintenance of UTxO RPC by TxPipe, through the 2026 Treasury Reserve Smart Contract administered by Intersect on behalf of the vendor. The requested amount is broken down as 420,000 ada for the work, 105,000 ada as contingency, and 15,750 ada for Intersect administration. The proposed work covers 12 months of part-time maintainer effort, protobuf specification maintenance, SDK maintenance, community support, and AI-friendly documentation and integration resources.

Several core claims were well-supported: the budget breakdown was clear, the technical scope of UTxO RPC was described, the funded deliverables were concrete, the Intersect budget-process support threshold was independently verifiable, and the proposal identified custody, oversight, role thresholds, addresses, references, and a community audit dashboard. However, some material claims remained unsupported by independent evidence in the review, especially the claim that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node, and the claim about TxPipe’s Project Catalyst delivery history.

The review gates were strong enough to show that the proposal can be audited and that it contains real maintenance deliverables, but treasury scrutiny is higher because it spends shared ada and sets precedent. Remaining gaps included thin independent evidence, missing sustainability and cost-benefit clarity, unknown execution risk, missing independent assurance, and no clear rollback or remedy path. A directional vote would be unblocked by pinned, independently verifiable public-chain evidence for the Net Change Limit, plus stronger independent evidence for the adoption and delivery-history claims.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 540.8k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect on behalf of the vendor
- finding: Stated amount: 540750
- finding: Deliverables: 12 months of part-time maintainer work for UTxO RPC, Maintenance of the protobuf specification including protocol compatibility, versioning, and documentation, Maintenance of official SDKs including dependency updates, performance improvements, and bug fixing, Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months after closure of the existing contract; exact dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification for UTxO-based blockchains using Protocol Buffers and SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface or ecosystem standard.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories covering the core specification, SDKs, documentation, and provider integrations, and is open source under Apache 2.0.
- finding: Claim (technical, supported_in_proposal, high materiality): The funded work would cover specification maintenance, SDK maintenance, community support, and AI-friendly documentation and integration resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved framework.
- missing: Independent evidence for: UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface or ecosystem standard.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.58
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
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface or ecosystem standard." — so cost or precedent may outweigh the benefit.
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
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 540750
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the proposal identifies concrete maintenance deliverables for established open-source developer infrastructure, includes governance-process and on-chain-verifiable references, and describes custody and oversight controls; the adjustment remains small because several high-materiality adoption and delivery-history claims are proposer asserted rather than evidenced inside the document.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface or ecosystem standard.
- Claims and evidence missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `4987a07f76b9656907ea346f369fa87cec23da16a5c93d3d3afcb1a52c1f5fd6`
- snapshot_bundle_hash: `92a6eb8a17bc4ea57549f9e418b56fa7c9ced271f9bddd10db84aafc985b14e4`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `d68b33ee7989803aaecd7edc03d77c134a98a7f1`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.1706, "YES": 0.3246}`

