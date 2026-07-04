# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.4833` (raw `-0.4533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.49` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims include useful budget structure, custody commitments, repayment mechanics, and audit timing, but the deterministic assessment already marks the proposal blocked for missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's hierarchy, the large treasury ask and asserted adoption and revenue-conversion assumptions justify a small cautionary negative nudge rather than a positive public-benefit nudge.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal request, and the review found too many core diligence gaps to justify spending shared ADA.

The proposal asked for ₳2,350,000 for 12 months of Eternl operations, maintenance, support, infrastructure, audits, and product improvements from August 2026 through July 2027. The proposer supported the basic budget framing: about $420,000 in annual costs, split across frontend, backend, support, admin, and audits, funding 6.0 FTE across 10 contributors. The proposal also included custody, stablecoin conversion, repayment, oversight, and independent audit commitments.

However, several important claims were not independently supported in the review. The planned Pro subscription revenue, the claim that about 5,500 paying users would cover annual costs, the install figures, and the 10-18% transaction-share claim remained proposer assertions rather than independently verified evidence. BEACN also treated the main Eternl UI remaining closed-source as a relevant technical fact, while noting that some libraries are said to be available through npm.

The key review gates did not clear. The treasury analysis was incomplete, including missing line-item budget depth and milestone-gated disbursement. The risk review was thin, with missing mitigation evidence and independent assurance. The synthesis was blocked by missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis. Even though the proposal made a credible case that Eternl has real operating costs and a structured funding request, BEACN’s treasury standard requires stronger evidence before approving a large withdrawal.

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
- finding: Requested: 12 months of operations, maintenance, and improvements for Eternl, including frontend and backend maintenance and development, backend infrastructure, user support, day-to-day operations, audits of fund use, and oversight metrics.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development, Backend infrastructure and operations, User support, Day-to-day operations, Independent audits of treasury fund use in February 2027 and August 2027, Oversight metrics including balances, conversion rates, transaction hashes, and treasury repayment hashes, Eternl Core rewrite and related performance improvements, Eternl Hub features, Enhanced hardware wallet support, Enhanced wallet data export, Governance tooling enhancements
- finding: Deadline/expiry: 12-month delivery period from August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual costs for a 12-month period.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as ₳1,292,500 for frontend, ₳587,500 for backend, ₳117,500 for support, ₳305,500 for admin, and ₳47,000 for audits.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, proposer_asserted, high materiality): Eternl plans to introduce Pro plans priced at $96 per year for personal users and $360 per year for companies, and says roughly 5,500 users would fully cover the annual $420,000 cost.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl states it has about 100,000 browser extension installs and about 30,000 Android and iOS installs combined.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposer says up to $420,000 worth of Ada will be converted into stablecoins in a public company wallet and any Ada above that amount will be returned to the treasury.
- missing: Independent evidence for: Eternl plans to introduce Pro plans priced at $96 per year for personal users and $360 per year for companies, and says roughly 5,500 users would fully cover the annual $420,000 cost.
- missing: Independent evidence for: Eternl states it has about 100,000 browser extension installs and about 30,000 Android and iOS installs combined.
- missing: Independent evidence for: Eternl claims that 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual costs for a 12-month period." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Eternl plans to introduce Pro plans priced at $96 per year for personal users and $360 per year for companies, and says roughly 5,500 users would fully cover the annual $420,000 cost." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual costs for a 12-month period." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims include useful budget structure, custody commitments, repayment mechanics, and audit timing, but the deterministic assessment already marks the proposal blocked for missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's hierarchy, the large treasury ask and asserted adoption and revenue-conversion assumptions justify a small cautionary negative nudge rather than a positive public-benefit nudge.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Eternl plans to introduce Pro plans priced at $96 per year for personal users and $360 per year for companies, and says roughly 5,500 users would fully cover the annual $420,000 cost.
- Claims and evidence missing: Independent evidence for: Eternl states it has about 100,000 browser extension installs and about 30,000 Android and iOS installs combined.
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
- input_hash: `77dcc4e6ff4d7631c895cc061941a236545c0629a4ac1a3906f90409c470ae36`
- snapshot_bundle_hash: `412d2a4c7ad2d58862fbfd99b9387127312f5e2ac76e19ac22c9b86c599c0e7f`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `961`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2119, "NO": 0.7472, "YES": 0.0409}`

