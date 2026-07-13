# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.11` (raw `-0.11` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7475` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims describe a public-good infrastructure maintenance request with specific deliverables, milestones, budget categories, return-of-unspent-funds language, and oversight mechanisms, while several important adoption and track-record claims remain proposer-asserted within the document. The deterministic assessment is already ready, and the evidence mix does not justify an additional directional nudge beyond the engine's captured treasury and evidence analysis.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work.

The proposal requests 1,785,333 ADA for Se7en Labs to maintain and improve Daedalus during the 2026-2027 contract year, administered through Intersect with project-specific smart contract disbursement controls. The scope includes protocol maintenance, node and wallet backend updates, hard fork readiness, dependency and platform support, release engineering, signed releases, hardware wallet support for Keystone and Flex, a CIP-30 dApp connector, user-facing CIP work, Japanese localisation, user support, and an architecture assessment by Q3 2027.

Several important commitments were supported in the proposal: Daedalus releases at least two weeks before every mainnet hard fork, keeping cardano-node no more than two major versions behind mainnet recommended, public Apache 2.0 outputs, a detailed budget, return of some unspent funds, and Intersect milestone and disbursement oversight. But some material claims still lacked independent evidence, including that Daedalus is Cardano’s only full-node desktop wallet and that it has about 4,000 monthly active users with a meaningfully higher true count.

The review gates found the anchor document available and replayable, but treasury actions require a higher bar because they spend shared ADA and set precedent. The vote could be unblocked by independently pinned public-chain evidence for the relevant Net Change Limit, plus stronger replayable evidence for the unsupported material claims, a clearer sustainability path and cost-benefit case, and more assurance around remedies if execution or governance risks materialize.

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
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027 delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc. via Intersect administration and project-specific smart contract disbursement controls
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including node upgrades, wallet backend updates, hard fork readiness, dependency maintenance, platform support, release engineering, and signed releases, Ecosystem expansion including Keystone and Flex hardware wallet support, CIP-30 dApp connector, user-facing CIP implementations, and Japanese localisation, User support across GitHub, community forums, direct channels, and Japanese-language support, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: contract year 2026-2027; specific milestone dates include architecture assessment by Q3 2027 and ongoing maintenance/user support for 52 weeks
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, medium materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be meaningfully higher.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs has maintained Daedalus under an IOG contract since January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to a compatible Daedalus release at least two weeks before every mainnet hard fork and to keeping cardano-node no more than two major versions behind mainnet recommended at any time.
- finding: Claim (technical, supported_in_proposal, medium materiality): The scope includes adding Keystone and Flex hardware wallet support and implementing a CIP-30 dApp connector within Daedalus during the contract period.
- finding: Claim (governance, supported_in_proposal, high materiality): All funded outputs are described as public assets under the Apache 2.0 license, including source code, build tooling, documentation, and release artifacts.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be meaningfully higher.
- missing: Independent evidence for: Se7en Labs has maintained Daedalus under an IOG contract since January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization.
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
- finding: Strongest YES: the proposal substantiates "The proposal commits to a compatible Daedalus release at least two weeks before every mainnet hard fork and to keeping cardano-node no more than two major versions behind mainnet recommended at any time." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal commits to a compatible Daedalus release at least two weeks before every mainnet hard fork and to keeping cardano-node no more than two major versions behind mainnet recommended at any time." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be meaningfully higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `6a0ab7d5c5552cdb16b146916b589920a11521ecdb402e572d5691ff626793eb`
- snapshot_bundle_hash: `6754223ba75164a4d6a75cc75923fbd9ab8fd005e9dbf0410872d9cd931892bc`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4d394ccfc21657ebcbf2e1dbb3e210682b5ea383`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5069, "NO": 0.3566, "YES": 0.1366}`

