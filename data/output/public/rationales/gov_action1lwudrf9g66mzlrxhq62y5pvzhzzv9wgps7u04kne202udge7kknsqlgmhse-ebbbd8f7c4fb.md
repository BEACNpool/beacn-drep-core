# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.5233` (raw `-0.5033` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The claims include meaningful stewardship mitigations such as a public wallet, audits, and repayment mechanics, but the assessment says evidence is thin and several high-materiality assumptions, including install base, transaction share, FTE need, and Pro-plan conversion, are largely proposer-asserted. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than extra support for spending.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury request did not meet the higher evidence bar for spending shared ADA, especially around the staffing cost basis and other material assumptions. The proposal asks for ₳2,350,000 to fund 12 months of Eternl operations, maintenance, infrastructure, support, audits, administration, and product improvements from August 2026 through July 2027.

The proposer supported several important points: the request is framed as about $420,000 in annual operating cost at roughly $0.1787 per ADA, with budget shares of 55% frontend, 25% backend, 5% support, 13% admin, and 2% audits. The proposal also includes stewardship measures, including converting up to $420,000 worth of ADA into stablecoins in a public company wallet, returning ADA above that amount to the treasury, independent audits in February and August 2027, and semiannual repayment assessments using surplus treasury funds and paid-plan income.

However, several high-materiality claims were not independently supported in the review. The 6.0 FTE staffing claim across 10 contributors at $70,000 per FTE was proposer-asserted, as were the browser, mobile install, and transaction-share claims. The review also found thin claims-and-evidence status, no documented milestone-gated disbursement, missing cost-benefit clarity, unknown execution risk, and missing dependency mapping or independent assurance.

The best case for YES is that Eternl substantiated the headline funding amount and included meaningful treasury stewardship commitments. But for BEACN, treasury withdrawals require elevated scrutiny because they spend shared ADA and set precedent. With unsupported material assumptions and no milestone-gated disbursement documented, the conservative evidence-based vote was NO.

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
- finding: Deep research dossier: complete
- finding: Requested: 12 months of Eternl operations, maintenance, and improvements including frontend/backend development, infrastructure, support, audits/oversight, and day-to-day operations
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development, Backend infrastructure and operations, User support, Administrative operations, Periodic independent audits of treasury fund use and oversight metrics, Eternl Core rewrite, Eternl Hub, enhanced hardware wallet support, wallet data export, and governance tooling enhancements
- finding: Deadline/expiry: Delivery period August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual operating costs for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget allocates 55% to frontend, 25% to backend, 5% to support, 13% to admin, and 2% to audits.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce Pro plans priced at $96/year for Personal and $360/year for Company users, and says roughly 5,500 paying users would cover the annual $420,000 cost.
- finding: Claim (adoption, proposer_asserted, medium materiality): Eternl states it has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposer commits to converting up to $420,000 worth of Ada into stablecoins in a public company wallet, returning any Ada above that amount to the treasury.
- missing: Independent evidence for: The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- missing: Independent evidence for: Eternl states it has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- missing: Independent evidence for: Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
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
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual operating costs for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 2350000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual operating costs for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The claims include meaningful stewardship mitigations such as a public wallet, audits, and repayment mechanics, but the assessment says evidence is thin and several high-materiality assumptions, including install base, transaction share, FTE need, and Pro-plan conversion, are largely proposer-asserted. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than extra support for spending.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- Claims and evidence missing: Independent evidence for: Eternl states it has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `ebbbd8f7c4fbe81a695e81fe4a42824ed7b3e18c99819bb0d2bba97cf42df3e2`
- snapshot_bundle_hash: `4a75eb0be9543b54bb581dfb92fd5b05331d5947a33b44ad2d758ad443c83fd4`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1758, "NO": 0.7845, "YES": 0.0397}`

