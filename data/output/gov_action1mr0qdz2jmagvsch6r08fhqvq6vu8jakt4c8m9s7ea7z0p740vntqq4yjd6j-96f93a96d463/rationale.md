# Rationale: gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.52` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal contains substantial scope, milestones, risk register, oversight descriptions, and some independently verifiable metrics, but the deterministic assessment identifies missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis for a large treasury withdrawal. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a cautious negative nudge rather than rewarding plausible public-good value that remains incompletely analyzed.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal, and the evidence dossier did not clear the higher bar required for spending shared ADA. The review found seven open blockers, including missing budget, feasibility, risk, alternatives, failure-mode, community impact, and complete proposal summary analysis.

The proposal requested 1,785,333 ADA for Se7en Labs to maintain and improve Daedalus through 2026-2027, with Intersect proposed to administer funds and verify milestones. The requested work included hard fork compatibility, 52 weeks of node and wallet backend maintenance, signed releases, Japanese localisation, Leios and Peras readiness work, hardware wallet support, a CIP-30 dApp connector, user support, and a public architecture assessment.

Some claims were supported in the proposal. The proposal stated that Daedalus private keys are generated and stored on the user’s device, are never transmitted to an external service, and that the source code is auditable under Apache License 2.0. The budget total and top-level categories were also stated, and Intersect oversight with monthly disbursement against verified work was described. But several important claims remained unsupported or thinly evidenced, including the claim that Daedalus is Cardano’s only full-node desktop wallet and the claim that telemetry shows about 4,000 monthly active users, with higher true usage.

The pinned anchor was available and the action could be reviewed, but the treasury analysis was incomplete, the claims-and-evidence review was thin, the risk review lacked mitigation evidence and independent assurance, and synthesis was blocked. Because treasury actions require elevated scrutiny, BEACN treated the incomplete diligence record and unsustainable treasury-flow signal as decisive. The result was a conservative NO: not a rejection of Daedalus as a public good, but a finding that this withdrawal was not sufficiently evidenced for approval.

## Review Tree
- overall_status: `blocked`

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027, including protocol maintenance, ecosystem expansion, user support, hardware wallet support, CIP-30 dApp connector, Japanese localisation, and architecture assessment.
- finding: Recipient: Se7en Labs, Inc., with administration and milestone verification by Intersect.
- finding: Stated amount: 1,785,333
- finding: Deliverables: Hard fork compatibility changes, testnet development builds, and stable releases at least 2 weeks before mainnet hard forks, 52 weeks of node and wallet backend maintenance, signed releases, Japanese translation coverage, and CI across platform targets, Leios and Peras readiness with compatible node versions and UX impact assessment, Keystone and Flex hardware wallet support, plus additional newer models as they emerge, CIP-30 dApp connector implementation, interoperability verification, and user documentation, Ongoing user support through GitHub, community forums, direct channels, and Japanese-language support, Public architecture assessment with recommendation and rationale
- finding: Deadline/expiry: Contract year through 2026-2027; architecture assessment by Q3 2027; IOG contract stated as closing August 31, 2026.
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is described as Cardano's only full-node desktop wallet that runs an embedded Cardano node and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal states Daedalus private keys are generated and stored on the user's device and never transmitted to an external service, with source code auditability under Apache License 2.0.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer states opt-in telemetry shows approximately 4,000 monthly active Daedalus users and that the true count is meaningfully higher because privacy-conscious full-node users are less likely to opt in.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs states it assumed responsibility for Daedalus under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, native Apple Silicon builds, the drt release CLI, and Nix build modernization.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says Se7en Labs shipped Daedalus 8.0 and 11.0 within the IOG contract period and that Daedalus 11.0 was the first wallet capable of crossing the node 11.0 hard fork.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget totals 1,785,333 ADA, composed of 1,666,667 ADA for labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee.
- missing: Independent evidence for: Daedalus is described as Cardano's only full-node desktop wallet that runs an embedded Cardano node and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: The proposer states opt-in telemetry shows approximately 4,000 monthly active Daedalus users and that the true count is meaningfully higher because privacy-conscious full-node users are less likely to opt in.
- missing: Independent evidence for: Se7en Labs states it assumed responsibility for Daedalus under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, native Apple Silicon builds, the drt release CLI, and Nix build modernization.
- missing: Independent evidence for: The proposal says Se7en Labs shipped Daedalus 8.0 and 11.0 within the IOG contract period and that Daedalus 11.0 was the first wallet capable of crossing the node 11.0 hard fork.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1.79M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal states Daedalus private keys are generated and stored on the user's device and never transmitted to an external service, with source code auditability under Apache License 2.0." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is described as Cardano's only full-node desktop wallet that runs an embedded Cardano node and derives wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1.79M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal states Daedalus private keys are generated and stored on the user's device and never transmitted to an external service, with source code auditability under Apache License 2.0." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal contains substantial scope, milestones, risk register, oversight descriptions, and some independently verifiable metrics, but the deterministic assessment identifies missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis for a large treasury withdrawal. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a cautious negative nudge rather than rewarding plausible public-good value that remains incompletely analyzed.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Daedalus is described as Cardano's only full-node desktop wallet that runs an embedded Cardano node and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: The proposer states opt-in telemetry shows approximately 4,000 monthly active Daedalus users and that the true count is meaningfully higher because privacy-conscious full-node users are less likely to opt in.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `96f93a96d463aea371ecb884be1cd4be17b41176bd2c8c4696cbbca93dab1467`
- snapshot_bundle_hash: `3ecc9b4e326b0d9f0c4d73bb74400434fe597ed0ea5e31fefb0c7267b569e43b`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1217`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2146, "NO": 0.7433, "YES": 0.0421}`

