# Rationale: gov_action1pa6a6yd7pdaxed9nqkshtvtu7jmqe5c8cpf0ej4lnatjj588qkpsq2x2sz2
Recommendation: **NO**
Score: `-0.5133` (raw `-0.4833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.49` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show a detailed concept and some itemized allocations, but the assessment is blocked by missing treasury, feasibility, risk, alternatives, and failure-mode analysis, while several high-materiality treasury protections and return mechanics are only proposer asserted. Under a large treasury ask, the doctrine favors caution when ecosystem upside is plausible but evidence coverage is incomplete.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large 10,000,000 ada treasury request and the review found too many unresolved evidence gaps, especially around budget analysis, feasibility, risk, alternatives, and failure modes.

The proposal asked the Cardano Treasury to fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms. It described two roughly USD 1 million pools using an approximate USD 0.20 per ada planning value: one for protocol infrastructure and staged launch liquidity, and one for delivery, audits, integrations, dashboards, governance reporting, legal and compliance work, documentation, education, partner activation, and launch coordination. The proposal also described FIRE and ICE assets, a shared BTC reserve architecture, reserve-ratio formulas, an initial 5.0x target reserve ratio, safety zones, public dashboards, monthly reports, and risk mitigations.

Several parts were supported in the proposal itself, including the requested amount, the two-pool planning structure, the staged launch-liquidity schedule, the FIRE and ICE design, and the stated reserve and safety mechanisms. However, important treasury protections were only proposer assertions, not independently evidenced in the review. That included the claim that profits, yield, and returns from treasury-supported launch liquidity would be returned quarterly to the Cardano Treasury, and the claim that launch-liquidity principal may be returned after Alchemy reaches a 30-day time-weighted average TVL of at least USD 60 million, subject to a later governance proposal.

The review gates did not clear the bar for a treasury withdrawal. The anchor document was available and replayable, and the strongest YES case was that the proposal substantiated the 10,000,000 ada request and its broad two-pool budget framing. But the treasury analysis was incomplete, the risk review was thin, synthesis was blocked, and seven decisive blockers remained open: missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis. For a large treasury action, BEACN treated those gaps as decisive and voted NO.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 10.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms.
- finding: Recipient: Sundial Protocol and Charms, with Intersect proposed as interim fund administrator subject to confirmation and final agreement.
- finding: Stated amount: 10,000,000 ada
- finding: Deliverables: Shared BTC reserve architecture with transparent safety mechanisms, Composable FIRE and ICE Cardano-native assets, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on public dashboards for reserve ratio, asset supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Independent security review, audit, and economic modeling, Staged treasury-supported launch liquidity, Legal/compliance work, documentation, ecosystem education, partner activation, and launch coordination
- finding: Deadline/expiry: Three-month staged liquidity deployment after enactment with monthly reporting; broader delivery deadline not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million split into two USD 1.0 million pools.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 is intended for protocol infrastructure and staged launch liquidity, kept separate from operating spend, deployed in three monthly tranches of approximately USD 250,000, USD 250,000, and USD 500,000.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 2 is intended for delivery, audit, integrations, dashboards, governance reporting, legal/compliance work, and go-to-market execution with itemized planning allocations totaling approximately USD 1.0 million.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will create a shared BTC reserve architecture for FIRE and ICE with reserve-ratio formulas, an initial 5.0x target reserve ratio, and safety zones that constrain minting and redemption as reserve conditions deteriorate.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual BTC upside asset, while ICE is described as a lower-volatility USD-denominated BTC-backed asset intended for wallet, DEX, dashboard, and DeFi integration.
- finding: Claim (economic, proposer_asserted, high materiality): The proposer states that profits, yield, and returns from treasury-supported launch liquidity will be returned to the Cardano Treasury quarterly, converted into ada through Cardano-native DEXs with methodology disclosed in monthly reports.
- missing: Independent evidence for: The proposer states that profits, yield, and returns from treasury-supported launch liquidity will be returned to the Cardano Treasury quarterly, converted into ada through Cardano-native DEXs with methodology disclosed in monthly reports.
- missing: Independent evidence for: The proposer states that launch liquidity principal may be returned after Alchemy reaches a 30-day time-weighted average TVL of at least USD 60 million, subject to a later formal governance proposal.
- missing: Independent evidence for: The proposal claims Cardano currently lacks a serious BTCfi infrastructure layer and risks Bitcoin-backed structured exposure consolidating on other chains and off-chain capital markets.
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
- finding: Requested ADA: 10.00M ADA
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million split into two USD 1.0 million pools." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that profits, yield, and returns from treasury-supported launch liquidity will be returned to the Cardano Treasury quarterly, converted into ada through Cardano-native DEXs with methodology disclosed in monthly reports." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 10.00M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million split into two USD 1.0 million pools." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show a detailed concept and some itemized allocations, but the assessment is blocked by missing treasury, feasibility, risk, alternatives, and failure-mode analysis, while several high-materiality treasury protections and return mechanics are only proposer asserted. Under a large treasury ask, the doctrine favors caution when ecosystem upside is plausible but evidence coverage is incomplete.
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
- Claims and evidence missing: Independent evidence for: The proposer states that profits, yield, and returns from treasury-supported launch liquidity will be returned to the Cardano Treasury quarterly, converted into ada through Cardano-native DEXs with methodology disclosed in monthly reports.
- Claims and evidence missing: Independent evidence for: The proposer states that launch liquidity principal may be returned after Alchemy reaches a 30-day time-weighted average TVL of at least USD 60 million, subject to a later formal governance proposal.
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
- input_hash: `6e96a82e9435b44c8392a42055960a8249b080e94ce8126125305929ab743283`
- snapshot_bundle_hash: `511ad49e22e777cc9031564befd33c48e8aec7ea198b33d5348fdd569a10547a`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1217`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2119, "NO": 0.7472, "YES": 0.0409}`

