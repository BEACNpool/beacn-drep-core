# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NO**
Score: `-0.5133` (raw `-0.4833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.49` | Readiness: `0.0`
> Reasoning layer (precomputed): A small negative nudge is justified because the request is large and economically complex, the deterministic assessment says treasury analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis are incomplete, and several high-materiality claims remain proposer-asserted despite acknowledged downside risks.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal with too many unresolved review blockers and unsupported material claims. The proposal asks for 9,000,000 ADA to be sold for USDM and deployed for 12 months into Strike Finance V2 liquidity infrastructure, so BEACN applied elevated scrutiny because shared treasury funds would be put at execution, market, custody, and precedent risk.

The proposal framed the request as a productive treasury deployment rather than grant funding. It committed to monthly public transparency reports, third-party assurance reports at deployment, month 6, and month 12, a month-6 yield return, and return of principal plus remaining yield at month 12 minus realized wind-down losses. It also described an independent multisig council and named risks including ADA appreciation, USDM depeg or redemption risk, smart contract risk, yield underperformance, liquidity risk, and multisig operational risk.

Some points were supported in the proposal: the 9,000,000 ADA request, the plan to sell ADA into USDM, the stated Strike V2 volume, trades, users, and revenue for 2026-03-20 through 2026-06-15, the reported two-month vault performance figures, the named risk categories, and the drawdown review triggers. But key claims remained only proposer-asserted or lacked independent evidence, including the modeled 10% USD-denominated APR and the broader historical Strike Finance adoption and revenue figures.

The review gates did not clear. Treasury analysis was incomplete, with missing budget analysis, no line-item budget, and no milestone-gated disbursement. Risk review was thin, with missing mitigation evidence and independent assurance. The synthesis was blocked, and the review also lacked a complete proposal summary, feasibility assessment, alternatives analysis, failure-mode analysis, and community impact analysis. For a treasury withdrawal of this size and complexity, BEACN concluded that the cost, risk, and precedent concerns outweighed the supported benefits on the evidence available.

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
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity
- finding: Recipient: independent council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta as administrator and multisig overseer
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy treasury-owned capital as USDM liquidity for Strike Finance V2, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets including remaining principal and realized yield at month 12, minus any realized losses in wind-down scenarios, Provide monthly public transparency reports covering deployment status, liquidity utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality metrics, distributions, and risks, Provide third-party assurance reports at deployment confirmation, month-6 yield distribution, and month-12 return of funds
- finding: Deadline/expiry: 12 months after deployment, with month-6 yield distribution
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA would be sold for USDM, modeled at ADA = 0.15 USD to produce approximately 1,350,000 USDM of liquidity.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal models a 10% USD-denominated annual percentage rate, generating approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, while stating returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike Finance reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit.
- finding: Claim (adoption, supported_in_proposal, medium materiality): Strike V2 data from 2026-03-20 through 2026-06-15 is presented as 87,288,044 USD total V2 volume, 410,800 total V2 trades, 2,681 total V2 users, and 30,105 USD total V2 revenue.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states the Strike Liquidity Provider vault has 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and a 4.97 Sharpe ratio over two months of history.
- missing: Independent evidence for: The proposal models a 10% USD-denominated annual percentage rate, generating approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, while stating returns are not guaranteed.
- missing: Independent evidence for: Strike Finance reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit.
- missing: Independent evidence for: The proposal states Strike Finance will not have unilateral custody or control of treasury assets because an independent multisig council will administer and oversee the deployment.
- missing: Independent evidence for: The proposal states Strike has never received Cardano Treasury funding and that this request fits within the current 2026 Net Change Limit.
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
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal models a 10% USD-denominated annual percentage rate, generating approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, while stating returns are not guaranteed." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small negative nudge is justified because the request is large and economically complex, the deterministic assessment says treasury analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis are incomplete, and several high-materiality claims remain proposer-asserted despite acknowledged downside risks.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal models a 10% USD-denominated annual percentage rate, generating approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, while stating returns are not guaranteed.
- Claims and evidence missing: Independent evidence for: Strike Finance reports more than 1.13 billion USD in cumulative volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit.
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
- input_hash: `bc9c509d5f9f27a37d365cb24bcedd43df3452c33d2ea665db7acab58a3d5c0c`
- snapshot_bundle_hash: `70eed9c0f9daa5c26c7614892e2c4de9e331fcc568566322ba8f869750a227b4`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `961`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2119, "NO": 0.7472, "YES": 0.0409}`

