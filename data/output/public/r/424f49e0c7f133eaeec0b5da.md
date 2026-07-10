# Rationale: gov_action1pa6a6yd7pdaxed9nqkshtvtu7jmqe5c8cpf0ej4lnatjj588qkpsq2x2sz2
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7758` | Readiness: `0.85`
> Reasoning layer (precomputed): A small negative nudge is warranted because the ask is large, technically novel, and dependent on pending administration, external protocol security, adoption, and future governance actions, while several strategic demand and Cardano-gap claims are asserted or only externally referenced rather than demonstrated in the proposal text. The proposal does include meaningful controls and budget detail, so the adjustment should be modest rather than maximal.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and the required Net Change Limit has not yet been pinned and independently verified from public chain evidence. That blocks a directional treasury vote under BEACN’s evidence rules, so this is a conservative hold rather than a judgment that the proposal should pass or fail.

The action requests 10,000,000 ada to fund Alchemy, a Cardano-native Bitcoin treasury protocol by Sundial Protocol and Charms. The proposal describes two roughly USD 1 million planning pools at an approximate USD 0.20 per ada reference value: one for protocol infrastructure and staged launch liquidity, and one for delivery, audits, integrations, dashboards, reporting, legal/compliance work, and launch execution. It also claims treasury-supported profits, yield, and returns would go back to the Cardano Treasury quarterly, with principal return dependent on later TVL conditions and governance approval.

Several core proposal details were supported in the proposal itself: the budget structure, the staged liquidity plan, the FIRE and ICE asset design, reserve-ratio formulas, safety zones, identified risks, and proposed mitigations such as overcollateralization, security review, dashboards, pause rules, reporting, and administrator oversight. Other claims were weaker. In particular, the claim that Cardano lacks a serious production BTCfi infrastructure layer, and that failure to fund this would push Bitcoin-backed structured exposure elsewhere, was treated as unsupported by independent evidence. Intersect is also only proposed as interim fund administrator, with confirmation and final agreement still pending.

The review found a replayable anchor document and a plausible strongest-YES case around the documented budget, but treasury withdrawals require elevated scrutiny because they spend shared ada and set precedent. The hold would be unblocked by a pinned, independently verified Net Change Limit from public chain evidence, plus stronger independent support for the strategic adoption claims, clearer sustainability and cost-benefit analysis, independent assurance, and a dependency map for execution and governance risk.

## Review Tree
- overall_status: `incomplete`

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
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms.
- finding: Recipient: Intersect is proposed as interim fund administrator subject to confirmation and final agreement; Sundial remains accountable for deployment and delivery with Charms as technical partner.
- finding: Stated amount: 10,000,000 ada
- finding: Deliverables: BTC reserve architecture with transparent safety mechanisms, Composable FIRE and ICE Cardano-native assets, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on public dashboards for reserve ratio, asset supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Independent security review, audit, and economic modeling, Staged launch liquidity deployed over three months, Legal/compliance work, documentation, DRep communications, partner activation, and launch coordination
- finding: Deadline/expiry: Staged liquidity deployment over three months after enactment, with monthly reporting; exact final delivery deadline not stated in document.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 would provide protocol infrastructure and staged launch liquidity, kept separate from operating spend and deployed in three monthly tranches of approximately USD 250,000, USD 250,000, and USD 500,000.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 2 would fund delivery, audit, integrations, dashboards, governance reporting, legal/compliance work, and go-to-market execution with itemized planning allocations totaling approximately USD 1.0 million.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal says profits, yield, and returns from treasury-supported launch liquidity will be returned to the Cardano Treasury quarterly, while principal may be returned only after a 30-day time-weighted average TVL of at least USD 60 million and a later governance approval.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy would use a shared BTC reserve backing FIRE and ICE, with reserve ratio formula (V x P) / L, FIRE price formula ((V x P) - L) / N+, an initial 5.0x target reserve ratio, and safety zones above 4.0x, between 2.0x and 4.0x, and below 2.0x.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual BTC reserve claim with first-loss downside and upside exposure, while ICE is described as a USD-denominated BTC-backed asset intended for lower-volatility exposure with growth potential.
- missing: Independent evidence for: The proposer asserts Cardano currently lacks a serious production BTCfi infrastructure layer and that failure to pass the proposal would leave Bitcoin-backed structured exposure to consolidate on other chains and off-chain markets.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 10000000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.74
- missing: sustainability path
- missing: cost-benefit clarity
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer asserts Cardano currently lacks a serious production BTCfi infrastructure layer and that failure to pass the proposal would leave Bitcoin-backed structured exposure to consolidate on other chains and off-chain markets." — so cost or precedent may outweigh the benefit.
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
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 10000000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small negative nudge is warranted because the ask is large, technically novel, and dependent on pending administration, external protocol security, adoption, and future governance actions, while several strategic demand and Cardano-gap claims are asserted or only externally referenced rather than demonstrated in the proposal text. The proposal does include meaningful controls and budget detail, so the adjustment should be modest rather than maximal.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer asserts Cardano currently lacks a serious production BTCfi infrastructure layer and that failure to pass the proposal would leave Bitcoin-backed structured exposure to consolidate on other chains and off-chain markets.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `64e861e262eb5205d59a72d9c98ab8b86b965377bdec54eebf6a8e1c27e60a91`
- snapshot_bundle_hash: `3da095ca8882f78e3a89459ce8c0da3e1284027d1bdc945b8ca3f310e2238594`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

