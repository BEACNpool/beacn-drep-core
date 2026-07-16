# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **NO**
Score: `-0.12` (binding treasury composite; advisory raw signal `-0.66`; LLM lean `+0.0` recorded, not added) | Confidence: `0.72` | Readiness: `0.8`
> Reasoning layer (precomputed): The claims show a potentially productive treasury deployment with explicit return, reporting, custody, and risk terms, but the major adoption, vault performance, yield, and audit claims are mostly proposer-asserted within the document rather than evidenced by included references. Because the deterministic assessment is already ready and hard gates are binding, the remaining evidence-quality concern is not enough to justify an additional directional nudge.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Strike Finance Liquidity Deployment. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure. It asks the treasury for 9000000 ADA. The strongest grounded claim is: The proposal requests 9,000,000 ADA for a 12-month liquidity deployment, not grant funding, with treasury ownership retained throughout deployment.

A material claim remains proposer-asserted or thinly supported: Strike reports more than 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.

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
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure
- finding: Recipient: Strike Finance liquidity deployment administered by an independent council
- finding: Stated amount: 9000000
- finding: Deliverables: Sell the deployed ADA for USDM to provide stablecoin-denominated Strike V2 liquidity, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12, Provide monthly public transparency reports covering deployment status, liquidity utilization, volume, open interest, P/L, yield, drawdown, stablecoin exposure, market quality, distributions, and risks, Provide independent third-party assurance reports at deployment confirmation, month 6, and month 12
- finding: Deadline/expiry: 12 months after deployment, with month-6 yield distribution
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment, not grant funding, with treasury ownership retained throughout deployment.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD, producing approximately 1,350,000 USDM of stablecoin liquidity, with actual notional dependent on deployment price.
- finding: Claim (economic, supported_in_proposal, high materiality): Under modeled assumptions of a 10% USD-denominated annual percentage rate, the deployment is expected to generate approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports more than 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike V2 reportedly produced 87,288,044 USD in total volume from 2026-03-20 through 2026-06-15, including 75,322,500 USD in 30-day volume and 29,220,000 USD in 7-day volume.
- finding: Claim (economic, proposer_asserted, high materiality): The Strike liquidity provider vault is described as live with two months of public performance history, 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and 208 depositors.
- missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: Strike V2 reportedly produced 87,288,044 USD in total volume from 2026-03-20 through 2026-06-15, including 75,322,500 USD in 30-day volume and 29,220,000 USD in 7-day volume.
- missing: Independent evidence for: The Strike liquidity provider vault is described as live with two months of public performance history, 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and 208 depositors.
- missing: Independent evidence for: The proposal says Strike V2 has had several unofficial technical reviews and that an official audit by Christian Schmitz is expected to be finalized by July 1, 2026, with the report to be published upon completion.
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
- finding: Strongest NO: a material claim is unsupported — "Strike reports more than 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Directional NO is supported by affirmative independent evidence of waste, duplication, excessive cost, or failed delivery — not by missing information.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 50% of rolling available capacity.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: Strike V2 reportedly produced 87,288,044 USD in total volume from 2026-03-20 through 2026-06-15, including 75,322,500 USD in 30-day volume and 29,220,000 USD in 7-day volume.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `8f97cc36b2ad928c3df5450a4e3df95fc60c69529969b990648940abfee9a262`
- snapshot_bundle_hash: `0e2e2bd826be7d10ed691f1bd3aecdb3d9b916c3cdf48be21e342a4d0bdf29dd`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.23, "NO": 0.64, "YES": 0.13}`

