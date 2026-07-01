# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9033` | Readiness: `0.0`
> Reasoning layer (precomputed): A small negative nudge is justified because the request is large, the deterministic assessment remains blocked on missing budget, feasibility, risk, alternatives, and failure-mode analysis, and several high-materiality claims rely on proposer-supplied figures or forward-looking modeled returns rather than completed audit evidence or independently linked references.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Strike Finance Liquidity Deployment. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: A 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure by selling ADA for USDM to provide stablecoin-denominated liquidity.. The recorded treasury amount is 9000000. The strongest grounded claim is: The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding.

A material weak point is that this claim remains proposer-asserted or thinly supported: Strike claims it has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: A 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure by selling ADA for USDM to provide stablecoin-denominated liquidity.
- finding: Recipient: Independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta as administrator; Strike Finance V2 liquidity infrastructure as deployment venue.
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy treasury-owned capital as USDM liquidity for Strike Finance V2, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of remaining treasury-owned deployed assets plus realized yield at month 12, minus any realized losses in a wind-down, Provide monthly public transparency reports covering deployment status, utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and risks, Provide third-party assurance reports for deployment confirmation, month-6 distribution, and month-12 return
- finding: Deadline/expiry: 12 months, with month-6 yield distribution and month-12 final return
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD to produce approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): Under modeled assumptions of a 10% USD-denominated APR, the deployment is expected to generate approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike claims it has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, supported_in_proposal, high materiality): Strike V2 data from 2026-03-20 through 2026-06-15 is presented as showing 87,288,044 USD total V2 volume, 410,800 trades, 2,681 users, 30,105 USD revenue, and peak open interest of 1,246,007 USD.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal claims Strike accounted for more than 50% of Cardano trading activity over the past six months.
- missing: Independent evidence for: Strike claims it has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: The proposal claims Strike accounted for more than 50% of Cardano trading activity over the past six months.
- missing: Independent evidence for: The proposal states Strike V2 has undergone unofficial reviews and that an official audit by Christian Schmitz is expected to be finalized by July 1, 2026, with the report published upon completion.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike claims it has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small negative nudge is justified because the request is large, the deterministic assessment remains blocked on missing budget, feasibility, risk, alternatives, and failure-mode analysis, and several high-materiality claims rely on proposer-supplied figures or forward-looking modeled returns rather than completed audit evidence or independently linked references.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~18 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Strike claims it has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: The proposal claims Strike accounted for more than 50% of Cardano trading activity over the past six months.
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
- input_hash: `5bcdd9e0c3091714e9d9d2b51e9b6011ccf34ab879581c0a69d7848c5e2c7b65`
- snapshot_bundle_hash: `34c4953d361b5fe68ee6ce6262e5e556180699b5df22476cf9963024f2df9da1`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `659`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1675, "NO": 0.792, "YES": 0.0404}`

