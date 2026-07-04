# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NO**
Score: `-0.5133` (raw `-0.4833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.49` | Readiness: `0.0`
> Reasoning layer (precomputed): A small cautionary nudge is justified because the claims show public-benefit alignment and some concrete milestones, but the deterministic assessment identifies thin evidence and missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. The doctrine prioritizes treasury stewardship and evidence quality over ecosystem growth, so the bounded lean should not reward plausible adoption upside without stronger verification.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal, and the review found the evidence package incomplete for the level of scrutiny required. The proposal asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed public API over 18 months, but key budget, feasibility, risk, alternatives, failure-mode, and community impact analysis remained missing.

The proposal made a clear public-good case: Blockfrost is described as infrastructure that lets developers use Cardano without running their own nodes, and it included milestones for a not-for-profit structure, governance transition, technical migration, public dashboards, IP transfer, continued service, and quarterly reporting. It also committed to transferring source code, trademarks, domains, and associated assets, and described a legal contract covering delivery schedule, dispute resolution, milestone acceptance, and third-party assurance.

Some claims were supported in the proposal, including the nature of Blockfrost’s service, the planned asset transfer, the requested amount, and the proposed contract structure. But several high-impact claims were still only proposer assertions or lacked independent evidence in the review, including the claim that Blockfrost recently served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, over 7 TB of API data, and that more than 50% of Cardano transactions are submitted through Blockfrost in most epochs.

The review gates did not clear enough of the treasury standard. The anchor document was available and replayable, but treasury analysis was incomplete, claims and evidence were thin, execution risk was unknown, mitigation evidence and independent assurance were missing, and synthesis was blocked by missing core analysis. BEACN therefore voted NO as a treasury stewardship decision: the proposal may describe valuable infrastructure, but the evidence did not justify this withdrawal at the required confidence level.

## Review Tree
- overall_status: `blocked`

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Transition Blockfrost into a free, community-governed public API operated under an independent not-for-profit or host organization, with 18 months of transition and operations funding.
- finding: Recipient: Input Output / Blockfrost transition under governance involving Intersect and CDH contract administration; final not-for-profit entity not yet stated.
- finding: Stated amount: 9,832,979 ADA
- finding: Deliverables: Establish or host a not-for-profit entity under a preliminary board, publish technical transition architecture and migration plan, and launch a public usage dashboard in Q3 2026., Hold a board election via on-chain voting under published rules in Q4 2026, with the elected board assuming its mandate., Serve all public API traffic for mainnet, preview, and preprod from the new stack in Q1 2027, transfer Blockfrost IP to the governing entity, and maintain current service performance through cutover., Open a public sustainability consultation in Q2-Q3 2027 and publish a proposal and documented outcome for the chosen long-term direction., Operate the public API through 2027 at a minimum 99% monthly uptime SLA and publish quarterly reports covering technical metrics and budget summary.
- finding: Deadline/expiry: 18-month transition and operations period with milestones from Q3 2026 through 2027.
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states Cardano Foundation developer ecosystem surveys show Blockfrost hosted-platform usage grew from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states more than 50% of all Cardano transactions are submitted through Blockfrost in most epochs.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal states more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has been difficult for financing that public-good operation.
- missing: Independent evidence for: The proposal states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal states more than 50% of all Cardano transactions are submitted through Blockfrost in most epochs.
- missing: Independent evidence for: The proposal states more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: The proposal states 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has been difficult for financing that public-good operation.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 9.83M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9.83M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own infrastructure or node." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small cautionary nudge is justified because the claims show public-benefit alignment and some concrete milestones, but the deterministic assessment identifies thin evidence and missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. The doctrine prioritizes treasury stewardship and evidence quality over ecosystem growth, so the bounded lean should not reward plausible adoption upside without stronger verification.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: The proposal states more than 50% of all Cardano transactions are submitted through Blockfrost in most epochs.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `6a91993b2bd5e14518a74711720119a7fe9d07e9798a8a58cc41e73c868d704f`
- snapshot_bundle_hash: `f0154eeedd446a78f09cd4b731e9b20cac3f3a2de58792ccc791c6269c63514e`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `960`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2119, "NO": 0.7472, "YES": 0.0409}`

