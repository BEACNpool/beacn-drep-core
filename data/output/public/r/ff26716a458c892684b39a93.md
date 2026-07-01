# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9033` | Readiness: `0.0`
> Reasoning layer (precomputed): The assessment already marks the action blocked for missing summary, budget, feasibility, risk, alternatives, and failure-mode analysis, so the adjustment should remain small. Within the extracted claims, the public-benefit case is plausible and some usage evidence is externally checkable, but several high-materiality adoption and economics claims are proposer-asserted, and the large treasury request depends on governance, sustainability, and execution assumptions that are not fully backed in the supplied record. A modest negative nudge is justified for treasury stewardship and evidence quality.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Blockfrost's transformation to not-for-profit. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Blockfrost's 18-month transition and operations as a free, community-governed not-for-profit public API for Cardano.. The recorded treasury amount is 9,832,979 ADA. The strongest grounded claim is: The proposal says Blockfrost usage in the Cardano Foundation developer ecosystem survey grew from 39.3% in 2022 to 71.5% in 2025 and provides links for each year.

A material weak point is that this claim remains proposer-asserted or thinly supported: Blockfrost is described as a reliable hosted REST interface that lets developers interact with Cardano without running their own infrastructure or node. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: Treasury withdrawal to fund Blockfrost's 18-month transition and operations as a free, community-governed not-for-profit public API for Cardano.
- finding: Recipient: not stated in document
- finding: Stated amount: 9,832,979 ADA
- finding: Deliverables: Legally establish a not-for-profit entity or sign a host-organization agreement under a preliminary board in Q3 2026., Publish a technical transition architecture and migration plan for community review in Q3 2026., Launch a public usage dashboard in Q3 2026., Hold a board election via on-chain voting under publicly published rules in Q4 2026., Have the newly elected board formally assume its mandate from the preliminary board in Q4 2026., Serve all public API traffic for mainnet, preview, and preprod from the new stack in Q1 2027., Legally transfer Blockfrost source code, trademarks, domain names, and associated assets to the governing entity in Q1 2027., Maintain current service performance throughout the cutover., Open a public sustainability consultation and publish a proposal for community feedback in Q2-Q3 2027., Operate the public API at minimum 99% monthly uptime and publish quarterly reports covering technical metrics and budget summary during 2027.
- finding: Deadline/expiry: 18 months of operations including transition period; listed milestones run from Q3 2026 through 2027.
- finding: Claim (adoption, proposer_asserted, high materiality): Blockfrost is described as a reliable hosted REST interface that lets developers interact with Cardano without running their own infrastructure or node.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposal says Blockfrost usage in the Cardano Foundation developer ecosystem survey grew from 39.3% in 2022 to 71.5% in 2025 and provides links for each year.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says more than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that 90% of Cardano traffic served through the Blockfrost API comes from the free tier, making the commercial model difficult for financing public-good operations.
- missing: Independent evidence for: Blockfrost is described as a reliable hosted REST interface that lets developers interact with Cardano without running their own infrastructure or node.
- missing: Independent evidence for: The proposal states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
- missing: Independent evidence for: The proposal states that in most Cardano epochs more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: The proposal says more than 100 Icebreakers have joined the effort to decentralize Blockfrost operations.
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
- finding: Six-month treasury flow regime: unknown (stale snapshot)
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
- finding: Strongest YES: the proposal substantiates "The proposal says Blockfrost usage in the Cardano Foundation developer ecosystem survey grew from 39.3% in 2022 to 71.5% in 2025 and provides links for each year." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost is described as a reliable hosted REST interface that lets developers interact with Cardano without running their own infrastructure or node." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal says Blockfrost usage in the Cardano Foundation developer ecosystem survey grew from 39.3% in 2022 to 71.5% in 2025 and provides links for each year." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The assessment already marks the action blocked for missing summary, budget, feasibility, risk, alternatives, and failure-mode analysis, so the adjustment should remain small. Within the extracted claims, the public-benefit case is plausible and some usage evidence is externally checkable, but several high-materiality adoption and economics claims are proposer-asserted, and the large treasury request depends on governance, sustainability, and execution assumptions that are not fully backed in the supplied record. A modest negative nudge is justified for treasury stewardship and evidence quality.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~19 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Blockfrost is described as a reliable hosted REST interface that lets developers interact with Cardano without running their own infrastructure or node.
- Claims and evidence missing: Independent evidence for: The proposal states that last month Blockfrost served 781k unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data.
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
- input_hash: `a083c9b1daabaf5103533d3094cce181352f445f568555b8dfccc93f828ac183`
- snapshot_bundle_hash: `0cf358b8ed263c282ba5010263a663170b7c266001b4dd83b83f52a7e40bfecd`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `714`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1675, "NO": 0.792, "YES": 0.0404}`

