# Rationale: 0f75dd11be0b7a6cb4b305a175b17cf4b60cd307c052fccabf9f572950e70583#0
Recommendation: **NO**
Score: `-0.12` (raw `-0.66` + doctrine-LLM nudge `-0.02`) | Confidence: `0.72` | Readiness: `0.85`
> Reasoning layer (precomputed): A small cautionary nudge is justified because the request is large, the proposal depends on novel BTCfi mechanics and administrator confirmation, and some high-materiality adoption and market-timing claims are asserted or only externally checkable even though the document provides meaningful controls and budget detail.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Alchemy by Sundial x Charms: Cardano-Native Bitcoin Treasury Protocol. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms, including reserve architecture, FIRE and ICE assets, dashboards, adapters, reporting, audits, administration, legal/compliance work, go-to-market execution, and staged launch liquidity. It asks the treasury for 10000000 ADA. The strongest grounded claim is: The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools.

A material claim remains proposer-asserted or thinly supported: The proposal asserts that Cardano currently lacks serious production BTCfi infrastructure and that without Alchemy, Bitcoin-backed structured exposure will continue consolidating on other chains and off-chain capital markets.

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
- finding: Requested: Fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms, including reserve architecture, FIRE and ICE assets, dashboards, adapters, reporting, audits, administration, legal/compliance work, go-to-market execution, and staged launch liquidity.
- finding: Recipient: Sundial Protocol and Charms, with Intersect proposed as interim fund administrator subject to confirmation and final agreement.
- finding: Stated amount: 10000000
- finding: Deliverables: Shared BTC reserve architecture with reserve-ratio mechanics and safety zones, Composable Cardano-native FIRE and ICE assets, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on public dashboards for reserve ratio, asset supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Independent security review, audit, and economic modeling, Three-month staged launch liquidity deployment, Legal/compliance disclosures, treasury reporting, risk documentation, and launch-readiness review
- finding: Deadline/expiry: Three-month liquidity deployment after enactment with monthly reporting; administrator confirmation expected within 30 days of enactment.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 is intended for protocol infrastructure and staged launch liquidity, kept separate from operating expenses, deployed over three months, and structured so profits, yield, and returns from the launch liquidity position are returned to the Cardano Treasury quarterly.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 2 is intended for delivery, audits, integrations, dashboards, governance reporting, legal/compliance work, and go-to-market execution with itemized planning allocations totaling approximately USD 1.0 million.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy proposes a shared BTC reserve architecture where FIRE and ICE are backed by the same BTC reserve, with reserve ratio formula (V x P) / L, FIRE price formula ((V x P) - L) / N+, an initial 5.0x reserve-ratio target, and safety zones above 4.0x, between 2.0x and 4.0x, and below 2.0x.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual claim on the BTC reserve after ICE commitments, while ICE is described as a USD-denominated BTC-backed asset designed for lower-volatility exposure with growth potential.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal asserts that Cardano currently lacks serious production BTCfi infrastructure and that without Alchemy, Bitcoin-backed structured exposure will continue consolidating on other chains and off-chain capital markets.
- missing: Independent evidence for: The proposal asserts that Cardano currently lacks serious production BTCfi infrastructure and that without Alchemy, Bitcoin-backed structured exposure will continue consolidating on other chains and off-chain capital markets.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal asserts that Cardano currently lacks serious production BTCfi infrastructure and that without Alchemy, Bitcoin-backed structured exposure will continue consolidating on other chains and off-chain capital markets." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for an approximately USD 2.0 million planning budget split into two approximately USD 1.0 million pools." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: A small cautionary nudge is justified because the request is large, the proposal depends on novel BTCfi mechanics and administrator confirmation, and some high-materiality adoption and market-timing claims are asserted or only externally checkable even though the document provides meaningful controls and budget detail.
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
- Claims and evidence missing: Independent evidence for: The proposal asserts that Cardano currently lacks serious production BTCfi infrastructure and that without Alchemy, Bitcoin-backed structured exposure will continue consolidating on other chains and off-chain capital markets.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `8ccc05cc434a9861c02398de88e85b00cb97661b7aaf4517c547f8a1fa37e46d`
- snapshot_bundle_hash: `ba950e3f1ff7b2fe26483f58a9943a485890408626ac66ec936521985dc53c6c`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.23, "NO": 0.64, "YES": 0.13}`

