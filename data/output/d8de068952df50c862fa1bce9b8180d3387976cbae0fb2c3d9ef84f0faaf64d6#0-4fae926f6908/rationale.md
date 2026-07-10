# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline evidence for a treasury withdrawal, especially the missing `treasury_amount_lovelace` field. This is a conservative, evidence-based hold: BEACN could not make a responsible directional recommendation while a core treasury field needed to verify the withdrawal was absent.

The proposal requested 1,785,333 ADA for Daedalus Wallet maintenance and improvements in 2026-2027, delivered by Se7en Labs, Inc. and administered by Intersect. The stated work includes hard fork readiness, compatible releases at least two weeks before each mainnet hard fork, Keystone and Flex hardware wallet support, a CIP-30 dApp connector, Japanese localisation, user support, an architecture assessment, test hardware, and an independent financial audit.

Some claims were supported in the proposal, including that Se7en Labs took responsibility for Daedalus under an IOG contract in January 2026 and has already shipped listed maintenance work, and that Intersect would administer and verify milestones. But other material claims remained unsupported by independent evidence, including that Daedalus is Cardano’s only full-node desktop wallet and that it has about 4,000 monthly active users from opt-in telemetry. The treasury review also lacked a sustainability path and cost-benefit clarity, while the risk review lacked independent assurance and a rollback or remedy path.

The vote could be unblocked by providing the missing treasury withdrawal amount field and stronger replayable evidence for the unsupported material claims, along with clearer treasury and risk evidence. Until then, BEACN’s ABSTAIN means the proposal may have credible parts, but the review record was not complete enough for a YES or NO vote.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Daedalus Wallet maintenance and improvements for 2026-2027 delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc., with administration by Intersect
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including node upgrades, hard fork readiness, and compatible releases at least 2 weeks before each mainnet hard fork, Ecosystem expansion including Keystone and Flex hardware wallet support, CIP-30 dApp connector, and Japanese localisation, Responsive user support including dedicated attention to the Japanese community, Architecture assessment covering current state, options, resource estimates, and recommendation, Independent financial audit and test hardware acquisition/maintenance
- finding: Deadline/expiry: Contract year through 2026-2027; architecture assessment by Q3 2027; IOG contract closes August 31, 2026
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, medium materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is claimed to be higher.
- finding: Claim (technical, supported_in_proposal, high materiality): Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend work, Apple Silicon builds, the drt release CLI, and Nix build modernization.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to compatible Daedalus stable releases at least 2 weeks before every mainnet hard fork during the contract period.
- finding: Claim (technical, supported_in_proposal, high materiality): The scope includes Keystone and Flex hardware wallet support, a CIP-30 dApp connector, full Japanese translation, ongoing user support, and an architecture assessment.
- finding: Claim (technical, independently_verifiable, medium materiality): All release-timing and version-currency metrics are stated to be independently verifiable from public GitHub repositories and the Cardano mainnet chain.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is claimed to be higher.
- missing: Independent evidence for: Se7en Labs says it does not monetize Daedalus usage and that all funded outputs will be public assets under the Apache 2.0 license.
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
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend work, Apple Silicon builds, the drt release CLI, and Nix build modernization." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: evidence is too thin for a directional vote while 1 blocker(s) remain open.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend work, Apple Silicon builds, the drt release CLI, and Nix build modernization." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, while the true count is claimed to be higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `4fae926f69089b9b3d7197d8520e567f710813eef16fa22f19f1879c1c245ce0`
- snapshot_bundle_hash: `608134a2e6eef98807e331572fcd8076f9235712b1b9d6a25ca09ba2276016da`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

