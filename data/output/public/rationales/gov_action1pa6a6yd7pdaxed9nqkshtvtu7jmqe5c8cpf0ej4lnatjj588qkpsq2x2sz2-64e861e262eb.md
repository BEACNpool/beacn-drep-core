# Rationale: gov_action1pa6a6yd7pdaxed9nqkshtvtu7jmqe5c8cpf0ej4lnatjj588qkpsq2x2sz2
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7758` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a relatively detailed proposal with explicit budget pools, staged liquidity deployment, risk acknowledgements, reporting commitments, and treasury-return mechanics, but the deterministic assessment already marked claims, treasury analysis, and risk review complete. Under the doctrine, these details are primarily execution-eligibility and treasury-stewardship factors already suited to the mechanical gates, so no additional advisory nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury request cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the project.

The proposal asks for 10,000,000 ada to fund Alchemy by Sundial x Charms, a Cardano-native Bitcoin treasury protocol with FIRE and ICE assets, shared BTC reserve architecture, dashboards, adapters, audits, reporting, legal/compliance work, go-to-market execution, and staged launch liquidity. The proposer describes Intersect as the interim fund administrator, subject to confirmation and final agreement, with Sundial accountable for delivery and Charms as technical partner.

Several claims were well-supported inside the proposal: the 10,000,000 ada request, the roughly USD 2 million planning budget split into two pools, the three-month staged liquidity plan, the FIRE and ICE reserve design, the 5.0x target reserve ratio with safety zones, quarterly return of profits/yield/returns to the Treasury, and several treasury protection mechanisms. But one material adoption claim remains unsupported by independent evidence: that Cardano lacks a credible production BTCfi infrastructure layer and risks losing Bitcoin-backed structured exposure markets to other ecosystems. The review also found thin claims-and-evidence status, missing sustainability and cost-benefit clarity, missing independent assurance, and a missing dependency map.

Because this is a TreasuryWithdrawal action, BEACN applies elevated scrutiny. The proposal has a pinned and replayable anchor document, and the strongest YES case clears some evidence gates. However, treasury votes consume shared ada and set precedent, so BEACN needs the public-chain Net Change Limit evidence, plus stronger independent support for the unsupported adoption claim and clearer treasury/risk analysis, before voting YES or NO.

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
- finding: Requested: Fund Alchemy by Sundial x Charms, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer with reserve architecture, FIRE and ICE assets, dashboards, adapters, reporting, audits, legal/compliance work, go-to-market execution, and staged launch liquidity.
- finding: Recipient: Intersect is proposed as interim fund administrator, subject to confirmation and final agreement; Sundial remains accountable for deployment and delivery with Charms as technical partner.
- finding: Stated amount: 10000000
- finding: Deliverables: Shared BTC reserve architecture with transparent safety mechanisms and reserve-ratio controls, Composable Cardano-native FIRE and ICE assets, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on dashboards for reserve ratio, supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Independent security review, audit, and economic modeling, Staged treasury-supported launch liquidity with profits, yield, and returns returned quarterly to the Cardano Treasury
- finding: Deadline/expiry: Three-month liquidity deployment after enactment with monthly reporting; Month 1, Month 2, and Month 3 tranche conditions are described, but total delivery deadline is not stated in document.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximately USD 0.20 ADA reference rate for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 is intended for protocol infrastructure and staged launch liquidity, deployed over three months in approximately USD 250,000, USD 250,000, and USD 500,000 tranches subject to audit, reporting, operational, liquidity, reserve-ratio, and dashboard conditions.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 2 is intended for delivery, audit, integrations, dashboards, legal/compliance, reporting, go-to-market, administration, and accounting, with itemized planning allocations totaling approximately USD 1.0 million.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will create a shared BTC reserve architecture where FIRE and ICE are backed by the same BTC reserve, with an initial target reserve ratio of 5.0x and behavior constrained by safety zones above 4.0x, between 2.0x and 4.0x, and below 2.0x.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual BTC exposure asset, while ICE is described as a lower-volatility USD-denominated BTC-backed exposure asset, both intended to circulate as composable Cardano-native primitives.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal asserts that Cardano currently lacks a credible production BTCfi infrastructure layer and risks losing Bitcoin-backed structured exposure markets to Ethereum, BNB, Solana, and Bitcoin-adjacent ecosystems.
- missing: Independent evidence for: The proposal asserts that Cardano currently lacks a credible production BTCfi infrastructure layer and risks losing Bitcoin-backed structured exposure markets to Ethereum, BNB, Solana, and Bitcoin-adjacent ecosystems.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximately USD 0.20 ADA reference rate for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal asserts that Cardano currently lacks a credible production BTCfi infrastructure layer and risks losing Bitcoin-backed structured exposure markets to Ethereum, BNB, Solana, and Bitcoin-adjacent ecosystems." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximately USD 0.20 ADA reference rate for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
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
- Claims and evidence missing: Independent evidence for: The proposal asserts that Cardano currently lacks a credible production BTCfi infrastructure layer and risks losing Bitcoin-backed structured exposure markets to Ethereum, BNB, Solana, and Bitcoin-adjacent ecosystems.
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
- snapshot_bundle_hash: `315d76a69ddc8f9976da99057ec2dcd029915409822517770f8878a072cec9b4`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

