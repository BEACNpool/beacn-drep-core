# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (raw `-0.66` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show plausible public-benefit infrastructure value and concrete milestone structure, but several high-materiality adoption, transaction-share, operating-cost, and sustainability claims are asserted or only externally checkable rather than evidenced within the proposal; given the deterministic assessment marks claims and evidence as thin, a small cautionary nudge is warranted for a large treasury withdrawal.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the idea.

The proposal asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed public API under an independent not-for-profit, with an 18-month transition and operations period from Q3 2026 through 2027. It includes legal setup or host-organization arrangements, public transition plans, a usage dashboard, board elections, migration of public API traffic, transfer of source code and related assets, uptime commitments, consultation, and quarterly technical and budget reporting.

Several important parts were supported in the proposal: the planned transfer of Blockfrost assets into community-governed stewardship, the free public API for mainnet, preview, and preprod, the proposed board structure, the budget breakdown, and the return of unspent post-transition infrastructure funds. The review also found one strong YES case: the claim that Blockfrost is the number-one hosted platform used by Cardano developers, with survey adoption rising from 39.3% in 2022 to 71.5% in 2025, was substantiated and cleared the evidence gates.

The hold comes from what remains unverified or thin for a treasury action of this size. The review lacked independent evidence for the claimed 781k unique visitors, 1.84 billion API requests, almost 700 requests per second, over 7 TB of API data in the prior month, and the claim that more than 50% of Cardano transactions are submitted through Blockfrost in most epochs. It also flagged missing clarity on sustainability, cost-benefit, independent assurance, and rollback or remedy paths. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus replayable evidence for the high-materiality usage and transaction-share claims and stronger support for the treasury risk questions.

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
- finding: Requested: Transition Blockfrost into a free, community-governed public API/public good under an independent not-for-profit, including 18 months of transition and operations.
- finding: Recipient: Input Output Global / Input Output, with Intersect administering delivery and treasury management through CDH-related arrangements described in the document
- finding: Stated amount: 9,832,979
- finding: Deliverables: Legally establish a not-for-profit entity or sign a host-organization agreement under the preliminary board in Q3 2026., Publish technical transition architecture and migration plan for community review in Q3 2026., Launch a public usage dashboard in Q3 2026., Hold a board election via on-chain voting under publicly published rules in Q4 2026., Have the elected board formally assume its mandate from the preliminary board in Q4 2026., Serve all public API traffic for mainnet, preview, and preprod from the new stack in Q1 2027., Legally transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity in Q1 2027., Maintain service performance at current levels during cutover., Open public consultation and publish a long-term sustainability proposal in Q2-Q3 2027., Operate the public API at a minimum 99% monthly uptime SLA with quarterly technical and budget reports during 2027 operational milestones.
- finding: Deadline/expiry: 18-month transition and operations period, with milestones from Q3 2026 through 2027
- finding: Claim (adoption, independently_verifiable, high materiality): Blockfrost is the number-one hosted platform used by Cardano developers and its reported survey adoption rose from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data in the prior month.
- finding: Claim (adoption, proposer_asserted, high materiality): In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): More than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal would transfer Blockfrost source code, trademarks, domains, and associated assets into stewardship by a community-governed not-for-profit entity.
- finding: Claim (technical, supported_in_proposal, high materiality): The not-for-profit would provide an open, free public API for Cardano mainnet, preview, and preprod networks in their current format.
- missing: Independent evidence for: Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data in the prior month.
- missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: More than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- missing: Independent evidence for: Long-term sustainability may come from paid tiers or a vendor-backed not-for-profit model, with future profits or fees intended to offset free-tier costs and potentially flow back to the treasury.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is the number-one hosted platform used by Cardano developers and its reported survey adoption rose from 39.3% in 2022 to 71.5% in 2025." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data in the prior month." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is the number-one hosted platform used by Cardano developers and its reported survey adoption rose from 39.3% in 2022 to 71.5% in 2025." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: The claims show plausible public-benefit infrastructure value and concrete milestone structure, but several high-materiality adoption, transaction-share, operating-cost, and sustainability claims are asserted or only externally checkable rather than evidenced within the proposal; given the deterministic assessment marks claims and evidence as thin, a small cautionary nudge is warranted for a large treasury withdrawal.
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
- Claims and evidence missing: Independent evidence for: Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data in the prior month.
- Claims and evidence missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `c93f3b0500fe640b2f8acfd947196e95b01cf0f7e9f7a2b0f455e2d2a9101260`
- snapshot_bundle_hash: `2b50db04a55c593dddeccf5a71e476e21291765b5e463c5e615a2b4208e438c0`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `a650e5f55d3662a45d71b3a19d5301fd64c2bbee`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

