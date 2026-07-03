# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NO**
Score: `-0.5133` (raw `-0.4833` + doctrine-LLM nudge `-0.03`) | Confidence: `1.0` | Readiness: `0.0`
> Reasoning layer (precomputed): A small negative nudge is justified because the request is large, involves treasury asset conversion into USDM and DeFi liquidity risk, and the deterministic assessment reports missing budget, feasibility, risk, alternatives, and failure-mode analysis. The document does include custody, reporting, return mechanics, and risk triggers, but most performance and yield claims are proposer-stated and not backed by references in the anchor text, so the evidence quality does not justify a positive spending nudge.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Strike Finance Liquidity Deployment. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure by selling ADA for USDM stablecoin liquidity, with treasury ownership retained and funds returned after the term.. The recorded treasury amount is 9,000,000 ADA. The strongest grounded claim is: The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding.

A material weak point is that this claim remains proposer-asserted or thinly supported: Strike claims more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure by selling ADA for USDM stablecoin liquidity, with treasury ownership retained and funds returned after the term.
- finding: Recipient: Independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta; Strike Finance would receive liquidity support but not unilateral custody.
- finding: Stated amount: 9,000,000 ADA
- finding: Deliverables: Deploy 9,000,000 ADA sold for USDM into Strike Finance V2 liquidity infrastructure, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets plus remaining realized yield at month 12, minus any realized losses in wind-down scenarios, Provide monthly public transparency reports covering deployment, utilization, volume, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and risks, Provide third-party assurance reports for deployment confirmation, month-6 yield distribution, and month-12 return of funds
- finding: Deadline/expiry: 12 months, with month-6 yield distribution and final return at month 12
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA would be sold for USDM, modeled at ADA = 0.15 USD to produce approximately 1,350,000 USDM of liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): Under modeled 10% USD-denominated annual yield assumptions, the deployment is expected to generate approximately 135,000 USD or 900,000 ADA-equivalent over 12 months, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike claims more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike claims it represented over 50% of Cardano trading activity over the past six months.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that V2 produced 87,288,044 USD total volume, 75,322,500 USD 30-day volume, 410,800 total trades, 2,681 total users, and 30,105 USD total revenue from 2026-03-20 through 2026-06-15.
- missing: Independent evidence for: Strike claims more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit.
- missing: Independent evidence for: Strike claims it represented over 50% of Cardano trading activity over the past six months.
- missing: Independent evidence for: The proposal states that V2 produced 87,288,044 USD total volume, 75,322,500 USD 30-day volume, 410,800 total trades, 2,681 total users, and 30,105 USD total revenue from 2026-03-20 through 2026-06-15.
- missing: Independent evidence for: The proposal states that the Strike Liquidity Provider vault has 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and a 4.97 Sharpe ratio after two months of history.
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
- finding: Six-month treasury flow regime: unsustainable
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike claims more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small negative nudge is justified because the request is large, involves treasury asset conversion into USDM and DeFi liquidity risk, and the deterministic assessment reports missing budget, feasibility, risk, alternatives, and failure-mode analysis. The document does include custody, reporting, return mechanics, and risk triggers, but most performance and yield claims are proposer-stated and not backed by references in the anchor text, so the evidence quality does not justify a positive spending nudge.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow signal is in unsustainable regime (advisory penalty applied).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Strike claims more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit.
- Claims and evidence missing: Independent evidence for: Strike claims it represented over 50% of Cardano trading activity over the past six months.
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
- input_hash: `e65652bbdd84613acaa0286c33b4062f38a6535b18b3fb617b371e3475d0ea8f`
- snapshot_bundle_hash: `b041eb4ab875b28b944b0b8f64327e32bf1fefcd612cd35272c19b21a3f52025`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `b97265e867768077aac16ceb31ccfe1be639d187`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `800`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1518, "NO": 0.8093, "YES": 0.0389}`

