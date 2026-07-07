# Rationale: gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j
Recommendation: **NO**
Score: `-0.3033` (raw `-0.2833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7958` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has strong public-good alignment and some independently verifiable delivery metrics, but the large treasury ask relies materially on proposer assertions about user count, prior delivery, team capability, and cost necessity. Under treasury stewardship and evidence quality principles, the bounded lean should apply a small caution nudge rather than reward spending on evidence that is partly unverifiable within the supplied claims.

## Plain-language explanation (precomputed)
BEACN voted NO because this large treasury request did not clear the higher evidence bar required for spending shared ADA. The proposal has strong public-good elements, but key claims supporting the need, impact, and cost justification were not independently evidenced in the supplied review.

The action requested 1,785,333 ADA for Se7en Labs, administered through Intersect, to maintain and improve Daedalus Wallet through 2026-2027. The work included protocol and hard fork readiness, wallet backend updates, release engineering, security and dependency maintenance, Keystone and Flex hardware wallet support, a CIP-30 dApp connector, Japanese localisation and support, and an architecture assessment by Q3 2027. The proposer claimed Daedalus is Cardano’s only full-node desktop wallet, has about 4,000 monthly active users by opt-in telemetry, and that Se7en Labs has been maintaining Daedalus under an IOG contract since January 2026.

Several parts were well-supported: the proposal anchor was pinned and replayable, public Apache 2.0 outputs were committed, release timing and version currency could be checked through public GitHub repositories and mainnet activity, the requested amount did not breach the applicable Net Change Limit at submission, and Intersect’s administration and milestone verification role was described. However, important claims remained unsupported or thin in the supplied evidence, including the full-node-wallet claim, the user-count claim, the sustainability path, cost-benefit clarity, independent assurance, and a rollback or remedy path.

Because this is a treasury withdrawal, BEACN applied elevated scrutiny. The review found medium execution risk, a flag score that reduced confidence, and an unsustainable treasury-flow signal. The strongest YES case was that the work would create public assets and had some verifiable delivery metrics, but the strongest NO case carried more weight: the proposal relied materially on proposer assertions for important claims behind a large funding request. That is why BEACN voted NO.

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
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Daedalus Wallet maintenance and improvements for 2026-2027 as a time and materials engagement.
- finding: Recipient: Se7en Labs, Inc., with administration and disbursement through Intersect
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including node upgrades, wallet backend updates, hard fork readiness, platform support, release engineering, security and dependency maintenance, Compatible stable Daedalus release at least 2 weeks before each mainnet hard fork, Keystone and Flex hardware wallet support in a stable release, CIP-30 dApp connector implementation in Daedalus with documentation and interoperability verification, Japanese localisation and Japanese-language user support throughout the contract period, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: Contract year through 2026-2027; architecture assessment by Q3 2027; ongoing maintenance and user support for 52 weeks
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, medium materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be meaningfully higher.
- finding: Claim (governance, supported_in_proposal, high materiality): All funded outputs, including source code, build tooling, documentation, and release artifacts, will be public assets under the Apache 2.0 license.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization.
- finding: Claim (governance, proposer_asserted, medium materiality): The team has operated under an IOG contract for Daedalus maintenance since January 2026, closing August 31, 2026, and has not received ada from the Cardano Treasury within the last 24 months.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to maintaining Daedalus compatibility with upcoming protocol changes, including hard forks, Leios, Peras, and Nested Transactions, with stable releases at least 2 weeks before mainnet activation.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be meaningfully higher.
- missing: Independent evidence for: Se7en Labs assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization.
- missing: Independent evidence for: The team has operated under an IOG contract for Daedalus maintenance since January 2026, closing August 31, 2026, and has not received ada from the Cardano Treasury within the last 24 months.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1785333
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.62
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: high
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
- finding: Strongest YES: the proposal substantiates "All funded outputs, including source code, build tooling, documentation, and release artifacts, will be public assets under the Apache 2.0 license." and clears the evidence gates.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1785333
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "All funded outputs, including source code, build tooling, documentation, and release artifacts, will be public assets under the Apache 2.0 license." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has strong public-good alignment and some independently verifiable delivery metrics, but the large treasury ask relies materially on proposer assertions about user count, prior delivery, team capability, and cost necessity. Under treasury stewardship and evidence quality principles, the bounded lean should apply a small caution nudge rather than reward spending on evidence that is partly unverifiable within the supplied claims.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be meaningfully higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `fda2829f5746e1beda10923bddf2178e841cb45257107136363c4ef4403d5809`
- snapshot_bundle_hash: `6eee5cf98c02135e8622f4f35bd46b9ccc087573dea53215d6a086a7aff0b96e`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1982, "NO": 0.7569, "YES": 0.0449}`

