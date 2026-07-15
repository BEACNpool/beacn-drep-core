# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1359` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `-0.01` recorded, not added) | Confidence: `0.754` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show useful open-source infrastructure, verifiable governance-process references, and structured fund controls, but the cost basis is thin for a part-time maintainer and the document does not explain how the AI-friendly work affects post-AI cost expectations. A small cautionary nudge is justified without overriding the engine's completed gates.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Dolos or its usefulness.

The action asks to withdraw 540,750 ada to fund Year 2 maintenance of Dolos by TxPipe, administered through the Intersect Treasury Reserve Smart Contract stake address. The proposal says this covers 420,000 ada for 12 months of part-time maintainer work, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. The requested work includes dependency updates, Cardano protocol compatibility, performance improvements, bug fixes, documentation, issue triage, contribution review, community communication, AI-friendly documentation, and milestone-based disbursement controls.

Several claims were supported well enough for review: the requested budget structure, the maintainer scope, the Intersect budget-process support claim, the use of treasury smart-contract administration, and the existence of public tracking. But important technical claims remained too thin or only proposer-asserted, including that Dolos is a lightweight Rust data node providing efficient chain-data access without full-node overhead, and that it exposes the stated query interfaces. The review also flagged missing sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path.

Because this is a treasury withdrawal, BEACN applies elevated scrutiny. The proposal had a pinned, replayable anchor document and a credible strongest YES case, but treasury spending consumes shared ada and sets precedent. A directional vote would be unblocked by pinned, independently verifiable public-chain evidence for the applicable Net Change Limit, plus stronger independent evidence for the key technical claims and clearer support for sustainability, cost-benefit, assurance, and remedy planning.

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
- finding: Requested: Fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address for administration on behalf of the vendor TxPipe
- finding: Stated amount: 540750
- finding: Deliverables: 12 months of part-time maintainer coverage for Dolos after the existing contract closes, Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public developer communication, AI-friendly documentation and integration resources for AI-driven development workflows, Administration through Intersect treasury smart contracts with milestone-based disbursement controls
- finding: Deadline/expiry: 12 months; grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for Dolos maintenance, with a total withdrawal of 540,750 ADA including a 15,750 ADA Intersect administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is described as a lightweight Cardano data node built in Rust that provides efficient chain-data access without the overhead of traditional full nodes.
- finding: Claim (technical, proposer_asserted, medium materiality): Dolos exposes five query interfaces, including Mini-Blockfrost HTTP, UTxO-RPC gRPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with Cardano-cli, Ogmios, and other tooling.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states that Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors, and links to the Dolos GitHub repository.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope covers dependency updates, protocol compatibility, performance improvements, bug fixes, documentation, issue triage, contribution review, community communication, and AI-friendly documentation and integration resources.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and includes references to voting records and audited results.
- missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides efficient chain-data access without the overhead of traditional full nodes.
- missing: Independent evidence for: Dolos exposes five query interfaces, including Mini-Blockfrost HTTP, UTxO-RPC gRPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with Cardano-cli, Ogmios, and other tooling.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Financial confidence: 0.68
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for Dolos maintenance, with a total withdrawal of 540,750 ADA including a 15,750 ADA Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Dolos is described as a lightweight Cardano data node built in Rust that provides efficient chain-data access without the overhead of traditional full nodes." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for Dolos maintenance, with a total withdrawal of 540,750 ADA including a 15,750 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.010 (display cap ±0.05) and had zero influence on the binding score: The claims show useful open-source infrastructure, verifiable governance-process references, and structured fund controls, but the cost basis is thin for a part-time maintainer and the document does not explain how the AI-friendly work affects post-AI cost expectations. A small cautionary nudge is justified without overriding the engine's completed gates.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides efficient chain-data access without the overhead of traditional full nodes.
- Claims and evidence missing: Independent evidence for: Dolos exposes five query interfaces, including Mini-Blockfrost HTTP, UTxO-RPC gRPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with Cardano-cli, Ogmios, and other tooling.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `dd9bc3311e28c42ee8642ac26143eda8eee991a91bcdf2f43cc4d160bd4410b8`
- snapshot_bundle_hash: `84eab42b334dbf73286ceb929e50bf17a20be1184c0e8ab25c9067e1abc0f97b`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `880436a840989202a38cccce66fd8f1cbf15004d`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5085, "NO": 0.1099, "YES": 0.3816}`

