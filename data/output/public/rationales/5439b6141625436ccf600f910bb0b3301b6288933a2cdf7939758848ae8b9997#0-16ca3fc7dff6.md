# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (binding treasury composite; advisory raw signal `-0.21`; LLM lean `-0.02` recorded, not added) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show strong public-benefit alignment and concrete deliverables, but several high-materiality adoption, dependency, traffic, and free-tier economics claims are proposer-asserted while the deterministic assessment already marks claims and evidence as thin. Under treasury stewardship and evidence-quality doctrine, this justifies only a small cautionary nudge rather than a directional merits judgment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury request cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence. That is a conservative, evidence-based hold, not a rejection of Blockfrost or of the public-good goal.

The proposal asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, with 18 months of transition and operations funding. It commits to a not-for-profit structure, public transition plans, on-chain board election rules, transfer of source code, trademarks, domains, and associated assets, public API operation with at least 99% monthly uptime, and quarterly technical and budget reports. The review found the proposal anchor pinned and replayable, and accepted that Blockfrost is a hosted REST interface used by Cardano developers without running their own node infrastructure.

Several important claims were not independently supported enough for a treasury withdrawal of this size. The adoption survey claim was independently verifiable through linked survey years, and the budget breakdown and governance commitments were supported in the proposal. But high-materiality claims about last month’s traffic, more than 50% of epoch transaction submissions, and the free-tier economics were proposer-asserted. The review also found the claims-and-evidence status thin, with missing sustainability-path clarity, cost-benefit clarity, independent assurance, and rollback or remedy path.

Because this is a treasury withdrawal, BEACN applies elevated scrutiny: shared ADA is being spent and precedent is being set. A directional vote would be unblocked by a pinned, independently verified Net Change Limit from public chain evidence, plus replayable public evidence for the major usage, dependency, traffic, and economics claims, along with clearer sustainability, cost-benefit, assurance, and remedy information.

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
- finding: Requested: Transition Blockfrost into a free, community-governed public good under an independent not-for-profit and fund 18 months of transition and operations.
- finding: Recipient: Input Output / Blockfrost transition administered through Intersect/CDH arrangements as described in the proposal
- finding: Stated amount: 9,832,979
- finding: Deliverables: Establish or host a not-for-profit entity and publish transition architecture, migration plan, and public usage dashboard in Q3 2026, Hold a board election via on-chain voting under public rules in Q4 2026, Serve all public API traffic from the new stack and transfer Blockfrost source code, trademarks, domains, and associated assets to the governing entity in Q1 2027, Conduct and publish a sustainability consultation in Q2-Q3 2027, Operate the public API with at least 99% monthly uptime and publish quarterly technical and budget reports during 2027
- finding: Deadline/expiry: 18-month transition and operations period, with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets Cardano developers read from and interact with the blockchain without running their own node infrastructure.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states that Blockfrost adoption in the Cardano Foundation developer ecosystem survey increased from 39.3% in 2022 to 71.5% in 2025 and provides links for each survey year.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal says 90% of all Cardano traffic served through the Blockfrost API comes from the free tier, making the commercial model difficult for financing public-good operations.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal commits to transferring all Blockfrost intellectual property, including source code, trademarks, domain names, and associated assets, to the governing not-for-profit entity as part of the transition.
- missing: Independent evidence for: The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal says 90% of all Cardano traffic served through the Blockfrost API comes from the free tier, making the commercial model difficult for financing public-good operations.
- missing: Independent evidence for: The proposal states that long-term sustainability after the 18-month funding period may come from not-for-profit commercial tiers or vendor-backed partner models, with future profits or fees supporting the treasury or not-for-profit operations.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets Cardano developers read from and interact with the blockchain without running their own node infrastructure." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets Cardano developers read from and interact with the blockchain without running their own node infrastructure." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims show strong public-benefit alignment and concrete deliverables, but several high-materiality adoption, dependency, traffic, and free-tier economics claims are proposer-asserted while the deterministic assessment already marks claims and evidence as thin. Under treasury stewardship and evidence-quality doctrine, this justifies only a small cautionary nudge rather than a directional merits judgment.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `16ca3fc7dff646d4ce2e8c3c44ebd8701aef3f41dc7c73136dcd8a551cc8fc08`
- snapshot_bundle_hash: `1aa4b53ed964208b5e89ff588c78051a151b071aff8aa99ba0136a1822bf2c48`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `3e3c343fc0dd14a03a92aad1216ba6620b3d0185`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

