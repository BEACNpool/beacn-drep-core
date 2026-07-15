# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **NO**
Score: `-0.12` (raw `-0.21` + doctrine-LLM nudge `-0.02`) | Confidence: `0.72` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit ecosystem growth and includes meaningful risk disclosures, reporting commitments, custody separation, and a non-grant return structure, but the largest adoption and yield inputs are mostly proposer-stated within the supplied document and the request exposes treasury funds to conversion, stablecoin, smart contract, and custody risks. Under the doctrine hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than a positive adjustment for growth potential.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Strike Finance Liquidity Deployment. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity. It asks the treasury for 9000000 ADA. The strongest grounded claim is: The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding, with treasury ownership retained throughout deployment.

A material claim remains proposer-asserted or thinly supported: Strike Finance states it has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit.

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
- finding: Recipient: independent multisig council / Strike Finance liquidity deployment
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy approximately 9,000,000 ADA worth of USDM liquidity into Strike Finance V2, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12, Provide monthly public transparency reports covering deployment status, liquidity utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality metrics, distributions, and material risks, Provide independent third-party assurance reports at deployment confirmation, month-6 distribution, and month-12 return
- finding: Deadline/expiry: 12 months after deployment; month-6 yield distribution; month-12 final return
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding, with treasury ownership retained throughout deployment.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD for approximately 1,350,000 USDM of stablecoin liquidity, with actual USDM notional depending on deployment conversion price.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal models a 10% USD-denominated annual percentage rate, generating approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, while stating returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike Finance states it has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike V2 public performance figures are presented for 2026-03-20 through 2026-06-15, including 87,288,044 USD total V2 volume, 410,800 total V2 trades, 2,681 users, 30,105 USD total V2 revenue, and 1,246,007 USD peak open interest.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asserts that the primary bottleneck to further Strike growth is liquidity depth and that increased stablecoin liquidity has correlated with higher V2 volume, trades, revenue, and vault TVL.
- missing: Independent evidence for: Strike Finance states it has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: Strike V2 public performance figures are presented for 2026-03-20 through 2026-06-15, including 87,288,044 USD total V2 volume, 410,800 total V2 trades, 2,681 users, 30,105 USD total V2 revenue, and 1,246,007 USD peak open interest.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding, with treasury ownership retained throughout deployment." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike Finance states it has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding, with treasury ownership retained throughout deployment." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal is aligned with public-benefit ecosystem growth and includes meaningful risk disclosures, reporting commitments, custody separation, and a non-grant return structure, but the largest adoption and yield inputs are mostly proposer-stated within the supplied document and the request exposes treasury funds to conversion, stablecoin, smart contract, and custody risks. Under the doctrine hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than a positive adjustment for growth potential.
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
- Claims and evidence missing: Independent evidence for: Strike Finance states it has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: Strike V2 public performance figures are presented for 2026-03-20 through 2026-06-15, including 87,288,044 USD total V2 volume, 410,800 total V2 trades, 2,681 users, 30,105 USD total V2 revenue, and 1,246,007 USD peak open interest.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `b10803b240c6d12a0863f5729d34009d52067f2e266c7537aa2ede99afa5fd8a`
- snapshot_bundle_hash: `abb1f20156224042d20afd139b8afc226135e06c5b26665eed700c1cf12174cf`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3d9c2c9681f9060eff076f9ca8f4e36a1ddb67a2`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.23, "NO": 0.64, "YES": 0.13}`

