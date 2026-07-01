# Rationale: gov_action1pa6a6yd7pdaxed9nqkshtvtu7jmqe5c8cpf0ej4lnatjj588qkpsq2x2sz2
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9033` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show a large treasury request with plausible ecosystem-growth objectives and some internal controls, but the deterministic assessment reports incomplete treasury, feasibility, risk, alternatives, and failure-mode analysis. Under the doctrine hierarchy, treasury stewardship and evidence quality outweigh speed and public-benefit growth, so the bounded nudge should be cautious and negative rather than rewarding an ambitious but thinly evidenced spend.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Alchemy by Sundial x Charms: Cardano-Native Bitcoin Treasury Protocol. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms.. The recorded treasury amount is 10,000,000 ada. The strongest grounded claim is: The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget.

A material weak point is that this claim remains proposer-asserted or thinly supported: The proposal says Cardano currently lacks a credible production BTCfi infrastructure layer and risks losing Bitcoin-backed structured exposure activity to other ecosystems. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Recipient: Intersect is proposed as interim fund administrator, subject to confirmation and final agreement; Sundial remains accountable for controlled deployment and delivery coordination.
- finding: Stated amount: 10,000,000 ada
- finding: Deliverables: Shared BTC reserve architecture with safety mechanisms and reserve-ratio rules, Composable Cardano-native FIRE and ICE assets, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on public dashboards for reserve ratio, asset supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Independent security review, audit, and economic modeling, Legal, compliance, disclosures, treasury reporting, risk documentation, and launch-readiness review, Treasury-supported staged launch liquidity
- finding: Deadline/expiry: Staged launch liquidity deployment over three months after enactment; monthly reporting is stated, but a full project completion deadline is not stated in document.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget.
- finding: Claim (economic, supported_in_proposal, high materiality): The request is split into two separated pools: approximately USD 1.0 million for protocol infrastructure and staged launch liquidity and approximately USD 1.0 million for delivery, audit, integrations, dashboards, governance reporting, legal/compliance work, and go-to-market execution.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 launch liquidity is described as treasury-supported, separated from operating spend, deployed in tranches, and structured so profits, yield, and returns are returned to the Cardano Treasury quarterly.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will create a shared BTC reserve architecture where FIRE and ICE are backed by the same BTC reserve, with reserve-ratio formulas and safety zones intended to constrain minting, redemption, and risky activity under stress.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual BTC exposure asset, while ICE is described as a lower-volatility USD-denominated BTC-backed asset with growth potential.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says Cardano currently lacks a credible production BTCfi infrastructure layer and risks losing Bitcoin-backed structured exposure activity to other ecosystems.
- missing: Independent evidence for: The proposal says Cardano currently lacks a credible production BTCfi infrastructure layer and risks losing Bitcoin-backed structured exposure activity to other ecosystems.
- missing: Independent evidence for: Charms is asserted to provide the technical foundation for issuing Bitcoin-native assets that can circulate as Cardano-native assets, while the proposal acknowledges bridge, oracle, asset-accounting, and protocol vulnerability risks.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says Cardano currently lacks a credible production BTCfi infrastructure layer and risks losing Bitcoin-backed structured exposure activity to other ecosystems." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show a large treasury request with plausible ecosystem-growth objectives and some internal controls, but the deterministic assessment reports incomplete treasury, feasibility, risk, alternatives, and failure-mode analysis. Under the doctrine hierarchy, treasury stewardship and evidence quality outweigh speed and public-benefit growth, so the bounded nudge should be cautious and negative rather than rewarding an ambitious but thinly evidenced spend.
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
- Claims and evidence missing: Independent evidence for: The proposal says Cardano currently lacks a credible production BTCfi infrastructure layer and risks losing Bitcoin-backed structured exposure activity to other ecosystems.
- Claims and evidence missing: Independent evidence for: Charms is asserted to provide the technical foundation for issuing Bitcoin-native assets that can circulate as Cardano-native assets, while the proposal acknowledges bridge, oracle, asset-accounting, and protocol vulnerability risks.
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
- input_hash: `8375a236cbd07e5d4dcf3ca88cf12076cd69fab81ecfa08320149afa11ca5a80`
- snapshot_bundle_hash: `154790a7c5b9cd7c68622db4681db741371569433ed1516c7fb160889393ff1f`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `617`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1675, "NO": 0.792, "YES": 0.0404}`

