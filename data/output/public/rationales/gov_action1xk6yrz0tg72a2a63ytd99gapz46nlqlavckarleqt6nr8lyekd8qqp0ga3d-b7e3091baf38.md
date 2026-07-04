# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.67` | Readiness: `0.9`
> Reasoning layer (precomputed): The proposal has plausible public-benefit alignment and includes milestone gating, audit, oversight, and a repayment structure, but the large treasury ask depends heavily on proposer-asserted adoption, mainnet status, commercial deployment, and revenue projections. Because the deterministic tree marks treasury analysis incomplete and BEACN doctrine prioritizes treasury stewardship and reproducible evidence over growth narratives, a small cautionary negative nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and key adoption and execution claims were not independently supported enough to justify spending 4,969,231 ada from shared funds.

The proposal asked to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency. The requested funds would cover a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, launch campaign, public metrics reporting, and a revenue-share repayment mechanism. The proposal did clearly state the amount, timeline, milestone structure, and intended deliverables, and it included public oversight through Intersect and the Sundae Labs TRSC/PSSC framework.

The concern was that several of the most important reasons to approve the withdrawal depended on proposer assertions rather than independent evidence. The review found missing independent evidence that Phase 1 is already live on Cardano mainnet and self-funded with over $130,000, and missing independent evidence for Sellout’s claimed user base, ticket volume, and event cadence. The proposal’s future adoption targets, including events on-chain, NFT tickets, wallets, interactions, and ticket revenue, also depended heavily on those commercial claims.

For BEACN, treasury actions require a higher bar because they spend shared ADA and set precedent. The review passed enough gates to produce a directional vote rather than abstain, but the treasury analysis was incomplete, the evidence status was thin, independent assurance and a dependency map were missing from the risk review, and treasury flow conditions added caution. On balance, the public benefit case was plausible, but the evidence did not clear the standard needed for a YES on a large treasury withdrawal.

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
- finding: Deep research dossier: required
- finding: Requested: Fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, audit, and launch campaign.
- finding: Recipient: Anvil Development Agency, Inc. / Intersect as budget administrator
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace with on-chain settlement, Smart-contract-enforced royalty splits, Configurable anti-scalping controls, Custodial wallet onboarding inside Sellout flow, Organizer dashboard and tools, Independent third-party smart-contract audit with published remediation, Public launch campaign and trade-show activations, Public metrics dashboard and quarterly reporting, Revenue-share repayment mechanism to the Cardano Treasury
- finding: Deadline/expiry: 8 months over five milestones
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22/ADA, over 8 months with milestone-based disbursement.
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 will deliver a secondary ticket marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, and public launch amplification.
- finding: Claim (economic, supported_in_proposal, high materiality): The team commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism that sends 25% of all fees until full reimbursement and 5% thereafter.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and runs 350+ events annually at current cadence.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital.
- missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and runs 350+ events annually at current cadence.
- missing: Independent evidence for: The proposal targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is described as a contracted anchor deployment projected to move $6M+ through Cardano in Year 1, based on $5.88M historical 2025 revenue.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22/ADA, over 8 months with milestone-based disbursement." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22/ADA, over 8 months with milestone-based disbursement." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has plausible public-benefit alignment and includes milestone gating, audit, oversight, and a repayment structure, but the large treasury ask depends heavily on proposer-asserted adoption, mainnet status, commercial deployment, and revenue projections. Because the deterministic tree marks treasury analysis incomplete and BEACN doctrine prioritizes treasury stewardship and reproducible evidence over growth narratives, a small cautionary negative nudge is justified.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital.
- Claims and evidence missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and runs 350+ events annually at current cadence.
- Claims and evidence status is thin.
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `b7e3091baf38d813876e2bb6f009c9fbe1534c7ae54c3b87a195845d65dd80d0`
- snapshot_bundle_hash: `fceb696e8c9efe00942987c077936ec89fdf3420b91fe0dd291af1b5548ea80e`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `31`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1957, "NO": 0.7629, "YES": 0.0414}`

