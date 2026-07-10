# Rationale: 0f75dd11be0b7a6cb4b305a175b17cf4b60cd307c052fccabf9f572950e70583#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline evidence for a treasury withdrawal: the `treasury_amount_lovelace` field was missing. Even though the proposal text says it requests 10,000,000 ada, BEACN requires the on-chain treasury amount field and source anchors to be complete before making a directional treasury vote.

The action requested funding for Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms. The proposal described FIRE and ICE assets backed by a shared BTC reserve, reserve-ratio rules, dashboards, SDKs and adapters, audits, legal and compliance work, governance reporting, staged launch liquidity, and go-to-market execution. It also claimed the budget would be split into two roughly USD 1 million pools, with one for protocol infrastructure and launch liquidity and the other for delivery, audits, integrations, reporting, compliance, and launch work.

Several claims were supported inside the proposal, including the requested 10,000,000 ada budget, the two-pool structure, the 5.0x target initial reserve ratio with safety zones, the descriptions of FIRE and ICE, and proposed treasury protections such as no DRep funds or personal compensation to principals, ADA price protection, pause rules, and refund or return conditions. But some important claims were still not independently evidenced, including the claim that Cardano lacks a serious production BTCfi infrastructure layer and the claim that Charms provides the Bitcoin/Cardano compatibility foundation needed for issuance and circulation into Cardano wallets, DEXs, and DeFi tooling.

This ABSTAIN is a conservative, evidence-based hold. A directional vote would require the missing treasury withdrawal amount field to be present, plus stronger evidence on the sustainability path, cost-benefit clarity, independent assurance, dependency map, and the unsupported technical and adoption claims. For a treasury action that consumes shared ADA and sets precedent, BEACN did not treat proposer assertions alone as enough to support or oppose the request.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Build and launch Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer with reserve architecture, FIRE/ICE assets, dashboards, adapters, reporting, audits, administration, legal/compliance work, go-to-market execution, and staged launch liquidity.
- finding: Recipient: Sundial Protocol and Charms, with Intersect proposed as interim fund administrator subject to confirmation and final agreement
- finding: Stated amount: 10,000,000 ada
- finding: Deliverables: Shared BTC reserve architecture with transparent safety mechanisms and reserve-ratio rules, Composable Cardano-native FIRE and ICE assets backed by a shared BTC reserve, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on dashboards for reserve ratio, asset supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards for future BTCfi projects, Independent security review, audit, and economic modeling, Staged treasury-supported launch liquidity deployed over three months, Legal, compliance, disclosures, treasury reporting, and launch-readiness review, Ecosystem education, DRep communications, partner activation, and launch coordination
- finding: Deadline/expiry: staged deployment after enactment, with three-month liquidity deployment and monthly reporting
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million split into two approximately USD 1.0 million pools.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 is intended for protocol infrastructure and staged launch liquidity, kept separate from operating expenses, deployed over three months, and designed to return profits, yield, and returns to the Cardano Treasury quarterly.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 2 is intended to fund delivery, audits, integrations, dashboards, governance reporting, legal/compliance work, and go-to-market execution with itemized planning allocations.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will use a shared BTC reserve architecture for FIRE and ICE with a target initial reserve ratio of 5.0x and safety zones above 4.0x, between 2.0x and 4.0x, and below 2.0x.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a residual high-volatility BTC exposure asset, while ICE is described as a lower-volatility USD-denominated BTC-backed exposure asset, both intended as composable Cardano-native primitives.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer asserts that Cardano currently lacks a serious production BTCfi infrastructure layer and risks Bitcoin-backed structured exposure consolidating on other chains and off-chain markets.
- missing: Independent evidence for: The proposer asserts that Cardano currently lacks a serious production BTCfi infrastructure layer and risks Bitcoin-backed structured exposure consolidating on other chains and off-chain markets.
- missing: Independent evidence for: The proposal says Charms provides the Bitcoin meta-protocol and Bitcoin/Cardano compatibility foundation needed for FIRE and ICE issuance and circulation into Cardano wallets, DEXs, and DeFi tooling.
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
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million split into two approximately USD 1.0 million pools." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposer asserts that Cardano currently lacks a serious production BTCfi infrastructure layer and risks Bitcoin-backed structured exposure consolidating on other chains and off-chain markets." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: evidence is too thin for a directional vote while 1 blocker(s) remain open.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: high
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million split into two approximately USD 1.0 million pools." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: The proposer asserts that Cardano currently lacks a serious production BTCfi infrastructure layer and risks Bitcoin-backed structured exposure consolidating on other chains and off-chain markets.
- Claims and evidence missing: Independent evidence for: The proposal says Charms provides the Bitcoin meta-protocol and Bitcoin/Cardano compatibility foundation needed for FIRE and ICE issuance and circulation into Cardano wallets, DEXs, and DeFi tooling.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `8fb0dc108fdcc9aa8e0ad1ca954572902326c4adbe1cb9600e146f4ca535e0ff`
- snapshot_bundle_hash: `f29e3913bd1b56f0d3e33adfb5fc77c87dacf970b6887f145f55f5a03887805e`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

