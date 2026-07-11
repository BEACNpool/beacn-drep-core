# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7758` | Readiness: `0.75`
> Reasoning layer (precomputed): The extracted claims show strong public-benefit alignment for critical developer infrastructure and some independently checkable adoption evidence, but the deterministic assessment already flags thin claims and incomplete overall status. Because treasury stewardship and evidence quality are prioritized above ecosystem growth, the supplied record does not justify an additional positive nudge beyond the mechanical score, while the hard-gate posture treats unresolved diligence as needs-more-info rather than an extra negative merits penalty.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for 9,832,979 ADA to fund Blockfrost’s transition into a free, community-governed not-for-profit public good, covering 18 months of transition and operations. It says the work would include creating or hosting the not-for-profit entity, publishing a technical migration plan and usage dashboard, holding a board election, transferring Blockfrost IP to the governing entity, opening public consultation on long-term sustainability, and operating the public API with uptime and reporting commitments through 2027.

Several core parts of the proposal were reviewable and supported in the proposal itself: Blockfrost is described as a hosted REST interface for Cardano developers, the anchor document was pinned and replayable, the budget breakdown was provided, and the proposal commits to public infrastructure reporting and returning unspent post-transition infrastructure budget. Some adoption evidence was independently verifiable, including cited Cardano Foundation survey links showing hosted-platform usage rising from 39.3% in 2022 to 71.5% in 2025.

The hold is conservative and evidence-based. Proposer assertions alone were not enough for a confident treasury vote, especially with stressed treasury-flow signals and missing items such as milestone-gated disbursement, a sustainability path, independent assurance, and a rollback or remedy path. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the unsupported material claims and the missing treasury and risk controls.

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
- finding: Requested: Treasury withdrawal to fund Blockfrost's transition into a free, community-governed not-for-profit public good and support 18 months of transition and operations.
- finding: Recipient: Input Output Global / Input Output, with administration involving Intersect and CDH according to the document
- finding: Stated amount: 9,832,979
- finding: Deliverables: Establish or host a not-for-profit entity and publish technical transition architecture, migration plan, and public usage dashboard in Q3 2026., Hold a board election via on-chain voting under published rules in Q4 2026., Serve all public API traffic from the new stack and legally transfer Blockfrost IP to the governing entity in Q1 2027., Open public consultation and publish a long-term sustainability proposal in Q2-Q3 2027., Operate the public API with at least 99% monthly uptime and publish quarterly technical and budget reports during 2027.
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is presented as a hosted REST interface that lets Cardano developers read from and interact with the blockchain without running their own node.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal states that Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- finding: Claim (adoption, independently_verifiable, high materiality): The document cites Cardano Foundation developer ecosystem survey links showing Blockfrost hosted-platform usage rising from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in the prior month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The document states that more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: The proposal states that Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- missing: Independent evidence for: The proposal states that in the prior month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The document states that more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9832979
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is presented as a hosted REST interface that lets Cardano developers read from and interact with the blockchain without running their own node." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is presented as a hosted REST interface that lets Cardano developers read from and interact with the blockchain without running their own node." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- Claims and evidence missing: Independent evidence for: The proposal states that in the prior month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `f834cbe6ce97b268c9f453eec13ab619c9b5ecb97075763fda9b0e46b17be46e`
- snapshot_bundle_hash: `eebceda953b4c37aeb22c441f6ea3f0f274cba0db75bc43552cc19224687e70c`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

