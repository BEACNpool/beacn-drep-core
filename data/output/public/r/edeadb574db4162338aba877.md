# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (binding treasury composite; advisory raw signal `-0.21`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show plausible public-benefit alignment for established Cardano infrastructure and include concrete milestones, governance mechanisms, and budget categories, while the deterministic assessment already captures that evidence is thin and incomplete; under the doctrine, unresolved independently verified diligence should remain a needs-more-info state rather than receive an additional directional nudge.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the idea.

The proposal requests 9,832,979 ADA to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, with Intersect administering treasury management and delivery assurance. The plan includes legal setup or a host-organization agreement, a technical migration plan, a usage dashboard, on-chain board election, public API service for mainnet, preview, and preprod, asset transfers, public consultation, a sustainability proposal, 99% monthly uptime, and quarterly technical and budget reporting over an 18-month period.

Some core claims were supported well enough for review. The proposal establishes Blockfrost as a hosted REST interface for Cardano developers, links its developer-survey adoption claims to Cardano Foundation survey pages, commits to transferring source code and related assets, describes a five-seat governance model, explains the budget split, and describes delivery assurance and treasury oversight mechanisms. But several important claims remain too thin for a treasury decision: the reported 781k visitors, 1.84 billion API requests, nearly 700 requests per second, over 7 TB of API data, and the claim that Blockfrost submits more than 50% of transactions in most Cardano epochs were not independently evidenced here. The review also found missing clarity on sustainability, cost-benefit, independent assurance, and rollback or remedy paths.

The hold would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus replayable public evidence for the major usage and transaction-share claims, clearer sustainability and cost-benefit support, and stronger assurance and remedy details. Until then, BEACN cannot responsibly turn this into a YES or NO vote.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 9.83M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Transition Blockfrost into a free, community-governed public good under an independent not-for-profit, including 18 months of transition and operations funding.
- finding: Recipient: Input Output / Blockfrost transition project, with Intersect administering treasury management and delivery assurance as described.
- finding: Stated amount: 9,832,979
- finding: Deliverables: Legally establish a not-for-profit entity or sign a host-organization agreement under the preliminary board., Publish technical transition architecture and migration plan for community review., Launch a public usage dashboard., Hold a board election via on-chain voting under published rules and install the elected board., Serve all public API traffic for mainnet, preview, and preprod from the new stack., Transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity., Open a public consultation and publish a long-term sustainability proposal., Operate the public API at a minimum 99% monthly uptime SLA and publish quarterly technical and budget reports.
- finding: Deadline/expiry: 18-month transition and operations period, with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is presented as a hosted REST interface that lets Cardano developers read from and interact with the blockchain without running their own infrastructure or node.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states that Blockfrost developer survey adoption grew from 39.3% in 2022 to 71.5% in 2025 and links to the Cardano Foundation survey pages for each year.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal states that more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal claims 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model cannot sustainably finance that public-good operation.
- missing: Independent evidence for: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal states that more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: The proposal claims 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model cannot sustainably finance that public-good operation.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9832979
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.68
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 2
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Blockfrost is presented as a hosted REST interface that lets Cardano developers read from and interact with the blockchain without running their own infrastructure or node." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
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
- Flag score present (3), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9832979
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is presented as a hosted REST interface that lets Cardano developers read from and interact with the blockchain without running their own infrastructure or node." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `5f5c582d46f010f4d9c768cadad3a7f87f99ecfa2f5261d5e3e82d7f5416c3b5`
- snapshot_bundle_hash: `d850bc01c63351118c068b8c5d41842363e14c3fb29d555431dee4bf6c5c3442`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `880436a840989202a38cccce66fd8f1cbf15004d`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

