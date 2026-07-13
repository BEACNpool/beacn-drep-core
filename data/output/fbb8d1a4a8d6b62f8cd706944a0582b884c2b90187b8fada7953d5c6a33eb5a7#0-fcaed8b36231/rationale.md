# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **YES**
Score: `0.2055` (raw `-0.33` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7414` | Readiness: `0.8`
> Reasoning layer (precomputed): A small cautionary nudge is justified because the ask is large, the deterministic assessment marks claims and evidence as thin, and several decision-critical adoption and counterfactual claims remain proposer-asserted even though the proposal does include some budget, custody, audit, and repayment structure.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Eternl: Path to Sustainability - v2. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal for 12 months of Eternl operations, maintenance, improvements, support, infrastructure, audits/oversight, and administration. It asks the treasury for 2350000 ADA. The strongest grounded claim is: The proposal requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual costs for 12 months.

A residual watch item: this claim remains proposer-asserted rather than independently shown: Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.

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
- finding: Requested: Treasury withdrawal for 12 months of Eternl operations, maintenance, improvements, support, infrastructure, audits/oversight, and administration.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development, Backend infrastructure and operations, User support, Day-to-day operations, Independent audits of treasury fund use and oversight metrics, Governance tooling enhancements, Eternl Core rewrite, Eternl Hub, hardware wallet support, and wallet data export work
- finding: Deadline/expiry: Delivery period August 2026 to July 2027
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual costs for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce Personal and Company Pro plans priced at $96/year and $360/year, and says about 5,500 paying users would cover the annual $420,000 cost.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl reports an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users.
- finding: Claim (economic, supported_in_proposal, high materiality): After withdrawal, Eternl says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): The Audits allocation is for independent audits of treasury fund use in February 2027 and August 2027, covering custody, conversion, spending, balances, Pro plan income relevant to repayment, and repayments or refunds.
- missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- missing: Independent evidence for: Eternl reports an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users.
- missing: Independent evidence for: Eternl says 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: Eternl states that without treasury funding it may let developers go, scale down to essential maintenance, shift focus outside Cardano, or remove the free option if paid licenses are insufficient.
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
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual costs for 12 months." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual costs for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: A small cautionary nudge is justified because the ask is large, the deterministic assessment marks claims and evidence as thin, and several decision-critical adoption and counterfactual claims remain proposer-asserted even though the proposal does include some budget, custody, audit, and repayment structure.
- Directional YES cleared ecosystem benefit, delivery, cost-efficiency, downside-protection, and portfolio-capacity floors.
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
- input_hash: `fcaed8b3623131f660cb4372425f03173c9b89324c6c241a5dd4285b52f91da5`
- snapshot_bundle_hash: `f18c457ce96e520f9bbc5c920c28ba1c27b30ab159e56e0b6ac24d22e7e45ece`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `7`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2255, "NO": 0.0496, "YES": 0.7249}`

