# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NO**
Score: `-0.4033` (raw `-0.3833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.75`
> Reasoning layer (precomputed): The proposal has plausible public-benefit alignment and gives milestone, budget, governance, and assurance structure, but several central claims supporting the large treasury request are proposer-asserted, including recent usage, transaction share, free-tier traffic, and long-term sustainability economics; with the deterministic assessment already marking evidence as thin, a small cautionary nudge is justified rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large Treasury withdrawal request and several central claims supporting the size and urgency of the funding were not independently evidenced.

The proposal asked for 9,832,979 ADA to fund an 18-month transition of Blockfrost into a free, community-governed not-for-profit public API, including ongoing operations through the transition. It proposed milestones from Q3 2026 through 2027, including legal setup or a host agreement, a technical migration plan, a board election, transfer of source code, trademarks, domains, and associated assets, continued API service, quarterly reports, and a 99% monthly uptime SLA.

BEACN found that some important claims were supported in the proposal, including the public-good governance goal, the requested budget categories, the six-person staffing plan, the expected infrastructure cost, and the use of contracts, milestone acceptance, Intersect delivery assurance, and third-party assurer signoff. The proposal also cited independently verifiable survey links for Blockfrost’s developer adoption.

The vote turned negative because the evidence record was still thin for a Treasury action of this scale. Key claims about recent usage, transaction share, free-tier traffic, and long-term sustainability economics were proposer-asserted rather than independently supported. The review also flagged missing milestone-gated disbursement detail, missing sustainability path detail, missing independent assurance, and no clear rollback or remedy path. Because Treasury withdrawals consume shared ADA and set precedent, BEACN applied elevated scrutiny and concluded that the documented evidence did not justify a YES vote.

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
- finding: Requested: Fund an 18-month transition of Blockfrost into a free, community-governed not-for-profit public API and ongoing operations during the transition period.
- finding: Recipient: not stated in document
- finding: Stated amount: 9,832,979
- finding: Deliverables: Q3 2026: legally establish a not-for-profit entity or sign a host-organization agreement, publish technical transition architecture and migration plan, and launch a public usage dashboard., Q4 2026: hold a board election via on-chain voting under published rules and have the newly elected board assume its mandate., Q1 2027: serve all public API traffic for mainnet, preview, and preprod from the new stack, transfer Blockfrost source code, trademarks, domains, and associated assets to the governing entity, and maintain current service performance through cutover., Q2-Q3 2027: open public consultation on long-term sustainability, publish a proposal for feedback, and document the chosen direction., 2027: operate the public API at a minimum 99% monthly uptime SLA and publish quarterly reports covering technical metrics and budget summary.
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that Blockfrost will become a free, community-governed public good owned by an independent not-for-profit through transfer of source code, trademarks, domains, and associated assets.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states that Blockfrost was used by 71.5% of surveyed Cardano developers in 2025, up from 39.3% in 2022, citing Cardano Foundation developer ecosystem survey links.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal states that more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that 90% of Cardano traffic served through the Blockfrost API comes from the free tier, making the current commercial model difficult for financing public-good operation.
- missing: Independent evidence for: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal states that more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: The proposal states that 90% of Cardano traffic served through the Blockfrost API comes from the free tier, making the current commercial model difficult for financing public-good operation.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9832979
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.67
- missing: milestone-gated disbursement
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
- finding: Flag count: 2
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal states that Blockfrost will become a free, community-governed public good owned by an independent not-for-profit through transfer of source code, trademarks, domains, and associated assets." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
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
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9832979
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal states that Blockfrost will become a free, community-governed public good owned by an independent not-for-profit through transfer of source code, trademarks, domains, and associated assets." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has plausible public-benefit alignment and gives milestone, budget, governance, and assurance structure, but several central claims supporting the large treasury request are proposer-asserted, including recent usage, transaction share, free-tier traffic, and long-term sustainability economics; with the deterministic assessment already marking evidence as thin, a small cautionary nudge is justified rather than a positive adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `3c19838149675ed88fbb0d9c8d3ec86b6c14a942b91cd61fdc2c2f792a80865a`
- snapshot_bundle_hash: `331e3485cebac698e060160f01a9d949c550e62498723e49d339e40e914d2722`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1825, "NO": 0.7762, "YES": 0.0413}`

