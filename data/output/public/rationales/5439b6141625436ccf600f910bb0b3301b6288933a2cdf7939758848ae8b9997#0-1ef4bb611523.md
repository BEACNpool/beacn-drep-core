# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (binding treasury composite; advisory raw signal `-0.66`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show strong public-benefit alignment for established infrastructure and include concrete milestones, governance intentions, budget categories, and some independently checkable adoption references. However, the deterministic assessment already marks claims and evidence as thin and overall status incomplete, so the bounded reasoning layer should not add a spending-positive nudge beyond the engine's treasury and evidence gates.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, funding 18 months of transition and operations. It proposes milestones including forming or hosting the not-for-profit, publishing a technical migration plan, launching a public usage dashboard, holding an on-chain board election, serving public API traffic from the new stack, transferring Blockfrost assets into community stewardship, maintaining uptime, and publishing quarterly technical and budget reports.

Some claims were supported well enough for review. The pinned proposal anchor was available and replayable, and the proposal substantiated the claim that Blockfrost is the number-one hosted platform used by Cardano developers, with survey adoption rising from 39.3% in 2022 to 71.5% in 2025. The proposal also supported its budget structure, including the 18-month ADA request, staffing and operations allocations, planned asset transfer, board structure, and commitment to return unspent post-transition infrastructure budget.

The hold is conservative and evidence-based. Several important claims still lacked independent evidence, including last month’s reported usage of 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data, as well as the claim that more than 50% of Cardano transactions are submitted through Blockfrost in most epochs. The review also found thin claims evidence, medium execution risk, missing sustainability-path and cost-benefit clarity, and missing independent assurance and rollback or remedy details. A directional vote would be unblocked by the verified Net Change Limit plus replayable public evidence for the material usage claims and clearer treasury, assurance, and remedy information.

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
- finding: Requested: Transition Blockfrost into a free, community-governed public good under an independent not-for-profit, funding 18 months of transition and operations.
- finding: Recipient: Input Output / Blockfrost transition structure, with Intersect/CDH contract administration described in the document
- finding: Stated amount: 9,832,979
- finding: Deliverables: Establish or host a not-for-profit entity and kick off transition in Q3 2026, Publish technical transition architecture and migration plan for community review, Launch a public usage dashboard, Hold an on-chain board election under published rules by Q4 2026, Serve all public API traffic for mainnet, preview, and preprod from the new stack by Q1 2027, Legally transfer Blockfrost source code, trademarks, domains, and associated assets to the governing entity, Maintain service performance through cutover, Open public sustainability consultation and publish a long-term sustainability proposal in Q2-Q3 2027, Operate the public API at minimum 99% monthly uptime with quarterly technical and budget reports
- finding: Deadline/expiry: 18-month transition and operations period, with milestones from Q3 2026 through 2027
- finding: Claim (adoption, independently_verifiable, high materiality): Blockfrost is the number-one hosted platform used by Cardano developers and survey adoption rose from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): More than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (economic, proposer_asserted, high materiality): Ninety percent of Cardano traffic served through the Blockfrost API comes from the free tier, making the current commercial model difficult to use for financing the public-good operation.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal will transfer Blockfrost source code, trademarks, domains, and associated assets into community stewardship under a community-governed not-for-profit.
- missing: Independent evidence for: Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: More than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: Ninety percent of Cardano traffic served through the Blockfrost API comes from the free tier, making the current commercial model difficult to use for financing the public-good operation.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is the number-one hosted platform used by Cardano developers and survey adoption rose from 39.3% in 2022 to 71.5% in 2025." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is the number-one hosted platform used by Cardano developers and survey adoption rose from 39.3% in 2022 to 71.5% in 2025." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
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
- Claims and evidence missing: Independent evidence for: Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `1ef4bb611523c38d1407cb190d96d7cfe8f9e4269e76f857066e5c8d93f36340`
- snapshot_bundle_hash: `a89d72e42096cfbd8fee775ab5ed2395059bf8c12fa448645c4bd011b95570c6`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `9e6d7de921490a42032dbcf21a53abc34f881376`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

