# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.33` (raw `-0.33` + doctrine-LLM nudge `-0.02`) | Confidence: `0.8025` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal has plausible public-benefit alignment for established wallet infrastructure and includes concrete cost, repayment, public-wallet, and audit mechanics, but the deterministic assessment marks claims and evidence as thin, and several high-materiality adoption and dependency claims are asserted without evidence in the document. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive spending nudge.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the wallet or its proposed work.

The proposal asks for ₳2,350,000 to fund 12 months of Eternl operations from August 2026 through July 2027, covering maintenance, cross-platform development, backend infrastructure, support, governance tooling, audits, public wallet monitoring, stablecoin conversion up to $420,000 worth of Ada, and return of any excess Ada to the treasury. The proposal itself supports the basic budget claim: ₳2,350,000 at about $0.1787 per Ada for roughly $420,000 in annual costs, including 6.0 FTE across 10 contributors at $70,000 per FTE.

The review found several useful accountability mechanics in the proposal, including public wallet monitoring, claimed independent audits in February 2027 and August 2027, on-chain Pro plan records, and published transaction hashes for repayments or donations. But important claims were still treated as thin or unsupported because they were proposer assertions rather than independently replayable public evidence, including Eternl’s platform availability, stated install base, and the claim that 10-18% of Cardano mainnet transactions are conducted via Eternl.

The main gates did not fail because the proposal was unreadable; the anchor was pinned and replayable, and the strongest YES case was recognized. The hold comes from treasury-specific scrutiny: shared ADA is being spent, the treasury flow signal is stressed, no milestone-gated disbursement was documented, cost-benefit clarity remained incomplete, execution risk was unknown, and independent assurance and dependency mapping were missing. A directional vote would be unblocked by a pinned, independently verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the material adoption, dependency, assurance, milestone, and cost-benefit claims.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, support, infrastructure, audits/oversight metrics, and continued development from August 2026 to July 2027.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development for web, browser extension, iOS, Android, and beta channel, Backend infrastructure and operations including multi-region servers, Cardano node operation, chain indexers, application servers, metadata aggregation, Hub services, monitoring, alerting, and incident response, User support through Discord ticketing, Telegram, public channels, ecosystem project support, wiki updates, and educational videos, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation tooling, Independent audits of treasury fund use in February 2027 and August 2027 plus oversight metrics covering balances, conversion rates, transaction hashes, and repayment hashes, Conversion of up to $420,000 worth of Ada into stablecoins, public company wallet monitoring, and return of any Ada above that amount to the treasury
- finding: Deadline/expiry: 12-month delivery period, August 2026 to July 2027
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,350,000 at about $0.1787 per Ada to cover approximately $420,000 in annual costs for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl reports an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposer claims that about 5,500 Pro plan buyers, or about 4.2% of the stated install base, would fully cover Eternl's annual $420,000 cost.
- finding: Claim (economic, proposer_asserted, high materiality): After withdrawal, the proposer says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- missing: Independent evidence for: Eternl reports an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users.
- missing: Independent evidence for: After withdrawal, the proposer says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- missing: Independent evidence for: The proposer says independent audits by an unaffiliated party will occur in February 2027 and August 2027 and will review custody, conversion, spending, balances, Pro plan income relevant to repayment, and refunds or repayments.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 2350000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: milestone-gated disbursement
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests ₳2,350,000 at about $0.1787 per Ada to cover approximately $420,000 in annual costs for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS." — so cost or precedent may outweigh the benefit.
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
- Flag score present (3), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2350000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests ₳2,350,000 at about $0.1787 per Ada to cover approximately $420,000 in annual costs for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal has plausible public-benefit alignment for established wallet infrastructure and includes concrete cost, repayment, public-wallet, and audit mechanics, but the deterministic assessment marks claims and evidence as thin, and several high-materiality adoption and dependency claims are asserted without evidence in the document. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive spending nudge.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- Claims and evidence missing: Independent evidence for: Eternl reports an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `70bc78ec31389e69bbebe2f25e9f4386e4e207f1eaca17aafa5ea8811d1c92c4`
- snapshot_bundle_hash: `34d27da5821b4795ae4fc3b944749a2b8f05764f076e2135666e2d37e6d54579`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4566, "NO": 0.4996, "YES": 0.0438}`

