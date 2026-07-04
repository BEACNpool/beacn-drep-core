# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.6333` (raw `-0.6033` + doctrine-LLM nudge `-0.03`) | Confidence: `0.64` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal has clear budget categories, custody commitments, audit timing, and repayment mechanics, but the deterministic assessment marks claims and evidence as thin and treasury analysis as incomplete. Several high-materiality claims central to the ask, including install base, transaction share, uptime, and Pro-plan conversion assumptions, are proposer-asserted rather than evidenced in the document. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge beyond the mechanical gates.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and several material claims behind the requested funding were not independently evidenced enough to meet BEACN’s higher bar for treasury spending.

The proposal asked for ₳2,350,000 for 12 months of Eternl operations from August 2026 through July 2027, covering frontend and backend maintenance, infrastructure, support, governance tooling, day-to-day operations, audits, and a transition toward paid Pro plans. The proposal did clearly state the requested amount, the approximate $420,000 valuation, budget categories, custody commitments, planned audit timing, and repayment mechanics. Those parts were reviewable and supported in the proposal.

The weaker evidence was around claims that mattered directly to cost, benefit, and precedent. The 6.0 FTE staffing model and $70,000 per FTE comparison were proposer-asserted without independent evidence. The claimed install base, Pro-plan conversion assumptions, transaction-share figures, and long uptime record were also treated as proposer assertions rather than independently evidenced facts. The review also found the treasury analysis incomplete, with no milestone-gated disbursement documented and cost-benefit clarity still missing.

The strongest case for YES was that Eternl did provide a clear ask, budget, custody plan, audit schedule, and repayment structure. But for BEACN, treasury withdrawals require elevated scrutiny because they spend shared ADA and set precedent. With thin claims-and-evidence status, incomplete treasury analysis, unknown execution risk, missing independent assurance, and a weak treasury flow context, the evidence did not justify a directional YES.

## Review Tree
- overall_status: `incomplete`

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
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: 12 months of operations, maintenance, and improvements for Eternl, including frontend and backend maintenance and development, backend infrastructure, user support, day-to-day operations, audits of fund use, and sustainability transition via paid Pro plans.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development for Chrome extension, web/PWA, iOS, Android, beta channel, security-critical upgrades, CIP support, hardfork feature support, multisig, dApp interoperability, app store compliance, and hardware wallet support., Backend infrastructure and operations including multi-region servers, Cardano nodes, DBSync/indexers, application servers, metadata aggregation, Hub backend services, and 24/7 monitoring/incident response., Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation tooling., User support through Discord ticketing, Telegram, public channels, project support channels, wiki updates, and short educational videos., Day-to-day operations including release management, coordination with vendors/developers/CIP authors, internal code review, and security practices., Periodic independent audits of treasury fund use in February 2027 and August 2027, plus oversight metrics including balances, conversion rates, transaction hashes, and repayment hashes., Launch and grow Eternl Pro plans intended to replace treasury support over time.
- finding: Deadline/expiry: 12-month delivery period, August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $420,000 using an exchange rate of about $0.1787 per Ada, to fund 12 months of operations from August 2026 through July 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as ₳1,292,500 frontend, ₳587,500 backend, ₳117,500 support, ₳305,500 admin, and ₳47,000 audits.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE, which the proposer characterizes as a reasonable lower-bound rate compared with other proposals exceeding $200,000 per FTE.
- finding: Claim (governance, supported_in_proposal, high materiality): Eternl says it will convert up to $420,000 worth of Ada into stablecoins, deposit it into a public company wallet, return any Ada above that amount to the treasury, avoid SPO delegation before conversion or return, and delegate voting power to the predefined abstain option.
- finding: Claim (governance, supported_in_proposal, high materiality): An independent party unaffiliated with Tastenkunst GmbH or the Eternl team is planned to audit treasury fund receipt, custody, conversion, spending, balances, Pro plan income relevant to repayment, and refunds or repayments in February 2027 and August 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl proposes a repayment mechanism where semiannual surplus treasury stablecoins plus paid-plan income above $420,000 would be used to repay up to $420,000 in Ada, followed by a potential additional donation of up to $210,000 worth of Ada from 50% of Pro-plan income above $420,000 after full repayment.
- missing: Independent evidence for: The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE, which the proposer characterizes as a reasonable lower-bound rate compared with other proposals exceeding $200,000 per FTE.
- missing: Independent evidence for: The proposer states Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs, and that about 5,500 Pro-plan users, roughly 4.2% of the install base, would fully cover the annual $420,000 cost.
- missing: Independent evidence for: The proposer states that 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: The proposer states Eternl has provided cross-platform Cardano access with basically zero downtime for over 5 years and is relied on for payments, staking, governance, and DApp interaction.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 2350000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.74
- missing: milestone-gated disbursement
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
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $420,000 using an exchange rate of about $0.1787 per Ada, to fund 12 months of operations from August 2026 through July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE, which the proposer characterizes as a reasonable lower-bound rate compared with other proposals exceeding $200,000 per FTE." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
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
- Treasury analysis: Requested ADA: 2350000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $420,000 using an exchange rate of about $0.1787 per Ada, to fund 12 months of operations from August 2026 through July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has clear budget categories, custody commitments, audit timing, and repayment mechanics, but the deterministic assessment marks claims and evidence as thin and treasury analysis as incomplete. Several high-materiality claims central to the ask, including install base, transaction share, uptime, and Pro-plan conversion assumptions, are proposer-asserted rather than evidenced in the document. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge beyond the mechanical gates.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE, which the proposer characterizes as a reasonable lower-bound rate compared with other proposals exceeding $200,000 per FTE.
- Claims and evidence missing: Independent evidence for: The proposer states Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs, and that about 5,500 Pro-plan users, roughly 4.2% of the install base, would fully cover the annual $420,000 cost.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `a1e92ba5c6a7a4a2d4fc33551c849deef3569b3768120b4dc4f52118b9b1cfce`
- snapshot_bundle_hash: `b5bbc9d6c7092cff5e3b56f915461d55ad4bfa350482e6b05de3eb722dc15b5f`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `32`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

