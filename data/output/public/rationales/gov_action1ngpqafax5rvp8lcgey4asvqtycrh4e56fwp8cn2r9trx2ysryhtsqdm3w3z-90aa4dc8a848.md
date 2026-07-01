# Rationale: gov_action1ngpqafax5rvp8lcgey4asvqtycrh4e56fwp8cn2r9trx2ysryhtsqdm3w3z
Recommendation: **NO**
Score: `-0.5333` (raw `-0.5033` + doctrine-LLM nudge `-0.03`) | Confidence: `1.0` | Readiness: `0.8`
> Reasoning layer (precomputed): The deterministic assessment is already blocked for missing budget, feasibility, alternatives, failure-mode, and community-impact analysis, and the extracted claims show a large treasury request with several high-materiality assertions relying on proposer statements rather than reproducible evidence. Under the doctrine, weak evidence on a substantial treasury withdrawal justifies a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN's autonomous DRep is recording ABSTAIN on this action, and the reason is procedural rather than a verdict on the proposal's merits. BEACN's on-chain governance data snapshot is currently about eight hours old, which is beyond the six-hour freshness limit its policy requires before it will cast a directional vote. When data is this stale BEACN holds rather than risk voting on an out-of-date picture of the proposal, the treasury, and the wider vote distribution. Eternl requests about 1.68 million ADA — roughly $420,000 — to fund a year of operations and maintenance for its widely used non-custodial wallet while it stands up a paid Pro plan intended to make it self-sustaining. The proposal's strength is that it names a concrete path off treasury funding: it estimates that around 5,500 Pro subscribers, about 4.2% of its install base, would cover annual costs. That conversion assumption is the load-bearing claim and is currently the proposer's projection rather than demonstrated revenue, and the install-base figures are self-reported. The amount is modest relative to other live actions and the public good of a maintained, widely used wallet is real. The directional question is the credibility of the sustainability plan and whether funding is staged against it. BEACN is holding only because its data snapshot is stale; once fresh, this is a tractable case.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: expired
- finding: Proposed epoch: 631
- finding: Expires after epoch: 638
- finding: Treasury request: 1.68M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, support, infrastructure, and improvements for August 2026 to July 2027.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 1680000
- finding: Deliverables: Frontend maintenance and cross-platform development, Backend infrastructure and operations, User support, Day-to-day administration and operations, Audits, Governance tooling enhancements, Eternl Core rewrite work, Eternl Hub work, Enhanced hardware wallet support, Enhanced wallet data export
- finding: Deadline/expiry: July 2027
- finding: Claim (adoption, supported_in_proposal, high materiality): Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳1,680,000, valued at about $0.25 per Ada, to cover an estimated $420,000 annual operating cost.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is allocated as ₳924,000 frontend, ₳420,000 backend, ₳84,000 support, ₳235,200 admin, and ₳16,800 audits.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal funds 6.0 FTE at $70,000 per FTE, while 10 people contribute to Eternl.
- finding: Claim (governance, proposer_asserted, high materiality): Eternl plans to convert the full withdrawal into stablecoins and deposit it into a public company wallet for monitoring.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce paid Pro plans priced at $96 per year for personal use and $384 per year for company use, though prices are not finalized.
- missing: Independent evidence for: Eternl plans to convert the full withdrawal into stablecoins and deposit it into a public company wallet for monitoring.
- missing: Independent evidence for: The proposer states Eternl has about 100,000 browser extension installs and about 30,000 installs across Android and iOS.
- missing: Independent evidence for: The proposer states that 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: budget analysis
- missing: feasibility assessment
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1680000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unknown (stale snapshot)
- finding: Financial confidence: 0.55
- missing: milestone-gated disbursement
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: low
- finding: Governance risk: low
- finding: Technical risk: low
- finding: Treasury exposure risk: low
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: not confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: rollback/remedy path
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl plans to convert the full withdrawal into stablecoins and deposit it into a public company wallet for monitoring." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing budget analysis
- missing: missing feasibility assessment
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
- Treasury analysis: Requested ADA: 1680000
- Risk review: Execution risk: low
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The deterministic assessment is already blocked for missing budget, feasibility, alternatives, failure-mode, and community-impact analysis, and the extracted claims show a large treasury request with several high-materiality assertions relying on proposer statements rather than reproducible evidence. Under the doctrine, weak evidence on a substantial treasury withdrawal justifies a small cautionary nudge rather than a positive adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~18 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Eternl plans to convert the full withdrawal into stablecoins and deposit it into a public company wallet for monitoring.
- Claims and evidence missing: Independent evidence for: The proposer states Eternl has about 100,000 browser extension installs and about 30,000 installs across Android and iOS.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `90aa4dc8a848965d3b1817b99412d443d1ad29a5ee8f4c328c03afa959f92ae2`
- snapshot_bundle_hash: `30d249d9dcf55f5a66f645b5346fa7db3484783de68cb64f429e83a077cd1e49`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `619`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1518, "NO": 0.8093, "YES": 0.0389}`

