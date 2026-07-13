# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.11` (raw `-0.11` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7475` | Readiness: `0.85`
> Reasoning layer (precomputed): The supplied claims show a public-good infrastructure maintenance proposal with concrete deliverables, verifiable release metrics, budget categories, and oversight mechanisms, while several important adoption and track-record assertions remain proposer-stated rather than evidenced inside the anchor. Because the deterministic assessment is already ready and the doctrine's hard gates and treasury analysis have been applied, the evidence mix does not justify an additional directional nudge beyond the mechanical score.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not support or opposition to the proposal.

The action asks for 1,785,333 ADA to fund Daedalus Wallet maintenance and improvements for 2026-2027 by Se7en Labs, with Intersect administering and disbursing funds. The proposal describes work including node and wallet backend maintenance, hard fork readiness, signed multi-platform releases, hardware wallet support, CIP-30 dApp connector work, user support, Japanese translation, a public architecture assessment, an independent financial audit, and test hardware.

Several parts of the proposal were supported in the review. The budget breakdown was stated, including labor, test hardware, audit, and Intersect administration costs. The proposal also states that unspent labor, hardware, or audit funds would be returned to the treasury, and that Intersect would verify milestones and disburse monthly against verified work. Some technical claims were also well-supported, including the statement that Daedalus private keys are generated and stored on the user’s device and not transmitted externally, with open-source Apache 2.0 code enabling auditability.

The hold remains because key evidence was still thin or missing. The review lacked independent evidence for the claim that Daedalus is Cardano’s only full-node desktop wallet and for the telemetry-based user-count claim. Treasury analysis was missing a sustainability path and clearer cost-benefit case, while risk review was missing independent assurance and a rollback or remedy path. The specific evidence that would unblock a directional vote is the pinned, independently verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the material claims and the missing treasury and risk details.

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
- finding: Requested: Treasury withdrawal to fund Daedalus Wallet maintenance and improvements for 2026-2027 delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc., with administration and disbursement through Intersect as described in the document
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including node upgrades, wallet backend updates, hard fork readiness, platform support, release engineering, CI maintenance, and security/dependency maintenance, Compatible stable Daedalus releases at least 2 weeks before each mainnet hard fork, Leios, Peras, and Nested Transactions readiness as those protocols progress toward testnet or mainnet, Keystone and Flex hardware wallet support, plus additional newer hardware wallet models as they emerge during the contract period, CIP-30 dApp connector implementation within Daedalus with documentation and interoperability verification, Ongoing user support through GitHub, community forums, and direct channels, including Japanese-language support, Full Japanese translation maintained across all new features during the contract year, Architecture assessment published publicly with recommendation and rationale, Independent financial audit of funds received and expended, Test hardware acquisition and maintenance for real-device release verification
- finding: Deadline/expiry: Contract year through 2026-2027; specific milestones list durations of 6, 8, 12, 20, 26, and 52 weeks, with architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is presented as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from chain without third-party APIs or trusted backends.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal states that Daedalus private keys are generated and stored on the user's device and never transmitted to any external service, with open-source Apache 2.0 code enabling auditability.
- finding: Claim (adoption, proposer_asserted, medium materiality): The document says opt-in telemetry shows approximately 4,000 monthly active Daedalus users and asserts the true count is meaningfully higher because privacy-conscious full-node users are less likely to opt in.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs states it assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, Nix modernization, and Daedalus 8.0 and 11.0.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal claims Daedalus 11.0 was the first wallet capable of crossing the node 11.0 hard fork.
- finding: Claim (technical, independently_verifiable, high materiality): The scope commits to maintaining Windows, macOS x86_64, macOS aarch64, and Linux builds, keeping releases cryptographically signed through an IOG signing arrangement, and keeping official releases independently verifiable through public repositories and the Cardano mainnet chain.
- missing: Independent evidence for: Daedalus is presented as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from chain without third-party APIs or trusted backends.
- missing: Independent evidence for: The document says opt-in telemetry shows approximately 4,000 monthly active Daedalus users and asserts the true count is meaningfully higher because privacy-conscious full-node users are less likely to opt in.
- missing: Independent evidence for: Se7en Labs states it assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, Nix modernization, and Daedalus 8.0 and 11.0.
- missing: Independent evidence for: The proposal claims Daedalus 11.0 was the first wallet capable of crossing the node 11.0 hard fork.
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
- finding: Strongest YES: the proposal substantiates "The proposal states that Daedalus private keys are generated and stored on the user's device and never transmitted to any external service, with open-source Apache 2.0 code enabling auditability." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is presented as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal states that Daedalus private keys are generated and stored on the user's device and never transmitted to any external service, with open-source Apache 2.0 code enabling auditability." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: Daedalus is presented as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: The document says opt-in telemetry shows approximately 4,000 monthly active Daedalus users and asserts the true count is meaningfully higher because privacy-conscious full-node users are less likely to opt in.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `018187643693713f1c656f95fadd6506b45229458aeacad65cdcee8e069f9e90`
- snapshot_bundle_hash: `fe12b6aea642dee761538ac61006c17a10e21ac420a93e81a1f2d6c393f8711c`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5069, "NO": 0.3566, "YES": 0.1366}`

