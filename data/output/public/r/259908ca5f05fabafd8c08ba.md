# Rationale: gov_action12sumv9qky4pkenmqp7gshv9nxqdk9zyn8gkd77fewkyy3t5tnxtsq457vgq
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9033` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims show potentially high public-benefit infrastructure value, but the deterministic assessment already identifies thin evidence and incomplete budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautious negative nudge rather than rewarding adoption claims that remain partly proposer-asserted.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Blockfrost's transformation to not-for-profit. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund an 18-month transition of Blockfrost into a free, community-governed not-for-profit public API, including operations, governance setup, service transition, and sustainability planning.. The recorded treasury amount is 9,832,979 ADA. The strongest grounded claim is: Blockfrost is the number-one hosted platform used by Cardano developers and grew from 39.3% survey usage in 2022 to 71.5% in 2025.

A material weak point is that this claim remains proposer-asserted or thinly supported: Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: Fund an 18-month transition of Blockfrost into a free, community-governed not-for-profit public API, including operations, governance setup, service transition, and sustainability planning.
- finding: Recipient: Input Output / Blockfrost transition under Intersect-administered treasury governance; final not-for-profit entity or host organization not yet determined in document
- finding: Stated amount: 9,832,979 ADA
- finding: Deliverables: Q3 2026: establish or host the not-for-profit entity, publish transition architecture and migration plan, and launch a public usage dashboard, Q4 2026: hold board election via on-chain voting under published rules and seat the elected board, Q1 2027: serve all public API traffic from the new stack, legally transfer Blockfrost IP, and maintain current service performance, Q2-Q3 2027: open public sustainability consultation and publish the chosen direction, 2027: operate the public API at minimum 99% monthly uptime and publish quarterly technical and budget reports
- finding: Deadline/expiry: 18-month funding period with milestones from Q3 2026 through 2027
- finding: Claim (adoption, independently_verifiable, high materiality): Blockfrost is the number-one hosted platform used by Cardano developers and grew from 39.3% survey usage in 2022 to 71.5% in 2025.
- finding: Claim (adoption, proposer_asserted, high materiality): Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- finding: Claim (adoption, proposer_asserted, high materiality): In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- finding: Claim (technical, proposer_asserted, medium materiality): More than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal would transfer Blockfrost source code, trademarks, domain names, and associated assets into community stewardship under an independent community-governed not-for-profit.
- finding: Claim (technical, supported_in_proposal, high materiality): The not-for-profit would provide an open, free public API for Cardano mainnet, preview, and preprod networks in their current format.
- missing: Independent evidence for: Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
- missing: Independent evidence for: More than 100 Icebreakers have joined the decentralized Blockfrost operator effort.
- missing: Independent evidence for: Long-term sustainability may come from paid commercial tiers or a vendor-backed not-for-profit model, with future profits or fees supporting the free public API and potentially flowing back to the Cardano Treasury.
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
- finding: Strongest YES: the proposal substantiates "Blockfrost is the number-one hosted platform used by Cardano developers and grew from 39.3% survey usage in 2022 to 71.5% in 2025." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Blockfrost is the number-one hosted platform used by Cardano developers and grew from 39.3% survey usage in 2022 to 71.5% in 2025." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims show potentially high public-benefit infrastructure value, but the deterministic assessment already identifies thin evidence and incomplete budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautious negative nudge rather than rewarding adoption claims that remain partly proposer-asserted.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~18 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Blockfrost served 781,000 unique visitors, more than 1.84 billion API requests, almost 700 requests per second, and over 7 TB of API data last month.
- Claims and evidence missing: Independent evidence for: In most Cardano epochs, more than 50% of all transactions are submitted through Blockfrost.
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
- input_hash: `ee64db38415bbb009d02b92c56f34aa973a432b64c4ddbfb9cc39f4f9e685799`
- snapshot_bundle_hash: `88e571018340a44c7cff5d8c270a80a6d9de74ca35e28c91e2c3fc61168b9f8d`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `572`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1675, "NO": 0.792, "YES": 0.0404}`

