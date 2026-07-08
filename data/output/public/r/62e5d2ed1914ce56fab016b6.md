# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.5233` (raw `-0.5033` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): A small negative nudge is justified because the ask is large and operational, the deterministic assessment marks claims and evidence as thin, and several high-materiality adoption and ecosystem-impact claims are proposer-asserted rather than evidenced in the document. The repayment, audit, and public-wallet commitments improve stewardship but do not fully offset the evidence gap for a treasury withdrawal of this size.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal request, and several material claims needed stronger independent evidence before shared ADA should be committed.

The proposal asked for ₳2,350,000 to fund 12 months of Eternl operations, maintenance, support, infrastructure, audits or oversight metrics, and continued development from August 2026 through July 2027. The proposer described Eternl as a non-custodial Cardano light wallet across web, browser extension, Android, and iOS, and that core description was supported in the proposal. The budget math was also stated clearly: about $420,000 in annual costs, 6.0 FTE across 10 contributors, conversion of up to $420,000 worth of ADA into stablecoins, and return of ADA above that amount to the treasury.

The review found that some important claims were only proposer-asserted rather than independently evidenced. That included the stated install base of about 100,000 browser-extension installs and 30,000 mobile installs, the claim that Eternl accounts for 10-18% of Cardano mainnet transactions, and the future independent-audit arrangement. The proposal did include stewardship commitments such as a public company wallet, planned audits, on-chain Pro plan records, and published reporting, but those did not fully offset the evidence gap for a treasury request of this size.

The treasury gates carried extra weight because this action withdraws shared ADA and sets precedent. The review also noted no documented milestone-gated disbursement, thin claims-and-evidence status, missing cost-benefit clarity, missing independent assurance, and an unknown execution-risk picture. BEACN’s NO vote reflects that the proposal may describe valuable work, but the evidence and safeguards were not strong enough for this level of treasury spending.

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
- finding: Requested: 12 months of operations, maintenance, support, infrastructure, audits/oversight metrics, and continued development for the Eternl Cardano light wallet.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development for browser extension, web/PWA, iOS, Android, and beta channel, Backend infrastructure and operations including multi-region servers, Cardano node operation, DBSync indexers, application servers, metadata aggregation, Hub backend services, and monitoring, User support through Discord ticketing, Telegram, public community channels, project support, wiki maintenance, and educational videos, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation, Independent audits of treasury fund use and oversight metrics in February 2027 and August 2027
- finding: Deadline/expiry: 12-month delivery period from August 2026 to July 2027
- finding: Claim (adoption, supported_in_proposal, high materiality): Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,350,000, calculated at about $0.1787 per Ada, to cover approximately $420,000 in annual costs.
- finding: Claim (economic, supported_in_proposal, high materiality): The funded work covers 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): If roughly 5,500 users, or about 4.2% of the stated install base, buy the planned Pro plan, that income would fully cover the annual $420,000 cost.
- finding: Claim (economic, supported_in_proposal, high materiality): The team will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- missing: Independent evidence for: Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- missing: Independent evidence for: Treasury-fund-use audits will be performed by an independent party unaffiliated with Tastenkunst GmbH or the Eternl team in February 2027 and August 2027.
- missing: Independent evidence for: Eternl says 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- finding: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): A small negative nudge is justified because the ask is large and operational, the deterministic assessment marks claims and evidence as thin, and several high-materiality adoption and ecosystem-impact claims are proposer-asserted rather than evidenced in the document. The repayment, audit, and public-wallet commitments improve stewardship but do not fully offset the evidence gap for a treasury withdrawal of this size.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- Claims and evidence missing: Independent evidence for: Treasury-fund-use audits will be performed by an independent party unaffiliated with Tastenkunst GmbH or the Eternl team in February 2027 and August 2027.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `b13ff24b1c499108ca110632cf2fc7da59cd8ff406880a54cacc7c8527a10b43`
- snapshot_bundle_hash: `a69cc99722994a58f1c4624dd9d5c1300397c657ad869a7e1c561882031e017b`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `3`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1758, "NO": 0.7845, "YES": 0.0397}`

