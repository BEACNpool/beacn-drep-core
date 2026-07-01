# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NO**
Score: `-0.4233` (raw `-0.3833` + doctrine-LLM nudge `-0.04`) | Confidence: `0.9133` | Readiness: `0.0`
> Reasoning layer (precomputed): The deterministic assessment is already blocked for missing budget, feasibility, risk, alternatives, and failure-mode analysis, and the proposal asks for a large treasury deployment involving sale of ADA into USDM, custody arrangements, market risk, and non-guaranteed modeled yield. Under BEACN doctrine, treasury stewardship and evidence quality justify a conservative negative nudge because many key benefits are asserted or modeled while the assessment identifies unresolved diligence gaps.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Strike Finance Liquidity Deployment. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: A 12-month productive treasury deployment of 9,000,000 ADA into Strike Finance V2 liquidity infrastructure, with the ADA sold for USDM to provide stablecoin-denominated liquidity.. The recorded treasury amount is 9,000,000. The strongest grounded claim is: The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding.

A material weak point is that this claim remains proposer-asserted or thinly supported: Strike reports cumulative traction including over 1.13 billion USD in volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity-provider profit. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: A 12-month productive treasury deployment of 9,000,000 ADA into Strike Finance V2 liquidity infrastructure, with the ADA sold for USDM to provide stablecoin-denominated liquidity.
- finding: Recipient: Independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta as stated inconsistently in the document.
- finding: Stated amount: 9,000,000
- finding: Deliverables: Deploy treasury-owned capital into Strike Finance V2 liquidity infrastructure for 12 months, Sell deployed ADA for USDM to provide stablecoin-denominated liquidity, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of remaining treasury-owned deployed assets, including principal and realized yield minus any realized losses, at month 12, Provide monthly public transparency reports covering deployment status, utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and material risks, Provide independent third-party assurance reports at deployment confirmation, month 6, and month 12
- finding: Deadline/expiry: 12 months after deployment; month-6 yield distribution; month-12 final return; audit expected July 1, 2026
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD, producing approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): Under modeled assumptions of a 10% USD-denominated APR, the deployment is expected to generate about 135,000 USD or 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports cumulative traction including over 1.13 billion USD in volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity-provider profit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states that Strike represented over 50% of Cardano trading activity during the past six months.
- finding: Claim (adoption, supported_in_proposal, high materiality): Strike V2 data from 2026-03-20 through 2026-06-15 is presented as evidence of growth in volume, trades, users, revenue, open interest, and vault TVL as liquidity deepened.
- missing: Independent evidence for: Strike reports cumulative traction including over 1.13 billion USD in volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity-provider profit.
- missing: Independent evidence for: The proposal states that Strike represented over 50% of Cardano trading activity during the past six months.
- missing: Independent evidence for: Strike aims to reach top-20 perpetual futures protocol status within 12 months and targets 1,000,000,000 USD in 30-day volume, 5,000 traders, and 5,000,000 USD annualized revenue run rate.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 9.00M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unknown (stale snapshot)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike reports cumulative traction including over 1.13 billion USD in volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity-provider profit." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9.00M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.040 (clamped to ±0.05): The deterministic assessment is already blocked for missing budget, feasibility, risk, alternatives, and failure-mode analysis, and the proposal asks for a large treasury deployment involving sale of ADA into USDM, custody arrangements, market risk, and non-guaranteed modeled yield. Under BEACN doctrine, treasury stewardship and evidence quality justify a conservative negative nudge because many key benefits are asserted or modeled while the assessment identifies unresolved diligence gaps.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~19 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Strike reports cumulative traction including over 1.13 billion USD in volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity-provider profit.
- Claims and evidence missing: Independent evidence for: The proposal states that Strike represented over 50% of Cardano trading activity during the past six months.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `fc5aa3b7f971618017552801f3847acf8f6f263a786e9bf38716d6218f19c4f3`
- snapshot_bundle_hash: `c4a8a3a8ec91aa18ba4fa3a1aed18adab976c0d4eafaf7ec8b9e73556d16480a`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `643`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.165, "NO": 0.7949, "YES": 0.0401}`

