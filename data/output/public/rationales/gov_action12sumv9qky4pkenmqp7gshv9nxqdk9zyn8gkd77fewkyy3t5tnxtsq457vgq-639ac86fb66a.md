# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NO**
Score: `-0.5133` (raw `-0.4833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.49` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit infrastructure alignment, but the deterministic assessment identifies thin evidence and missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN doctrine, treasury stewardship and evidence quality outweigh public-benefit growth when verification is incomplete, so a small cautionary negative nudge is justified without overriding the engine's blocked status.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal request, and the review found too many unresolved evidence, budget, feasibility, risk, and impact gaps to justify spending 9,832,979 ADA from shared treasury funds.

The proposal asked to fund Blockfrost’s 18-month transition into a free, community-governed not-for-profit public API for Cardano, with milestones from Q3 2026 through 2027. It proposed creating or hosting a not-for-profit entity, publishing a transition architecture and migration plan, holding an on-chain board election, transferring Blockfrost source code and related assets to the governing entity, consulting publicly on long-term sustainability, and operating the public API with a 99% monthly uptime SLA and quarterly technical and budget reports.

Some claims were supported in the proposal. The review found replayable evidence for the claim that Blockfrost usage in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025. The proposal also supported its commitments to transfer intellectual property, describe delivery and assurance arrangements, return some unspent infrastructure funds, and publish quarterly reports. But several important claims remained proposer-asserted or thinly evidenced, including usage figures such as 781k unique visitors, 1.84 billion API requests, most-epoch transaction submission share, and the basic reliability claim about Blockfrost as hosted infrastructure.

The review gates did not clear the higher bar required for treasury spending. The anchor document was available, but the treasury analysis was incomplete, including missing line-item budget and milestone-gated disbursement detail. Risk review was thin, with missing mitigation evidence and independent assurance. The synthesis was blocked by missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis. BEACN’s NO is therefore a treasury-stewardship vote: the public-benefit case was plausible, but the evidence package was not strong enough for this amount of ADA.

## Review Tree
- overall_status: `blocked`

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Fund Blockfrost's transition into a free, community-governed not-for-profit public API for Cardano, including 18 months of transition and operations.
- finding: Recipient: Input Output / Blockfrost transition administered through Intersect and Cardano Development Holdings arrangements as described in the document
- finding: Stated amount: 9832979
- finding: Deliverables: Establish or host a not-for-profit entity and publish transition architecture, migration plan, and public usage dashboard in Q3 2026., Hold a board election via on-chain voting under published rules in Q4 2026., Serve all public API traffic from the new stack and legally transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity in Q1 2027., Run a public sustainability consultation and publish the chosen long-term direction in Q2-Q3 2027., Operate the public API at a minimum 99% monthly uptime SLA with quarterly technical and budget reports during 2027.
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (technical, proposer_asserted, high materiality): Blockfrost is presented as a reliable hosted REST interface that lets Cardano developers interact with the blockchain without running their own infrastructure or node.
- finding: Claim (adoption, independently_verifiable, high materiality): The document states that Blockfrost usage in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025, with links to each annual survey result.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): The document claims that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says more than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- finding: Claim (economic, proposer_asserted, high materiality): The proposer claims 90% of all Cardano traffic served through the Blockfrost API comes from the free tier, making the commercial model difficult for financing the public-good operation.
- missing: Independent evidence for: Blockfrost is presented as a reliable hosted REST interface that lets Cardano developers interact with the blockchain without running their own infrastructure or node.
- missing: Independent evidence for: The proposer states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- missing: Independent evidence for: The document claims that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal says more than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 9.83M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The document states that Blockfrost usage in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025, with links to each annual survey result." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost is presented as a reliable hosted REST interface that lets Cardano developers interact with the blockchain without running their own infrastructure or node." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9.83M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The document states that Blockfrost usage in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025, with links to each annual survey result." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show plausible public-benefit infrastructure alignment, but the deterministic assessment identifies thin evidence and missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN doctrine, treasury stewardship and evidence quality outweigh public-benefit growth when verification is incomplete, so a small cautionary negative nudge is justified without overriding the engine's blocked status.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Blockfrost is presented as a reliable hosted REST interface that lets Cardano developers interact with the blockchain without running their own infrastructure or node.
- Claims and evidence missing: Independent evidence for: The proposer states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `639ac86fb66a8a42a6dfd8e2240eca438e07c4cf9f787a82efed92c7e201d051`
- snapshot_bundle_hash: `7d5f566822a1f8ada1f651e6956597149bebb4ae2075b651a9997d3fe6ae31a5`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1217`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2119, "NO": 0.7472, "YES": 0.0409}`

