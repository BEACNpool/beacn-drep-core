# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.4833` (raw `-0.4533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9733` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims show a plausible public-benefit wallet maintenance case, but the deterministic assessment already flags thin evidence and missing budget, feasibility, risk, alternatives, and failure-mode analysis. Given the large treasury request, non-milestone structure, asserted adoption metrics, and reliance on future paid-plan uptake and repayment mechanics, BEACN's treasury stewardship and evidence-quality priorities justify a small cautionary negative nudge rather than a positive lean.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Eternl: Path to Sustainability - v2. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal for 12 months of Eternl operations, maintenance, and improvements, including frontend/backend work, infrastructure, support, admin, and audits/oversight.. The recorded treasury amount is 2350000. The strongest grounded claim is: Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month delivery period from August 2026 to July 2027.

A material weak point is that this claim remains proposer-asserted or thinly supported: The proposal states Eternl costs around $420,000 per year and funds 6.0 FTE across 10 contributors at $70,000 per FTE. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: Treasury withdrawal for 12 months of Eternl operations, maintenance, and improvements, including frontend/backend work, infrastructure, support, admin, and audits/oversight.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: 12 months of frontend and backend maintenance and development, Backend infrastructure and operations, User support and day-to-day operations, Governance tooling enhancements, Eternl Core rewrite, Eternl Hub work, hardware wallet support, and wallet data export improvements, Periodic independent audits of treasury fund use and oversight metrics
- finding: Deadline/expiry: Delivery period August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month delivery period from August 2026 to July 2027.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states Eternl costs around $420,000 per year and funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget allocates 55% to frontend, 25% to backend, 5% to support, 13% to admin, and 2% to audits.
- finding: Claim (economic, proposer_asserted, high materiality): Eternl plans to convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal says periodic independent audits in February 2027 and August 2027 will review fund receipt, custody, conversion, spending, balances, Pro plan income relevant to repayment, and treasury refunds or repayments.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans Personal and Company Pro plans at $96/year and $360/year, and claims roughly 5,500 paying users would fully cover the annual $420,000 cost.
- missing: Independent evidence for: The proposal states Eternl costs around $420,000 per year and funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- missing: Independent evidence for: Eternl plans to convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- missing: Independent evidence for: The proposal says periodic independent audits in February 2027 and August 2027 will review fund receipt, custody, conversion, spending, balances, Pro plan income relevant to repayment, and treasury refunds or repayments.
- missing: Independent evidence for: The proposal states Eternl has about 100,000 browser extension installs and about 30,000 installs across Android and iOS.
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
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states Eternl costs around $420,000 per year and funds 6.0 FTE across 10 contributors at $70,000 per FTE." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims show a plausible public-benefit wallet maintenance case, but the deterministic assessment already flags thin evidence and missing budget, feasibility, risk, alternatives, and failure-mode analysis. Given the large treasury request, non-milestone structure, asserted adoption metrics, and reliance on future paid-plan uptake and repayment mechanics, BEACN's treasury stewardship and evidence-quality priorities justify a small cautionary negative nudge rather than a positive lean.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow signal is in unsustainable regime (advisory penalty applied).
- Claims and evidence missing: Independent evidence for: The proposal states Eternl costs around $420,000 per year and funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- Claims and evidence missing: Independent evidence for: Eternl plans to convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
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
- input_hash: `c5181022edfc16aff69c8f3540917197da11ef106b91cc1083f4023eaaeacffa`
- snapshot_bundle_hash: `88244b44b72590c9a04054de188e6bbbb93c064ba9810a4771a95f2c5b4ff5f5`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `b97265e867768077aac16ceb31ccfe1be639d187`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `800`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1548, "NO": 0.8062, "YES": 0.039}`

