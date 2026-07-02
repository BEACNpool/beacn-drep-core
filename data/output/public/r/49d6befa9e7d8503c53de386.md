# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9333` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit growth and some milestone/oversight structure, but the deterministic assessment is blocked by missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's values hierarchy, a large treasury withdrawal with many high-materiality proposer-asserted adoption and execution claims, plus an unfinished repayment-base definition, justifies a small cautionary negative nudge rather than a positive one.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw 4,969,231 ada for Cardano Enterprise Adoption: Ticketing Platform. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, audit, and launch campaign.. The recorded treasury amount is 4,969,231. The strongest grounded claim is: The proposal requests 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over 8 months.

A material weak point is that this claim remains proposer-asserted or thinly supported: Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded by Sellout with over $130,000 of its own capital. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, audit, and launch campaign.
- finding: Recipient: not stated in document
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace for listing, pricing, and reselling tickets with on-chain settlement, Smart-contract-level royalty enforcement for configured artist and venue shares, Configurable anti-scalping controls including price ceilings, transfer limits, identity-binding, and time-based restrictions, Custodial wallet onboarding inside Sellout's existing flow, Organizer dashboard and tools for resale parameters, ticket lifecycle data, royalty distributions, and ticket verification, Independent third-party smart-contract security audit with published report and remediation, Public launch campaign including Big Storm campaign and three trade-show activations, Public metrics dashboard and final governance report
- finding: Deadline/expiry: 8 months over five milestone-gated milestones
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over 8 months.
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded by Sellout with over $130,000 of its own capital.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 is intended to deliver a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, and a professional launch campaign.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal projects 12-month outcomes of 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism where 25% of all fees is paid until full reimbursement, then 5% permanently, with quarterly public reporting.
- missing: Independent evidence for: Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded by Sellout with over $130,000 of its own capital.
- missing: Independent evidence for: The proposal says Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- missing: Independent evidence for: The proposal projects 12-month outcomes of 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets.
- missing: Independent evidence for: Anvil claims a track record including 250+ Cardano projects delivered, 456,000+ assets minted, 50,000,000+ ADA staked through Anvil infrastructure, and 267,000+ on-chain transactions.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 4.97M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over 8 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded by Sellout with over $130,000 of its own capital." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 4.97M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, inclusive of a 3% Intersect administration fee, over 8 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show plausible public-benefit growth and some milestone/oversight structure, but the deterministic assessment is blocked by missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's values hierarchy, a large treasury withdrawal with many high-materiality proposer-asserted adoption and execution claims, plus an unfinished repayment-base definition, justifies a small cautionary negative nudge rather than a positive one.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow signal is in unsustainable regime (advisory penalty applied).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 is described as already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification, funded by Sellout with over $130,000 of its own capital.
- Claims and evidence missing: Independent evidence for: The proposal says Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `3dc01583b70d1612d41a6835e995d158c3b57ba79f6a5cb2df38ef44c636f187`
- snapshot_bundle_hash: `ac9253400b6634e3fb98af2185526b99863e1af6db400eef17c509fb34d0550e`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4fbc4829bb6142608e4d32087d1ed0565eaf5b12`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `799`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.164, "NO": 0.7957, "YES": 0.0403}`

