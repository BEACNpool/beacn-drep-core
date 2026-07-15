# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **YES**
Score: `0.12` (raw `-0.11` + doctrine-LLM nudge `+0.02`) | Confidence: `0.75` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims describe established public-good infrastructure, open-source outputs, milestone-based administration, return of unspent funds, and independently verifiable release/version metrics. The nudge remains small because several important adoption and track-record claims are proposer-asserted and the amount is material treasury spending.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Se7en Labs: Daedalus Wallet Maintenance and Improvements 2026-2027. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Daedalus Wallet Maintenance and Improvements 2026-2027 delivered by Se7en Labs, Inc. It asks the treasury for 1,785,333 ADA. The strongest grounded claim is: The proposed work includes protocol maintenance, hard fork readiness, hardware wallet support, CIP-30, Japanese localisation, user support, and an architecture assessment.

A residual watch item: this claim remains proposer-asserted rather than independently shown: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.

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
- finding: Recipient: Se7en Labs, Inc., administered through Intersect with milestone-based monthly disbursements
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including cardano-node/cardano-wallet upgrades, hard fork readiness, platform support, release engineering, and security/dependency maintenance, Compatible Daedalus release at least 2 weeks before each mainnet hard fork, Leios, Peras, and Nested Transactions readiness, Keystone and Flex hardware wallet support, CIP-30 dApp connector implementation, User support including Japanese-language support and full Japanese translation maintenance, Architecture assessment published by Q3 2027, Independent financial audit and return of unspent labor, hardware, and audit budgets
- finding: Deadline/expiry: Contract year covering 2026-2027; ongoing maintenance and user support for 52 weeks; architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, high materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting true usage is meaningfully higher.
- finding: Claim (adoption, proposer_asserted, high materiality): Se7en Labs has operated under an IOG contract for Daedalus maintenance since January 2026 and shipped Daedalus 8.0 and 11.0 during that period.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed work includes protocol maintenance, hard fork readiness, hardware wallet support, CIP-30, Japanese localisation, user support, and an architecture assessment.
- finding: Claim (governance, independently_verifiable, medium materiality): All release-timing and version-currency success metrics are independently verifiable from public GitHub repositories and the Cardano mainnet chain.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested withdrawal is 1,785,333 ADA, allocated to 1,666,667 ADA for team labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and 52,000 ADA for Intersect administration.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting true usage is meaningfully higher.
- missing: Independent evidence for: Se7en Labs has operated under an IOG contract for Daedalus maintenance since January 2026 and shipped Daedalus 8.0 and 11.0 during that period.
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
- finding: Strongest YES: the proposal substantiates "The proposed work includes protocol maintenance, hard fork readiness, hardware wallet support, CIP-30, Japanese localisation, user support, and an architecture assessment." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposed work includes protocol maintenance, hard fork readiness, hardware wallet support, CIP-30, Japanese localisation, user support, and an architecture assessment." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims describe established public-good infrastructure, open-source outputs, milestone-based administration, return of unspent funds, and independently verifiable release/version metrics. The nudge remains small because several important adoption and track-record claims are proposer-asserted and the amount is material treasury spending.
- Directional YES cleared ecosystem benefit, delivery, cost-efficiency, downside-protection, and portfolio-capacity floors.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting true usage is meaningfully higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `4f8c7d3eeb35ec3f9ca26168986c764fcc223bb4a381d4ca2d32d48e2c9968c9`
- snapshot_bundle_hash: `9899a217534e251188a49bbce22c5816de28c5c928c9c92addc2e115875414c2`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3d9c2c9681f9060eff076f9ca8f4e36a1ddb67a2`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2263, "NO": 0.1263, "YES": 0.6475}`

