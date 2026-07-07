# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.75`
> Reasoning layer (precomputed): The proposal has strong public-benefit framing and some checkable adoption references, but several high-materiality usage, transaction-share, free-tier, and cost claims are largely proposer asserted while the deterministic assessment already labels claims and evidence as thin. Given the large treasury withdrawal and incomplete status, the remaining evidence-quality gap justifies a small cautionary negative nudge rather than a positive lean.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and several material claims needed stronger independent evidence before shared ADA should be committed.

The proposal asked for 9,832,979 ADA to transition Blockfrost into a free, community-governed not-for-profit public API for Cardano and fund 18 months of transition and operations. It described deliverables including a not-for-profit entity or host agreement, migration planning, a public usage dashboard, board election, transfer of public API traffic and intellectual property, sustainability consultation, quarterly reporting, and a 99% monthly uptime target.

The review found some important claims were supported. The proposal clearly explained Blockfrost as hosted API infrastructure for developers, cited independently checkable Cardano Foundation survey links showing rising hosted-service usage, committed to transferring source code and related assets, described the proposed board structure, and provided a budget breakdown. But other high-materiality claims were still mainly proposer asserted, including recent visitor and request volumes, transaction-share claims, free-tier traffic share, and the background claim about Blockfrost’s founding and IOG transition.

Because this is a treasury withdrawal, BEACN applied a higher evidence bar. The anchor document was available and replayable, and the counterargument review identified a real public-benefit case. However, the claims-and-evidence status remained thin, execution risk was unknown, and the review was missing milestone-gated disbursement, a sustainability path, independent assurance, and a rollback or remedy path. On balance, the public-good case was not enough to overcome the evidence and risk gaps for a withdrawal of this size.

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
- finding: Requested: Transition Blockfrost into a free, community-governed not-for-profit public API for Cardano and fund 18 months of transition and operations.
- finding: Recipient: Input Output / Blockfrost transition through the proposed governance and contract structure
- finding: Stated amount: 9832979
- finding: Deliverables: Not-for-profit entity establishment or host-organization agreement, transition architecture and migration plan, and public usage dashboard in Q3 2026, Board election via on-chain voting under published rules in Q4 2026, Transition of public API traffic for mainnet, preview, and preprod to the new stack and transfer of Blockfrost intellectual property in Q1 2027, Public sustainability consultation and proposal in Q2-Q3 2027, Sustained operations with minimum 99% monthly uptime SLA, public dashboard verification, and quarterly technical and budget reports in 2027
- finding: Deadline/expiry: 18-month transition and operations period, with listed milestones through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node.
- finding: Claim (other, proposer_asserted, medium materiality): The proposal states that Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal cites Cardano Foundation developer ecosystem survey links showing Blockfrost hosted-service usage rising from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that 90% of all Cardano traffic served through the Blockfrost API comes from the free tier, making the commercial model difficult for funding public-good operations.
- missing: Independent evidence for: The proposal states that Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- missing: Independent evidence for: The proposal states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal states that 90% of all Cardano traffic served through the Blockfrost API comes from the free tier, making the commercial model difficult for funding public-good operations.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has strong public-benefit framing and some checkable adoption references, but several high-materiality usage, transaction-share, free-tier, and cost claims are largely proposer asserted while the deterministic assessment already labels claims and evidence as thin. Given the large treasury withdrawal and incomplete status, the remaining evidence-quality gap justifies a small cautionary negative nudge rather than a positive lean.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that Blockfrost was founded in 2020 by Five Binaries and joined IOG in 2024 with the goal of decentralizing it.
- Claims and evidence missing: Independent evidence for: The proposal states that last month Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `e9b8f7f025ec4d46a47004748752b517fbaabf43bda39df564d6eb479ca627f4`
- snapshot_bundle_hash: `044b17e43011fa2c9c6e66de8a606f35ba671feb4b098b55e5b7f3e79c48401e`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.181, "NO": 0.778, "YES": 0.0409}`

