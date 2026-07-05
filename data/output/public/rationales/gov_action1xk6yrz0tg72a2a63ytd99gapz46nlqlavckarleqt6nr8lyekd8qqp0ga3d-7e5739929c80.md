# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NO**
Score: `-0.3133` (raw `-0.2833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7983` | Readiness: `0.9`
> Reasoning layer (precomputed): The document provides a detailed budget, milestones, oversight structure, and repayment concept, but the highest-value claims around existing volume, contracted deployment, projected on-chain activity, and repayment capacity are mostly proposer-asserted or only future-verifiable. Given the large treasury ask and BEACN's hierarchy prioritizing treasury stewardship and evidence quality over growth speed, a small cautionary negative nudge is justified beyond the mechanical assessment.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and several of the highest-value claims were not backed by independent, replayable evidence.

The action requested 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, with Intersect acting as budget administrator through the Sundae Labs TRSC/PSSC framework. The proposal said the funds would support an 8-month, five-milestone plan covering a secondary marketplace, on-chain settlement, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, launch activity, a public metrics dashboard, and quarterly reporting.

Several basic proposal claims were supported in the proposal itself: the requested amount, the stated dollar equivalent at $0.22 per ADA, the 3% Intersect administration fee, milestone-gated disbursements, the Phase 2 deliverables, the repayment concept, unused contingency return, and the statement that the withdrawal did not breach the applicable Net Change Limit. The anchor document was available, pinned, and replayable, and the review found a credible YES case around the structured budget and delivery framework.

The NO came from evidence quality and treasury stewardship. The proposal’s most important adoption and readiness claims were still mostly proposer-asserted or future-verifiable, including that Phase 1 is already live on Cardano mainnet with the listed functionality and over $130,000 invested, that Sellout has 200,000+ registered users and 250,000+ tickets issued, and that the Yellowstone Club deployment and 12-month adoption targets would generate the stated Cardano activity. The review also noted thin claims-and-evidence status, missing independent assurance, a missing dependency map, medium execution risk, and an advisory treasury-flow penalty. For a treasury withdrawal of this size, BEACN required stronger independent evidence before supporting the spend.

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
- finding: Requested: Treasury withdrawal to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency.
- finding: Recipient: Intersect as budget administrator for disbursement through the Sundae Labs TRSC/PSSC framework, with Anvil/Sellout delivering the project.
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace with on-chain settlement, Smart-contract royalty enforcement, Per-event anti-scalping controls, Custodial wallet onboarding inside Sellout flow, Organizer dashboard and verification tools, Independent third-party smart-contract audit with published remediation, Public launch campaign and trade-show activations, Public metrics dashboard and quarterly reporting
- finding: Deadline/expiry: 8 months across five milestones
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 invested.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over 8 months with milestone-gated disbursements.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 will deliver a secondary ticket marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, and launch amplification.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move over $6 million through Cardano in Year 1, based on $5.88 million in 2025 historical activity.
- finding: Claim (adoption, proposer_asserted, high materiality): The project targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6 million+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- missing: Independent evidence for: Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 invested.
- missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment projected to move over $6 million through Cardano in Year 1, based on $5.88 million in 2025 historical activity.
- missing: Independent evidence for: The project targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6 million+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over 8 months with milestone-gated disbursements." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 invested." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, stated as approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over 8 months with milestone-gated disbursements." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The document provides a detailed budget, milestones, oversight structure, and repayment concept, but the highest-value claims around existing volume, contracted deployment, projected on-chain activity, and repayment capacity are mostly proposer-asserted or only future-verifiable. Given the large treasury ask and BEACN's hierarchy prioritizing treasury stewardship and evidence quality over growth speed, a small cautionary negative nudge is justified beyond the mechanical assessment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification funded by Sellout with over $130,000 invested.
- Claims and evidence missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `7e5739929c80be11dd3ecf25c5887336b44e6787c579b89d2a866cd8b9f6cc7a`
- snapshot_bundle_hash: `5878eeb0182e8f57509c2fd2a262556b36dd9d73fb134ebdca962fc40cd9455c`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1961, "NO": 0.7594, "YES": 0.0445}`

