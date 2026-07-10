# Rationale: gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7808` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a clearly scoped public-good maintenance proposal with concrete deliverables, success metrics, and some independently verifiable outputs, but many key factual assertions about usage, prior delivery, team track record, and cost necessity remain proposer-asserted within the document. The deterministic treasury and risk rules appear to have already captured the main spending, oversight, and evidence issues, so no additional bounded nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a Treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal requested 1,785,333 ADA for a time-and-materials engagement for Daedalus maintenance and improvements in 2026-2027, administered through Intersect for Se7en Labs. It covered protocol maintenance, releases before hard forks, Nix and dependency work, security patches, platform support, binary signing continuity, Japanese translation and support, Keystone and Flex hardware wallet support, CIP-30 support, user support, and a public architecture assessment by Q3 2027.

Several parts of the proposal were well structured. The budget was broken down into 1,666,667 ADA for team labor, 33,333 ADA for test hardware, 33,333 ADA for a financial audit, and a 52,000 ADA Intersect administration fee. The proposal also gave concrete success metrics, including signed releases, platform CI coverage, version-currency targets, hardware wallet support, CIP-30 support, Japanese support, and a public architecture assessment. Intersect administration, milestone verification, monthly disbursement against verified work, a dedicated auditable account, and external oversight were also described.

The hold is conservative and evidence-based. The proposal anchor was available and replayable, but the claims-and-evidence record was thin, with missing independent evidence for material claims such as Daedalus being Cardano’s only full-node desktop wallet and the roughly 4,000 monthly active user figure. Treasury review also lacked a clear sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path. The evidence that would unblock a directional vote is pinned, independently verifiable Net Change Limit evidence from public chain data, plus replayable public evidence for the material product and adoption claims.

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
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027 as a time-and-materials engagement covering protocol maintenance, ecosystem expansion, user support, and related oversight.
- finding: Recipient: Se7en Labs, Inc. administered through Intersect
- finding: Stated amount: 1,785,333
- finding: Deliverables: Integrate cardano-node and cardano-wallet releases and maintain Nix build infrastructure, dependency updates, security patches, and platform compatibility., Provide Daedalus-compatible stable releases at least 2 weeks before each mainnet hard fork and maintain Leios, Peras, and Nested Transactions readiness., Maintain binary signing continuity through the IOG signing arrangement for official releases., Maintain Windows, macOS x86_64, macOS aarch64, and Linux platform builds with full Japanese translation across new features., Add Keystone and Flex hardware wallet support and support newer hardware wallet models as they emerge., Implement a CIP-30 dApp connector in Daedalus with documentation and no external API dependency., Provide ongoing user support through GitHub, community forums, and direct channels, including Japanese-language support., Publish a Daedalus architecture assessment by Q3 2027.
- finding: Deadline/expiry: Contract year through 2026-2027; architecture assessment by Q3 2027; IOG contract noted as closing August 31, 2026.
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is presented as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from chain data without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states that opt-in telemetry shows approximately 4,000 monthly active Daedalus users, with true usage asserted to be higher because privacy-conscious users are less likely to opt in.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs says it has maintained Daedalus under an IOG contract since January 2026 and shipped Mithril snapshot bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal says Se7en Labs has not received ADA from the Cardano Treasury within the last 24 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested 1,785,333 ADA budget is allocated to 1,666,667 ADA for team labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal states that any unspent labor, hardware, or audit budget at contract close will be returned to the treasury.
- missing: Independent evidence for: Daedalus is presented as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from chain data without third-party APIs or trusted backends.
- missing: Independent evidence for: The proposal states that opt-in telemetry shows approximately 4,000 monthly active Daedalus users, with true usage asserted to be higher because privacy-conscious users are less likely to opt in.
- missing: Independent evidence for: Se7en Labs says it has maintained Daedalus under an IOG contract since January 2026 and shipped Mithril snapshot bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization.
- missing: Independent evidence for: The proposal says Se7en Labs has not received ADA from the Cardano Treasury within the last 24 months.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1785333
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
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
- finding: Strongest YES: the proposal substantiates "The requested 1,785,333 ADA budget is allocated to 1,666,667 ADA for team labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is presented as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from chain data without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The requested 1,785,333 ADA budget is allocated to 1,666,667 ADA for team labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Daedalus is presented as Cardano's only full-node desktop wallet, deriving wallet and governance data directly from chain data without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: The proposal states that opt-in telemetry shows approximately 4,000 monthly active Daedalus users, with true usage asserted to be higher because privacy-conscious users are less likely to opt in.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `3f6bf165bef09c0437ec8ba119e6b340c47839e11f08c1f31bc1322d93a74bcf`
- snapshot_bundle_hash: `a3991afcb68e10fb7ac91e4b2031f30189ee4d72fd1fc4662907d6b1719a6457`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

