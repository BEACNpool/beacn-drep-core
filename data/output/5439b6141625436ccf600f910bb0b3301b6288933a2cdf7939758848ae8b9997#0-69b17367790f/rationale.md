# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (binding treasury composite; advisory raw signal `-0.21`; LLM lean `-0.02` recorded, not added) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show strong public-benefit alignment and some independently checkable adoption evidence, but several highly material adoption, cost, and sustainability assertions are proposer-stated rather than independently supported in the document. Given the assessment that claims and evidence are thin and the action is a large treasury withdrawal, a small cautionary nudge is justified without treating missing diligence as affirmative evidence against the proposal.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the idea.

The proposal asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, with 18 months of funding for staffing, operations, infrastructure, legal work, and accounting. It lays out milestones from Q3 2026 through 2027, including legal setup, a migration plan, a public usage dashboard, an on-chain board election, transfer of source code and associated assets, public API operation, uptime commitments, and quarterly reporting.

Some parts were well supported. The anchor document was pinned and replayable, and the proposal cited Cardano Foundation developer survey links showing Blockfrost hosted-platform usage rising from 39.3% in 2022 to 71.5% in 2025. Other material claims were still only proposer-stated or thinly evidenced, including reliability claims, some adoption and traffic figures, the share of transactions submitted through Blockfrost, the free-tier traffic claim, and parts of the sustainability case. The review also found missing cost-benefit clarity, missing sustainability path, missing independent assurance, and no clear rollback or remedy path.

The review gates show why BEACN held. The proposal cleared the basic intake and had a pinned source anchor, but treasury withdrawals require elevated scrutiny because they spend shared ADA and set precedent. Execution risk was rated medium, the treasury flow signal was stressed, and confidence was reduced by a flag score. A YES case exists around public-good alignment and independently checkable adoption evidence, but BEACN needs the verified Net Change Limit, stronger independent evidence for material claims, clearer cost-benefit and sustainability details, and stronger assurance and remedy plans before casting a directional vote.

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
- finding: Requested: Transition Blockfrost into a free, community-governed public good under an independent not-for-profit and fund 18 months of transition and operations.
- finding: Recipient: Input Output Global / Blockfrost transition under Intersect-administered treasury governance, with eventual governing not-for-profit entity; exact withdrawal recipient address not stated in document.
- finding: Stated amount: 9,832,979
- finding: Deliverables: Not-for-profit entity legally established or host-organization agreement signed under the preliminary board in Q3 2026., Technical transition architecture and migration plan published for community review in Q3 2026., Public usage dashboard live in Q3 2026., Board election held via on-chain voting under public rules in Q4 2026., Newly elected board formally assumes its mandate from the preliminary board in Q4 2026., All public API traffic for mainnet, preview, and preprod served by the new stack in Q1 2027., Blockfrost source code, trademarks, domain names, and associated assets legally transferred to the governing entity in Q1 2027., Public API operated at minimum 99% monthly uptime SLA during 2027 operational milestones., Quarterly reports published covering technical metrics and budget summary.
- finding: Deadline/expiry: 18-month funding period, with named milestones from Q3 2026 through 2027
- finding: Claim (technical, proposer_asserted, high materiality): Blockfrost is presented as a reliable hosted REST interface that lets Cardano developers read from and interact with the chain without running and maintaining their own node.
- finding: Claim (other, proposer_asserted, medium materiality): The proposal says Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- finding: Claim (adoption, independently_verifiable, high materiality): The document cites Cardano Foundation developer ecosystem survey links showing Blockfrost hosted-platform usage rising from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: Blockfrost is presented as a reliable hosted REST interface that lets Cardano developers read from and interact with the chain without running and maintaining their own node.
- missing: Independent evidence for: The proposal says Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- missing: Independent evidence for: The proposer states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- missing: Independent evidence for: The proposer states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
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
- finding: Strongest YES: the proposal substantiates "The document cites Cardano Foundation developer ecosystem survey links showing Blockfrost hosted-platform usage rising from 39.3% in 2022 to 71.5% in 2025." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost is presented as a reliable hosted REST interface that lets Cardano developers read from and interact with the chain without running and maintaining their own node." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The document cites Cardano Foundation developer ecosystem survey links showing Blockfrost hosted-platform usage rising from 39.3% in 2022 to 71.5% in 2025." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims show strong public-benefit alignment and some independently checkable adoption evidence, but several highly material adoption, cost, and sustainability assertions are proposer-stated rather than independently supported in the document. Given the assessment that claims and evidence are thin and the action is a large treasury withdrawal, a small cautionary nudge is justified without treating missing diligence as affirmative evidence against the proposal.
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
- Claims and evidence missing: Independent evidence for: Blockfrost is presented as a reliable hosted REST interface that lets Cardano developers read from and interact with the chain without running and maintaining their own node.
- Claims and evidence missing: Independent evidence for: The proposal says Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `69b17367790fde88073c9fa6b07b302f95aaf90cecf2dc3b54274efd9eaaaff4`
- snapshot_bundle_hash: `3cbadb44a78d9a1effa1cd8a02672ed0269d838d36e4d41a8da5545b26cce240`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `d68b33ee7989803aaecd7edc03d77c134a98a7f1`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

