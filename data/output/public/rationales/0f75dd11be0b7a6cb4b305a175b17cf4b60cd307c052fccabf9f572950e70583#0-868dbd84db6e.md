# Rationale: 0f75dd11be0b7a6cb4b305a175b17cf4b60cd307c052fccabf9f572950e70583#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.21` (raw `-0.21` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7725` | Readiness: `0.85`
> Reasoning layer (precomputed): The document provides unusually detailed budget structure, tranche logic, safety mechanisms, reporting commitments, and treasury-return provisions, but the largest value claims still depend on future adoption, external administrator confirmation, security review, and market validation that the extraction record cannot verify beyond the proposal text. The deterministic assessment already marked claims, treasury analysis, and risk review complete, so no additional bounded nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for 10,000,000 ada to fund Alchemy, a Cardano-native Bitcoin treasury protocol and BTCfi infrastructure layer by Sundial Protocol and Charms. It describes two roughly USD 1 million budget pools: one for protocol infrastructure and staged launch liquidity over three months, and one for delivery work including audits, integrations, dashboards, legal and compliance work, reporting, go-to-market, administration, and related costs. It also describes FIRE and ICE assets backed by a shared BTC reserve, with a target initial reserve ratio of 5.0x and safety zones intended to limit risky activity as reserve conditions weaken.

Several core budget and design claims were supported in the proposal, including the requested amount, the two-pool budget structure, the staged liquidity plan, the FIRE and ICE reserve architecture, and the plan to return treasury-supported launch liquidity profits or yield to the Cardano Treasury quarterly. However, some important governance claims were still only proposer assertions, including the claim that there are no DRep funds or personal compensation to Sundial or Charms principals, and the claim that Intersect would serve as interim fund administrator with accounting, custody, reporting, and delegation controls. The review also found thin claims-and-evidence status, missing sustainability-path and cost-benefit clarity, missing independent assurance, and an incomplete dependency map. Execution risk was rated high.

This is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would require the applicable Net Change Limit to be pinned and independently verified from public chain evidence, along with stronger independent evidence for the unresolved governance and treasury-control claims, clearer sustainability and cost-benefit analysis, independent assurance, and a fuller dependency map.

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
- finding: Recipient: Intersect is proposed as interim fund administrator, subject to confirmation and final agreement; Sundial remains accountable for deployment and delivery coordination with Charms.
- finding: Stated amount: 10,000,000 ada
- finding: Deliverables: Shared BTC reserve architecture with FIRE and ICE assets, Staged treasury-supported launch liquidity, Open-source SDKs and adapters for wallets, DEXs, and DeFi protocols, Always-on public dashboards for reserve ratio, supply, liquidity health, fee flows, and deployment status, Monthly governance reports and reporting standards, Independent security review, audit, and economic modeling, Legal/compliance work, disclosures, risk documentation, and launch-readiness review, Ecosystem education, DRep communications, partner activation, and launch coordination
- finding: Deadline/expiry: Staged deployment after enactment, with three-month liquidity deployment and monthly reporting; specific full delivery deadline not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million split into two approximately USD 1.0 million pools.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 1 will support protocol infrastructure and staged launch liquidity, kept separate from operating expenses and deployed over three months in approximate tranches of USD 250,000, USD 250,000, and USD 500,000.
- finding: Claim (economic, supported_in_proposal, high materiality): Pool 2 will fund delivery, audits, integrations, dashboards, legal/compliance, reporting, go-to-market, administration, and related work according to itemized planning allocations totaling approximately USD 1.0 million.
- finding: Claim (technical, supported_in_proposal, high materiality): Alchemy will use a shared BTC reserve architecture with FIRE and ICE backed by the same BTC reserve, a target initial reserve ratio of 5.0x, and safety zones that constrain minting, redemption, and risky activity as reserve conditions weaken.
- finding: Claim (technical, supported_in_proposal, high materiality): FIRE is described as a volatility-absorbing residual BTC exposure asset, while ICE is described as a lower-volatility USD-denominated BTC-backed exposure asset intended to be composable across Cardano wallets, DEXs, dashboards, and DeFi protocols.
- finding: Claim (economic, supported_in_proposal, high materiality): Profits, yield, and returns generated by the treasury-supported launch liquidity position will be returned to the Cardano Treasury quarterly, while principal may be returned only after Alchemy reaches a 30-day time-weighted average TVL of at least USD 60 million and a later governance proposal approves the return action.
- missing: Independent evidence for: The proposal states that there are no DRep funds or personal compensation to Sundial or Charms principals, and that if external investment funds Alchemy development, the development portion of the request will roll into additional treasury-supported launch liquidity.
- missing: Independent evidence for: The proposal says Intersect would serve as interim fund administrator if confirmed, supporting accounting, fund separation, milestone verification, reporting, and custody controls, with administrator-held ada kept in auditable accounts delegated to auto-abstain.
- missing: Independent evidence for: The proposal claims Cardano currently lacks a production BTCfi infrastructure layer and risks Bitcoin-backed structured exposure consolidating on Ethereum, BNB, Solana, and off-chain markets if Alchemy is not funded.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million split into two approximately USD 1.0 million pools." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that there are no DRep funds or personal compensation to Sundial or Charms principals, and that if external investment funds Alchemy development, the development portion of the request will roll into additional treasury-supported launch liquidity." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 10,000,000 ada, using an approximate USD 0.20 per ada reference value for a planning budget of about USD 2.0 million split into two approximately USD 1.0 million pools." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: The proposal states that there are no DRep funds or personal compensation to Sundial or Charms principals, and that if external investment funds Alchemy development, the development portion of the request will roll into additional treasury-supported launch liquidity.
- Claims and evidence missing: Independent evidence for: The proposal says Intersect would serve as interim fund administrator if confirmed, supporting accounting, fund separation, milestone verification, reporting, and custody controls, with administrator-held ada kept in auditable accounts delegated to auto-abstain.
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
- input_hash: `868dbd84db6ea72c920d2f5bcf031a99889243815f4fabe5102ee535059fbb9b`
- snapshot_bundle_hash: `7322296c0f259ba8d5d9b110b871761b0cc24aee9a4d493d60a75a00e0bc31c4`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.446, "YES": 0.0492}`

