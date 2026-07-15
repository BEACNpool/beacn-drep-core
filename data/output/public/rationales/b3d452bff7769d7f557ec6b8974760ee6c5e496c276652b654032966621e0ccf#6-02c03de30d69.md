# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#6
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.33` (raw `-0.33` + doctrine-LLM nudge `+0.0`) | Confidence: `0.8025` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit infrastructure value and some independently checkable governance, benchmark, NCL, and smart-contract administration evidence, while important adoption and non-funding impact claims remain largely proposer-asserted and the document contains an inconsistency between 26 and 15 counted teams. The deterministic assessment is already ready, so no additional score nudge is justified beyond the engine's checks.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal needs independent public verification of the applicable Net Change Limit before a directional vote is justified. This is a conservative, evidence-based hold, not a rejection of the work itself.

The action requests 1,162,746 ada for annual maintenance and enhancement of MLabs Plutarch and Ply, administered through the 2026 Treasury Reserve Smart Contract stake address by Intersect for MLabs. The proposal covers maintenance, compatibility work, bug fixes, optimizations, documentation, examples, technical blog posts, and developer-experience improvements. The proposal’s technical description of Plutarch and Ply was well supported, and the anchor document was available, pinned, and replayable. It also states that the withdrawal did not breach the 350M Net Change Limit for Epoch 613 to Epoch 713 at submission, and that funds would be managed through Intersect using Sundae Labs treasury-management smart contracts with oversight and milestone-based controls.

The review found that several important claims were still thin or unsupported by independent evidence. In particular, the claimed ecosystem adoption numbers for Plutarch and Ply were proposer-asserted rather than independently evidenced, and the claimed need for continued maintenance across ledger, Plutus, UPLC, tooling, and possible Dijkstra-era changes also lacked independent support. The treasury review also flagged missing sustainability path and cost-benefit clarity, while the risk review lacked independent assurance and a rollback or remedy path.

The evidence that would unblock a directional vote is a pinned, independently verifiable Net Change Limit check from public chain evidence, plus stronger replayable evidence for the material adoption and maintenance-need claims. Until that is available, BEACN’s position is to hold rather than overstate confidence on a treasury withdrawal that consumes shared ada and sets precedent.

## Review Tree
- overall_status: `incomplete`

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
- finding: Deep research dossier: complete
- finding: Requested: Annual funding for maintenance and enhancement of MLabs Plutarch and Ply, including maintenance, compatibility, bug fixes, optimizations, documentation, examples, technical blog posts, and developer-experience improvements.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect for the vendor MLabs
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience, Critical breakages and serious vulnerabilities, Protocol-era and hard-fork compatibility, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, proposer_asserted, high materiality): MLabs says Plutarch and Ply have been extensively used across the Cardano ecosystem, with an internal audit counting at least 26 teams in the motivation section and at least 15 teams in the rationale section.
- finding: Claim (technical, independently_verifiable, medium materiality): MLabs says Plutarch scripts rank among the smallest in its public cross-language benchmark suite while requiring comparatively low on-chain compute and memory.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says continued maintenance is needed to track Cardano ledger, Plutus, UPLC, tooling, and possible Dijkstra-era changes during the funding period.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says non-funding could increase friction, migration risk, uncertainty, bespoke workarounds, expensive smart contract stack migrations, or avoidable rewrites for existing adopters.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal claims alignment with Cardano 2030 Pillar 2 Adoption & Utility by supporting developer experience and core open-source smart contract tooling.
- missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used across the Cardano ecosystem, with an internal audit counting at least 26 teams in the motivation section and at least 15 teams in the rationale section.
- missing: Independent evidence for: The proposal says continued maintenance is needed to track Cardano ledger, Plutus, UPLC, tooling, and possible Dijkstra-era changes during the funding period.
- missing: Independent evidence for: The proposal says non-funding could increase friction, migration risk, uncertainty, bespoke workarounds, expensive smart contract stack migrations, or avoidable rewrites for existing adopters.
- missing: Independent evidence for: The proposal claims alignment with Cardano 2030 Pillar 2 Adoption & Utility by supporting developer experience and core open-source smart contract tooling.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1162746
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.58
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
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "MLabs says Plutarch and Ply have been extensively used across the Cardano ecosystem, with an internal audit counting at least 26 teams in the motivation section and at least 15 teams in the rationale section." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1162746
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Proposal clears individual quality floors but is not currently portfolio-eligible: insufficient remaining NCL capacity after higher-ranked proposals.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 30% of rolling available capacity.
- Claims and evidence missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used across the Cardano ecosystem, with an internal audit counting at least 26 teams in the motivation section and at least 15 teams in the rationale section.
- Claims and evidence missing: Independent evidence for: The proposal says continued maintenance is needed to track Cardano ledger, Plutus, UPLC, tooling, and possible Dijkstra-era changes during the funding period.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `02c03de30d6982dbd77e667469c5121cb9f9da1162315a8ac362e1eff0bfd8e5`
- snapshot_bundle_hash: `b62a3bc4e1aabf1dff97ddd64f8aa7d3ea70bdb3c4b93bd0feca6ec79d2eb543`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4566, "NO": 0.4996, "YES": 0.0438}`

