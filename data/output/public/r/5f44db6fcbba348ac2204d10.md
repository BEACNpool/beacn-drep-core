# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NO**
Score: `-0.3033` (raw `-0.2833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7958` | Readiness: `0.9`
> Reasoning layer (precomputed): The proposal is unusually detailed on budget, milestones, oversight, and repayment mechanics, but the highest-value justification depends on large adoption and revenue projections, existing-user migration, and anchor-deployment claims that are mostly asserted in the document rather than evidenced there. Given the doctrine's preference for treasury stewardship and reproducible evidence over plausible growth upside, a small cautionary negative nudge is warranted beyond mechanical scoring.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury request depended on major adoption and revenue claims that were mostly asserted in the proposal rather than independently evidenced, and treasury withdrawals require a higher evidence bar.

The action requested 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform by Sellout.io and Anvil, administered through Intersect using the Sundae Labs TRSC/PSSC framework. The proposal described a secondary ticket marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, a security audit, launch campaign, public dashboard, and final governance reporting over eight months.

Several parts were well-supported in the proposal: the amount requested, the eight-month milestone structure, the 3% administration fee, the planned deliverables, milestone-gated disbursement, unused contingency return, quarterly reporting, audit and oversight review, and a revenue-share repayment plan. But the highest-value case for funding relied on claims that were not independently evidenced in the review, including that Phase 1 is already live on Cardano mainnet, that Sellout has 200,000+ registered users and 250,000+ tickets issued, and that the Yellowstone Club deployment would move more than $6 million through Cardano in Year 1.

The review found the proposal detailed and reviewable, with a pinned anchor document available, medium execution risk, and no decisive open blocker. However, claims-and-evidence coverage was thin, independent assurance and a dependency map were missing from the risk review, and the treasury flow signal was in an unsustainable regime. Given the size of the withdrawal, the shared treasury precedent, and the gap between asserted upside and replayable evidence, BEACN took the conservative position and voted NO.

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
- finding: Requested: Treasury withdrawal to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, security audit, and launch campaign.
- finding: Recipient: Intersect as budget administrator by prior agreement, holding and disbursing funds through the Sundae Labs TRSC/PSSC framework for Anvil/Sellout project delivery.
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace for listing, pricing, and reselling tickets with on-chain settlement, Smart-contract royalty enforcement for artists and venues on resales, Configurable anti-scalping controls including price ceilings, transfer limits, identity-binding, and time restrictions, Custodial wallet onboarding inside Sellout's existing flow with self-custody export referenced in milestones, Organizer dashboard and tools for resale parameters, ticket lifecycle data, royalty distributions, and verification, Independent third-party smart-contract security audit with report and remediation published, Public launch campaign including Big Storm campaign and NIVA, INTIX, and Pollstar Live! trade-show activations, Public metrics dashboard and final governance report
- finding: Deadline/expiry: 8 months across five milestones
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over 8 months with milestone-gated disbursement.
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded by Sellout with over $130,000 of its own capital.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 is intended to deliver a secondary ticket marketplace, smart-contract royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent security audit, and launch amplification.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal projects 12-month outcomes of 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move $6M+ through Cardano in Year 1, based on stated 2025 historical revenue of $5.88M.
- missing: Independent evidence for: Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded by Sellout with over $130,000 of its own capital.
- missing: Independent evidence for: The proposer states that Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- missing: Independent evidence for: The proposal projects 12-month outcomes of 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move $6M+ through Cardano in Year 1, based on stated 2025 historical revenue of $5.88M.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over 8 months with milestone-gated disbursement." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded by Sellout with over $130,000 of its own capital." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over 8 months with milestone-gated disbursement." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal is unusually detailed on budget, milestones, oversight, and repayment mechanics, but the highest-value justification depends on large adoption and revenue projections, existing-user migration, and anchor-deployment claims that are mostly asserted in the document rather than evidenced there. Given the doctrine's preference for treasury stewardship and reproducible evidence over plausible growth upside, a small cautionary negative nudge is warranted beyond mechanical scoring.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded by Sellout with over $130,000 of its own capital.
- Claims and evidence missing: Independent evidence for: The proposer states that Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `a0a16aa9fbf68ccf62ef80ea5c90f26fa049f61145907f4d1a9151502f011e96`
- snapshot_bundle_hash: `2d7772b8ae85da4a111ba2d95399afae0e2cdd3071af64ae85299fdaaf8c1dc7`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1982, "NO": 0.7569, "YES": 0.0449}`

