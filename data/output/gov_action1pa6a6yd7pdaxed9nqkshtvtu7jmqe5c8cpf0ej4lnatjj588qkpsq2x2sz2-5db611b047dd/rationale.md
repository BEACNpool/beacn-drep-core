# Rationale: gov_action1pa6a6yd7pdaxed9nqkshtvtu7jmqe5c8cpf0ej4lnatjj588qkpsq2x2sz2
Recommendation: **NO**
Score: `-0.4033` (raw `-0.3833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal provides unusually detailed budgeting, controls, staged liquidity mechanics, and risk disclosures, but the ask is large and several core value claims depend on adoption, external market analogies, administrator confirmation, and future governance actions rather than completed or reproducible evidence in the document. Under the doctrine's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive spending nudge.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large Treasury request, and a key value claim was not independently supported: that Cardano lacks a production BTCfi infrastructure layer and that Alchemy would provide broadly reusable infrastructure for wallets, DEXs, DeFi protocols, and future BTCfi projects.

The proposal requested 10,000,000 ada for Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms. It described a shared BTC reserve model with FIRE and ICE assets, staged treasury-supported launch liquidity, open-source SDKs and adapters, public dashboards, monthly governance reports, independent security review, audit and economic modeling, legal and compliance work, and ecosystem launch coordination. The proposal also said the ada request used an approximate USD 0.20 reference value, for a planning budget of about USD 2 million split into two roughly USD 1 million pools.

Several claims were well-supported inside the proposal: the budget structure, the treasury-owned launch liquidity design, quarterly return of profits or yield to the Treasury, the 5.0x target initial reserve ratio, safety zones, dashboards, monthly reporting, milestone gating, pause rules, refund conditions, ADA price protection, and administrator oversight. The review also found a pinned, replayable anchor document and recognized a strong YES case that the funding amount and budget framing were substantiated.

The NO came from the higher evidence bar for Treasury withdrawals. This action would spend shared ada and create precedent, so proposer assertions were not enough for core adoption and ecosystem-value claims. The review found thin claims-and-evidence status, missing cost-benefit clarity, no sustainability path in the Treasury analysis, missing independent assurance, and no dependency map. Intersect’s role as interim administrator was also still subject to confirmation and final agreement, and the return of launch liquidity depended on a later governance proposal. Taken together, BEACN judged that the proposal had meaningful detail and controls, but not enough independent evidence to justify a 10,000,000 ada Treasury withdrawal.

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
- finding: Deliverables: Shared BTC reserve architecture with FIRE and ICE assets, Staged treasury-supported launch liquidity, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on public dashboards for reserve ratio, supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Independent security review, audit, and economic modeling, Legal, compliance, disclosures, treasury reporting, and launch-readiness review, Ecosystem education, DRep communications, partner activation, and launch coordination
- finding: Deadline/expiry: Three-month staged launch liquidity deployment after enactment, with monthly reporting; exact full delivery deadline not stated in document.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is split into two separated pools of approximately USD 1.0 million each, one for protocol infrastructure and staged launch liquidity and one for delivery, audit, integrations, dashboards, governance reporting, legal/compliance work, and go-to-market execution.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 launch liquidity is described as treasury-supported and treasury-owned, with profits, yield, and returns returned to the Cardano Treasury quarterly after conversion into ada through Cardano-native DEXs.
- finding: Claim (governance, supported_in_proposal, high materiality): The launch liquidity principal may be returned to the Treasury after Alchemy reaches a 30-day time-weighted average TVL of at least USD 60 million, subject to a later formal governance proposal and approval.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will use a shared BTC reserve architecture where FIRE and ICE are backed by the same BTC reserve, with a target initial reserve ratio of 5.0x and safety zones that constrain minting and redemption below specified reserve-ratio thresholds.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is proposed as a volatility-absorbing residual BTC exposure asset, while ICE is proposed as a USD-denominated BTC-backed lower-volatility asset with growth potential.
- missing: Independent evidence for: The proposal states that Cardano currently lacks a production BTCfi infrastructure layer and that Alchemy would provide reusable infrastructure for wallets, DEXs, DeFi protocols, and future BTCfi projects.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Cardano currently lacks a production BTCfi infrastructure layer and that Alchemy would provide reusable infrastructure for wallets, DEXs, DeFi protocols, and future BTCfi projects." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal provides unusually detailed budgeting, controls, staged liquidity mechanics, and risk disclosures, but the ask is large and several core value claims depend on adoption, external market analogies, administrator confirmation, and future governance actions rather than completed or reproducible evidence in the document. Under the doctrine's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive spending nudge.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that Cardano currently lacks a production BTCfi infrastructure layer and that Alchemy would provide reusable infrastructure for wallets, DEXs, DeFi protocols, and future BTCfi projects.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `5db611b047dd859e56f51a017114228dd6dcf8d7cb53b829e6f3369f58c0cff0`
- snapshot_bundle_hash: `03fb434d39a286afb09ed38a5734ce77fd7e415ab65e253acf14d41374abfd99`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1825, "NO": 0.7762, "YES": 0.0413}`

