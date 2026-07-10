# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.4933` (raw `-0.4933` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal has a coherent structure with custody, reporting, risk triggers, and return terms, but the core economic case depends on proposer-reported traction, a short vault history, modeled yield, and material exposure to ADA price, USDM, smart contract, and custody risks. Given the large treasury amount and limited independently verifiable support in the supplied document, a small cautionary negative nudge is justified beyond the mechanical assessment.

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Strike Finance Liquidity Deployment. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity. It asks the treasury for 9000000 ADA. The strongest grounded claim is: The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding.

A material claim remains proposer-asserted or thinly supported: Under conservative modeled assumptions, the deployment is expected to generate approximately 900,000 ADA-equivalent in annual yield, but returns are not guaranteed. Reason code: VERIFIED_NCL_REQUIRED.

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
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Under conservative modeled assumptions, the deployment is expected to generate approximately 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- Claims and evidence missing: Independent evidence for: Strike reports over 1.13 billion USD in cumulative volume, roughly 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `1b091b80946f67485feefea5fb75a44b5fb54c34efc039817dd93cb3cf83751b`
- snapshot_bundle_hash: `ca05e4a2b66aa03269e7c6d89f3280ccafad8b0d753561d4240620337ec9f050`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

