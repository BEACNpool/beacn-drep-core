# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (binding treasury composite; advisory raw signal `-0.66`; LLM lean `-0.02` recorded, not added) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show a plausible public-benefit infrastructure case, but several high-materiality usage, transaction-share, free-tier, and sustainability claims are proposer-asserted while the deterministic assessment already marks claims and evidence as thin and overall status incomplete. Under BEACN's hierarchy, treasury stewardship and evidence quality justify only a small cautionary nudge rather than a stronger directional judgment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and the required Net Change Limit was not pinned and independently verified from public chain evidence. That blocks a directional treasury vote under BEACN’s rules, even though the proposal presents a plausible public-good case for Blockfrost.

The action asks for 9,832,979 ADA to fund 18 months of transition and operations, moving Blockfrost into a free, community-governed not-for-profit public API for Cardano. The proposer commits to legal setup or a host-organization agreement, a technical transition plan, a public usage dashboard, an on-chain board election, migration of public API traffic, transfer of source code and related assets, sustainability consultation, quarterly reporting, and a 99% monthly uptime SLA during 2027. The proposal also gives a budget of $1,478,266 for staffing, $360,000 for operations and infrastructure, and $30,000 for legal and accounting.

Some claims were well-supported in the proposal: the funding amount, the description of Blockfrost as hosted Cardano API infrastructure, the planned asset transfer to a community-governed entity, the proposed board structure, and the budget categories. The adoption claim based on Cardano Foundation developer survey figures was marked independently verifiable. But several high-materiality claims remained proposer-asserted, including last month’s traffic figures, the claim that more than 50% of Cardano transactions are submitted through Blockfrost in most epochs, and the claim that 90% of Cardano traffic served through Blockfrost comes from the free tier. The review also found thin claims-and-evidence status, missing sustainability path, missing cost-benefit clarity, missing independent assurance, and no clear rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the public-good argument. A directional vote would be unblocked by the applicable Net Change Limit being pinned and independently verified from public chain evidence, along with stronger independent evidence for the key usage, transaction-share, free-tier, sustainability, assurance, and remedy claims that materially affect treasury risk.

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
- finding: Requested: Transition Blockfrost into a free, community-governed not-for-profit public API/public good for Cardano, including 18 months of transition and operations.
- finding: Recipient: Input Output / Blockfrost transition under Intersect/CDH contract and treasury smart-contract administration
- finding: Stated amount: 9,832,979 ADA
- finding: Deliverables: Legally establish a not-for-profit entity or sign a host-organization agreement under a preliminary board in Q3 2026., Publish technical transition architecture and migration plan for community review in Q3 2026., Launch a public usage dashboard in Q3 2026., Hold a board election via on-chain voting under published rules in Q4 2026., Serve all public API traffic for mainnet, preview, and preprod from the new stack in Q1 2027., Transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity in Q1 2027., Open a public sustainability consultation and publish a long-term model proposal in Q2-Q3 2027., Operate the public API at a minimum 99% monthly uptime SLA during 2027 and publish quarterly technical and budget reports.
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,832,979 ADA, equivalent to $1,868,266 at $0.19 per ADA, to fund 18 months of Blockfrost transition and operations.
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers interact with Cardano without running their own node infrastructure.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposer says Blockfrost adoption in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025, with links to the survey pages.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer says Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer says more than 50% of all transactions are submitted through Blockfrost in most Cardano epochs.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has struggled to finance that public-good operation.
- missing: Independent evidence for: The proposer says Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposer says more than 50% of all transactions are submitted through Blockfrost in most Cardano epochs.
- missing: Independent evidence for: The proposal states that 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has struggled to finance that public-good operation.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,832,979 ADA, equivalent to $1,868,266 at $0.19 per ADA, to fund 18 months of Blockfrost transition and operations." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer says Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,832,979 ADA, equivalent to $1,868,266 at $0.19 per ADA, to fund 18 months of Blockfrost transition and operations." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims show a plausible public-benefit infrastructure case, but several high-materiality usage, transaction-share, free-tier, and sustainability claims are proposer-asserted while the deterministic assessment already marks claims and evidence as thin and overall status incomplete. Under BEACN's hierarchy, treasury stewardship and evidence quality justify only a small cautionary nudge rather than a stronger directional judgment.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 50% of rolling available capacity.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer says Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: The proposer says more than 50% of all transactions are submitted through Blockfrost in most Cardano epochs.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `71b262d697ef58b0de3f106a8efb61b1a873242bba7de7a7afd4cd1305c2e8ea`
- snapshot_bundle_hash: `ed252f6f5a59e70ea1e3079168754b5978627618cf10d577a99977a9031e3b38`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

