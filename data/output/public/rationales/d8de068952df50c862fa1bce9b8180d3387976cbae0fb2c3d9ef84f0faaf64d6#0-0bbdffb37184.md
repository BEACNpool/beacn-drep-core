# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.11` (raw `-0.11` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7475` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit infrastructure maintenance and provides concrete deliverables, milestones, budget categories, success metrics, and oversight mechanics, while several important adoption and track-record claims remain proposer-asserted rather than evidenced inside the document. Because the deterministic assessment is already ready and the evidence mix is neither unusually stronger nor weaker than the rules appear to capture, no advisory nudge is warranted.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work or the proposer.

The action asks for 1,785,333 ADA for Se7en Labs to maintain and improve Daedalus during a 52-week contract year, administered through Intersect and project-specific smart contract arrangements. The proposal covers hard fork readiness, protocol and node upgrades, hardware wallet support, CIP-30 dApp connector work, Japanese localisation and support, user support, dependency and security maintenance, Nix reproducible builds, and an architecture assessment by Q3 2027.

Several parts of the proposal were well-supported. The anchored proposal is pinned and replayable. The budget breakdown is clear, including maintenance, test hardware, audit, and Intersect administration. The proposal commits to Daedalus releases at least two weeks before each mainnet hard fork, development builds on relevant testnets, four platform builds, dependency maintenance, and reproducible Nix builds. It also describes monthly disbursement against verified work, milestone oversight, treasury management smart contracts, and an external oversight committee.

The hold remains because treasury withdrawals require a higher evidence bar. Some material claims were still unsupported by independent evidence, including that Daedalus is Cardano’s only full-node desktop wallet and that it has about 4,000 monthly active users with higher true usage implied. The review also found thin claims evidence, missing sustainability and cost-benefit clarity, missing independent assurance, and no clear rollback or remedy path. A directional vote would be unblocked by a verified public-chain Net Change Limit and stronger replayable evidence for the material claims and treasury-risk questions.

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
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027, delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc. via Intersect administration and project-specific smart contract arrangements
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance, node upgrades, hard fork readiness, and compatible releases at least 2 weeks before each mainnet hard fork, Keystone and Flex hardware wallet support and support for newer hardware wallet models as they emerge, CIP-30 dApp connector implementation within Daedalus, Japanese localisation and Japanese-language user support, Ongoing user support through GitHub, community forums, and direct channels, Security and dependency maintenance for Electron, Node.js, wallet dependencies, Nix build infrastructure, and platform compatibility, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: Contract year covering 52 weeks, with architecture assessment by Q3 2027 and IOG contract stated as closing August 31, 2026
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, high materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is asserted to be higher because privacy-conscious users are less likely to opt in.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and shipped items including Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, Nix modernization, and Daedalus 8.0 and 11.0.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to compatible Daedalus releases at least 2 weeks before every mainnet hard fork, with development builds on relevant testnets and all four platform builds maintained.
- finding: Claim (technical, supported_in_proposal, high materiality): The funded scope includes maintaining Daedalus security and dependencies, preserving auditable local key generation, storage, and signing, and keeping releases reproducibly buildable through Nix.
- finding: Claim (economic, proposer_asserted, medium materiality): All funded outputs are described as public assets under the Apache License 2.0, with Se7en Labs claiming no subscription revenue, customer relationship capture, token value, or IP exclusivity from the work.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is asserted to be higher because privacy-conscious users are less likely to opt in.
- missing: Independent evidence for: Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and shipped items including Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, Nix modernization, and Daedalus 8.0 and 11.0.
- missing: Independent evidence for: All funded outputs are described as public assets under the Apache License 2.0, with Se7en Labs claiming no subscription revenue, customer relationship capture, token value, or IP exclusivity from the work.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1785333
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "The proposal commits to compatible Daedalus releases at least 2 weeks before every mainnet hard fork, with development builds on relevant testnets and all four platform builds maintained." and clears the evidence gates.
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
- Treasury analysis: Requested ADA: 1785333
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal commits to compatible Daedalus releases at least 2 weeks before every mainnet hard fork, with development builds on relevant testnets and all four platform builds maintained." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Proposal clears individual quality floors but is not currently portfolio-eligible: insufficient remaining NCL capacity after higher-ranked proposals.
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
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is asserted to be higher because privacy-conscious users are less likely to opt in.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `0bbdffb371848f2590bd28c5cfc6dafe3cce7d2dfc8c78c0f1e6480bbc5df3e7`
- snapshot_bundle_hash: `9d53b7073c18f39de7dc13df0ba6945c1531a4b7bdb70fcaf909774e7aec95da`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `a650e5f55d3662a45d71b3a19d5301fd64c2bbee`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5069, "NO": 0.3566, "YES": 0.1366}`

