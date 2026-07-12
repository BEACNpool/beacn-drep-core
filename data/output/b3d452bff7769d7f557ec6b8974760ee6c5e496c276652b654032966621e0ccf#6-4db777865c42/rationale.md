# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#6
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.0` | Readiness: `0`


## Plain-language explanation (deterministic-template)
BEACN's autonomous DRep recorded ABSTAIN on "Withdraw 1,162,746 ada for MLabs Core Tool Maintenance & Enhancement: Plutarc..." (TreasuryWithdrawals). This is a conservative, evidence-based hold rather than opposition. The action requests 1.16M ADA from the treasury. A key material claim lacks independent support: "MLabs says Plutarch and Ply have been extensively used across the Cardano ecosystem and reports an internal audit count of at least 26 teams building with them.". Open questions before a directional vote: freshness gate failed. Reason code: STALE_DATA. (Plain-language summary generated deterministically; a model-written explanation appears here when the reasoning layer is enabled.)

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
- finding: Requested: Annual treasury funding for MLabs Core Tool Maintenance & Enhancement for Plutarch and Ply, including maintenance, compatibility, bug fixes, optimizations, documentation, examples, technical blog posts, and developer-experience improvements.
- finding: Recipient: Intersect treasury reserve smart contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor MLabs.
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience, Critical breakages and serious vulnerabilities, Protocol-era and hard-fork compatibility, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, proposer_asserted, high materiality): MLabs says Plutarch and Ply have been extensively used across the Cardano ecosystem and reports an internal audit count of at least 26 teams building with them.
- finding: Claim (adoption, proposer_asserted, medium materiality): The rationale separately says MLabs conservatively counted at least 15 teams building with Plutarch and Ply.
- finding: Claim (technical, independently_verifiable, high materiality): MLabs’ public cross-language benchmarks are cited as showing Plutarch scripts ranking among the smallest in the benchmark suite with comparatively low on-chain compute and memory.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that if Plutarch and Ply fall behind ledger and Plutus/UPLC evolution, existing adopters may face more friction, migration risk, bespoke workarounds, or avoidable rewrites.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission under the approved Budget Process Framework.
- missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used across the Cardano ecosystem and reports an internal audit count of at least 26 teams building with them.
- missing: Independent evidence for: The rationale separately says MLabs conservatively counted at least 15 teams building with Plutarch and Ply.
- missing: Independent evidence for: The proposal states that if Plutarch and Ply fall behind ledger and Plutus/UPLC evolution, existing adopters may face more friction, migration risk, bespoke workarounds, or avoidable rewrites.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.64
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
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
- finding: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "MLabs says Plutarch and Ply have been extensively used across the Cardano ecosystem and reports an internal audit count of at least 26 teams building with them." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: freshness gate failed
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Data freshness check failed: data is 91636s old, max allowed is 21600s
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce reliable recommendation with stale data.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- All scoring suspended until fresh data is available.
- Claims and evidence missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used across the Cardano ecosystem and reports an internal audit count of at least 26 teams building with them.
- Claims and evidence missing: Independent evidence for: The rationale separately says MLabs conservatively counted at least 15 teams building with Plutarch and Ply.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: freshness gate failed
- Synthesis status is blocked.

## Reproducibility
- input_hash: `4db777865c42f57643f57d1985968230b285c6fad5114287f9efc4430e44821a`
- snapshot_bundle_hash: `3094fae4e4ff954aaf5456d7ca1412bf66e409bc7ee21fdf3eae91515ed7980b`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `eec0908e48c56be13e86e06ac5d9440d0cac813a`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `91636`
- uncertainty_band: `LOW`
- evidence_depth_score: `2`
- decision_probs: `{"ABSTAIN": 0.32, "NO": 0.34, "YES": 0.34}`

- **DATA STALE**: age exceeded threshold

