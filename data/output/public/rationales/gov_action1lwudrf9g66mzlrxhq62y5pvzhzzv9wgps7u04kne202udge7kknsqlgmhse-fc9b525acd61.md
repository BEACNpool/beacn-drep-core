# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.4833` (raw `-0.4533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9733` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims include a large treasury request with some useful budget and oversight detail, but key material assumptions such as install base, transaction share, Pro-plan conversion, annual cost sufficiency, and feasibility are mostly proposer-asserted; combined with the deterministic assessment's blocked status and incomplete treasury, feasibility, risk, alternatives, and failure-mode analysis, a small cautionary nudge is justified.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Eternl: Path to Sustainability - v2. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12 months of Eternl operations, maintenance, and improvements, including frontend and backend maintenance and development, backend infrastructure, user support, day-to-day operations, and audit/oversight activities.. The recorded treasury amount is 2350000. The strongest grounded claim is: The proposal requests ₳2,350,000 at about $0.1787 per Ada to fund 12 months of work costing around $420,000 per year.

A material weak point is that this claim remains proposer-asserted or thinly supported: Eternl is a non-custodial Cardano light wallet available for web, browser extension, Android, and iOS. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: 2.35M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: 12 months of Eternl operations, maintenance, and improvements, including frontend and backend maintenance and development, backend infrastructure, user support, day-to-day operations, and audit/oversight activities.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Keep Eternl secure, compatible, stable, and available during Cardano evolution., Frontend maintenance and cross-platform development for browser extension, web/PWA, iOS, Android, and beta channel., Backend infrastructure and operations including multi-region servers, Cardano node operation, DBSync indexers, application servers, metadata aggregation, and monitoring., User support through Discord ticketing, Telegram, public channels, ecosystem-project support, wiki updates, and educational videos., Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation., Periodic independent audits of treasury fund use in February 2027 and August 2027 with oversight metrics., Introduce Eternl Pro paid plans and assess repayment or donation to the treasury every December and June.
- finding: Deadline/expiry: 12-month delivery period, August 2026 to July 2027
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl is a non-custodial Cardano light wallet available for web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,350,000 at about $0.1787 per Ada to fund 12 months of work costing around $420,000 per year.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 55% frontend, 25% backend, 5% support, 13% admin, and 2% audits.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.
- finding: Claim (economic, supported_in_proposal, high materiality): If about 4.2% of the install base, roughly 5,500 users, buy a Pro plan, Pro income alone would fully cover the annual $420,000 cost.
- finding: Claim (economic, proposer_asserted, high materiality): After withdrawal, the team says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet available for web, browser extension, Android, and iOS.
- missing: Independent evidence for: Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.
- missing: Independent evidence for: After withdrawal, the team says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- missing: Independent evidence for: Eternl says 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- finding: Requested ADA: 2.35M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable
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
- finding: Strongest YES: the proposal substantiates "The proposal requests ₳2,350,000 at about $0.1787 per Ada to fund 12 months of work costing around $420,000 per year." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl is a non-custodial Cardano light wallet available for web, browser extension, Android, and iOS." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 2.35M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests ₳2,350,000 at about $0.1787 per Ada to fund 12 months of work costing around $420,000 per year." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims include a large treasury request with some useful budget and oversight detail, but key material assumptions such as install base, transaction share, Pro-plan conversion, annual cost sufficiency, and feasibility are mostly proposer-asserted; combined with the deterministic assessment's blocked status and incomplete treasury, feasibility, risk, alternatives, and failure-mode analysis, a small cautionary nudge is justified.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow signal is in unsustainable regime (advisory penalty applied).
- Claims and evidence missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet available for web, browser extension, Android, and iOS.
- Claims and evidence missing: Independent evidence for: Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.
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
- input_hash: `fc9b525acd61c748d0997655651b9aa617a3797716bb8ed83e3c3a7fce4dbdbb`
- snapshot_bundle_hash: `577ba659bcf83848d999579b436716df1666990aa8a2725906843534624afcbf`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4fbc4829bb6142608e4d32087d1ed0565eaf5b12`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `801`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1548, "NO": 0.8062, "YES": 0.039}`

