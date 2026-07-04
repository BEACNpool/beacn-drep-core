# Rationale: gov_action1pa6a6yd7pdaxed9nqkshtvtu7jmqe5c8cpf0ej4lnatjj588qkpsq2x2sz2
Recommendation: **NO**
Score: `-0.5133` (raw `-0.4833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.49` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal contains substantial internal detail, but the deterministic assessment remains blocked for missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis. Under BEACN doctrine, a large treasury withdrawal with incomplete diligence and thin risk review warrants a conservative negative nudge even where the proposal describes treasury protections and public-benefit intent.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large 10,000,000 ada treasury withdrawal, and the review record was incomplete on core diligence: budget analysis, feasibility, risk, alternatives, failure modes, and community impact.

The proposal asked the Cardano Treasury to fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms. It described two roughly USD 1 million planning pools, with one for protocol infrastructure and staged launch liquidity, and one for delivery, audits, integrations, dashboards, reporting, legal/compliance, administration, and go-to-market work. The proposal also described FIRE and ICE assets backed by a shared BTC reserve, reserve-ratio rules, public dashboards, monthly governance reports, independent review, and treasury-owned launch liquidity.

Several internal claims were well-supported in the proposal itself, including the requested amount, the two-pool budget structure, the planned reserve-ratio design, the FIRE and ICE asset descriptions, and the intended return of liquidity profits to the Treasury. But an important adoption claim was not independently supported: that Cardano lacks serious production BTCfi infrastructure and that Alchemy would provide the reusable primitives and liquidity needed to attract Bitcoin-aligned capital.

The treasury review gates did not clear. The anchor document was available, and the strongest YES case was acknowledged: the proposal did substantiate its 10,000,000 ada request and broad planning budget. But treasury withdrawals require elevated scrutiny because they spend shared ADA and create precedent. With thin claims-and-evidence status, incomplete treasury analysis, thin risk review, no stated deadline, and seven decisive blockers still open, BEACN’s evidence-based conclusion was NO.

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
- finding: Stated amount: 10000000
- finding: Deliverables: Shared BTC reserve architecture with transparent safety mechanisms and reserve-ratio rules, Composable Cardano-native FIRE and ICE assets, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on public dashboards for reserve ratio, asset supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Independent security review, audit, and economic modeling, Staged launch liquidity deployed over three months, Legal/compliance work, disclosures, DRep communications, partner activation, fund administration, and accounting
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 is intended for protocol infrastructure and staged launch liquidity, kept separate from operating expenses, deployed in three tranches over three months, and structured so profits, yield, and returns from launch liquidity are returned to the Cardano Treasury quarterly.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 2 is intended for delivery, audit, integrations, dashboards, governance reporting, legal/compliance work, fund administration, and go-to-market execution with itemized planning allocations totaling approximately USD 1.0 million.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will create a shared BTC reserve architecture backing FIRE and ICE with a reserve-ratio formula, an initial 5.0x target reserve ratio, and safety zones that constrain minting and redemption as reserve conditions weaken.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual BTC-backed claim with upside and first-loss downside, while ICE is described as lower-volatility USD-denominated BTC-backed exposure with growth potential.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states that launch liquidity will be treasury-supported and treasury-owned, with an initial target of approximately USD 800,000 FIRE-side liquidity and USD 200,000 ICE-side liquidity subject to optimization.
- missing: Independent evidence for: The document claims Cardano lacks a serious production BTCfi infrastructure layer and that Alchemy would provide reusable Cardano BTCfi primitives, reporting, integrations, and liquidity to attract Bitcoin-aligned capital.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The document claims Cardano lacks a serious production BTCfi infrastructure layer and that Alchemy would provide reusable Cardano BTCfi primitives, reporting, integrations, and liquidity to attract Bitcoin-aligned capital." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal contains substantial internal detail, but the deterministic assessment remains blocked for missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis. Under BEACN doctrine, a large treasury withdrawal with incomplete diligence and thin risk review warrants a conservative negative nudge even where the proposal describes treasury protections and public-benefit intent.
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
- Claims and evidence missing: Independent evidence for: The document claims Cardano lacks a serious production BTCfi infrastructure layer and that Alchemy would provide reusable Cardano BTCfi primitives, reporting, integrations, and liquidity to attract Bitcoin-aligned capital.
- Claims and evidence missing: complete proposal summary
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
- input_hash: `7184aac8bfc8717e765154ca5a35084916d61cf2c8213884f8b20b988a0846a8`
- snapshot_bundle_hash: `89146dce221800bacd620ee3f6d5cf7cee91164f40ade99476f5d58645785aea`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `960`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2119, "NO": 0.7472, "YES": 0.0409}`

