# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NO**
Score: `-0.3133` (raw `-0.2833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.8333` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal includes a detailed budget and milestone structure, but the deterministic assessment is blocked for missing complete summary, budget, feasibility, risk, alternatives, and failure-mode analysis, while several high-materiality adoption and repayment assumptions remain proposer-asserted. Under treasury stewardship and evidence-quality priorities, the bounded adjustment should lean cautiously negative rather than reward plausible but insufficiently evidenced ecosystem growth.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw 4,969,231 ada for Cardano Enterprise Adoption: Ticketing Platform. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw treasury funds for Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, audit, and launch campaign.. The recorded treasury amount is 4,969,231. The strongest grounded claim is: The requested withdrawal is 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee, over 8 months.

A material weak point is that this claim remains proposer-asserted or thinly supported: Phase 1 of the ticketing platform is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: Withdraw treasury funds for Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, audit, and launch campaign.
- finding: Recipient: Intersect as budget administrator, with funds administered through the Sundae Labs TRSC/PSSC framework for Anvil/Sellout project delivery.
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary ticket resale marketplace settling transactions on-chain, Smart-contract royalty enforcement for artists and venues, Per-event anti-scalping controls including price ceilings, transfer limits, identity-binding, and time restrictions, Custodial wallet onboarding inside Sellout's existing user flow, Organizer tools for resale parameters, ticket lifecycle data, royalty distributions, and ticket verification, Independent third-party smart-contract security audit with published report and remediation, Public launch campaign including Big Storm marketing and three trade-show activations, Public metrics dashboard, quarterly reports, and final governance report
- finding: Deadline/expiry: 8 months across five milestones
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 of the ticketing platform is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- finding: Claim (economic, proposer_asserted, medium materiality): Sellout has invested over $130,000 of its own capital into Phase 1.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested withdrawal is 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee, over 8 months.
- finding: Claim (adoption, proposer_asserted, high materiality): Phase 2 is projected to deliver 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6 million+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposer commits that 25% of all fees will be sent to the Treasury until $1,093,231 is reimbursed, then reduced to a permanent 5% fee, with quarterly public reporting.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment and is projected to move over $6 million through Cardano in Year 1.
- missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- missing: Independent evidence for: Sellout has invested over $130,000 of its own capital into Phase 1.
- missing: Independent evidence for: Phase 2 is projected to deliver 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6 million+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is presented as a contracted anchor deployment and is projected to move over $6 million through Cardano in Year 1.
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
- finding: Six-month treasury flow regime: unknown (stale snapshot)
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
- finding: Strongest YES: the proposal substantiates "The requested withdrawal is 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee, over 8 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 of the ticketing platform is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The requested withdrawal is 4,969,231 ada, described as approximately $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee, over 8 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal includes a detailed budget and milestone structure, but the deterministic assessment is blocked for missing complete summary, budget, feasibility, risk, alternatives, and failure-mode analysis, while several high-materiality adoption and repayment assumptions remain proposer-asserted. Under treasury stewardship and evidence-quality priorities, the bounded adjustment should lean cautiously negative rather than reward plausible but insufficiently evidenced ecosystem growth.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~18 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet and includes on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- Claims and evidence missing: Independent evidence for: Sellout has invested over $130,000 of its own capital into Phase 1.
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
- input_hash: `84d06c34a67c79caeee96ac35029ab90b2d4c8bfdffd5c2e0334b18513a7cb87`
- snapshot_bundle_hash: `95cda310c666802d328de8855f3d5e903306b57ca92dca18200c21b49fdb7e20`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `658`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1914, "NO": 0.7642, "YES": 0.0443}`

