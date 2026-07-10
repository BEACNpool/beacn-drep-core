# Rationale: gov_action1pa6a6yd7pdaxed9nqkshtvtu7jmqe5c8cpf0ej4lnatjj588qkpsq2x2sz2
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7758` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is detailed and includes meaningful treasury protections, staged funding, reporting, risk acknowledgments, and return mechanisms, but a large treasury request depends on several high-materiality claims that remain proposer-asserted within the extracted record, especially Cardano's BTCfi gap, Charms readiness, adoption potential, and the adequacy of the technical controls. A small cautionary negative nudge is justified because the doctrine prioritizes treasury stewardship and evidence quality over plausible ecosystem growth.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and the directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for 10,000,000 ada to fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms. It describes a roughly $2.0 million planning budget, split between protocol infrastructure and staged launch liquidity on one side, and delivery, audits, integrations, dashboards, governance reporting, legal/compliance work, and go-to-market execution on the other. It also proposes three monthly liquidity tranches, monthly reporting, public dashboards, security review, economic modeling, administrator oversight, and mechanisms for returning profits, yield, and returns to the Cardano Treasury.

Several core claims were supported in the proposal itself: the requested amount, the budget split, the shared BTC reserve design for FIRE and ICE, staged liquidity deployment, treasury return mechanics, risk acknowledgments, and proposed administrator controls. But several high-materiality claims remained unsupported by independent replayable evidence in the extracted record, including the claim that Cardano lacks credible production BTCfi infrastructure, that this market will consolidate elsewhere without action, and that Charms is ready to provide the Bitcoin-native logic and compatibility needed for Cardano wallets, DEXs, and DeFi tooling.

This is a conservative, evidence-based hold, not a rejection of the idea. The review gates confirmed that the proposal anchor was pinned and replayable, and the strongest YES case did clear evidence gates around the 10,000,000 ada request and planning budget. But treasury actions require elevated scrutiny, the claims-and-evidence record was thin, execution risk was unknown, and the review still lacked items such as independent assurance, a dependency map, cost-benefit clarity, and a sustainability path. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger independent evidence for the material adoption and technical-readiness claims.

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
- finding: Deliverables: Shared BTC reserve architecture with safety mechanisms and target reserve ratio., Composable Cardano-native FIRE and ICE assets backed by a shared BTC reserve., Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols., Always-on public dashboards showing reserve ratio, asset supply, liquidity health, fee flows, and deployment status., Monthly governance reports and reporting standards for future BTCfi projects., Staged treasury-supported launch liquidity separated from operating spend., Independent security review, audit, economic modeling, legal/compliance work, documentation, and go-to-market execution.
- finding: Deadline/expiry: Three-month staged liquidity deployment after enactment with monthly reporting; full delivery deadline not stated in document.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference rate for an approximately USD 2.0 million planning budget.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is split into two approximately USD 1.0 million pools: one for protocol infrastructure and staged launch liquidity and one for delivery, audit, integrations, dashboards, governance reporting, legal/compliance, and go-to-market execution.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will create a shared BTC reserve architecture where FIRE and ICE are backed by the same BTC reserve and governed by reserve-ratio formulas and safety zones.
- finding: Claim (governance, supported_in_proposal, high materiality): Pool 1 launch liquidity will be deployed in three monthly tranches of approximately USD 250,000, USD 250,000, and USD 500,000 after specified readiness, reporting, and performance checks.
- finding: Claim (economic, supported_in_proposal, high materiality): All profits, yield, and returns generated by the launch liquidity position will be returned to the Cardano Treasury quarterly, while principal may be returned after a 30-day time-weighted average TVL of at least USD 60 million and a later governance approval.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal asserts that Cardano currently lacks a credible production BTCfi infrastructure layer and risks Bitcoin-backed structured exposure consolidating on other chains and off-chain markets.
- missing: Independent evidence for: The proposal asserts that Cardano currently lacks a credible production BTCfi infrastructure layer and risks Bitcoin-backed structured exposure consolidating on other chains and off-chain markets.
- missing: Independent evidence for: The proposal states that Charms provides Bitcoin-native logic and compatibility infrastructure allowing FIRE and ICE to circulate into Cardano wallets, DEXs, and DeFi tooling.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference rate for an approximately USD 2.0 million planning budget." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal asserts that Cardano currently lacks a credible production BTCfi infrastructure layer and risks Bitcoin-backed structured exposure consolidating on other chains and off-chain markets." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference rate for an approximately USD 2.0 million planning budget." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: The proposal is detailed and includes meaningful treasury protections, staged funding, reporting, risk acknowledgments, and return mechanisms, but a large treasury request depends on several high-materiality claims that remain proposer-asserted within the extracted record, especially Cardano's BTCfi gap, Charms readiness, adoption potential, and the adequacy of the technical controls. A small cautionary negative nudge is justified because the doctrine prioritizes treasury stewardship and evidence quality over plausible ecosystem growth.
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
- Claims and evidence missing: Independent evidence for: The proposal asserts that Cardano currently lacks a credible production BTCfi infrastructure layer and risks Bitcoin-backed structured exposure consolidating on other chains and off-chain markets.
- Claims and evidence missing: Independent evidence for: The proposal states that Charms provides Bitcoin-native logic and compatibility infrastructure allowing FIRE and ICE to circulate into Cardano wallets, DEXs, and DeFi tooling.
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
- snapshot_bundle_hash: `0c7200f76999a825b65a9078150391a946f93ed0d7b2fe748714b03ae7844cb3`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

