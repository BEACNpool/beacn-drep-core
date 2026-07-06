# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NO**
Score: `-0.3033` (raw `-0.2833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7958` | Readiness: `0.9`
> Reasoning layer (precomputed): The proposal has meaningful public-benefit alignment and some verifiable oversight/on-chain reporting hooks, but the largest value drivers are forward-looking adoption, revenue, and repayment claims, and the repayment revenue-base is not finalized until M1. Under a treasury stewardship lens, that evidence mix justifies a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal asks for a large amount of shared ADA while key value-driving claims were not independently supported. The proposal has useful structure and some verifiable oversight, but treasury spending requires a higher evidence bar than proposer assertions alone.

The action requested 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform by Sellout.io and Anvil, including a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an audit, launch activity, public reporting, and a revenue-share repayment mechanism. The proposal clearly supported the requested amount, approximate dollar value, 3% Intersect administration fee, milestone-based disbursement over eight months, and the commitment to repay through fee sharing.

The strongest supported case for YES was that the budget and administration structure were reviewable, with Intersect oversight, milestone controls, public dashboard visibility, and future on-chain metrics reporting. But several major adoption and execution claims remained thin or unsupported by independent evidence, including that Phase 1 is already live on Cardano mainnet with CIP-68 ticketing and attendance verification, and that Sellout has 200,000+ users, 250,000+ tickets issued, and 350+ events annually. The revenue-share base also would not be finalized until M1 contracting.

The review gates therefore passed enough to evaluate the proposal, but not enough to justify this treasury withdrawal. Elevated treasury scrutiny, medium execution risk, missing independent assurance, a missing dependency map, thin claims-and-evidence status, and an unsustainable treasury-flow signal all weighed against approval. BEACN’s NO is a stewardship decision: the public-benefit case may be meaningful, but the evidence provided did not clear the bar for spending nearly 5 million ada from the treasury.

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
- finding: Recipient: Anvil Development Agency, Inc. / Intersect as budget administrator
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace with on-chain settlement, Smart-contract royalty enforcement, Per-event anti-scalping controls, Custodial wallet onboarding inside Sellout's flow, Organizer dashboard and ticket lifecycle tools, Independent third-party security audit with remediation report, Public launch campaign and three trade-show activations, Public metrics dashboard and quarterly reporting, Revenue-share repayment mechanism to the Cardano Treasury
- finding: Deadline/expiry: 8 months over five milestones
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, equivalent to about $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee and disbursed against milestones over 8 months.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and runs 350+ events annually at current cadence.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move over $6 million through Cardano in year one, based on $5.88 million in 2025 historical ticket volume.
- finding: Claim (economic, supported_in_proposal, high materiality): The team commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism where 25% of fees are paid until reimbursement, then 5% permanently, with exact revenue-base definition finalized in M1 contracting.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6 million+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital.
- missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and runs 350+ events annually at current cadence.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move over $6 million through Cardano in year one, based on $5.88 million in 2025 historical ticket volume.
- missing: Independent evidence for: The proposal targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6 million+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, equivalent to about $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee and disbursed against milestones over 8 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, equivalent to about $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee and disbursed against milestones over 8 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has meaningful public-benefit alignment and some verifiable oversight/on-chain reporting hooks, but the largest value drivers are forward-looking adoption, revenue, and repayment claims, and the repayment revenue-base is not finalized until M1. Under a treasury stewardship lens, that evidence mix justifies a small cautionary nudge rather than a positive adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 of its own capital.
- Claims and evidence missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and runs 350+ events annually at current cadence.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `f8ffb1e1bfc5d3461259e1d2372ce5b2c00aa55f38cd6e192f301692f7f3fcda`
- snapshot_bundle_hash: `1a1d24c28890798e9899253296aae8137fc7ec65a592b7c7e0c4a4cc09c777ba`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1982, "NO": 0.7569, "YES": 0.0449}`

