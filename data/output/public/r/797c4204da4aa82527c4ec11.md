# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.5333` (raw `-0.5033` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal has useful treasury-protection commitments such as public wallet monitoring, capped stablecoin conversion, repayment mechanics, and fund-use audits, but the assessment marks claims and evidence as thin and several high-materiality adoption and transaction-share claims are only proposer asserted. Given the large withdrawal, non-milestone structure, closed main UI, and reliance on future paid-plan uptake, a small cautionary nudge is justified beyond the mechanical assessment.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal with thin independent evidence for key benefit claims. The proposal included useful safeguards, but the review found that the requested spend, precedent risk, and unsupported adoption claims did not meet the higher bar BEACN applies when shared treasury ADA is being withdrawn.

The action requested ₳2,350,000 for 12 months of Eternl operations from August 2026 through July 2027, including maintenance, infrastructure, support, development, Pro plan rollout, work on Eternl Core and Hub, hardware wallet support, wallet export, governance tooling, public reporting, and semiannual fund-use audits. Eternl said its annual operating cost is about $420,000 for 6.0 FTE across 10 contributors, that it would convert up to $420,000 worth of ADA into stablecoins, keep funds in a public company wallet, return ADA above that amount, and run repayment checks using remaining treasury funds and Pro plan income.

The review treated those budget, custody, reporting, repayment, and audit commitments as supported by the proposal. It also noted that the pinned anchor document was available and replayable, and the strongest YES case was that the basic request and delivery period were substantiated. However, several material claims were only proposer asserted, especially the claimed 100,000 browser-extension users, 30,000 mobile users, the estimate that 5,500 Pro users would fully cover annual costs, and the claim that 10-18% of Cardano mainnet transactions are conducted through Eternl.

The gates that mattered most were treasury scrutiny, claims and evidence, and risk review. Treasury scrutiny was elevated because this consumes shared ADA; the review also found no documented milestone-gated disbursement, missing cost-benefit clarity, unknown execution risk, no independent assurance, and no dependency map. With a large non-milestone withdrawal, closed main UI, reliance on future paid-plan uptake, and thin evidence on high-materiality adoption claims, BEACN’s conservative conclusion was NO.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, support, infrastructure, and improvements while Eternl introduces paid Pro plans.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: 12 months of frontend and backend maintenance and development, backend infrastructure and operations, user support and day-to-day operations, periodic independent audits of treasury fund use in February 2027 and August 2027, public reporting of balances, conversion rates, transaction hashes, Pro plan earnings, and treasury repayment or donation hashes, launch and development of Eternl Pro plans, continued work on Eternl Core rewrite, Eternl Hub, hardware wallet support, wallet data export, and governance tooling
- finding: Deadline/expiry: August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month delivery period from August 2026 to July 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states Eternl's annual operating cost is about $420,000 and funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal commits to semiannual repayment checks using remaining treasury stablecoins and paid plan income, with surplus repaid until $420,000 equivalent has been returned and possible additional donations capped at $210,000 equivalent.
- finding: Claim (governance, supported_in_proposal, high materiality): The audits allocation is for independent audits of treasury fund receipt, custody, conversion, spending, remaining balances, Pro plan income relevant to repayment, and refunds or repayments, not technical security audits.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl claims an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users, and says about 5,500 Pro users would fully cover the $420,000 annual cost.
- missing: Independent evidence for: Eternl claims an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users, and says about 5,500 Pro users would fully cover the $420,000 annual cost.
- missing: Independent evidence for: Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: Eternl says that without treasury funds, it may have to let developers go, scale down to essential maintenance, focus outside the Cardano ecosystem, or remove the free option if paid licenses are insufficient beyond August.
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
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl claims an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users, and says about 5,500 Pro users would fully cover the $420,000 annual cost." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has useful treasury-protection commitments such as public wallet monitoring, capped stablecoin conversion, repayment mechanics, and fund-use audits, but the assessment marks claims and evidence as thin and several high-materiality adoption and transaction-share claims are only proposer asserted. Given the large withdrawal, non-milestone structure, closed main UI, and reliance on future paid-plan uptake, a small cautionary nudge is justified beyond the mechanical assessment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Eternl claims an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users, and says about 5,500 Pro users would fully cover the $420,000 annual cost.
- Claims and evidence missing: Independent evidence for: Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `3f108479cfc9aff35253f3cab0cfd6c9dbc5cfb86bd27e313812ffe3d7da7546`
- snapshot_bundle_hash: `847eb1a3c18cea4004159263971a83e40422ecca260ef62dc0adb04f863fa1c4`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1758, "NO": 0.7845, "YES": 0.0397}`

