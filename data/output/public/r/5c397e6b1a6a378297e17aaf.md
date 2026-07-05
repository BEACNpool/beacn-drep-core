# Rationale: gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j
Recommendation: **NO**
Score: `-0.2833` (raw `-0.2833` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7908` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show a public-good maintenance proposal with concrete deliverables, milestones, budget categories, and some independently verifiable metrics, while several important adoption, track-record, and refund assertions remain proposer-stated within the document. The deterministic treasury and evidence gates appear to capture the main stewardship and verification concerns, so no additional discretionary nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not clear the higher evidence bar required for spending shared ADA, especially with a material technical claim left unsupported.

The proposal requested 1,785,333 ADA for Se7en Labs, Inc. to maintain and improve Daedalus Wallet through 2026-2027. The work included protocol and hard fork maintenance, wallet backend updates, hardware wallet support, a CIP-30 dApp connector, Japanese localisation, user support, security and dependency maintenance, signed releases, reproducible Nix builds, and an architecture assessment. The proposer also described Intersect as the administrator and independent milestone verifier, with monthly disbursements tied to verified work.

Several parts of the proposal were supported well enough to count in its favor. The review accepted that Se7en Labs said it took over Daedalus responsibility under an IOG contract in January 2026 and had shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization. The budget breakdown was also clear, and some release metrics were described as independently verifiable through public GitHub repositories and the Cardano mainnet chain.

The NO vote came from the unresolved weaknesses around evidence, treasury sustainability, and risk. The claim that Daedalus is Cardano’s only full-node desktop wallet, deriving wallet and governance data directly from the chain without third-party APIs or trusted backends, lacked independent evidence in the review. The claimed user numbers were also not independently evidenced, claims-and-evidence status was thin, and the treasury review was missing a sustainability path and cost-benefit clarity. Because this was a treasury withdrawal, BEACN applied elevated scrutiny and found that the unsupported material claim and missing treasury/risk assurances outweighed the supported parts of the proposal.

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
- finding: Recipient: Se7en Labs, Inc. via Intersect-administered treasury withdrawal and monthly disbursement controls
- finding: Stated amount: 1785333
- finding: Deliverables: Protocol maintenance including node upgrades, wallet backend updates, hard fork readiness, and compatible releases at least 2 weeks before each mainnet hard fork, Ecosystem expansion including Keystone and Flex hardware wallet support, CIP-30 dApp connector, and Japanese localisation, User support across GitHub, community forums, direct channels, and Japanese-language support, Security and dependency maintenance for Electron, Node.js, wallet-adjacent dependencies, reproducible Nix builds, and signed releases, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: contract year 2026-2027; ongoing maintenance and user support for 52 weeks; architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is described as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while asserting the true count is meaningfully higher because privacy-conscious users are less likely to opt in.
- finding: Claim (technical, supported_in_proposal, high materiality): Se7en Labs says it assumed Daedalus responsibility under an IOG contract in January 2026 and has shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization since then.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal claims the team shipped Daedalus 8.0 and 11.0 during the IOG contract period and that Daedalus 11.0 was the first wallet capable of crossing the node 11.0 hard fork.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested 1,785,333 ADA budget is allocated as 1,666,667 ADA for labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and 52,000 ADA for the Intersect administration fee.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer states any unspent labor, hardware, or audit budget at contract close will be returned to the treasury.
- missing: Independent evidence for: Daedalus is described as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: The proposal states Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while asserting the true count is meaningfully higher because privacy-conscious users are less likely to opt in.
- missing: Independent evidence for: The proposal claims the team shipped Daedalus 8.0 and 11.0 during the IOG contract period and that Daedalus 11.0 was the first wallet capable of crossing the node 11.0 hard fork.
- missing: Independent evidence for: The proposer states any unspent labor, hardware, or audit budget at contract close will be returned to the treasury.
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
- finding: Strongest YES: the proposal substantiates "Se7en Labs says it assumed Daedalus responsibility under an IOG contract in January 2026 and has shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization since then." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is described as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Se7en Labs says it assumed Daedalus responsibility under an IOG contract in January 2026 and has shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization since then." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- No additional inference.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Daedalus is described as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: The proposal states Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while asserting the true count is meaningfully higher because privacy-conscious users are less likely to opt in.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `6b678d2e032ccd0f53063d3ccfaa8f35a1c4d5e3d93c4738e7bc337ad21db461`
- snapshot_bundle_hash: `58e11ff08945ddd4345721bbd1fd64db799d7e321a69a1486144ecd4c419ca28`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2025, "NO": 0.7517, "YES": 0.0458}`

