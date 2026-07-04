# Rationale: gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j
Recommendation: **NO**
Score: `-0.2933` (raw `-0.2833` + doctrine-LLM nudge `-0.01`) | Confidence: `0.7933` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is comparatively detailed and aligned with public-benefit infrastructure maintenance, but the large time-and-materials labor request and cost-efficiency assertions are not strongly evidenced in the supplied claims, so treasury stewardship and evidence quality justify only a small cautionary nudge.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury request asks for a large time-and-materials withdrawal, but the supplied evidence did not strongly establish cost-benefit clarity or independently support some material claims behind the case for funding.

The proposal requested 1,785,333 ADA for Se7en Labs, Inc. to maintain and improve Daedalus during 2026-2027, with Intersect administering funds and verifying milestones. The proposed work includes hard fork readiness, node upgrades, platform support, release engineering, hardware wallet support, CIP-30 dApp connector work, Japanese localisation and support, public support channels, an architecture assessment by Q3 2027, audit costs, and test hardware. The proposer also committed to returning unspent labor, hardware, and audit budget to the treasury.

Several parts of the proposal were well-supported in the review. The anchor document was available and replayable. The request amount and budget lines were stated clearly. The proposal supported commitments around Daedalus compatibility before hard forks, Intersect administration, milestone-based monthly disbursement, and public/forkable outputs. The review also recognized the strongest YES case: Daedalus is open-source under Apache License 2.0, and the funded outputs were presented as public assets.

The NO came from treasury stewardship and evidence quality. Treasury withdrawals require a higher bar because they spend shared ADA and set precedent. The review found thin claims-and-evidence support, missing independent evidence for the “only full-node desktop wallet” claim and the user-count claim, no clear sustainability path, weak cost-benefit clarity, missing independent assurance, and no rollback or remedy path. Execution risk was medium, and the treasury flow signal was in an unsustainable regime, so BEACN treated the proposal as insufficiently evidenced for a directional YES.

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
- finding: Requested: Treasury withdrawal to fund Daedalus Wallet Maintenance and Improvements 2026-2027 as a time and materials engagement.
- finding: Recipient: Se7en Labs, Inc., with administration and milestone verification by Intersect as described in the document
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including node upgrades, hard fork readiness, platform support, release engineering, and security/dependency maintenance, Compatible Daedalus release at least 2 weeks before every mainnet hard fork, Keystone and Flex hardware wallet support, plus newer hardware wallet models as they emerge during the contract period, CIP-30 dApp connector implementation in Daedalus with user documentation and dApp interoperability, Japanese localisation and Japanese-language user support throughout the contract period, Responsive user support via GitHub, community forums, and direct channels, Public architecture assessment by Q3 2027, Financial audit and test hardware acquisition, with unspent labor, hardware, and audit budget returned to the treasury
- finding: Deadline/expiry: Contract year 2026-2027; ongoing maintenance and user support for 52 weeks; architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is described as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, independently_verifiable, high materiality): Daedalus is open-source under the Apache License 2.0, and the proposer says all funded outputs will be public assets that remain forkable by anyone.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states that opt-in telemetry shows approximately 4,000 monthly active Daedalus users, while asserting the true count is meaningfully higher because privacy-conscious users are less likely to opt in.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs says it assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization.
- finding: Claim (technical, independently_verifiable, high materiality): The team claims it shipped Daedalus 8.0 and 11.0 during the IOG contract period and that Daedalus 11.0 was the first wallet capable of crossing the node 11.0 hard fork.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to maintaining Daedalus compatibility with upcoming hard forks, with testnet verification and a stable compatible release at least 2 weeks before each mainnet activation.
- missing: Independent evidence for: Daedalus is described as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: The proposal states that opt-in telemetry shows approximately 4,000 monthly active Daedalus users, while asserting the true count is meaningfully higher because privacy-conscious users are less likely to opt in.
- missing: Independent evidence for: Se7en Labs says it assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization.
- missing: Independent evidence for: The document claims Se7en Labs has not received ADA from the Cardano Treasury within the last 24 months and has instead operated under a direct IOG contract for Daedalus maintenance since January 2026, closing August 31, 2026.
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
- finding: Strongest YES: the proposal substantiates "Daedalus is open-source under the Apache License 2.0, and the proposer says all funded outputs will be public assets that remain forkable by anyone." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is described as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Daedalus is open-source under the Apache License 2.0, and the proposer says all funded outputs will be public assets that remain forkable by anyone." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.010 (clamped to ±0.05): The proposal is comparatively detailed and aligned with public-benefit infrastructure maintenance, but the large time-and-materials labor request and cost-efficiency assertions are not strongly evidenced in the supplied claims, so treasury stewardship and evidence quality justify only a small cautionary nudge.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Daedalus is described as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: The proposal states that opt-in telemetry shows approximately 4,000 monthly active Daedalus users, while asserting the true count is meaningfully higher because privacy-conscious users are less likely to opt in.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `66bcf353a113aa373f26ddf3dd95bbf5d2cd14714e9ceb401fd19c025cbc3a0e`
- snapshot_bundle_hash: `41ec2d22bbd13ac28c9f52704589563d230afc464be731862140c96284d36c2a`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2003, "NO": 0.7543, "YES": 0.0454}`

