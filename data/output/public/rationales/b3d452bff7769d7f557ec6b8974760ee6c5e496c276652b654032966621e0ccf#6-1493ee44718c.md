# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#6
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was missing baseline evidence required for a responsible treasury vote, especially the required `treasury_amount_lovelace` field for a treasury withdrawal. This is a conservative, evidence-based hold, not a judgment that the work is bad or that the proposal should fail.

The action requested 1,162,746 ada for MLabs Core Tool Maintenance & Enhancement for Plutarch and Ply, submitted by Intersect on behalf of MLabs, with funds going to the 2026 Treasury Reserve Smart Contract stake address. The proposal said this included 1,128,880 ada for maintenance, compatibility, and developer experience work, plus a 33,866 ada Intersect administration fee. It described work on Plutarch and Ply maintenance, serious breakages and vulnerabilities, protocol-era and hard-fork compatibility, bug fixes, optimizations, documentation, examples, and developer experience improvements. No deadline was stated in the document.

Some claims were supported in the proposal or independently verifiable: the requested amount, the on-chain withdrawal value, the basic descriptions of Plutarch and Ply, the Intersect budget-process support threshold, the Net Change Limit claim, oversight and milestone controls, and prior funding disclosures. Other claims were not strong enough for a confident directional vote. The review found unsupported adoption evidence because the document gave inconsistent counts of at least 26 teams in one place and at least 15 teams in another, and it lacked independent evidence for future compatibility work around ledger, Plutus, tooling evolution, and possible Dijkstra-era changes.

The gates did not clear. Intake was blocked, claims and evidence were thin, treasury analysis was incomplete, risk review had unknown execution risk, and synthesis was blocked. A YES case exists because the proposal substantiates the requested amount and fee structure, but the review still had an open blocker. A NO case exists because a material adoption claim was unsupported. To unblock a directional vote, BEACN would need the missing treasury withdrawal baseline field, a complete line-item budget, clear milestone-gated disbursement evidence, independent assurance, a rollback or remedy path, and independent evidence for the unsupported adoption and future-compatibility claims.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal for MLabs Core Tool Maintenance & Enhancement for Plutarch and Ply.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor MLabs
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1: Plutarch and Ply maintenance, compatibility, and developer experience, Critical breakages and serious vulnerabilities, Protocol-era and hard-fork compatibility, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements, Intersect budget administration
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,162,746 ADA, consisting of 1,128,880 ADA for Plutarch and Ply maintenance, compatibility, and developer experience plus a 33,866 ADA Intersect administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The on-chain treasury withdrawal reward value is 1,162,746,000,000 lovelace to the 2026 Treasury Reserve Smart Contract stake address.
- finding: Claim (technical, supported_in_proposal, medium materiality): Plutarch is described as a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply is described as helping serialize Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, unsupported, high materiality): MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, but the document gives inconsistent internal audit counts of at least 26 teams in the motivation and at least 15 teams in the rationale.
- finding: Claim (technical, independently_verifiable, medium materiality): The proposer claims Plutarch scripts rank among the smallest in MLabs' public cross-language benchmark suite while requiring comparatively low on-chain compute and memory.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says the next funding period is expected to cover Cardano ledger, Plutus, tooling evolution, and protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land during the funding period.
- missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, but the document gives inconsistent internal audit counts of at least 26 teams in the motivation and at least 15 teams in the rationale.
- missing: Independent evidence for: The proposal says the next funding period is expected to cover Cardano ledger, Plutus, tooling evolution, and protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land during the funding period.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,162,746 ADA, consisting of 1,128,880 ADA for Plutarch and Ply maintenance, compatibility, and developer experience plus a 33,866 ADA Intersect administration fee." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, but the document gives inconsistent internal audit counts of at least 26 teams in the motivation and at least 15 teams in the rationale." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,162,746 ADA, consisting of 1,128,880 ADA for Plutarch and Ply maintenance, compatibility, and developer experience plus a 33,866 ADA Intersect administration fee." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, but the document gives inconsistent internal audit counts of at least 26 teams in the motivation and at least 15 teams in the rationale.
- Claims and evidence missing: Independent evidence for: The proposal says the next funding period is expected to cover Cardano ledger, Plutus, tooling evolution, and protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land during the funding period.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `1493ee44718ca9df04d0daa9ca6a9f5beae3e484e57f4770731fd10f29749e74`
- snapshot_bundle_hash: `2ea143d438c16c1cc1ce5bd09bf16359baca30a7f7eeb305fb9c7fc0c03fe718`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

