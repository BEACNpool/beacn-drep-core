# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **NO**
Score: `-0.12` (binding treasury composite; advisory raw signal `-0.21`; LLM lean `-0.02` recorded, not added) | Confidence: `0.72` | Readiness: `0.8`
> Reasoning layer (precomputed): A small cautionary nudge is justified because the proposal depends on modeled yield, conversion of ADA into USDM, operational custody, stablecoin and smart contract risks, and a pending audit, while several adoption and performance figures are asserted in the document without external references despite the large treasury exposure. The document does include risk disclosures, reporting commitments, and custody controls, so the adjustment should remain small rather than overriding the engine's ready status.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Strike Finance Liquidity Deployment. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity. It asks the treasury for 9000000 ADA. The strongest grounded claim is: The proposal requests 9,000,000 ADA for a 12-month liquidity deployment, not grant funding, with treasury ownership retained throughout deployment.

A material claim remains proposer-asserted or thinly supported: Strike claims more than 1.13 billion USD in cumulative volume, more than 968,000 trades, more than 3,071 unique traders, more than 1.16 million USD in protocol revenue, and more than 3.25 million USD in liquidity provider profit.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: 9.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity.
- finding: Recipient: Independent council administrator composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta, for Strike Finance V2 liquidity deployment.
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy 9,000,000 ADA sold for USDM into Strike Finance V2 liquidity infrastructure for 12 months., Return realized yield from the first six months to the Cardano Treasury at month 6., Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12, minus any realized losses in a wind-down., Provide monthly public transparency reports covering deployment status, utilization, volume, open interest, profit and loss, yield, drawdown, stablecoin exposure, market quality metrics, distributions, and material risks., Provide independent third-party assurance reports at deployment confirmation, month-6 yield distribution, and month-12 return of funds.
- finding: Deadline/expiry: 12 months from deployment, with month-6 yield distribution and monthly reporting
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment, not grant funding, with treasury ownership retained throughout deployment.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD to produce approximately 1,350,000 USDM of stablecoin liquidity, with actual notional dependent on deployment price.
- finding: Claim (economic, supported_in_proposal, high materiality): Under modeled assumptions of a 10% USD-denominated annual percentage rate, the deployment is expected to generate about 135,000 USD or 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike claims more than 1.13 billion USD in cumulative volume, more than 968,000 trades, more than 3,071 unique traders, more than 1.16 million USD in protocol revenue, and more than 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, supported_in_proposal, high materiality): Strike V2 data from 2026-03-20 through 2026-06-15 is presented as evidence of accelerating volume, revenue, trades, users, and open interest as liquidity deepened.
- finding: Claim (economic, supported_in_proposal, high materiality): The Strike Liquidity Provider vault is described as live with two months of public performance history, 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and 208 depositors.
- missing: Independent evidence for: Strike claims more than 1.13 billion USD in cumulative volume, more than 968,000 trades, more than 3,071 unique traders, more than 1.16 million USD in protocol revenue, and more than 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: The proposal states that Christian Schmitz is conducting an official audit expected by July 1, 2026, and that the report will be published upon completion.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9000000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.66
- missing: milestone-gated disbursement
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment, not grant funding, with treasury ownership retained throughout deployment." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike claims more than 1.13 billion USD in cumulative volume, more than 968,000 trades, more than 3,071 unique traders, more than 1.16 million USD in protocol revenue, and more than 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 9000000
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment, not grant funding, with treasury ownership retained throughout deployment." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: A small cautionary nudge is justified because the proposal depends on modeled yield, conversion of ADA into USDM, operational custody, stablecoin and smart contract risks, and a pending audit, while several adoption and performance figures are asserted in the document without external references despite the large treasury exposure. The document does include risk disclosures, reporting commitments, and custody controls, so the adjustment should remain small rather than overriding the engine's ready status.
- Directional NO is supported by affirmative independent evidence of waste, duplication, excessive cost, or failed delivery — not by missing information.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Strike claims more than 1.13 billion USD in cumulative volume, more than 968,000 trades, more than 3,071 unique traders, more than 1.16 million USD in protocol revenue, and more than 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: The proposal states that Christian Schmitz is conducting an official audit expected by July 1, 2026, and that the report will be published upon completion.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `6c87f2f1a304244cb41ca837d8984a75c42d5cf5c0a1f332775c6afaecb988eb`
- snapshot_bundle_hash: `88516627fe34ce9bb8cbd85e91166ccc181c54a6df8afb25f841d4cd6b1a6bac`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `3e3c343fc0dd14a03a92aad1216ba6620b3d0185`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.23, "NO": 0.64, "YES": 0.13}`

