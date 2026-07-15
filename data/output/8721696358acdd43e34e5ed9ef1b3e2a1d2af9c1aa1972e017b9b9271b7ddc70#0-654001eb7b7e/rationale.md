# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **NO**
Score: `-0.12` (binding treasury composite; advisory raw signal `-0.21`; LLM lean `+0.0` recorded, not added) | Confidence: `0.72` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit ecosystem growth and includes risk disclosures, custody structure, reporting, and return terms, but many material adoption, performance, and assurance claims are asserted in the document without references or completed audit evidence; the deterministic assessment already marked the review ready, so no additional directional nudge is justified.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Strike Finance Liquidity Deployment. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure by selling 9,000,000 ADA for USDM stablecoin liquidity. It asks the treasury for 9000000 ADA. The strongest grounded claim is: Strike Finance requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment rather than grant funding.

A material claim remains proposer-asserted or thinly supported: Strike reports more than 1.13 billion USD in cumulative volume, about one million trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.

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
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure by selling 9,000,000 ADA for USDM stablecoin liquidity.
- finding: Recipient: Independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta; operationally for Strike Finance V2 liquidity infrastructure.
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy treasury-owned capital as USDM-denominated liquidity for Strike Finance V2., Return realized yield from the first six months to the Cardano Treasury at month 6., Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, to the Cardano Treasury at month 12, subject to realized losses described in wind-down terms., Provide monthly public transparency reports covering deployment status, liquidity utilization, volume, open interest, profit and loss, yield, drawdown, stablecoin exposure, market quality metrics, distributions, and material risks., Provide third-party assurance reports at deployment confirmation, month-6 yield distribution, and month-12 return of funds.
- finding: Deadline/expiry: 12 months, with month-6 yield distribution and month-12 return of funds
- finding: Claim (economic, supported_in_proposal, high materiality): Strike Finance requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, with the actual USDM notional depending on the conversion price at deployment and reported transparently.
- finding: Claim (economic, supported_in_proposal, high materiality): Using ADA at 0.15 USD and a modeled 10% USD-denominated annual percentage rate, the deployment is expected to generate about 135,000 USD or 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports more than 1.13 billion USD in cumulative volume, about one million trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, medium materiality): Strike claims it represented more than 50% of Cardano trading activity over the past six months.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states V2 launched on 2026-03-20 and produced 87,288,044 USD in total V2 volume, 410,800 total V2 trades, 2,681 total V2 users, and 30,105 USD in total V2 revenue through 2026-06-15.
- missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, about one million trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: Strike claims it represented more than 50% of Cardano trading activity over the past six months.
- missing: Independent evidence for: The proposal states V2 launched on 2026-03-20 and produced 87,288,044 USD in total V2 volume, 410,800 total V2 trades, 2,681 total V2 users, and 30,105 USD in total V2 revenue through 2026-06-15.
- missing: Independent evidence for: The Strike Liquidity Provider vault is described as having 985,271.59 USD TVL, 43.52% APR, +8.85% all-time period return, +69,537.24 USD all-time profit and loss, 1.15% maximum drawdown, and 208 depositors.
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
- finding: Strongest YES: the proposal substantiates "Strike Finance requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike reports more than 1.13 billion USD in cumulative volume, about one million trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Strike Finance requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment rather than grant funding." and clears the evidence gates.
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
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, about one million trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: Strike claims it represented more than 50% of Cardano trading activity over the past six months.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `654001eb7b7e1630e92402cfed8bd18f2cbf981d8f199a19fb4b0a570ebd6c22`
- snapshot_bundle_hash: `d0f2abc93291cbdd77b8746d98001eb0b65a6ffa7cb8605ed1f565ba250fe22a`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `880436a840989202a38cccce66fd8f1cbf15004d`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.23, "NO": 0.64, "YES": 0.13}`

