# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.4833` (raw `-0.4533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.49` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show a public-benefit wallet maintenance case and some repayment/transparency mechanisms, but the deterministic assessment already identifies thin evidence and missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN doctrine, treasury stewardship and evidence quality outweigh plausible ecosystem growth, so the bounded adjustment should lean cautiously negative rather than reward an incompletely evidenced treasury ask.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal request with too many unresolved evidence gaps, especially around budget detail, feasibility, risk, alternatives, and failure modes.

The proposal asked for ₳2,350,000 for 12 months of Eternl operations from August 2026 through July 2027, covering maintenance, development, infrastructure, support, oversight, and the launch of an Eternl Pro plan. The proposer said this represented about $420,000 in annual costs, with up to $420,000 worth of Ada converted into stablecoins, held in a public company wallet, and any excess Ada returned to the treasury. The proposal also included planned independent audits of treasury fund use in February 2027 and August 2027, public wallet monitoring, Pro plan earnings reports, and repayment assessments every December and June.

Some claims were supported by the proposal itself, including the requested amount, the planned stablecoin conversion and public wallet, the Pro plan pricing, the repayment concept, and the audit/oversight structure. But key claims remained unsupported by independent evidence, including the stated 6.0 FTE staffing model across 10 contributors, Eternl’s install numbers, and its claimed share of Cardano mainnet transactions. The review also found the treasury analysis incomplete because it lacked a line-item budget and milestone-gated disbursement, while the risk review was thin because mitigation evidence and independent assurance were missing.

Because treasury withdrawals consume shared ADA and set precedent, BEACN applies elevated scrutiny. Here, the proposal had a replayable anchor and a plausible public-benefit case, but the review gates did not clear: claims and evidence were thin, treasury analysis was incomplete, risk review was thin, and synthesis was blocked. The strongest YES case was that the basic ₳2.35 million request and annual cost target were substantiated, but seven major blockers remained open, so BEACN’s evidence-based conclusion was NO.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, support, infrastructure, audits/oversight, and development while a Pro plan is introduced.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: 12 months of frontend and backend maintenance and development, backend infrastructure and operations, user support and day-to-day operations, public company wallet monitoring after converting up to $420,000 worth of Ada into stablecoins, periodic independent audits of treasury fund use in February 2027 and August 2027, oversight metrics including balances, conversion rates, transaction hashes, and treasury repayment hashes, Eternl Pro plan for personal and company use, repayment assessments every December and June based on remaining treasury stablecoins and paid plan income
- finding: Deadline/expiry: Delivery period August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month period costing around $420,000 per year.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl will introduce Pro plans priced at $96/year for personal users and $360/year for company users, and estimates that about 5,500 users would fully cover the annual $420,000 cost.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl states it has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- missing: Independent evidence for: Eternl states it has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- missing: Independent evidence for: Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: Eternl says that without treasury funds and enough license sales beyond August, it may let developers go, scale down to essential maintenance, focus outside Cardano, or remove the free option.
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
- finding: Strongest YES: the proposal substantiates "Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month period costing around $420,000 per year." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month period costing around $420,000 per year." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show a public-benefit wallet maintenance case and some repayment/transparency mechanisms, but the deterministic assessment already identifies thin evidence and missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN doctrine, treasury stewardship and evidence quality outweigh plausible ecosystem growth, so the bounded adjustment should lean cautiously negative rather than reward an incompletely evidenced treasury ask.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- Claims and evidence missing: Independent evidence for: Eternl states it has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
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
- input_hash: `dfbe38f04b9a5dca95317f89f1c2fac6654fe50b2355ff8877225b09d18c3833`
- snapshot_bundle_hash: `1038f3f85d3e55538ab749ca8dd945f174d49bcf5e975bbbcd77c50df71fb62f`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1218`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2119, "NO": 0.7472, "YES": 0.0409}`

