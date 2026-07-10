# Rationale: gov_action1pa6a6yd7pdaxed9nqkshtvtu7jmqe5c8cpf0ej4lnatjj588qkpsq2x2sz2
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7758` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal gives more detail than a thin treasury ask, including separated pools, staged liquidity, risk mitigations, audit allocation, reporting, pause rules, and return conditions. However, the requested amount is large, key adoption and market-need claims rely partly on proposer framing or external references rather than evidence contained in the document, and the technical/economic design remains novel with material reserve, oracle, bridge, and protocol-layer risks. A small cautionary negative nudge is justified beyond the mechanical assessment because treasury stewardship and evidence quality should dominate plausible ecosystem-growth upside.

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Alchemy by Sundial x Charms: Cardano-Native Bitcoin Treasury Protocol. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer with reserve architecture, FIRE and ICE assets, dashboards, adapters, reporting, audits, legal/compliance work, go-to-market execution, and staged launch liquidity. It asks the treasury for 10000000 ADA. The strongest grounded claim is: The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools.

A material claim remains proposer-asserted or thinly supported: The proposer states that Cardano currently lacks a serious production BTCfi infrastructure layer and that without Alchemy, Bitcoin-backed structured exposure will continue consolidating on other chains and off-chain markets. Reason code: VERIFIED_NCL_REQUIRED.

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
- finding: Requested: Fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer with reserve architecture, FIRE and ICE assets, dashboards, adapters, reporting, audits, legal/compliance work, go-to-market execution, and staged launch liquidity.
- finding: Recipient: Sundial Protocol and Charms, with Intersect proposed as interim fund administrator subject to confirmation and final agreement
- finding: Stated amount: 10000000
- finding: Deliverables: Shared BTC reserve architecture with reserve-ratio safety mechanisms, Composable Cardano-native FIRE and ICE assets, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on public dashboards for reserve ratio, asset supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Independent security review, audit, and economic modeling, Staged treasury-supported launch liquidity, Legal/compliance work, disclosures, risk documentation, and go-to-market execution
- finding: Deadline/expiry: Three-month staged liquidity deployment after enactment with monthly reporting; full delivery deadline not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 will support protocol infrastructure and staged launch liquidity, remain separate from operating spend, deploy in three monthly tranches, and return launch-liquidity profits, yield, and returns to the Cardano Treasury quarterly.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 2 will fund delivery, audits, integrations, dashboards, legal/compliance work, reporting, administration, and go-to-market execution through itemized planning allocations totaling approximately USD 1.0 million.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will use a shared BTC reserve for FIRE and ICE, targeting an initial 5.0x reserve ratio with safety zones above 4.0x, between 2.0x and 4.0x, and below 2.0x to constrain minting, redemption, and risky activity under stress.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual BTC-backed claim, while ICE is described as a lower-volatility USD-denominated BTC-backed asset, both intended to be composable Cardano-native primitives.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that Cardano currently lacks a serious production BTCfi infrastructure layer and that without Alchemy, Bitcoin-backed structured exposure will continue consolidating on other chains and off-chain markets.
- missing: Independent evidence for: The proposer states that Cardano currently lacks a serious production BTCfi infrastructure layer and that without Alchemy, Bitcoin-backed structured exposure will continue consolidating on other chains and off-chain markets.
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
- finding: Strongest NO: a material claim is unsupported — "The proposer states that Cardano currently lacks a serious production BTCfi infrastructure layer and that without Alchemy, Bitcoin-backed structured exposure will continue consolidating on other chains and off-chain markets." — so cost or precedent may outweigh the benefit.
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
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal gives more detail than a thin treasury ask, including separated pools, staged liquidity, risk mitigations, audit allocation, reporting, pause rules, and return conditions. However, the requested amount is large, key adoption and market-need claims rely partly on proposer framing or external references rather than evidence contained in the document, and the technical/economic design remains novel with material reserve, oracle, bridge, and protocol-layer risks. A small cautionary negative nudge is justified beyond the mechanical assessment because treasury stewardship and evidence quality should dominate plausible ecosystem-growth upside.
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
- Claims and evidence missing: Independent evidence for: The proposer states that Cardano currently lacks a serious production BTCfi infrastructure layer and that without Alchemy, Bitcoin-backed structured exposure will continue consolidating on other chains and off-chain markets.
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
- snapshot_bundle_hash: `7c80a2d587a5763d28cc3905b3ab9b9147e8d969b62a90acbebbead45ad0c8df`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

