# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (binding treasury composite; advisory raw signal `-0.53`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): A small positive nudge is justified because the supplied claims describe established public infrastructure, NCL compliance, external references for the budget vote and smart-contract audits, and concrete custody and oversight mechanics. The nudge remains small because the core technical and adoption benefits are mostly proposer-asserted in the anchor text rather than demonstrated with detailed metrics or reproducible delivery evidence.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action requests 3,810,423 ada for Mithril Protocol continuous development through Intersect-administered treasury management contracts: 3,699,440 ada for development and 110,983 ada for the Intersect budget administration fee. The proposal says funds would move through a 2026 Treasury Reserve Smart Contract and a project-specific contract, with milestone-based disbursement controls, reporting obligations, oversight, non-staking behavior, auto-abstain DRep delegation, and a public dashboard. Those custody and oversight mechanics were supported in the proposal, and the proposal also referenced the Intersect budget process, audited results, treasury-contract code, and audit reports.

The main technical and adoption case was thinner. The proposer asserted that Mithril addresses slow full-node synchronization and centralized-trust light client reliance, enables rapid state verification, and could reduce onboarding friction for exchanges, wallets, and monitoring tools. Those may be important benefits, but the review found the core technical and adoption claims were mostly proposer-asserted rather than independently demonstrated with detailed metrics or reproducible delivery evidence. The review also noted missing or uncertain items including a line-item budget, sustainability path, independent assurance, rollback or remedy path, and unknown execution risk.

This is a conservative, evidence-based hold, not a rejection of Mithril. A directional vote would be unblocked by pinned, independently verifiable Net Change Limit evidence from public chain data, plus stronger independent evidence for the main technical claims, clearer budget detail, a sustainability path, independent assurance, and a defined remedy path if execution fails.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 3.81M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Mithril Protocol continuous development through Intersect-administered treasury management contracts.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with project-specific contract addr1x9d6k9z6t6fvsetj2djmerargk475lef9gfvshy4rwh4h7jm4v295h5jepjhy5m9hj86x3dtafljj2sjepwf2xa0t0aq048cay stated for later project funding.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Use of Intersect treasury management smart contract framework, Milestone-based disbursement controls and reporting obligations
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol continuous development and 110,983 ada for an Intersect budget administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril is presented as addressing slow full-node synchronization and centralized-trust light client reliance by using stake-based threshold multi-signatures to certify Cardano state trustlessly.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer claims Mithril enables rapid state verification for nodes and applications without relying on the entire chain.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states that faster sync times would reduce onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and references voting, documentation, audited results, and audit report sources.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states the requested amount does not, at submission time, individually or in aggregate breach the 350M ada Net Change Limit covering Epoch 613 to Epoch 713, and links to the relevant governance action.
- missing: Independent evidence for: Mithril is presented as addressing slow full-node synchronization and centralized-trust light client reliance by using stake-based threshold multi-signatures to certify Cardano state trustlessly.
- missing: Independent evidence for: The proposer claims Mithril enables rapid state verification for nodes and applications without relying on the entire chain.
- missing: Independent evidence for: The proposal states that faster sync times would reduce onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- missing: Independent evidence for: The document states Teragone has not previously received direct Cardano treasury or community governance funding but has worked on Mithril for several years through IOG-funded collaboration.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 3810423
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.45
- missing: line-item budget
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol continuous development and 110,983 ada for an Intersect budget administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Mithril is presented as addressing slow full-node synchronization and centralized-trust light client reliance by using stake-based threshold multi-signatures to certify Cardano state trustlessly." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 3810423
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol continuous development and 110,983 ada for an Intersect budget administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the supplied claims describe established public infrastructure, NCL compliance, external references for the budget vote and smart-contract audits, and concrete custody and oversight mechanics. The nudge remains small because the core technical and adoption benefits are mostly proposer-asserted in the anchor text rather than demonstrated with detailed metrics or reproducible delivery evidence.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 50% of rolling available capacity.
- Claims and evidence missing: Independent evidence for: Mithril is presented as addressing slow full-node synchronization and centralized-trust light client reliance by using stake-based threshold multi-signatures to certify Cardano state trustlessly.
- Claims and evidence missing: Independent evidence for: The proposer claims Mithril enables rapid state verification for nodes and applications without relying on the entire chain.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `2bdeee385fa5d5f3008f023fb1b02ff5c6c48d46567e6867434b3a7057ea5762`
- snapshot_bundle_hash: `a707faa82cf70d3f8215572813f67cc486813140c0d1d879dc9d87b37cd8a741`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

