# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NO**
Score: `-0.6633` (raw `-0.6333` + doctrine-LLM nudge `-0.03`) | Confidence: `0.64` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal provides unusually concrete terms, metrics, custody structure, reporting commitments, and risk disclosures, but the treasury stewardship concern remains substantial because 9,000,000 ADA would be converted into USDM and exposed to stablecoin, market, smart-contract, and custody risks while key performance and audit claims are largely proposer-supplied within the anchor document. The deterministic engine already captures the incomplete treasury analysis and hard gates, so the bounded nudge is only a modest caution penalty for evidence quality and downside protection.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal that would convert 9,000,000 ADA into USDM liquidity, and the review found that the upside case was not supported strongly enough to justify the treasury, stablecoin, market, smart-contract, custody, and execution risks.

The proposal asked for a 12-month deployment into Strike Finance V2 liquidity infrastructure, handled by an independent multisig council rather than Strike having unilateral custody. It promised monthly transparency reports, third-party assurance reports, a month-6 return of realized yield, and a month-12 return of the remaining treasury-owned assets plus yield, minus any realized wind-down losses. The proposer framed this as productive treasury deployment rather than grant funding, with the ADA sold into USDM and modeled as about 1,350,000 USDM of liquidity.

Several core facts were supported inside the proposal: the requested amount and 12-month structure, the USDM deployment model, the stated V2 volume and usage figures from March 20 to June 15, 2026, the reported vault TVL/APR/return/drawdown, the independent multisig custody design, and the listed risk disclosures. But important parts of the benefit case remained thin or proposer-supplied, including the expected roughly 900,000 ADA-equivalent annual yield and broader Strike historical adoption and revenue claims. The review also noted missing independent assurance, no documented milestone-gated disbursement, an incomplete treasury diligence dossier, missing dependency mapping, and an unknown execution-risk assessment.

The evidence gates were strong enough to review the action, and the best YES case was acknowledged: the proposal was unusually concrete and clearly structured as a treasury-owned liquidity deployment. But treasury withdrawals carry a higher bar because they consume shared ADA and set precedent. With unsupported material claims, incomplete treasury analysis, no milestone-gated release, and substantial downside exposure, BEACN’s evidence-based conclusion was that the costs and risks outweighed the proven benefits, so the vote was NO.

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
- finding: Deep research dossier: required
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure by selling withdrawn ADA for USDM-denominated liquidity
- finding: Recipient: independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta, for deployment into Strike Finance V2
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy treasury-owned capital into Strike Finance V2 USDM liquidity for 12 months, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of remaining treasury-owned deployed assets plus remaining realized yield at month 12, minus any realized losses in a wind-down, Provide monthly public transparency reports covering deployment status, liquidity utilization, volume, open interest, profit and loss, yield, drawdown, stablecoin exposure, market quality metrics, distributions, and material risks, Publish third-party assurance reports for deployment confirmation, month-6 yield distribution, and month-12 return of funds
- finding: Deadline/expiry: 12 months from deployment, with month-6 yield distribution
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD as approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, proposer_asserted, high materiality): Under modeled assumptions, the deployment is expected to generate approximately 900,000 ADA-equivalent annual yield, but the document states these returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports more than 1.13 billion USD in cumulative volume, about one million trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, supported_in_proposal, high materiality): The document states V2 produced 87,288,044 USD total volume, 75,322,500 USD 30-day volume, 410,800 total trades, 2,681 total users, and 30,105 USD total revenue from 2026-03-20 through 2026-06-15.
- finding: Claim (economic, supported_in_proposal, high materiality): The Strike liquidity provider vault is reported as having 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and a two-month operating history.
- missing: Independent evidence for: Under modeled assumptions, the deployment is expected to generate approximately 900,000 ADA-equivalent annual yield, but the document states these returns are not guaranteed.
- missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, about one million trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: Christian Schmitz is stated to be conducting an official audit expected by July 1, 2026, with the report to be published upon completion.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Under modeled assumptions, the deployment is expected to generate approximately 900,000 ADA-equivalent annual yield, but the document states these returns are not guaranteed." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal provides unusually concrete terms, metrics, custody structure, reporting commitments, and risk disclosures, but the treasury stewardship concern remains substantial because 9,000,000 ADA would be converted into USDM and exposed to stablecoin, market, smart-contract, and custody risks while key performance and audit claims are largely proposer-supplied within the anchor document. The deterministic engine already captures the incomplete treasury analysis and hard gates, so the bounded nudge is only a modest caution penalty for evidence quality and downside protection.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- No milestone-gated disbursement documented.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Under modeled assumptions, the deployment is expected to generate approximately 900,000 ADA-equivalent annual yield, but the document states these returns are not guaranteed.
- Claims and evidence missing: Independent evidence for: Strike reports more than 1.13 billion USD in cumulative volume, about one million trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `77a84b79616a3efb0fee50dfc50b62da142c62a76194c8f88ebe7b7e74f378a1`
- snapshot_bundle_hash: `134c1122aa3f576ce00da372a163cf742f2d7a2a6bca6029cf33f44ff8a96181`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `32`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

