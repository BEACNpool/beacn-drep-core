# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2384` (raw `-0.66` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7496` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal describes a plausible public-good infrastructure transition and includes milestones, reporting, and governance mechanisms, but several highly material adoption, traffic, transaction-share, free-tier, and cost claims are proposer-asserted while the deterministic assessment already marks claims and evidence as thin and the overall status as incomplete. Given the large treasury request, the small nudge should favor caution rather than spending until independently verified diligence is complete.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the idea.

The proposal asks for 9,832,979 ADA to fund Blockfrost’s 18-month transition into a free, community-governed not-for-profit public API for Cardano. It describes milestones for forming or hosting a not-for-profit entity, publishing a technical migration plan and usage dashboard, holding an on-chain board election, transferring intellectual property, serving public API traffic from the new stack, consulting on sustainability, and publishing technical and budget reports.

Several parts of the case were supported: the anchor document was available and replayable, the proposal clearly explains Blockfrost’s role as hosted Cardano API infrastructure, it includes governance and reporting mechanisms, and it provides an 18-month budget. But several material claims remain unsupported or only proposer-asserted, including traffic volumes, transaction-share claims, free-tier economics, infrastructure cost assumptions, and parts of Blockfrost’s organizational history. The review also found thin claims-and-evidence status, medium execution risk, and missing work on sustainability path, cost-benefit clarity, independent assurance, and dependency mapping.

For BEACN to move from NEEDS_MORE_INFO to a directional yes or no, the applicable Net Change Limit must be pinned and independently verified from public chain evidence. The proposal would also need stronger replayable evidence for the material adoption, traffic, transaction-share, cost, and sustainability claims, because treasury withdrawals consume shared ADA and require a higher standard of proof.

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
- finding: Requested: Treasury withdrawal to fund Blockfrost's 18-month transition and operations as a free, community-governed not-for-profit public API for Cardano.
- finding: Recipient: not stated in document
- finding: Stated amount: 9,832,979
- finding: Deliverables: Establish a not-for-profit entity or host-organization agreement under a preliminary board in Q3 2026, publish a technical transition architecture and migration plan, and launch a public usage dashboard., Hold a board election via on-chain voting under public rules in Q4 2026, with results verifiable on-chain and the elected board assuming its mandate., By Q1 2027, serve all public API traffic for mainnet, preview, and preprod from the new stack, transfer Blockfrost intellectual property to the governing entity, and maintain current service performance during cutover., In Q2-Q3 2027, open public consultation on long-term sustainability, publish a sustainability proposal for community feedback, and document the chosen direction., Operate the public API during 2027 at a minimum 99% monthly uptime SLA, publish quarterly technical and budget reports, and make monthly milestones verifiable against dashboard data.
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node.
- finding: Claim (other, proposer_asserted, medium materiality): The proposal says Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal cites Cardano Foundation developer ecosystem survey links showing Blockfrost hosted-platform usage rising from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost and that more than 100 Icebreakers have joined the decentralization effort.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal says 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has struggled to finance this public-good operation.
- missing: Independent evidence for: The proposal says Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- missing: Independent evidence for: The proposal states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost and that more than 100 Icebreakers have joined the decentralization effort.
- missing: Independent evidence for: The proposal says 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has struggled to finance this public-good operation.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal describes a plausible public-good infrastructure transition and includes milestones, reporting, and governance mechanisms, but several highly material adoption, traffic, transaction-share, free-tier, and cost claims are proposer-asserted while the deterministic assessment already marks claims and evidence as thin and the overall status as incomplete. Given the large treasury request, the small nudge should favor caution rather than spending until independently verified diligence is complete.
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
- Claims and evidence missing: Independent evidence for: The proposal says Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- Claims and evidence missing: Independent evidence for: The proposal states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `b84734a0d9937dd7760c0efef7db91ab04701ed4fbf49c30910088320375e2ac`
- snapshot_bundle_hash: `b204a73c91ccd54312cb0c694d9c293646ed027fa286b8a8724d498d9447aa34`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4869, "NO": 0.048, "YES": 0.4651}`

