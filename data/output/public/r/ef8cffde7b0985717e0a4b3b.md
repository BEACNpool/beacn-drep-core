# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a high-impact treasury withdrawal and the required deep-research dossier was not complete enough to support a directional vote.

The proposal asked for 9,000,000 ADA to be deployed for 12 months into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM, yield returned at month 6, and all treasury-owned assets plus remaining yield returned at month 12. The proposer described this as a productive treasury deployment rather than a grant, with treasury ownership retained, monthly transparency reports, third-party assurance reports, and an independent multisig council administering custody.

Several core proposal details were supported in the proposal itself: the requested amount and 12-month structure, the modeled ADA-to-USDM deployment, the projected but not guaranteed yield, the council custody model, the listed risks, and the governance review triggers for drawdowns or missed reporting. However, important adoption and performance claims still lacked independent evidence, including Strike’s reported cumulative volume, trade count, trader count, protocol revenue, liquidity provider profit, and vault metrics such as TVL, APR, all-time return, drawdown, Sharpe ratio, and depositor count.

This is a conservative, evidence-based hold. A directional vote would require the missing alternatives analysis, stronger independently replayable evidence for the material performance and adoption claims, a more complete treasury analysis including line-item budget and milestone-gated disbursement, and risk review materials including independent assurance and a dependency map. Until those gates pass, BEACN cannot responsibly treat the proposal as ready for YES or NO.

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
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity and returned with realized yield.
- finding: Recipient: Independent council administering Strike Finance liquidity deployment
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy treasury-owned capital into Strike Finance V2 USDM liquidity infrastructure, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12, Provide monthly public transparency reports covering deployment, utilization, volume, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and material risks, Provide third-party assurance reports at deployment confirmation, month 6, and month 12
- finding: Deadline/expiry: 12 months after deployment, with month-6 yield distribution
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment, not grant funding, with treasury ownership retained throughout deployment.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD to produce approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployment is modeled to generate approximately 900,000 ADA-equivalent in annual yield at a 10% USD-denominated APR, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, more than 3,000 unique traders, more than 1.16 million USD protocol revenue, and more than 3.25 million USD liquidity provider profit.
- finding: Claim (adoption, supported_in_proposal, high materiality): Strike V2 data from 2026-03-20 through 2026-06-15 is presented as showing accelerating volume, revenue, trades, users, and open interest as liquidity deepened.
- finding: Claim (economic, proposer_asserted, high materiality): The Strike Liquidity Provider vault is described as having about 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, 4.97 Sharpe ratio, and 208 depositors after two months.
- missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, more than 3,000 unique traders, more than 1.16 million USD protocol revenue, and more than 3.25 million USD liquidity provider profit.
- missing: Independent evidence for: The Strike Liquidity Provider vault is described as having about 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, 4.97 Sharpe ratio, and 208 depositors after two months.
- missing: alternatives analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 9000000
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.60
- missing: line-item budget
- missing: milestone-gated disbursement
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: high
- finding: Governance risk: high
- finding: Technical risk: high
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment, not grant funding, with treasury ownership retained throughout deployment." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Strike reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, more than 3,000 unique traders, more than 1.16 million USD protocol revenue, and more than 3.25 million USD liquidity provider profit." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing alternatives analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9000000
- Risk review: Execution risk: high
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment, not grant funding, with treasury ownership retained throughout deployment." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional voting is blocked until dossier quality gates pass.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Dossier completeness not confirmed for this treasury proposal.
- Claims and evidence missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, more than 3,000 unique traders, more than 1.16 million USD protocol revenue, and more than 3.25 million USD liquidity provider profit.
- Claims and evidence missing: Independent evidence for: The Strike Liquidity Provider vault is described as having about 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, 4.97 Sharpe ratio, and 208 depositors after two months.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing alternatives analysis
- Synthesis status is blocked.

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.
- Missing dossier section: alternatives analysis

## Reproducibility
- input_hash: `24407892614762d5d833d9fdfc1f8f06a0be769d96984c43fae2ba5ff6efe9d6`
- snapshot_bundle_hash: `414e774c9dd02c2fc58a7659327b3ff96f52177ba01d3119afbf48b40bfec4e8`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

