# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7808` | Readiness: `0.9`
> Reasoning layer (precomputed): The proposal has meaningful public-benefit upside and provides a relatively detailed budget, milestone structure, oversight framework, and repayment concept, but the largest value claims depend on asserted user base, contracted deployment, transaction volumes, and revenue projections that are not evidenced within the supplied document. Because the ask is large and the revenue-share details are partly deferred to M1 contracting, a small cautionary negative nudge is justified beyond the mechanical gates.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large Treasury withdrawal and a required Net Change Limit check has not yet been pinned and independently verified from public chain evidence. That blocks a directional YES or NO vote under BEACN’s evidence rules.

The proposal asks for 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency. It describes an eight-month, milestone-gated plan for a secondary marketplace, on-chain settlement, smart-contract royalties, anti-scalping controls, wallet onboarding, organizer tools, a third-party audit, launch activity, public metrics, and quarterly reporting. The proposer also describes a repayment plan using 25% of fees until $1,093,231 is reimbursed, then 5% afterward, with final revenue-base definitions deferred to M1 contracting.

Several parts were well-supported within the proposal itself: the amount requested, the timeline, the milestone structure, the planned deliverables, the budget line items, the Intersect/TRSC/PSSC administration framework, and the repayment concept. But several material adoption claims remain only proposer-asserted in the supplied review, including Phase 1 being live on mainnet, Sellout’s user and ticketing numbers, the Yellowstone Club anchor deployment, and the projected on-chain events, tickets, interactions, revenue, and wallet creation. The review also noted thin claim evidence, missing independent assurance, and a missing dependency map.

This is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would be unblocked by the applicable Net Change Limit being pinned and independently verified from public chain evidence, plus stronger independent evidence for the major adoption and execution claims, especially Phase 1 mainnet activity, current Sellout traction, and the anchor deployment/revenue projections.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 4.97M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, security audit, and launch campaign.
- finding: Recipient: Anvil Development Agency, Inc. / Intersect as budget administrator under the described TRSC/PSSC framework
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace with on-chain settlement, Smart-contract royalty enforcement, Per-event anti-scalping controls, Custodial wallet onboarding inside Sellout's flow, Organizer dashboard and tools, Independent third-party security audit with published remediation, Public launch campaign and trade-show activations, Public metrics dashboard and quarterly reporting
- finding: Deadline/expiry: 8 months over five milestones
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursement.
- finding: Claim (adoption, proposer_asserted, high materiality): Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 is intended to deliver a secondary ticket marketplace, smart-contract-enforced royalties, anti-scalping controls, wallet onboarding, organizer tools, an audit, and launch amplification.
- finding: Claim (economic, supported_in_proposal, high materiality): The team commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism using 25% of fees until full reimbursement and 5% afterward, with final revenue-base definitions to be established in M1 contracting.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout is asserted to have 200,000+ registered users, 250,000+ tickets issued to date, and 350+ events annually at current cadence.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6M+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- missing: Independent evidence for: Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital.
- missing: Independent evidence for: Sellout is asserted to have 200,000+ registered users, 250,000+ tickets issued to date, and 350+ events annually at current cadence.
- missing: Independent evidence for: The proposal targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6M+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move more than $6M through Cardano in Year 1, based on $5.88M in 2025 historical revenue.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 4969231
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.74
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursement." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital." — so cost or precedent may outweigh the benefit.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 4969231
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursement." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has meaningful public-benefit upside and provides a relatively detailed budget, milestone structure, oversight framework, and repayment concept, but the largest value claims depend on asserted user base, contracted deployment, transaction volumes, and revenue projections that are not evidenced within the supplied document. Because the ask is large and the revenue-share details are partly deferred to M1 contracting, a small cautionary negative nudge is justified beyond the mechanical gates.
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
- Claims and evidence missing: Independent evidence for: Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital.
- Claims and evidence missing: Independent evidence for: Sellout is asserted to have 200,000+ registered users, 250,000+ tickets issued to date, and 350+ events annually at current cadence.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `6b0c013556ee0118b6f09090423749cc3bbc725dbafffb72a07335fcbe2412ad`
- snapshot_bundle_hash: `5f61749e3c3baab34f27f80b793bdf209a6dbacb35f6247a03c0698343982fc4`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

