# Rationale: 0f75dd11be0b7a6cb4b305a175b17cf4b60cd307c052fccabf9f572950e70583#0
Recommendation: **NO**
Score: `-0.12` (binding treasury composite; advisory raw signal `-0.66`; LLM lean `+0.0` recorded, not added) | Confidence: `0.72` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a detailed treasury structure with milestones, fund separation, audit allocation, reporting, and return concepts, but several central adoption and technical-delivery claims remain proposer assertions within the document. The deterministic assessment is already ready, so the evidence-quality and stewardship considerations do not justify an additional directional nudge beyond the mechanical score.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Alchemy by Sundial x Charms: Cardano-Native Bitcoin Treasury Protocol. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms. It asks the treasury for 10000000 ADA. The strongest grounded claim is: The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget.

A material claim remains proposer-asserted or thinly supported: Launch liquidity will be treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly through disclosed conversion and reporting processes.

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
- finding: Recipient: Sundial Protocol and Charms, with Intersect proposed as interim fund administrator subject to confirmation and final agreement.
- finding: Stated amount: 10000000
- finding: Deliverables: Shared BTC reserve architecture with transparent safety mechanisms and reserve-ratio rules, Composable Cardano-native FIRE and ICE assets, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Public dashboards showing reserve ratio, asset supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Independent security review, audit, and economic modeling, Staged treasury-supported launch liquidity, Legal, compliance, disclosures, treasury reporting, and risk documentation, Go-to-market execution, ecosystem education, DRep communications, partner activation, and launch coordination
- finding: Deadline/expiry: Three-month staged liquidity deployment after enactment, with monthly reporting; administrator confirmation expected within 30 days of enactment.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is split into approximately USD 1.0 million for protocol infrastructure and staged launch liquidity and approximately USD 1.0 million for delivery, audit, integrations, dashboards, governance reporting, legal/compliance work, and go-to-market execution.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will create a shared BTC reserve architecture where FIRE and ICE are backed by the same BTC reserve, with reserve-ratio formulas and safety zones governing minting, redemption, and pauses.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual BTC-backed claim, while ICE is described as lower-volatility USD-denominated BTC-backed exposure intended for wallet, DEX, dashboard, and DeFi integration.
- finding: Claim (economic, proposer_asserted, high materiality): Launch liquidity will be treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly through disclosed conversion and reporting processes.
- finding: Claim (governance, supported_in_proposal, medium materiality): The launch-liquidity principal may be returned after Alchemy reaches a 30-day time-weighted average TVL of at least USD 60 million, subject to a later formal governance proposal for DRep and Constitutional Committee review.
- missing: Independent evidence for: Launch liquidity will be treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly through disclosed conversion and reporting processes.
- missing: Independent evidence for: The proposal states that Charms provides Bitcoin/Cardano compatibility infrastructure and the technical foundation for issuing Bitcoin-native assets that can circulate as Cardano-native assets.
- missing: Independent evidence for: The proposal asserts that Cardano lacks a serious production BTCfi infrastructure layer and that failure to fund Alchemy would leave Bitcoin-backed structured exposure to consolidate on other chains and off-chain capital markets.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: high
- finding: Governance risk: medium
- finding: Technical risk: high
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Launch liquidity will be treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly through disclosed conversion and reporting processes." — so cost or precedent may outweigh the benefit.
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
- Flag score present (3), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: high
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional NO is supported by affirmative independent evidence of waste, duplication, excessive cost, or failed delivery — not by missing information.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 50% of rolling available capacity.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Launch liquidity will be treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly through disclosed conversion and reporting processes.
- Claims and evidence missing: Independent evidence for: The proposal states that Charms provides Bitcoin/Cardano compatibility infrastructure and the technical foundation for issuing Bitcoin-native assets that can circulate as Cardano-native assets.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `78eaeefa6c6ed10d2e45d24aae78977495af6f3fd3bab0242202f8f22310be77`
- snapshot_bundle_hash: `286b31ad655a95fdc8baf6a539062fb7c96ffa9c6b303c9be59d12c3e033c7b1`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.23, "NO": 0.64, "YES": 0.13}`

