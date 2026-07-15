# Rationale: 0f75dd11be0b7a6cb4b305a175b17cf4b60cd307c052fccabf9f572950e70583#0
Recommendation: **NO**
Score: `-0.12` (binding treasury composite; advisory raw signal `-0.66`; LLM lean `+0.0` recorded, not added) | Confidence: `0.72` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show a detailed structure for fund separation, staged deployment, reporting, audits, pause rules, and return conditions, while the main market-need and adoption claims remain largely proposer asserted or externally checkable rather than established inside the document. Under the doctrine, those considerations are already core treasury-stewardship and evidence-quality inputs, so no additional nudge beyond the deterministic assessment is justified.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Alchemy by Sundial x Charms: Cardano-Native Bitcoin Treasury Protocol. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms. It asks the treasury for 10000000 ADA. The strongest grounded claim is: The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of approximately USD 2.0 million.

A material claim remains proposer-asserted or thinly supported: Pool 1 launch liquidity will be treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly.

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
- finding: Recipient: Sundial Protocol and Charms, with Intersect proposed as interim fund administrator subject to confirmation and final agreement
- finding: Stated amount: 10000000
- finding: Deliverables: Shared BTC reserve architecture with transparent safety mechanisms, Composable FIRE and ICE Cardano-native assets, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on public dashboards for reserve ratio, asset supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Staged treasury-supported launch liquidity, Independent security review, audit, and economic modeling, Legal, compliance, disclosures, treasury reporting, and launch-readiness review
- finding: Deadline/expiry: Three-month liquidity deployment after enactment with monthly reporting; other final delivery deadline not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of approximately USD 2.0 million.
- finding: Claim (economic, supported_in_proposal, high materiality): The request is split into two separated pools of approximately USD 1.0 million each, one for protocol infrastructure and staged launch liquidity and one for delivery, audit, integrations, dashboards, governance reporting, legal/compliance work, and go-to-market execution.
- finding: Claim (economic, proposer_asserted, high materiality): Pool 1 launch liquidity will be treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will use a shared BTC reserve backing FIRE and ICE, with a target initial reserve ratio of 5.0x and safety zones that constrain minting and redemption below stated reserve-ratio thresholds.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual BTC-backed claim, while ICE is described as a lower-volatility USD-denominated BTC-backed asset, both intended as composable Cardano-native primitives.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal commits to dashboards, monthly governance reports, audit allocation, milestone gating, pause rules, refund conditions, ADA price protection, and fund separation as accountability controls.
- missing: Independent evidence for: Pool 1 launch liquidity will be treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly.
- missing: Independent evidence for: The proposal states that Cardano currently lacks a production BTCfi infrastructure layer and that failure to fund Alchemy would leave Bitcoin-backed structured exposure to consolidate on other chains and off-chain markets.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of approximately USD 2.0 million." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Pool 1 launch liquidity will be treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of approximately USD 2.0 million." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: Pool 1 launch liquidity will be treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly.
- Claims and evidence missing: Independent evidence for: The proposal states that Cardano currently lacks a production BTCfi infrastructure layer and that failure to fund Alchemy would leave Bitcoin-backed structured exposure to consolidate on other chains and off-chain markets.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `649423f3a56892baeccc5fe4fea3db459ef14ca3838034803a74122b2689f883`
- snapshot_bundle_hash: `73079bc2b51dc8491884346d7b0d8a0a3b39d3cccb1fa583d9491598943b0504`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.23, "NO": 0.64, "YES": 0.13}`

