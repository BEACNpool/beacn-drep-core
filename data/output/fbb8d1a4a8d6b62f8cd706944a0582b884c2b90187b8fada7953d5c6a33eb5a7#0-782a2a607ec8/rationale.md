# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **YES**
Score: `0.2055` (binding treasury composite; advisory raw signal `-0.33`; LLM lean `-0.02` recorded, not added) | Confidence: `0.7414` | Readiness: `0.8`
> Reasoning layer (precomputed): A small cautionary nudge is justified because several high-materiality adoption and counterfactual-risk claims, including install base, transaction share, and consequences of non-funding, are proposer-asserted rather than independently evidenced in the supplied document. The proposal does include useful treasury-stewardship commitments such as excess Ada return, public wallet monitoring, repayment mechanics, and fund-use audits, so the adjustment should remain small rather than strongly negative.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Eternl: Path to Sustainability - v2. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal for 12 months of Eternl operations, maintenance, and improvements, including frontend and backend maintenance and development, backend infrastructure, user support, day-to-day operations, audits, and oversight metrics. It asks the treasury for 2350000 ADA. The strongest grounded claim is: Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to fund a 12-month delivery period from August 2026 through July 2027.

A residual watch item: this claim remains proposer-asserted rather than independently shown: Eternl reports an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users combined.

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
- finding: Requested: Treasury withdrawal for 12 months of Eternl operations, maintenance, and improvements, including frontend and backend maintenance and development, backend infrastructure, user support, day-to-day operations, audits, and oversight metrics.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Convert up to $420,000 worth of Ada into stablecoins and deposit it into a public company wallet for monitoring, Return any Ada above $420,000 to the treasury, Hold any Ada before conversion or return in an auditable account, not delegated to an SPO, and delegated to the predefined abstain voting option, Fund 6.0 FTE distributed across 10 contributors at $70,000 per FTE, Maintain and develop Eternl across web, browser extension, Android, and iOS, Operate backend infrastructure including Cardano nodes, DBSync indexers, application servers, metadata aggregation, and monitoring, Provide user support through Discord, Telegram, public channels, ecosystem project channels, wiki updates, and educational videos, Run independent audits of treasury fund use in February 2027 and August 2027, Publish oversight metrics including balances, conversion rates, transaction hashes, and treasury repayment hashes, Assess treasury repayment every December and June based on remaining treasury stablecoins and paid plan income
- finding: Deadline/expiry: 12-month delivery period from August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to fund a 12-month delivery period from August 2026 through July 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states Eternl costs about $420,000 per year and that the requested funds cover 6.0 FTE at $70,000 per FTE across 10 contributors.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as ₳1,292,500 frontend, ₳587,500 backend, ₳117,500 support, ₳305,500 admin, and ₳47,000 audits.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce Personal and Company Pro plans priced at $96/year and $360/year, and says about 5,500 paying users would fully cover the annual $420,000 cost.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl reports an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users combined.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: Eternl reports an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users combined.
- missing: Independent evidence for: The proposal says 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: Eternl says that without treasury funding and sufficient paid license sales beyond August, it may let developers go, scale down to essential maintenance, shift focus outside Cardano, and potentially remove the free option.
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
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to fund a 12-month delivery period from August 2026 through July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl reports an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users combined." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to fund a 12-month delivery period from August 2026 through July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: A small cautionary nudge is justified because several high-materiality adoption and counterfactual-risk claims, including install base, transaction share, and consequences of non-funding, are proposer-asserted rather than independently evidenced in the supplied document. The proposal does include useful treasury-stewardship commitments such as excess Ada return, public wallet monitoring, repayment mechanics, and fund-use audits, so the adjustment should remain small rather than strongly negative.
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
- Claims and evidence missing: Independent evidence for: Eternl reports an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users combined.
- Claims and evidence missing: Independent evidence for: The proposal says 10-18% of Cardano mainnet transactions are conducted via Eternl.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `782a2a607ec840db5d0ae1815175a42d06e8c5a89e5ba8ab6cdca879f64cd7c3`
- snapshot_bundle_hash: `643bdbe24e749e6ff1b58e07da10d8c6d8d99da8dc03f57759e5f490dd5e86a2`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `d68b33ee7989803aaecd7edc03d77c134a98a7f1`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2255, "NO": 0.0496, "YES": 0.7249}`

