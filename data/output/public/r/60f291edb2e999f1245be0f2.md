# Rationale: gov_action1pa6a6yd7pdaxed9nqkshtvtu7jmqe5c8cpf0ej4lnatjj588qkpsq2x2sz2
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is more detailed than a thin treasury ask and includes staged deployment, audits, reporting, fund separation, pause rules, and some externally checkable market references, but the requested amount is large and several decisive benefits depend on unverified adoption, treasury-return, and administrator-execution assumptions. Under the doctrine, public-benefit ecosystem growth does not outweigh treasury stewardship when upside and demand translation are only partially evidenced, so a small cautionary negative nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large 10,000,000 ada treasury request, and the strongest claimed treasury upside was not independently supported. The proposal was detailed, but treasury withdrawals require a higher evidence bar because they spend shared ADA and set precedent.

The action requested funding for Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms. The proposal described two roughly USD 1 million planning pools: one for protocol infrastructure and staged launch liquidity, and one for delivery, audits, integrations, dashboards, legal and compliance work, administration, and go-to-market. It also described FIRE and ICE assets backed by a shared BTC reserve, reserve-ratio rules, staged liquidity deployment, dashboards, monthly reporting, security review, and economic modeling.

Several parts were well-supported in the proposal itself, including the amount requested, the budget split, the staged liquidity tranches, the FIRE and ICE reserve design, and the stated risk mitigations. Some market-demand references were independently checkable. But key claims remained thin or unsupported, especially the claim that profits, yield, and returns from launch liquidity would be returned quarterly to the Cardano Treasury, and the claim that Cardano lacks serious production BTCfi infrastructure such that not funding Alchemy would push this activity elsewhere.

The review gates found a pinned and replayable anchor document, and the counterargument pass recognized a real YES case: the proposal was more complete than a thin treasury ask and cleared some evidence gates. But the treasury analysis was missing a sustainability path and cost-benefit clarity, the risk review lacked independent assurance and a dependency map, and the broader treasury flow signal was already in an unsustainable regime. On balance, BEACN concluded that the public-benefit case did not outweigh treasury stewardship concerns, so the evidence supported a NO vote.

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
- finding: Requested: Fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms.
- finding: Recipient: Sundial Protocol and Charms, with Intersect proposed as interim fund administrator subject to confirmation and final agreement.
- finding: Stated amount: 10,000,000 ada
- finding: Deliverables: Shared BTC reserve architecture with FIRE and ICE assets, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on dashboards for reserve ratio, asset supply, liquidity health, fee flows, and deployment status, Monthly governance reports and BTCfi reporting standards, Independent security review, audit, and economic modeling, Staged launch liquidity and treasury-supported reserve deployment
- finding: Deadline/expiry: Staged liquidity deployment over three months after enactment, with monthly reporting; other final delivery dates are not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 is intended for protocol infrastructure and staged launch liquidity, with launch liquidity kept separate from operating expenses and deployed in three monthly tranches of approximately USD 250,000, USD 250,000, and USD 500,000.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 2 is intended for delivery, audit, integrations, dashboards, legal/compliance work, administration, and go-to-market, with itemized planning allocations totaling approximately USD 1.0 million.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will create a shared BTC reserve architecture where FIRE and ICE are backed by the same BTC reserve, with reserve-ratio formulas, a 5.0x initial target reserve ratio, and safety zones at above 4.0x, between 2.0x and 4.0x, and below 2.0x.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual Bitcoin-backed claim, while ICE is described as a lower-volatility USD-denominated BTC-backed asset, both intended to be composable Cardano-native assets.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that profits, yield, and returns generated by the launch liquidity position will be returned to the Cardano Treasury quarterly, converted into ada through Cardano-native DEXs with methodology disclosed in monthly reports.
- missing: Independent evidence for: The proposal states that profits, yield, and returns generated by the launch liquidity position will be returned to the Cardano Treasury quarterly, converted into ada through Cardano-native DEXs with methodology disclosed in monthly reports.
- missing: Independent evidence for: The proposal asserts that Cardano currently lacks a serious production BTCfi infrastructure layer and that failure to fund Alchemy would leave Bitcoin-backed structured exposure consolidating on other chains and off-chain markets.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 10000000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest NO: a material claim is unsupported — "The proposal states that profits, yield, and returns generated by the launch liquidity position will be returned to the Cardano Treasury quarterly, converted into ada through Cardano-native DEXs with methodology disclosed in monthly reports." — so cost or precedent may outweigh the benefit.
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
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal is more detailed than a thin treasury ask and includes staged deployment, audits, reporting, fund separation, pause rules, and some externally checkable market references, but the requested amount is large and several decisive benefits depend on unverified adoption, treasury-return, and administrator-execution assumptions. Under the doctrine, public-benefit ecosystem growth does not outweigh treasury stewardship when upside and demand translation are only partially evidenced, so a small cautionary negative nudge is justified.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that profits, yield, and returns generated by the launch liquidity position will be returned to the Cardano Treasury quarterly, converted into ada through Cardano-native DEXs with methodology disclosed in monthly reports.
- Claims and evidence missing: Independent evidence for: The proposal asserts that Cardano currently lacks a serious production BTCfi infrastructure layer and that failure to fund Alchemy would leave Bitcoin-backed structured exposure consolidating on other chains and off-chain markets.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `af0ad6991328d6adf601f620236995b613fdbc419d34bacfbdfa1d2c8477bcc1`
- snapshot_bundle_hash: `bbba92f3e67183416f6eced43b7568bf21fb232a63a2c413cc74bbf2f73b6083`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.181, "NO": 0.778, "YES": 0.0409}`

