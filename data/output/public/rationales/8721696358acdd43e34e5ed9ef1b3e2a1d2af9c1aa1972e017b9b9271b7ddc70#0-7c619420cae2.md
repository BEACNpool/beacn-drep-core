# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline evidence needed for a responsible treasury vote. This is a conservative, evidence-based hold, not a rejection of the idea.

The proposal requested a 12-month deployment of 9,000,000 ADA into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM and treasury ownership retained during deployment. It proposed returning first-six-month realized yield at month 6, returning deployed assets plus remaining realized yield at month 12 minus any realized wind-down losses, publishing monthly transparency reports, and providing third-party assurance reports. The proposal also identified major risks, including ADA appreciation underperformance, USDM depeg or redemption risk, smart contract risk, yield underperformance, liquidity risk, and multisig custody or operational risk.

Some claims were supported within the proposal itself, including the requested 9,000,000 ADA deployment, the USDM liquidity model, the modeled 10% USD-denominated APR, the 12-month return structure, and the statement that Strike Finance would not have unilateral custody or control. However, several important claims remained only proposer-asserted or lacked independent evidence in the review, including Strike’s claimed historical volume, trade count, user count, protocol revenue, liquidity provider profit, share of Cardano trading activity, vault performance figures, and audit status.

The abstain would be unblocked by a complete review record: the missing treasury withdrawal amount field, a complete proposal summary, line-item budget analysis, milestone-gated disbursement plan, feasibility assessment, risk and failure-mode analysis, alternatives analysis, community impact analysis, independent evidence for major adoption and performance claims, mitigation evidence, and independent assurance. Without that baseline, BEACN could not vote YES or NO without pretending to have more certainty than the evidence supported.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity
- finding: Recipient: Strike Finance liquidity deployment administered by an independent council/multisig composed of Rami from Snek, Phil from Surf, and James from Monetra/Snek/Surf/Moneta as stated inconsistently in the document
- finding: Stated amount: 9,000,000 ADA
- finding: Deliverables: Deploy treasury-owned capital into Strike Finance V2 USDM liquidity for 12 months, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets plus remaining realized yield at month 12, minus any realized losses in a wind-down, Provide monthly public transparency reports covering deployment status, liquidity utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality metrics, distributions, and material risks, Provide third-party assurance reports for deployment confirmation, month-6 yield distribution, and month-12 return of funds
- finding: Deadline/expiry: 12 months after deployment, with midpoint yield return at month 6
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month non-grant liquidity deployment into Strike Finance V2, with treasury ownership retained throughout deployment.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA would be sold for USDM, modeled at ADA = 0.15 USD to produce approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal models a 10% USD-denominated annual percentage rate generating approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, but states these returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike Finance claims it has processed over 1.13 billion USD in cumulative volume, facilitated roughly 968,000 to 1,001,000 trades, served over 3,000 unique traders, produced over 1.16 million USD in protocol revenue, and generated over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The document claims Strike represented over 50% of Cardano trading activity over the past six months.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says V2 public data from 2026-03-20 through 2026-06-15 shows 87,288,044 USD total V2 volume, 410,800 trades, 2,681 users, 30,105 USD revenue, and peak open interest of 1,246,007 USD.
- missing: Independent evidence for: Strike Finance claims it has processed over 1.13 billion USD in cumulative volume, facilitated roughly 968,000 to 1,001,000 trades, served over 3,000 unique traders, produced over 1.16 million USD in protocol revenue, and generated over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: The document claims Strike represented over 50% of Cardano trading activity over the past six months.
- missing: Independent evidence for: The proposal says V2 public data from 2026-03-20 through 2026-06-15 shows 87,288,044 USD total V2 volume, 410,800 trades, 2,681 users, 30,105 USD revenue, and peak open interest of 1,246,007 USD.
- missing: Independent evidence for: The proposal states the Strike Liquidity Provider vault has 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, +69,537.24 USD all-time P&L, 1.15% maximum drawdown, and a 4.97 Sharpe ratio.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.68
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
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month non-grant liquidity deployment into Strike Finance V2, with treasury ownership retained throughout deployment." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Strike Finance claims it has processed over 1.13 billion USD in cumulative volume, facilitated roughly 968,000 to 1,001,000 trades, served over 3,000 unique traders, produced over 1.16 million USD in protocol revenue, and generated over 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month non-grant liquidity deployment into Strike Finance V2, with treasury ownership retained throughout deployment." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: Strike Finance claims it has processed over 1.13 billion USD in cumulative volume, facilitated roughly 968,000 to 1,001,000 trades, served over 3,000 unique traders, produced over 1.16 million USD in protocol revenue, and generated over 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: The document claims Strike represented over 50% of Cardano trading activity over the past six months.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `7c619420cae255d3ec4c3c61d0c22723a6030ec91b8ef4fa36d68958dab86371`
- snapshot_bundle_hash: `96616cc90a386eabbfda4a1147021dfed852178c129158409533e7ac43c76b56`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

