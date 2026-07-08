# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NO**
Score: `-0.5633` (raw `-0.5333` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal has a coherent structure with custody, reporting, risk triggers, and return terms, but the core economic case depends on proposer-reported traction, a short vault history, modeled yield, and material exposure to ADA price, USDM, smart contract, and custody risks. Given the large treasury amount and limited independently verifiable support in the supplied document, a small cautionary negative nudge is justified beyond the mechanical assessment.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and the core economic case was not supported by enough independent, replayable evidence. The proposal had a coherent structure, but the expected return depended on modeled yield, proposer-reported traction, and a short vault history, while exposing treasury funds to ADA price risk, USDM risk, smart contract risk, and custody or operational risk.

The action requested 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure. The ADA would be sold for USDM, modeled at ADA = 0.15 USD, to create about 1,350,000 USDM of stablecoin liquidity. The proposal said the first six months of realized yield would be returned to the Cardano Treasury at month 6, and that all treasury-owned deployed assets, including remaining principal and realized yield, would be returned at month 12. It also promised monthly transparency reports and third-party assurance reports at deployment, month 6, and month 12.

Several basic claims were supported in the proposal: the amount requested, the 12-month deployment structure, the ADA-to-USDM liquidity plan, the independent multisig custody arrangement, and the stated risk categories. But important claims were not independently evidenced in the supplied review, including the projected 900,000 ADA-equivalent annual yield and the reported cumulative Strike traction figures. The review also found the evidence base thin, no documented milestone-gated disbursement, missing independent assurance in the risk review, and no dependency map.

The proposal passed enough intake and anchor checks to be reviewed, and the strongest YES case was that this was structured as a productive deployment rather than ordinary grant spending. But treasury withdrawals require a higher bar because they consume shared ADA and set precedent. With 9,000,000 ADA at stake, unsupported material return claims and unresolved execution evidence outweighed the potential benefit, so BEACN voted NO.

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
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity
- finding: Recipient: Strike Finance liquidity deployment administered by an independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy 9,000,000 ADA sold for USDM into Strike Finance V2 liquidity infrastructure for 12 months, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12, Provide monthly public transparency reports covering deployment status, utilization, volume, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and material risks, Provide independent third-party assurance reports at deployment confirmation, month-6 yield distribution, and month-12 return of funds
- finding: Deadline/expiry: 12 months after deployment; month-6 yield distribution; audit expected by July 1, 2026
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD, producing approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, proposer_asserted, high materiality): Under conservative modeled assumptions, the deployment is expected to generate approximately 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports over 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states Strike represented over 50% of Cardano trading activity during the past six months.
- finding: Claim (adoption, supported_in_proposal, medium materiality): The proposal states V2 produced 87,288,044 USD in total volume, 410,800 trades, 2,681 users, and 30,105 USD in revenue from 2026-03-20 through 2026-06-15.
- missing: Independent evidence for: Under conservative modeled assumptions, the deployment is expected to generate approximately 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- missing: Independent evidence for: Strike reports over 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: The proposal states Strike represented over 50% of Cardano trading activity during the past six months.
- missing: Independent evidence for: The Strike Liquidity Provider vault is reported as having 985,271.59 USD TVL, 43.52% APR, +8.85% all-time period return, 1.15% maximum drawdown, and a 4.97 all-time Sharpe ratio over two months of history.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Under conservative modeled assumptions, the deployment is expected to generate approximately 900,000 ADA-equivalent in annual yield, but returns are not guaranteed." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has a coherent structure with custody, reporting, risk triggers, and return terms, but the core economic case depends on proposer-reported traction, a short vault history, modeled yield, and material exposure to ADA price, USDM, smart contract, and custody risks. Given the large treasury amount and limited independently verifiable support in the supplied document, a small cautionary negative nudge is justified beyond the mechanical assessment.
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
- Claims and evidence missing: Independent evidence for: Under conservative modeled assumptions, the deployment is expected to generate approximately 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- Claims and evidence missing: Independent evidence for: Strike reports over 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `1b091b80946f67485feefea5fb75a44b5fb54c34efc039817dd93cb3cf83751b`
- snapshot_bundle_hash: `f11d19e0cf172277abe50765187233442906a643dce1b7c6616380f1b0e3cfbf`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `3`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1758, "NO": 0.7845, "YES": 0.0397}`

