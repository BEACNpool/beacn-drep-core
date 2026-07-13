# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (raw `-0.66` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show meaningful public-benefit alignment for established infrastructure, but several high-materiality adoption and dependency claims are proposer-asserted, and the large treasury ask relies on future sustainability paths that are not yet selected or evidenced. Given the deterministic assessment marks claims and evidence as thin, a small cautionary negative nudge is justified rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed not-for-profit public API/public good and fund 18 months of transition and operations. It says this would include creating or hosting a not-for-profit entity, publishing a technical transition plan, launching a public usage dashboard, holding a board election, serving mainnet/preview/preprod API traffic from the new stack, transferring Blockfrost source code and related assets, consulting on sustainability, and maintaining at least 99% monthly uptime with quarterly reporting.

Several parts of the case are meaningful and supported in the proposal: the IP transfer commitment, the 18-month budget breakdown, the uptime commitment, and the claim that Blockfrost ranked as the number-one hosted platform in the Cardano Foundation developer ecosystem survey, rising from 39.3% usage in 2022 to 71.5% in 2025. But other high-materiality claims remain proposer-asserted rather than independently evidenced, including last month’s usage figures, the claim that more than 50% of transactions in most epochs are submitted through Blockfrost, and the sustainability path after the funded period.

This is a conservative, evidence-based hold, not a rejection of the public-good aim. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger independent evidence for the major usage and dependency claims, clearer cost-benefit and sustainability analysis, and stronger assurance around execution risk and rollback or remedy paths.

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
- finding: Requested: Transition Blockfrost into a free, community-governed not-for-profit public API/public good and fund 18 months of transition and operations.
- finding: Recipient: not stated in document
- finding: Stated amount: 9,832,979
- finding: Deliverables: Legally establish a not-for-profit entity or sign a host-organization agreement under a preliminary board., Publish technical transition architecture and migration plan for community review., Launch a public usage dashboard., Hold a board election via on-chain voting under published rules., Serve all public API traffic for mainnet, preview, and preprod from the new stack., Legally transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity., Open a sustainability consultation and publish a long-term model proposal for community feedback., Operate the public API at minimum 99% monthly uptime and publish quarterly reports covering technical metrics and budget summary.
- finding: Deadline/expiry: 18 months, with milestones from Q3 2026 through 2027
- finding: Claim (adoption, independently_verifiable, high materiality): Blockfrost is the number-one hosted platform used by Cardano developers in the Cardano Foundation developer ecosystem survey, rising from 39.3% usage in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): More than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (economic, proposer_asserted, high materiality): Ninety percent of Cardano traffic served through the Blockfrost API comes from the free tier, making the current commercial model difficult for financing public-good operations.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal would transfer all Blockfrost intellectual property, including source code, trademarks, domains, and associated assets, into a community-governed not-for-profit entity.
- missing: Independent evidence for: Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: More than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: Ninety percent of Cardano traffic served through the Blockfrost API comes from the free tier, making the current commercial model difficult for financing public-good operations.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is the number-one hosted platform used by Cardano developers in the Cardano Foundation developer ecosystem survey, rising from 39.3% usage in 2022 to 71.5% in 2025." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is the number-one hosted platform used by Cardano developers in the Cardano Foundation developer ecosystem survey, rising from 39.3% usage in 2022 to 71.5% in 2025." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: The claims show meaningful public-benefit alignment for established infrastructure, but several high-materiality adoption and dependency claims are proposer-asserted, and the large treasury ask relies on future sustainability paths that are not yet selected or evidenced. Given the deterministic assessment marks claims and evidence as thin, a small cautionary negative nudge is justified rather than a positive adjustment.
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
- Claims and evidence missing: Independent evidence for: Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `e14f189f0da7b3f4b06ceddbceda307b353282a921b3269d87cc70b6e5701ef1`
- snapshot_bundle_hash: `2d71480d710bee17b17a92d8288d8dbb4881182176ec86461e0ddcc9facc7d06`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

