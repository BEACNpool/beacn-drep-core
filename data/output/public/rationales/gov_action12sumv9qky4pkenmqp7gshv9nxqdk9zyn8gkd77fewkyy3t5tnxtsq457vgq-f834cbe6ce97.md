# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7758` | Readiness: `0.75`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit infrastructure and gives concrete milestones, governance concepts, budget categories, and some externally checkable adoption references, but several high-materiality claims are asserted without direct evidence in the document and the long-term sustainability model is explicitly deferred. Given the large treasury ask and the doctrine's caution around treasury stewardship and evidence quality, a small negative nudge is warranted beyond the mechanical assessment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and the applicable Net Change Limit still needs to be pinned and independently verified from public chain evidence before a directional vote can be justified.

The proposal asks for 9,832,979 ADA to fund an 18-month transition of Blockfrost into a free, community-governed not-for-profit public API for Cardano, including operations during the transition. The proposer describes concrete milestones: forming or hosting a not-for-profit entity, publishing a technical migration plan, launching usage reporting, holding a board election, moving public API traffic to the new stack, transferring Blockfrost assets, consulting on long-term sustainability, and publishing technical and budget reports. The proposal also explains a five-seat governance model and gives budget categories, with most funding allocated to staffing.

Several important claims were supported inside the proposal, including the requested amount, the 18-month purpose, the proposed governance structure, the intended transfer of source code, trademarks, domains, and other assets, and the high-level budget split. One adoption claim, survey growth from 39.3% in 2022 to 71.5% in 2025, was marked independently verifiable through cited survey pages. But other high-materiality adoption claims were only proposer asserted, including last month’s usage figures and the claim that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.

This is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger independent evidence for the major usage and transaction-share claims, clearer milestone-gated disbursement, a more developed sustainability path, independent assurance, and a rollback or remedy path.

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
- finding: Requested: Fund an 18-month transition of Blockfrost into a free, community-governed not-for-profit public API for Cardano, including operations during the transition period.
- finding: Recipient: Input Output will contract with Cardano Development Holdings and Intersect will administer delivery assurance; the final withdrawal recipient is not stated in document.
- finding: Stated amount: 9832979
- finding: Deliverables: Legally establish a not-for-profit entity or sign a host-organization agreement under a preliminary board in Q3 2026., Publish a technical transition architecture and migration plan for community review in Q3 2026., Launch a public usage dashboard in Q3 2026., Hold a board election via on-chain voting under published rules in Q4 2026., Serve all public API traffic for mainnet, preview, and preprod from the new stack in Q1 2027., Legally transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity in Q1 2027., Open a public consultation and publish a proposal on long-term sustainability in Q2-Q3 2027., Operate the public API at a minimum 99% monthly uptime SLA and publish quarterly technical and budget reports during 2027.
- finding: Deadline/expiry: 18 months, with milestones from Q3 2026 through 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,832,979 ADA, stated as 1,868,266 USD at 0.19 USD per ADA, for 18 months of transition and operations.
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node infrastructure.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states that Blockfrost usage in the Cardano Foundation developer ecosystem survey grew from 39.3% in 2022 to 71.5% in 2025, with links to the cited survey pages.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposed governance model uses a five-seat board, with four seats for open-source infrastructure development entities and one community seat, preceded by a named preliminary board.
- missing: Independent evidence for: The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal presents possible post-funding sustainability models, including paid tiers or vendor-backed membership fees, but leaves the final long-term model to the future board.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,832,979 ADA, stated as 1,868,266 USD at 0.19 USD per ADA, for 18 months of transition and operations." and clears the evidence gates.
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
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9832979
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,832,979 ADA, stated as 1,868,266 USD at 0.19 USD per ADA, for 18 months of transition and operations." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal is aligned with public-benefit infrastructure and gives concrete milestones, governance concepts, budget categories, and some externally checkable adoption references, but several high-materiality claims are asserted without direct evidence in the document and the long-term sustainability model is explicitly deferred. Given the large treasury ask and the doctrine's caution around treasury stewardship and evidence quality, a small negative nudge is warranted beyond the mechanical assessment.
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
- Claims and evidence missing: Independent evidence for: The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
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
- snapshot_bundle_hash: `08e135ae69cac23c9b42adecc17b3a1af1995d5d68f5fcbc5ccc9196ae00bcfd`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

