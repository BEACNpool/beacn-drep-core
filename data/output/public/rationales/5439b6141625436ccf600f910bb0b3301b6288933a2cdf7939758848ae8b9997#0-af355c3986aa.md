# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (raw `-0.66` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has strong public-benefit alignment and detailed governance and milestone commitments, but several central adoption and dependency claims are asserted without direct evidence in the document, while the ask is large and staffing-heavy. Given the deterministic assessment already marks evidence as thin and the doctrine prioritizes treasury stewardship and evidence quality before ecosystem growth, a small cautionary negative nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the idea.

The action asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, with 18 months of transition and operations. The proposal commits to a transition architecture, migration plan, public usage dashboard, board election, legal transfer of Blockfrost intellectual property, sustainability consultation, uptime targets, and quarterly technical and budget reports.

Several parts were well supported in the proposal: the requested budget, the promised IP transfer, the governance structure using contracts, milestone acceptance, Intersect delivery assurance, third-party assurance, and treasury-management smart contracts. The strongest supporting case was the independently verifiable claim that Cardano Foundation developer ecosystem surveys show Blockfrost hosted-platform usage rising from 39.3% in 2022 to 71.5% in 2025. But other central claims remained unsupported by independent replayable evidence, including the claim that Blockfrost is a reliable hosted REST interface for developers, the latest traffic figures, and the claim that most Cardano epochs see more than 50% of transactions submitted through Blockfrost.

The review found that the proposal anchor was pinned and replayable, the counterargument pass was completed, and execution risk was medium. But treasury withdrawals require elevated scrutiny because they consume shared ADA and set precedent. The review also flagged thin evidence, stressed treasury-flow conditions, missing sustainability-path and cost-benefit clarity, and missing independent assurance and rollback or remedy path. A directional vote would be unblocked by a pinned, independently verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the unsupported adoption, dependency, sustainability, assurance, and remedy claims.

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
- finding: Recipient: Input Output / Blockfrost transition via Intersect-administered treasury management and a not-for-profit entity to be established or hosted.
- finding: Stated amount: 9,832,979 ADA
- finding: Deliverables: Establish or host a not-for-profit entity, publish transition architecture and migration plan, and launch a public usage dashboard in Q3 2026., Hold a board election via on-chain voting under published rules in Q4 2026., Serve all public API traffic from the new stack and legally transfer Blockfrost intellectual property in Q1 2027., Run sustainability consultation and publish a long-term model proposal in Q2-Q3 2027., Operate the public API with minimum 99% monthly uptime and publish quarterly technical and budget reports during 2027.
- finding: Deadline/expiry: 18 months of operations including transition period; milestones run from Q3 2026 through 2027.
- finding: Claim (technical, proposer_asserted, high materiality): Blockfrost is presented as a reliable hosted REST interface that lets developers interact with Cardano without running their own node infrastructure.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal says Cardano Foundation developer ecosystem surveys show Blockfrost hosted-platform usage grew from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (economic, proposer_asserted, high materiality): The proposer states that 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has struggled to finance the public-good operation.
- missing: Independent evidence for: Blockfrost is presented as a reliable hosted REST interface that lets developers interact with Cardano without running their own node infrastructure.
- missing: Independent evidence for: The proposer states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposer states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal says more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
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
- finding: Strongest YES: the proposal substantiates "The proposal says Cardano Foundation developer ecosystem surveys show Blockfrost hosted-platform usage grew from 39.3% in 2022 to 71.5% in 2025." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost is presented as a reliable hosted REST interface that lets developers interact with Cardano without running their own node infrastructure." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal says Cardano Foundation developer ecosystem surveys show Blockfrost hosted-platform usage grew from 39.3% in 2022 to 71.5% in 2025." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal has strong public-benefit alignment and detailed governance and milestone commitments, but several central adoption and dependency claims are asserted without direct evidence in the document, while the ask is large and staffing-heavy. Given the deterministic assessment already marks evidence as thin and the doctrine prioritizes treasury stewardship and evidence quality before ecosystem growth, a small cautionary negative nudge is justified.
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
- Claims and evidence missing: Independent evidence for: Blockfrost is presented as a reliable hosted REST interface that lets developers interact with Cardano without running their own node infrastructure.
- Claims and evidence missing: Independent evidence for: The proposer states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `af355c3986aaa9d61c30b5569d36c2b352ee5c9f8340d29fe7c8d7070cdddc42`
- snapshot_bundle_hash: `dd005e41188b8d345459dd28d4c13ae20233ac2c777cd438685c71eb62952a6e`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4d394ccfc21657ebcbf2e1dbb3e210682b5ea383`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

