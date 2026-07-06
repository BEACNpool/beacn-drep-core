# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NO**
Score: `-0.5633` (raw `-0.5333` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): A small negative nudge is warranted because the request is large and depends on modeled yield, stablecoin conversion, custody execution, and many performance claims that are mostly asserted in the document without attached references, while the official audit is described as expected rather than completed. The proposal does include custody, reporting, return, and wind-down terms, so the adjustment should remain modest rather than a hard negative.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal with thin independent evidence for important performance and adoption claims. The proposal had useful structure, but the higher bar for spending shared ADA was not met.

The action requested 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure. The ADA would be sold for USDM to provide stablecoin liquidity, with modeled yield returned at month 6 and remaining treasury-owned assets returned at month 12, minus any realized losses. The proposer framed this as productive liquidity deployment rather than grant funding, and that core request was supported in the proposal.

Several safeguards were documented: an independent multisig council, monthly transparency reports, third-party assurance reports, and review or wind-down triggers tied to drawdown and missed reporting. Those were positive factors. However, key claims about Strike’s cumulative volume, trade count, unique traders, protocol revenue, liquidity provider profit, and share of Cardano trading activity were proposer assertions without independent replayable evidence in the review. The official audit was also described as expected rather than completed.

The review gates therefore produced a conservative NO. Treasury actions require elevated scrutiny because they consume shared ADA and set precedent. Missing milestone-gated disbursement, missing independent assurance, missing dependency mapping, unknown execution risk, and an unsustainable treasury flow signal all weighed against approval, even though the proposal included reporting, custody, return, and wind-down terms.

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
- finding: Requested: A 12-month deployment of treasury-owned ADA into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity.
- finding: Recipient: Independent council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta; Strike Finance V2 liquidity infrastructure is the deployment target.
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy 9,000,000 ADA sold for USDM into Strike Finance V2 liquidity infrastructure for 12 months., Return realized yield from the first six months to the Cardano Treasury at month 6., Return 100% of treasury-owned deployed assets, including remaining principal and realized yield minus any realized losses, at month 12., Provide monthly public transparency reports covering deployment status, utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and material risks., Provide third-party assurance reports for deployment confirmation, month-6 yield distribution, and month-12 return of funds.
- finding: Deadline/expiry: 12 months, with midpoint yield return at month 6
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month productive liquidity deployment into Strike Finance V2 rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD to create approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): Under modeled assumptions of a 10% USD-denominated annual percentage rate, the deployment is expected to generate about 135,000 USD or 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Strike accounted for more than 50% of Cardano trading activity over the past six months.
- finding: Claim (adoption, proposer_asserted, medium materiality): Strike V2 public data from 2026-03-20 through 2026-06-15 is presented as showing 87,288,044 USD total V2 volume, 410,800 total V2 trades, 2,681 total V2 users, 30,105 USD total V2 revenue, and peak open interest of 1,246,007 USD.
- missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: The proposal states that Strike accounted for more than 50% of Cardano trading activity over the past six months.
- missing: Independent evidence for: Strike V2 public data from 2026-03-20 through 2026-06-15 is presented as showing 87,288,044 USD total V2 volume, 410,800 total V2 trades, 2,681 total V2 users, 30,105 USD total V2 revenue, and peak open interest of 1,246,007 USD.
- missing: Independent evidence for: The Strike Liquidity Provider vault is described as having 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and 4.97 Sharpe ratio over two months of public performance history.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9000000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: milestone-gated disbursement
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month productive liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 9000000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month productive liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small negative nudge is warranted because the request is large and depends on modeled yield, stablecoin conversion, custody execution, and many performance claims that are mostly asserted in the document without attached references, while the official audit is described as expected rather than completed. The proposal does include custody, reporting, return, and wind-down terms, so the adjustment should remain modest rather than a hard negative.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- No milestone-gated disbursement documented.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: The proposal states that Strike accounted for more than 50% of Cardano trading activity over the past six months.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `6aa65dd1bc4b1bb16f8c766fc9408fd6127ed423568eaf4af98832690de7b07c`
- snapshot_bundle_hash: `81c4aad77a7711076e3fcdff7c415c37437dbdfdf5c639d4576a059d672579d0`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1758, "NO": 0.7845, "YES": 0.0397}`

