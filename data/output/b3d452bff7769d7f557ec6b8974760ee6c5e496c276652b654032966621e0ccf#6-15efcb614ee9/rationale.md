# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#6
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a high-impact treasury withdrawal and the required deep-research dossier was not complete enough to support a directional vote. This is a conservative, evidence-based hold, not a rejection of the work.

The action requested 1,162,746 ada for MLabs Core Tool Maintenance & Enhancement for Plutarch and Ply, administered through the 2026 Treasury Reserve Smart Contract stake address by Intersect for the vendor. The proposal says the funds would cover annual maintenance, compatibility, developer experience, critical breakages, vulnerabilities, protocol-era and hard-fork compatibility, bug fixes, optimizations, documentation, examples, and technical writing. No deadline was stated in the document.

Some claims were supported or independently verifiable. The review found support for the technical description of Plutarch and Ply, the requested amount and Intersect administration fee, the Hydra Voting threshold result, the stated Net Change Limit status, and the planned Intersect/Sundae Labs treasury management controls. But several important claims remained thin or unsupported, including independent evidence for the claimed number of teams using Plutarch and Ply, evidence around the proposed funding period and compatibility work, a line-item budget, a sustainability path, independent assurance, a dependency map, feasibility assessment, alternatives analysis, and failure-mode analysis.

Because treasury votes consume shared ada and set precedent, BEACN requires a higher evidence bar. A directional vote would be unblocked by a completed deep-research dossier that includes the missing feasibility, alternatives, and failure-mode analysis, plus stronger public evidence for adoption, budget detail, sustainability, dependencies, and independent assurance.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.16M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund MLabs Core Tool Maintenance & Enhancement for Plutarch and Ply annual maintenance and enhancement.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect for the vendor.
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience, Critical breakages and serious vulnerabilities, Protocol-era and hard-fork compatibility, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts through controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, proposer_asserted, high materiality): MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale later states a conservative count of at least 15 teams.
- finding: Claim (technical, independently_verifiable, medium materiality): MLabs' public cross-language benchmarks show Plutarch scripts rank among the smallest in the benchmark suite while requiring comparatively low on-chain compute and memory.
- finding: Claim (technical, proposer_asserted, high materiality): The proposed funding period is intended to cover ongoing Cardano ledger, Plutus, and tooling evolution, including protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal claims continued maintenance will reduce friction, migration risk, uncertainty, bespoke workarounds, and avoidable rewrites for teams maintaining production systems.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal claims alignment with Cardano 2030 Pillar 2, specifically Adoption & Utility and A.3 Developer Experience for open-source SDKs, frameworks, and infrastructure.
- missing: Independent evidence for: MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale later states a conservative count of at least 15 teams.
- missing: Independent evidence for: The proposed funding period is intended to cover ongoing Cardano ledger, Plutus, and tooling evolution, including protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land.
- missing: Independent evidence for: The proposal claims continued maintenance will reduce friction, migration risk, uncertainty, bespoke workarounds, and avoidable rewrites for teams maintaining production systems.
- missing: Independent evidence for: The proposal claims alignment with Cardano 2030 Pillar 2, specifically Adoption & Utility and A.3 Developer Experience for open-source SDKs, frameworks, and infrastructure.
- missing: feasibility assessment
- missing: alternatives analysis
- missing: failure-mode analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1162746
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: not confirmed
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.60
- missing: line-item budget
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: low
- finding: Treasury exposure risk: low
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts through controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." though 3 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale later states a conservative count of at least 15 teams." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing feasibility assessment
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1162746
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts through controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." though 3 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional voting is blocked until dossier quality gates pass.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Dossier completeness not confirmed for this treasury proposal.
- Claims and evidence missing: Independent evidence for: MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale later states a conservative count of at least 15 teams.
- Claims and evidence missing: Independent evidence for: The proposed funding period is intended to cover ongoing Cardano ledger, Plutus, and tooling evolution, including protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing feasibility assessment
- Synthesis missing: missing alternatives analysis
- Synthesis status is blocked.

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.
- Missing dossier section: feasibility assessment
- Missing dossier section: alternatives analysis
- Missing dossier section: failure-mode analysis

## Reproducibility
- input_hash: `15efcb614ee917db842be2d7f8bda5d27cce8eaea99b219eedada4b12b6fe0a5`
- snapshot_bundle_hash: `77698411ccbd7e62a4f0c23b8daf23010cd6c8aea948adf296c43be67e6ab3eb`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

