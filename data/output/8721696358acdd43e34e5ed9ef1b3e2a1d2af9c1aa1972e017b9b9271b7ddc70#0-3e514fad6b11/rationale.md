# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **NO**
Score: `-0.12` (raw `-0.66` + doctrine-LLM nudge `-0.03`) | Confidence: `0.72` | Readiness: `0.8`
> Reasoning layer (precomputed): A small cautionary nudge is justified because the request is large, principal is converted from ADA to USDM, returns are modeled rather than guaranteed, key traction figures are mostly proposer-asserted in a document with no references, and the audit is described as pending rather than completed in the supplied text.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Strike Finance Liquidity Deployment. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM stablecoin liquidity and returned after the deployment period with realized yield minus any losses. It asks the treasury for 9000000 ADA. The strongest grounded claim is: The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding.

A material claim remains proposer-asserted or thinly supported: Strike Finance claims cumulative traction of more than 1.13 billion USD in volume, about one million trades, over 3,000 unique traders, more than 1.16 million USD protocol revenue, and more than 3.25 million USD liquidity provider profit.

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
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM stablecoin liquidity and returned after the deployment period with realized yield minus any losses.
- finding: Recipient: Independent council administrator for Strike Finance V2 liquidity deployment
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy 9,000,000 ADA sold for USDM into Strike Finance V2 liquidity infrastructure, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12, minus any realized losses in a wind-down, Provide monthly public transparency reports covering deployment, utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and risks, Use independent multisig administration and third-party assurance reports for deployment confirmation, month-6 distribution, and month-12 return
- finding: Deadline/expiry: 12 months after deployment, with midpoint yield return at month 6
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, with modeling assuming ADA equals 0.15 USD and approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal models a 10% USD-denominated annual return, approximately 135,000 USD or 900,000 ADA-equivalent, but states these returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike Finance claims cumulative traction of more than 1.13 billion USD in volume, about one million trades, over 3,000 unique traders, more than 1.16 million USD protocol revenue, and more than 3.25 million USD liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states that Strike represented over 50% of Cardano trading activity during the past six months.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal reports V2 public data from 2026-03-20 to 2026-06-15, including 87,288,044 USD total V2 volume, 410,800 trades, 2,681 users, and 30,105 USD total V2 revenue.
- missing: Independent evidence for: Strike Finance claims cumulative traction of more than 1.13 billion USD in volume, about one million trades, over 3,000 unique traders, more than 1.16 million USD protocol revenue, and more than 3.25 million USD liquidity provider profit.
- missing: Independent evidence for: The proposal states that Strike represented over 50% of Cardano trading activity during the past six months.
- missing: Independent evidence for: The proposal reports V2 public data from 2026-03-20 to 2026-06-15, including 87,288,044 USD total V2 volume, 410,800 trades, 2,681 users, and 30,105 USD total V2 revenue.
- missing: Independent evidence for: The proposal says Christian Schmitz is conducting an official audit expected by July 1, 2026, and that the report will be published upon completion.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike Finance claims cumulative traction of more than 1.13 billion USD in volume, about one million trades, over 3,000 unique traders, more than 1.16 million USD protocol revenue, and more than 3.25 million USD liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: A small cautionary nudge is justified because the request is large, principal is converted from ADA to USDM, returns are modeled rather than guaranteed, key traction figures are mostly proposer-asserted in a document with no references, and the audit is described as pending rather than completed in the supplied text.
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
- Claims and evidence missing: Independent evidence for: Strike Finance claims cumulative traction of more than 1.13 billion USD in volume, about one million trades, over 3,000 unique traders, more than 1.16 million USD protocol revenue, and more than 3.25 million USD liquidity provider profit.
- Claims and evidence missing: Independent evidence for: The proposal states that Strike represented over 50% of Cardano trading activity during the past six months.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `3e514fad6b119e723ddfb0aa605a7ad0d8b2e18727a22bbd1807ecb66e30cc6a`
- snapshot_bundle_hash: `3d7eebc33e1bfa9ddd6245e723b9ae644455ef6af5315dae7942933c05b96fb6`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.23, "NO": 0.64, "YES": 0.13}`

