# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NO**
Score: `-0.4033` (raw `-0.3833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.75`
> Reasoning layer (precomputed): The supplied claims show meaningful public-benefit alignment and some concrete milestones, but several high-materiality adoption and operational dependency claims are proposer-asserted, and the sustainability path remains conditional rather than committed. Given the large treasury withdrawal and the assessment that claims and evidence are thin, a small cautionary negative nudge is justified beyond the mechanical score.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and some of the most material usage and dependency claims were not backed by independent, replayable evidence.

The proposal asked for 9,832,979 ADA to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, funding 18 months of transition and operations. It included milestones for creating or hosting the entity, publishing transition plans, electing a board, moving public API traffic to the new stack, transferring intellectual property, consulting on long-term sustainability, maintaining 99% monthly uptime, and publishing quarterly technical and budget reports.

The strongest supported case for YES was that Blockfrost appears to have significant ecosystem use: the proposal substantiated that 71.5% of respondents in the 2025 Cardano developer ecosystem survey used Blockfrost, up from 39.3% in 2022. The proposal also gave concrete governance and budget details, including a five-seat board model, planned asset transfer, staffing, operations, infrastructure, legal, and accounting allocations.

The NO came from the evidence and treasury-risk gates. Claims that Blockfrost recently served 781,000 unique visitors, over 1.84 billion API requests, almost 700 requests per second, more than 7 TB of API data, and that more than 50% of Cardano transactions are submitted through Blockfrost in most epochs were proposer-asserted rather than independently evidenced. The review also found thin claims-and-evidence status, no milestone-gated disbursement, an unresolved sustainability path, unknown execution risk, no independent assurance, and no rollback or remedy path. For a treasury action of this size, BEACN required a higher evidentiary bar than the proposal cleared.

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
- finding: Requested: Transition Blockfrost into a free, community-governed public good under an independent, community-governed not-for-profit and fund 18 months of transition and operations.
- finding: Recipient: not stated in document
- finding: Stated amount: 9832979
- finding: Deliverables: Q3 2026: establish or host the not-for-profit entity, publish technical transition architecture and migration plan, and launch a public usage dashboard., Q4 2026: hold a board election via on-chain voting under public rules and have the elected board assume its mandate., Q1 2027: serve all public API traffic for mainnet, preview, and preprod from the new stack, transfer Blockfrost intellectual property to the governing entity, and maintain current service performance during cutover., Q2-Q3 2027: open public consultation on long-term sustainability, publish a sustainability proposal for feedback, and document the chosen direction., 2027: operate the public API at a minimum 99% monthly uptime SLA and publish quarterly technical and budget reports.
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (adoption, independently_verifiable, high materiality): Blockfrost is used by 71.5% of respondents in the 2025 Cardano developer ecosystem survey, up from 39.3% in 2022.
- finding: Claim (adoption, proposer_asserted, high materiality): Last month, Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): More than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal will transfer Blockfrost source code, trademarks, domain names, and associated assets into stewardship by the governing not-for-profit entity.
- finding: Claim (governance, supported_in_proposal, high materiality): The not-for-profit governance model will use a five-seat board with four seats for open-source Cardano infrastructure entities and one community seat, with elections targeted by the end of 2026 and appointment no later than Q1 2027.
- missing: Independent evidence for: Last month, Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: More than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- missing: Independent evidence for: Long-term sustainability may come from a not-for-profit commercial offering or a vendor-backed model, with future profits or fees intended to offset free-tier costs and reduce future treasury dependence.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is used by 71.5% of respondents in the 2025 Cardano developer ecosystem survey, up from 39.3% in 2022." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Last month, Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is used by 71.5% of respondents in the 2025 Cardano developer ecosystem survey, up from 39.3% in 2022." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The supplied claims show meaningful public-benefit alignment and some concrete milestones, but several high-materiality adoption and operational dependency claims are proposer-asserted, and the sustainability path remains conditional rather than committed. Given the large treasury withdrawal and the assessment that claims and evidence are thin, a small cautionary negative nudge is justified beyond the mechanical score.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Last month, Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- Claims and evidence missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `a0667472f4321fb8d7f4aa45778c28e406ae7b935a15303e810198f555b32b2e`
- snapshot_bundle_hash: `48a2a98c77294b324b22bff4657c2d685e14421351f506805b94f5bf0628b0ee`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1825, "NO": 0.7762, "YES": 0.0413}`

