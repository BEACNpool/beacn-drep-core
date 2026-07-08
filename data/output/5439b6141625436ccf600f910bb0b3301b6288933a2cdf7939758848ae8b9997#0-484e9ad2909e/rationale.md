# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was missing baseline evidence needed for a responsible treasury decision. This is a conservative, evidence-based hold, not a rejection of Blockfrost’s usefulness or the idea of a not-for-profit transition.

The proposal requested funding for an 18-month transition and operation of Blockfrost as a free, community-governed not-for-profit public API for Cardano, with a stated amount of 9,832,979 ADA and milestones running from Q3 2026 through 2027. It claimed Blockfrost is widely used, including a cited rise in Cardano Foundation developer ecosystem survey usage from 39.3% in 2022 to 71.5% in 2025, and it described plans for a not-for-profit entity, public dashboard, board election, asset transfer, sustainability consultation, uptime SLA, and quarterly reporting.

Some proposal claims were supported inside the proposal, including the requested budget split across staffing, operations and infrastructure, and legal and accounting, and the governance model with a five-seat board. The strongest supported YES case was the independently verifiable developer survey usage claim. However, several material claims remained unsupported by independent evidence, including claims about Blockfrost’s reliability, recent traffic volumes, share of Cardano transaction submissions, execution risk, and mitigation evidence.

The review gates did not clear enough evidence for a directional vote. Intake was blocked because `treasury_amount_lovelace` was missing for a treasury withdrawal, claims and evidence were thin, treasury analysis was incomplete, and risk review was thin. A YES or NO vote would need the missing baseline fields, a complete proposal summary, full budget analysis, feasibility and risk analysis, alternatives and failure-mode analysis, community impact analysis, milestone-gated disbursement evidence, and independent assurance.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Fund an 18-month transition and operation of Blockfrost as a free, community-governed not-for-profit public API for Cardano.
- finding: Recipient: not stated in document
- finding: Stated amount: 9,832,979
- finding: Deliverables: Establish a not-for-profit entity or host-organization agreement and publish a technical transition architecture and migration plan in Q3 2026., Launch a public usage dashboard in Q3 2026., Hold a board election via on-chain voting under published rules in Q4 2026., Serve all public API traffic for mainnet, preview, and preprod from the new stack in Q1 2027., Transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity in Q1 2027., Open a public sustainability consultation and publish a long-term sustainability proposal in Q2-Q3 2027., Operate the public API at a minimum 99% monthly uptime SLA and publish quarterly technical and budget reports during 2027.
- finding: Deadline/expiry: 18 months, with milestones from Q3 2026 through 2027
- finding: Claim (adoption, proposer_asserted, high materiality): Blockfrost is presented as a reliable hosted REST interface that lets developers interact with Cardano without running their own node infrastructure.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states that Blockfrost usage in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025, with links to the survey pages.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal states that more than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,832,979 ADA, equivalent to 1,868,266 USD at 0.19 USD per ADA, for 18 months of transition and operations.
- missing: Independent evidence for: Blockfrost is presented as a reliable hosted REST interface that lets developers interact with Cardano without running their own node infrastructure.
- missing: Independent evidence for: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal states that more than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.74
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal states that Blockfrost usage in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025, with links to the survey pages." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost is presented as a reliable hosted REST interface that lets developers interact with Cardano without running their own node infrastructure." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: evidence is too thin for a directional vote while 1 blocker(s) remain open.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal states that Blockfrost usage in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025, with links to the survey pages." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: Blockfrost is presented as a reliable hosted REST interface that lets developers interact with Cardano without running their own node infrastructure.
- Claims and evidence missing: Independent evidence for: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `484e9ad2909e0bd9cb06f135ebbb3eeb201333dfc892cbe5c681b6fb1b7e4a95`
- snapshot_bundle_hash: `7c058317325d412be82cfa35ebc043eb1d73a1ca2609f961dd00e5d8058ea3cc`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

