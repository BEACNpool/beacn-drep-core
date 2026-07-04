# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NO**
Score: `-0.5133` (raw `-0.4833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.64` | Readiness: `0.75`
> Reasoning layer (precomputed): The proposal has strong public-benefit alignment and some checkable governance and usage references, but the deterministic assessment marks claims and evidence as thin and treasury analysis incomplete for a large treasury withdrawal. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NO because this is a large treasury withdrawal and the review found the evidence and treasury diligence too thin for the amount requested.

The action asked for 9,832,979 ADA to transition Blockfrost into a free, community-governed not-for-profit public API for Cardano and fund 18 months of transition and operations. The proposal claims Blockfrost is important public infrastructure, widely used by developers, and heavily relied on for free-tier Cardano traffic. Some parts were well-supported in the proposal, including the description of Blockfrost as a reliable hosted REST interface, the commitment to transfer source code, trademarks, domains, and related assets to the new governing entity, the proposed board structure, the requested budget, and quarterly reporting. The review also noted independently checkable references for developer survey adoption and Intersect’s treasury-management process.

The main weaknesses were in the high-impact claims and treasury controls. Independent evidence was missing for the claimed recent traffic numbers, including 781,000 unique visitors, 1.84 billion API requests, nearly 700 requests per second, and more than 7 TB of API data, and also for the claim that more than 50% of Cardano transactions are submitted through Blockfrost in most epochs. The treasury analysis was incomplete, with missing detail on milestone-gated disbursement and the long-term sustainability path. The risk review also lacked independent assurance and a rollback or remedy path.

Several gates did pass: the pinned anchor document was available, the action could be reviewed, and the strongest YES case was recognized, namely that Blockfrost’s public infrastructure value was substantiated enough to clear evidence gates. But treasury withdrawal actions require elevated scrutiny because they spend shared ADA and set precedent. With thin evidence, incomplete treasury diligence, unknown execution risk, and a caution signal on treasury flow, BEACN’s evidence-based conclusion was NO.

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
- finding: Deep research dossier: required
- finding: Requested: Transition Blockfrost into a free, community-governed not-for-profit public API for Cardano and fund 18 months of transition and operations.
- finding: Recipient: Input Output Global / Intersect-managed treasury process for the Blockfrost not-for-profit transition
- finding: Stated amount: 9832979
- finding: Deliverables: Establish a not-for-profit entity or host-organization agreement under a preliminary board in Q3 2026., Publish technical transition architecture and migration plan for community review., Launch a public usage dashboard., Hold a board election via on-chain voting under published rules in Q4 2026., Serve all public API traffic for mainnet, preview, and preprod from the new stack in Q1 2027., Legally transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity., Maintain current service performance during cutover., Open public consultation and publish a long-term sustainability proposal in Q2-Q3 2027., Operate the public API at a minimum 99% monthly uptime SLA during sustained operations., Publish quarterly reports covering technical metrics and budget summary.
- finding: Deadline/expiry: 18-month transition and operations period, with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a reliable hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal says Blockfrost was the number-one hosted platform used by Cardano developers in the Cardano Foundation developer ecosystem surveys, rising from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): The document states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and more than 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): The document states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (economic, proposer_asserted, high materiality): The proposer says 90% of all Cardano traffic served through the Blockfrost API comes from the free tier, making the commercial model difficult for financing the public-good operation.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal commits to transferring all Blockfrost intellectual property, including source code, trademarks, domain names, and associated assets, to the governing not-for-profit entity as part of the transition.
- missing: Independent evidence for: The document states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and more than 7 TB of API data.
- missing: Independent evidence for: The document states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposer says 90% of all Cardano traffic served through the Blockfrost API comes from the free tier, making the commercial model difficult for financing the public-good operation.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a reliable hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The document states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and more than 7 TB of API data." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a reliable hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has strong public-benefit alignment and some checkable governance and usage references, but the deterministic assessment marks claims and evidence as thin and treasury analysis incomplete for a large treasury withdrawal. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than a positive adjustment.
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
- Claims and evidence missing: Independent evidence for: The document states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and more than 7 TB of API data.
- Claims and evidence missing: Independent evidence for: The document states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `29d64b6f0b6083bf86243a67979eab55be510ec320b49fe99350952c13a8130b`
- snapshot_bundle_hash: `3afef130f967f18628562fe50a8b84e8a774bb087694cfb0c9b225743fd139f8`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `31`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

