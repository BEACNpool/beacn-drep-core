# Rationale: gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.52` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show a public-good maintenance case with some concrete milestones and oversight mechanics, but the deterministic assessment is blocked for missing budget, feasibility, risk, alternatives, failure-mode, and complete summary analysis. Under BEACN's hierarchy, a large treasury withdrawal with incomplete diligence should receive a cautious negative nudge rather than a spending-positive lean.

## Plain-language explanation (precomputed)
BEACN voted NO because this is a large treasury withdrawal and the review dossier was incomplete on several core diligence questions. The proposal includes a meaningful public-good case for maintaining Daedalus, but BEACN’s process requires stronger evidence before supporting a 1.785 million ADA withdrawal from the shared treasury.

The action requested 1,785,333 ADA for Se7en Labs, Inc., administered through Intersect with milestone-based controls, to maintain and improve Daedalus through 2026-2027. The proposed work includes protocol maintenance, hard fork readiness, backend and platform support, signed releases, hardware wallet support, CIP-30 and other user-facing CIP work, Japanese localisation, user support, and an architecture assessment by Q3 2027. The proposal stated that Intersect would verify milestones, hold funds in an auditable account, and disburse monthly against verified work.

Some claims were supported inside the proposal, especially the commitment to ship a compatible Daedalus release at least two weeks before every mainnet hard fork, the stated budget breakdown, and the plan to return unspent labor, hardware, or audit funds. Some items were independently verifiable in principle, such as release timing and version currency through public GitHub repositories and the Cardano mainnet chain. But important claims remained unsupported by independent evidence in the review, including the claim that Daedalus is Cardano’s only full-node desktop wallet and the claim of approximately 4,000 monthly active users from opt-in telemetry.

The decisive issue was not that the proposal lacked value; it was that too many review gates were still open for a treasury action. The review found missing or incomplete budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, community impact analysis, and a complete proposal summary. Treasury scrutiny was elevated because the action spends shared ADA, risk review was thin, execution risk was unknown, and the treasury flow signal was in an unsustainable regime. On the available evidence, BEACN took the conservative position and voted NO.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 1.79M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027 delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc. via Intersect administration and milestone-based disbursement controls
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including node upgrades, wallet backend updates, hard fork readiness, platform support, release engineering, security and dependency maintenance, and signed releases, Ecosystem expansion including Keystone and Flex hardware wallet support, CIP-30 dApp connector, user-facing CIP implementations, and Japanese localisation, User support across GitHub, community forums, direct channels, and Japanese-language support, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: contract year through 2026-2027; architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is described as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count claimed to be meaningfully higher.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs says it assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend work, Apple Silicon builds, a release CLI, and Nix build modernization.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to a compatible Daedalus release at least two weeks before every mainnet hard fork during the contract period.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget totals 1,785,333 ADA, including 1,666,667 ADA for labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee.
- finding: Claim (economic, supported_in_proposal, medium materiality): The proposal states any unspent labor, hardware, or audit budget will be returned to the treasury.
- missing: Independent evidence for: Daedalus is described as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: The proposal states Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count claimed to be meaningfully higher.
- missing: Independent evidence for: Se7en Labs says it assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend work, Apple Silicon builds, a release CLI, and Nix build modernization.
- missing: Independent evidence for: The proposal states Se7en Labs has not received ada from the Cardano Treasury within the last 24 months.
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
- finding: Requested ADA: 1.79M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "The proposal commits to a compatible Daedalus release at least two weeks before every mainnet hard fork during the contract period." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is described as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1.79M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal commits to a compatible Daedalus release at least two weeks before every mainnet hard fork during the contract period." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show a public-good maintenance case with some concrete milestones and oversight mechanics, but the deterministic assessment is blocked for missing budget, feasibility, risk, alternatives, failure-mode, and complete summary analysis. Under BEACN's hierarchy, a large treasury withdrawal with incomplete diligence should receive a cautious negative nudge rather than a spending-positive lean.
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
- Claims and evidence missing: Independent evidence for: Daedalus is described as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: The proposal states Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count claimed to be meaningfully higher.
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
- input_hash: `73a23fad54da758bc2aaefab4372cfd012bb9594c11646fd31958fc7054df951`
- snapshot_bundle_hash: `4c13f55706fd3c27a1602cbeee9b0d58e0aafcf353e9e4be4ed3e3f5eb2c028c`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `960`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2146, "NO": 0.7433, "YES": 0.0421}`

