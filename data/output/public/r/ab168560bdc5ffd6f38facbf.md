# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NO**
Score: `-0.5633` (raw `-0.5333` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): A small cautionary negative adjustment is justified because the ask is large, requires selling ADA into USDM, relies heavily on modeled yield and proposer-reported performance figures, and includes material stablecoin, custody, market, and smart contract risks. The document does include return terms, multisig oversight, reporting, and risk triggers, so the adjustment should be modest rather than maximal.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal with material execution risk, and several important performance and adoption claims were not backed by independent, replayable evidence.

The action requested 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure. The proposal said the ADA would be sold for USDM to provide stablecoin liquidity, with modeled annual yield of about 900,000 ADA-equivalent, month-6 yield returned to the Treasury, and all treasury-owned deployed assets plus remaining realized yield returned at month 12. It also proposed monthly transparency reports and third-party assurance reports at deployment, month 6, and month 12.

Some core facts were supported in the proposal: this was presented as a productive liquidity deployment rather than grant funding; the ADA-to-USDM conversion, return terms, independent multisig custody, reporting commitments, and named risks were described. But several material claims remained only proposer-asserted or thinly evidenced, including Strike’s cumulative volume, trade count, user count, protocol revenue, liquidity provider profit, V2 usage figures, and vault performance metrics. For a treasury withdrawal, proposer assertions alone are not enough.

The review gates treated treasury withdrawals with elevated scrutiny. The proposal had a pinned anchor document and a defensible strongest-YES case, but the treasury review found no milestone-gated disbursement, the risk review lacked independent assurance and a dependency map, execution risk was unknown, and the treasury flow signal was in an unsustainable regime. Given the size of the ask, the sale of ADA into USDM, reliance on modeled yield, and unresolved evidence gaps, BEACN judged that the cost, risk, and precedent outweighed the supported benefit.

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
- finding: Recipient: Independent multisig council administering Strike Finance liquidity deployment
- finding: Stated amount: 9000000
- finding: Deliverables: Sell 9,000,000 ADA for USDM to provide Strike Finance V2 stablecoin liquidity, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets including remaining principal and realized yield at month 12, Provide monthly public transparency reports covering deployment, utilization, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and risks, Provide third-party assurance reports at deployment confirmation, month 6, and month 12
- finding: Deadline/expiry: 12 months from deployment, with month-6 yield distribution
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure, not grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, with the proposal modeling ADA at 0.15 USD to produce approximately 1,350,000 USDM of liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): Under modeled assumptions, the deployment is expected to generate about 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports more than 1.13 billion USD in cumulative volume, more than 968,000 trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike V2 public data from 2026-03-20 through 2026-06-15 shows 87,288,044 USD in total V2 volume, 410,800 total V2 trades, 2,681 total V2 users, and 30,105 USD in total V2 revenue.
- finding: Claim (economic, proposer_asserted, high materiality): The Strike Liquidity Provider vault is reported as having 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and a 4.97 Sharpe ratio after two months.
- missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, more than 968,000 trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: Strike V2 public data from 2026-03-20 through 2026-06-15 shows 87,288,044 USD in total V2 volume, 410,800 total V2 trades, 2,681 total V2 users, and 30,105 USD in total V2 revenue.
- missing: Independent evidence for: The Strike Liquidity Provider vault is reported as having 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and a 4.97 Sharpe ratio after two months.
- missing: Independent evidence for: The proposal states that Christian Schmitz is conducting an official audit expected by July 1, 2026 and that the report will be published upon completion.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure, not grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike reports more than 1.13 billion USD in cumulative volume, more than 968,000 trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure, not grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small cautionary negative adjustment is justified because the ask is large, requires selling ADA into USDM, relies heavily on modeled yield and proposer-reported performance figures, and includes material stablecoin, custody, market, and smart contract risks. The document does include return terms, multisig oversight, reporting, and risk triggers, so the adjustment should be modest rather than maximal.
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
- Claims and evidence missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, more than 968,000 trades, more than 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: Strike V2 public data from 2026-03-20 through 2026-06-15 shows 87,288,044 USD in total V2 volume, 410,800 total V2 trades, 2,681 total V2 users, and 30,105 USD in total V2 revenue.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `a8b251f0120527a299d26bd718f6a5201b712f4ab08195512cc4918b7d7456a1`
- snapshot_bundle_hash: `c55fa276fc536331f190f97cda7662979c321042b2343e55dcdaa028d7c02a2c`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1758, "NO": 0.7845, "YES": 0.0397}`

