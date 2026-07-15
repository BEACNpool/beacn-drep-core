# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (binding treasury composite; advisory raw signal `-0.66`; LLM lean `-0.02` recorded, not added) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has strong public-benefit alignment and concrete milestones, but several high-materiality adoption and dependency claims are asserted without embedded verification while the deterministic assessment labels claims and evidence as thin. Given the large treasury request, the small nudge is toward caution on evidence quality and treasury stewardship rather than against the project concept.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the project concept.

The proposal asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, with 18 months of funding for legal setup, technical migration, public dashboards, board elections, API operations, asset transfer, consultation, uptime commitments, and quarterly reporting. The proposal is reviewable because the anchor document is pinned and replayable, and it does make some well-supported claims: Blockfrost is described as a hosted REST interface for Cardano developers, the budget and milestones are laid out, and the proposal commits to transferring source code, trademarks, domains, and associated assets to the governing entity.

The evidence was thinner on several material claims. The proposal cited independently verifiable survey links for developer adoption growth from 39.3% in 2022 to 71.5% in 2025, but other high-impact claims were only proposer asserted, including last month’s 781,000 unique visitors, 1.84 billion API requests, almost 700 requests per second, over 7 TB of API data, and the claim that more than 50% of Cardano transactions are submitted through Blockfrost in most epochs. The review also noted missing clarity on the sustainability path, cost-benefit case, independent assurance, and rollback or remedy path.

Because this is a large treasury withdrawal, BEACN applies elevated scrutiny. The proposal has strong public-benefit alignment and concrete milestones, but treasury spending consumes shared ADA and sets precedent. A directional vote would be unblocked by a pinned, independently verified Net Change Limit from public chain evidence, plus replayable independent evidence for the major usage and dependency claims and stronger clarity on sustainability, cost-benefit, assurance, and remedies.

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
- finding: Requested: Transition Blockfrost into a free, community-governed public good under an independent community-governed not-for-profit and fund 18 months of transition and operations.
- finding: Recipient: Input Output / Blockfrost not-for-profit transition, with governance and administration involving Intersect/CDH as described
- finding: Stated amount: 9,832,979
- finding: Deliverables: Legally establish a not-for-profit entity or sign a host-organization agreement under the preliminary board in Q3 2026, Publish technical transition architecture and migration plan for community review in Q3 2026, Launch a public usage dashboard in Q3 2026, Hold a board election via on-chain voting under public rules in Q4 2026, Serve all public API traffic for mainnet, preview, and preprod from the new stack in Q1 2027, Legally transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity in Q1 2027, Open public consultation and publish a long-term sustainability proposal in Q2-Q3 2027, Operate the public API at a minimum 99% monthly uptime SLA during 2027, Publish quarterly reports covering technical metrics and budget summary
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node infrastructure.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal says Blockfrost developer-survey adoption rose from 39.3% in 2022 to 71.5% in 2025, citing Cardano Foundation survey links for each year.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that more than 50% of all Cardano transactions are submitted through Blockfrost in most epochs.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal asserts that 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has struggled to finance the public-good operation.
- missing: Independent evidence for: The proposal states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- missing: Independent evidence for: The proposal states that more than 50% of all Cardano transactions are submitted through Blockfrost in most epochs.
- missing: Independent evidence for: The proposal says more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: The proposal asserts that 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has struggled to finance the public-good operation.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node infrastructure." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node infrastructure." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal has strong public-benefit alignment and concrete milestones, but several high-materiality adoption and dependency claims are asserted without embedded verification while the deterministic assessment labels claims and evidence as thin. Given the large treasury request, the small nudge is toward caution on evidence quality and treasury stewardship rather than against the project concept.
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
- Claims and evidence missing: Independent evidence for: The proposal states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- Claims and evidence missing: Independent evidence for: The proposal states that more than 50% of all Cardano transactions are submitted through Blockfrost in most epochs.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `39bb8070c07f7f5b1b810a81673ba26c70d154ce5fa011c0bbd476cfde3dcf36`
- snapshot_bundle_hash: `3c3f56b3605e1cdbaecdba240c91c7378da49aee36c9f72ceb3b21041986177a`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

