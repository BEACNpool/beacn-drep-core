# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NO**
Score: `-0.3133` (raw `-0.2833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7983` | Readiness: `0.9`
> Reasoning layer (precomputed): The proposal is detailed and includes milestone gating, audit, oversight, and a repayment concept, but the large treasury ask depends heavily on asserted adoption, contracted deployment, revenue projections, and an M1-finalized repayment base. Under BEACN doctrine, that evidence gap warrants a small cautionary nudge rather than added support for spending.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large Treasury withdrawal, and several material adoption and execution claims were not independently supported by replayable evidence.

The action requested 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency. The proposal described an 8-month, five-milestone plan covering a secondary ticket marketplace, on-chain royalties, anti-scalping controls, wallet onboarding, organizer tools, an independent smart-contract audit, launch activity, public reporting, and a revenue-share mechanism intended to reimburse the Treasury.

The proposal was detailed in several important areas. It clearly stated the requested amount, the approximate dollar value used by the proposer, the milestone-gated structure, the deliverables, oversight through Intersect using the Sundae Labs TRSC/PSSC framework, and the intended repayment concept. However, key claims behind the case for spending remained proposer-asserted rather than independently verified, including that Phase 1 is already live on Cardano mainnet and self-funded with more than $130,000, that Sellout has 200,000+ registered users, 250,000+ tickets issued, and 350+ events annually, and that the targeted adoption volumes would follow from the proposed rollout.

The review gates allowed the proposal to be reviewed because the anchor document was available, pinned, and replayable. But Treasury withdrawals require elevated scrutiny because they spend shared ada and set precedent. The review found medium execution risk, thin claims-and-evidence support, missing independent assurance, and no dependency map. BEACN’s NO vote reflects that the proposal had real structure, oversight, and repayment ideas, but the evidence did not meet the higher bar needed for a Treasury spend of this size.

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
- finding: Requested: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including secondary marketplace, on-chain royalties, anti-scalping controls, wallet onboarding, organizer tools, security audit, and launch campaign.
- finding: Recipient: Anvil Development Agency, Inc. and Intersect as budget administrator by prior agreement
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace for listing, pricing, and reselling tickets with on-chain settlement, Smart-contract royalty enforcement for artists and venues, Configurable per-event anti-scalping controls including price ceilings, transfer limits, identity-binding, and time-based restrictions, Custodial wallet onboarding inside Sellout's existing user flow with self-custody export planned in testnet milestone, Organizer dashboard and tools for resale parameters, ticket lifecycle data, royalty distributions, and ticket verification, Independent third-party smart-contract security audit with published report and remediation, Public launch campaign including Big Storm campaign and three trade-show activations, Public metrics dashboard and quarterly reporting to the Cardano Forum, Contractual revenue-share repayment mechanism to reimburse the Treasury
- finding: Deadline/expiry: 8 months across five milestones
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursement.
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 deliverables include a secondary marketplace, smart-contract royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, and launch amplification.
- finding: Claim (economic, supported_in_proposal, high materiality): The team commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism where 25% of fees are paid until full reimbursement and 5% thereafter.
- finding: Claim (economic, supported_in_proposal, high materiality): The exact revenue-base definition and cadence for repayment will be finalized in M1 contracting with the appointed oversight committee.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout is described as having 200,000+ registered users, 250,000+ tickets issued to date, and 350+ events annually at current cadence.
- missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital.
- missing: Independent evidence for: Sellout is described as having 200,000+ registered users, 250,000+ tickets issued to date, and 350+ events annually at current cadence.
- missing: Independent evidence for: The proposal targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move $6M+ through Cardano in Year 1, based on $5.88M historical 2025 volume.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 4969231
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest NO: a material claim is unsupported — "Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital." — so cost or precedent may outweigh the benefit.
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
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal is detailed and includes milestone gating, audit, oversight, and a repayment concept, but the large treasury ask depends heavily on asserted adoption, contracted deployment, revenue projections, and an M1-finalized repayment base. Under BEACN doctrine, that evidence gap warrants a small cautionary nudge rather than added support for spending.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital.
- Claims and evidence missing: Independent evidence for: Sellout is described as having 200,000+ registered users, 250,000+ tickets issued to date, and 350+ events annually at current cadence.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `9e91a8737c99bc7c2d586cfe35c7a633e73b9ec24fa4a87bf0068b5d0146e933`
- snapshot_bundle_hash: `ac44af3f48bf3d1e9dc9de1b49c7a2281a35cba7fdde15a45a10bb2204dfc791`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1961, "NO": 0.7594, "YES": 0.0445}`

