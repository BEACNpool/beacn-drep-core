# Rationale: 5439b6141625436ccf600f910bb0b3301b6288933a2cdf7939758848ae8b9997#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2015` (raw `-0.21` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7404` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit infrastructure and includes a concrete milestone and governance framework, but several of the most material adoption, dependency, and cost-sustainability claims are asserted rather than evidenced inside the document. Given the deterministic assessment already marks claims and evidence as thin for a large treasury withdrawal, a small cautionary nudge is warranted rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and the applicable Net Change Limit was not pinned and independently verified from public chain evidence. Until that treasury-flow guardrail is verified, BEACN will not cast a directional vote.

The proposal asks for 9,832,979 ADA to transition Blockfrost into a free, community-governed public good under an independent not-for-profit, with 18 months of transition and operations funded through milestones running from Q3 2026 through 2027. It claims strong ecosystem adoption, including Cardano Foundation survey growth from 39.3% in 2022 to 71.5% in 2025, and commits to transferring source code, trademarks, domains, and associated assets into a community-governed entity. The budget breakdown and governance framework were present in the proposal, and the pinned anchor document was available and replayable.

Several important claims were still not independently evidenced inside the review. The survey adoption claim was treated as substantiated, but material claims about Blockfrost’s basic hosted REST role, recent traffic volumes, transaction share, Icebreaker participation, and the free-tier sustainability problem were treated as proposer assertions or thinly supported. Treasury review also found missing clarity on the sustainability path and cost-benefit case, while risk review still lacked independent assurance and a rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the public-good goal. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus replayable public evidence for the material adoption, dependency, traffic, sustainability, assurance, and remedy claims that carry the treasury-risk case.

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
- finding: Recipient: Input Output / Blockfrost transition administered through Intersect and CDH-related contract arrangements
- finding: Stated amount: 9832979
- finding: Deliverables: Not-for-profit entity established or host-organization agreement signed, transition architecture and migration plan published, and public usage dashboard live in Q3 2026, Board election held via on-chain voting under published rules and elected board assumes mandate in Q4 2026, Public API traffic for mainnet, preview, and preprod served by the new stack, Blockfrost IP transferred to the governing entity, and service performance maintained in Q1 2027, Public sustainability consultation and proposal for long-term model published in Q2-Q3 2027, Public API operated with minimum 99% monthly uptime SLA and quarterly technical and budget reports during 2027
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (technical, proposer_asserted, high materiality): Blockfrost provides a hosted REST interface that lets developers read from and interact with Cardano without running their own node.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal says Blockfrost adoption in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025, with links to the survey pages.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says more than 50% of all Cardano transactions are submitted through Blockfrost in most epochs.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says more than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that 90% of all Cardano traffic served through the Blockfrost API comes from the free tier and that the current commercial model has struggled to finance the public-good operation.
- missing: Independent evidence for: Blockfrost provides a hosted REST interface that lets developers read from and interact with Cardano without running their own node.
- missing: Independent evidence for: The proposal says Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: The proposal says more than 50% of all Cardano transactions are submitted through Blockfrost in most epochs.
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
- finding: Strongest YES: the proposal substantiates "The proposal says Blockfrost adoption in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025, with links to the survey pages." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost provides a hosted REST interface that lets developers read from and interact with Cardano without running their own node." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal says Blockfrost adoption in the Cardano Foundation developer ecosystem survey rose from 39.3% in 2022 to 71.5% in 2025, with links to the survey pages." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal is aligned with public-benefit infrastructure and includes a concrete milestone and governance framework, but several of the most material adoption, dependency, and cost-sustainability claims are asserted rather than evidenced inside the document. Given the deterministic assessment already marks claims and evidence as thin for a large treasury withdrawal, a small cautionary nudge is warranted rather than a positive adjustment.
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
- Claims and evidence missing: Independent evidence for: Blockfrost provides a hosted REST interface that lets developers read from and interact with Cardano without running their own node.
- Claims and evidence missing: Independent evidence for: The proposal says Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `989126a5134149fb903cc96b76065c422617617830c658dbae3516cc71810bc8`
- snapshot_bundle_hash: `7775231951e1e8b2b09c064af3fc644f7537cf584cafd2917b9cfa4fec1ebdde`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3d9c2c9681f9060eff076f9ca8f4e36a1ddb67a2`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5031, "NO": 0.0498, "YES": 0.4471}`

