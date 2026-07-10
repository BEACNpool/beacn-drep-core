# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7758` | Readiness: `0.75`
> Reasoning layer (precomputed): The claims show plausible public-benefit infrastructure value and some checkable adoption evidence, but the ask is large, many critical usage and economic claims are asserted without primary backing in the document, and the long-term sustainability model is explicitly deferred to a future board process. Under the supplied assessment that claims and evidence are thin, a small cautionary negative nudge is justified beyond the mechanical score.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and directional voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for 9,832,979 ADA to fund an 18-month transition of Blockfrost into a free, community-governed not-for-profit public API for Cardano. It describes milestones from Q3 2026 through 2027, including creating or hosting a not-for-profit entity, publishing a technical migration plan and usage dashboard, holding an on-chain board election, transferring Blockfrost intellectual property, maintaining service performance during cutover, consulting on long-term sustainability, and publishing quarterly technical and budget reports. The recipient was not stated in the document.

Several claims were supported well enough for review: the proposal explains what Blockfrost does, cites ecosystem survey adoption figures, describes the planned asset transfer, outlines a five-seat governance model, and gives a budget split across staffing, operations, infrastructure, legal, and accounting. But important claims remained unsupported by independent public evidence, including the stated recent usage figures, the claim that more than 50% of Cardano transactions in most epochs are submitted through Blockfrost, and the economic claim that 90% of Cardano traffic served through Blockfrost comes from the free tier. The review also found thin evidence overall, unknown execution risk, no milestone-gated disbursement, no settled sustainability path, no independent assurance, and no rollback or remedy path.

This is a conservative, evidence-based hold. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the major usage and economic claims, clearer milestone-gated treasury controls, a more concrete sustainability path, independent assurance, and a defined rollback or remedy plan.

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
- finding: Recipient: not stated in document
- finding: Stated amount: 9832979
- finding: Deliverables: Establish a not-for-profit entity or host-organization agreement under a preliminary board in Q3 2026, publish a technical transition architecture and migration plan, and launch a public usage dashboard., Hold a board election via on-chain voting under public rules in Q4 2026 and have the elected board assume its mandate., Serve all public API traffic for mainnet, preview, and preprod from the new stack in Q1 2027, transfer Blockfrost intellectual property to the governing entity, and maintain current service performance during cutover., Open a public sustainability consultation in Q2-Q3 2027 and publish a proposal and documented outcome for the long-term model., Operate the public API at a minimum 99% monthly uptime SLA during 2027 and publish quarterly reports covering technical metrics and budget summary.
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal states that Blockfrost was the number-one hosted platform in the Cardano Foundation developer ecosystem survey and cites usage percentages rising from 39.3% in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data in the prior month.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that more than 50% of transactions in most Cardano epochs are submitted through Blockfrost.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has been difficult to use to finance the public-good operation.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal says all Blockfrost source code, trademarks, domain names, and associated assets will be transferred to a community-governed not-for-profit entity.
- missing: Independent evidence for: The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data in the prior month.
- missing: Independent evidence for: The proposal states that more than 50% of transactions in most Cardano epochs are submitted through Blockfrost.
- missing: Independent evidence for: The proposal states that 90% of Cardano traffic served through the Blockfrost API comes from the free tier and that the commercial model has been difficult to use to finance the public-good operation.
- missing: Independent evidence for: The proposal says long-term sustainability after the 18-month period will be decided by the community-led board, with possible commercial paid tiers or a vendor-backed not-for-profit model returning profits or fees to the ecosystem.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data in the prior month." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is described as a hosted REST interface that lets developers read from and interact with Cardano without running their own node." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims show plausible public-benefit infrastructure value and some checkable adoption evidence, but the ask is large, many critical usage and economic claims are asserted without primary backing in the document, and the long-term sustainability model is explicitly deferred to a future board process. Under the supplied assessment that claims and evidence are thin, a small cautionary negative nudge is justified beyond the mechanical score.
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
- Claims and evidence missing: Independent evidence for: The proposal states that Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, nearly 700 requests per second, and over 7 TB of API data in the prior month.
- Claims and evidence missing: Independent evidence for: The proposal states that more than 50% of transactions in most Cardano epochs are submitted through Blockfrost.
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
- snapshot_bundle_hash: `95b3a1d90f3a3f51e2740ff3f433263c5e5715d53b23164e3465bd214221cced`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

