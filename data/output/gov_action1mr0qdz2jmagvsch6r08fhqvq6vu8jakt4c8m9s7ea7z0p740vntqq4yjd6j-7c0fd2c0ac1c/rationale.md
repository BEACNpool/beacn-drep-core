# Rationale: gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j
Recommendation: **NO**
Score: `-0.2633` (raw `-0.2833` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7858` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the proposal describes public open-source infrastructure, independently verifiable release/version metrics, milestone-based administration, and return of unspent funds, which improves evidence quality and treasury stewardship beyond a thin discretionary ask. The adjustment remains small because several important track-record, user-count, and cost-efficiency claims are proposer-asserted, and the doctrine calls for caution on treasury spending.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury request did not clear the higher evidence bar for spending shared ADA: important claims about Daedalus’s unique role, user count, sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path remained thin or unsupported.

The action requested 1,785,333 ADA for Se7en Labs, Inc. to maintain and improve Daedalus over a 52-week time-and-materials engagement, with Intersect administering funds and verifying milestones. The work included hard fork readiness, cardano-node and cardano-wallet integration, release engineering, hardware wallet support, a CIP-30 dApp connector, Japanese localisation and support, and an architecture assessment by Q3 2027.

The review found several positives. The proposal anchor was available and replayable. It supported claims that Daedalus private keys stay on the user’s device, that the code is auditable under Apache License 2.0, that hard fork compatible releases would ship at least two weeks before mainnet activations, and that release timing and version metrics could be checked through public GitHub repositories and the Cardano mainnet chain. It also described milestone-based administration by Intersect, a dedicated auditable account, and return of unspent labor, hardware, and audit funds.

However, treasury withdrawals require elevated scrutiny. The review found missing independent evidence for the claim that Daedalus is Cardano’s only full-node desktop wallet and for the claimed user activity figures. It also found the claims-and-evidence record thin, medium execution risk, missing sustainability and cost-benefit clarity, and no independent assurance or rollback/remedy path. With the treasury flow signal in an unsustainable regime and an advisory penalty applied, the supported benefits were not enough to outweigh the evidence gaps and treasury precedent risk.

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
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027 delivered by Se7en Labs, Inc. as a time and materials treasury-funded engagement.
- finding: Recipient: Se7en Labs, Inc. with Intersect serving as administrator and milestone verifier
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including cardano-node and cardano-wallet integration, hard fork readiness, dependency updates, release engineering, and platform support, Compatible Daedalus stable release at least 2 weeks before each mainnet hard fork, Keystone and Flex hardware wallet support plus newer hardware wallet models as they emerge, CIP-30 dApp connector implementation in Daedalus with documentation and dApp interoperability verification, Ongoing user support including Japanese-language support and full Japanese translation across shipped features, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: 52-week contract period, with architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (technical, supported_in_proposal, high materiality): Daedalus private keys are generated and stored on the user's device and are never transmitted to an external service, with source code auditability under the Apache License 2.0.
- finding: Claim (adoption, proposer_asserted, medium materiality): Opt-in telemetry shows approximately 4,000 monthly active Daedalus users, while the proposer asserts the true count is meaningfully higher because privacy-conscious users are less likely to opt in.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, native Apple Silicon builds, the drt release CLI, and Nix build modernization.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to keeping Daedalus compatible with upcoming hard forks and shipping a stable compatible release at least two weeks before each mainnet activation.
- finding: Claim (adoption, supported_in_proposal, medium materiality): The proposal includes ecosystem expansion through Keystone and Flex hardware wallet support, a CIP-30 dApp connector, Japanese localisation, and user support.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Opt-in telemetry shows approximately 4,000 monthly active Daedalus users, while the proposer asserts the true count is meaningfully higher because privacy-conscious users are less likely to opt in.
- missing: Independent evidence for: Se7en Labs assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, native Apple Silicon builds, the drt release CLI, and Nix build modernization.
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
- finding: Strongest YES: the proposal substantiates "Daedalus private keys are generated and stored on the user's device and are never transmitted to an external service, with source code auditability under the Apache License 2.0." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Daedalus private keys are generated and stored on the user's device and are never transmitted to an external service, with source code auditability under the Apache License 2.0." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by +0.020 (clamped to ±0.05): A small positive nudge is justified because the proposal describes public open-source infrastructure, independently verifiable release/version metrics, milestone-based administration, and return of unspent funds, which improves evidence quality and treasury stewardship beyond a thin discretionary ask. The adjustment remains small because several important track-record, user-count, and cost-efficiency claims are proposer-asserted, and the doctrine calls for caution on treasury spending.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: Opt-in telemetry shows approximately 4,000 monthly active Daedalus users, while the proposer asserts the true count is meaningfully higher because privacy-conscious users are less likely to opt in.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `7c0fd2c0ac1cfbf05957f4b8c77f3b37bba9961296a265d0490fb9b38e804dbe`
- snapshot_bundle_hash: `06f38c23d91f5deeb8429d54972e00e8d9e36440354637ab5ea4f9bb2e1ea0cc`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.207, "NO": 0.7464, "YES": 0.0467}`

