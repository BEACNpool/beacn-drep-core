# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1515` (raw `-0.11` + doctrine-LLM nudge `+0.03`) | Confidence: `0.7579` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the proposal describes established infrastructure maintenance with public-good licensing, concrete deliverables, milestone-based oversight, and several independently verifiable release and version-currency metrics; however, the large treasury ask and some proposer-asserted adoption and return-of-funds claims warrant keeping the adjustment modest.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work described.

The proposal asks for 1,785,333 ADA for Se7en Labs to maintain and improve Daedalus through 2026-2027, administered through Intersect and project-specific treasury management contracts. The stated scope includes keeping Daedalus current with cardano-node and cardano-wallet, hard fork readiness, signed releases, platform support, Keystone and Flex hardware wallet support, CIP-30 dApp connector work, user support including Japanese-language support, and an architecture assessment by Q3 2027.

Several parts of the proposal were well supported: the anchor document was available and replayable, the scope and success metrics were concrete, the budget was broken down, and the proposal substantiated that Se7en Labs took responsibility for Daedalus under an IOG contract in January 2026 and shipped Daedalus 8.0 and 11.0 during that period. Other important claims were not independently supported in the review, including the claim that Daedalus is Cardano’s only full-node desktop wallet and the claim about roughly 4,000 monthly active users with a higher true count.

The review gates showed enough substance to keep the action reviewable, but not enough verified evidence for a YES or NO. Treasury scrutiny was elevated, claims-and-evidence status was thin, execution risk was unknown, and the review was missing independent assurance, a rollback or remedy path, sustainability path, and cost-benefit clarity. A directional vote would be unblocked by pinned, independently verifiable Net Change Limit evidence from the public chain, plus stronger replayable evidence for the key technical and adoption claims.

## Review Tree
- overall_status: `incomplete`

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
- finding: Snapshot freshness source: governance_actions_all.csv
- finding: Deep research dossier: complete
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027 delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc. via Intersect administration and project-specific treasury management contracts
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including cardano-node and cardano-wallet updates, hard fork readiness, platform support, release engineering, and signed releases, Hardware wallet support for Keystone and Flex, plus additional newer devices as they emerge, CIP-30 dApp connector implementation within Daedalus with documentation and interoperability verification, User support across GitHub, community forums, and direct channels, including Japanese-language support and full Japanese translation maintenance, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: Contract year through 2026-2027; architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, high materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is asserted to be meaningfully higher.
- finding: Claim (adoption, independently_verifiable, high materiality): Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and shipped Daedalus 8.0 and 11.0 during that contract period.
- finding: Claim (technical, supported_in_proposal, high materiality): The requested scope includes maintenance, node and wallet backend currency, security and dependency updates, hard fork integration, Leios/Peras/Nested Transactions readiness, binary signing continuity, platform support, localization, hardware wallets, CIP-30, user-facing CIPs, user support, and an architecture assessment.
- finding: Claim (technical, supported_in_proposal, high materiality): Success metrics include releases at least two weeks before each mainnet hard fork, cardano-node no more than two major versions behind mainnet recommendation, 100% signed official releases, CI passing on four platform builds, Keystone/Flex support, CIP-30 availability, Japanese support, and a public architecture assessment by Q3 2027.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal states that release-timing and version-currency metrics are independently verifiable from public GitHub repositories and the Cardano mainnet chain without applicant self-reporting.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is asserted to be meaningfully higher.
- missing: Independent evidence for: The proposer states that any unspent labor, hardware, and audit budget at contract close is returned to the treasury.
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
- finding: Financial confidence: 0.70
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and shipped Daedalus 8.0 and 11.0 during that contract period." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and shipped Daedalus 8.0 and 11.0 during that contract period." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.030 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the proposal describes established infrastructure maintenance with public-good licensing, concrete deliverables, milestone-based oversight, and several independently verifiable release and version-currency metrics; however, the large treasury ask and some proposer-asserted adoption and return-of-funds claims warrant keeping the adjustment modest.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is asserted to be meaningfully higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `dce6cb37a0812b869be2f087a90322f70b4a543f35922c8e6a8f513e54bf7df0`
- snapshot_bundle_hash: `f92e3a4bc62af27313f3d12487c7b6dc86e939b11475d7a681717c1b8140e3c5`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `82a02efa3be4dedf61fea1548ca03635163347a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `20`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5095, "NO": 0.0938, "YES": 0.3968}`

