# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#7
Recommendation: **NEEDS_MORE_INFO**
Score: `0.027` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7268` | Readiness: `0.65`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe maintenance of established open-source infrastructure, include several independently checkable governance and repository references, and provide concrete fund-management controls; the nudge remains small because key adoption and delivery-history claims are still largely proposer-asserted within the document and the ask draws real treasury funds.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Oura or TxPipe.

The action asks to withdraw 540,750 ada for 12 months of Oura maintenance and enhancement, with Intersect administering funds through the 2026 Treasury Reserve Smart Contract. The proposal says this includes 525,000 ada for the work and a 15,750 ada Intersect administration fee. It describes Oura as a Rust-native Cardano event pipeline tool, lists planned maintenance work such as dependency updates, protocol compatibility, performance improvements, bug fixing, documentation, contribution review, and developer communication, and provides public governance and repository references.

Several claims were well-supported inside the proposal, including the total amount requested, the administration fee, the 12-month maintainer rationale, the description of Oura’s technical role, and the proposed Intersect fund-management structure. Some claims had weaker support: ecosystem-wide usage, prior Catalyst funding history, and TxPipe delivery history were treated as proposer-asserted or missing independent evidence. The review also found thin claims-and-evidence status, missing line-item budget detail, missing milestone-gated disbursement evidence, unknown execution risk, no independent assurance, and no rollback or remedy path.

The evidence that would unblock a directional vote is the pinned, independently verifiable Net Change Limit from public chain evidence. Stronger independent evidence for ecosystem adoption, past funding and delivery history, line-item budgeting, milestone controls, independent assurance, and remedy paths would also improve confidence, but the decisive reason for this hold is the missing verified Net Change Limit required for treasury withdrawal scrutiny.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 540.8k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Oura by TxPipe maintenance and enhancement for 12 months, with Intersect administering funds on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, for Oura by TxPipe via Intersect administration
- finding: Stated amount: 540750
- finding: Deliverables: WP1 - Oura Maintenance and Enhancement, Part-time maintainer for Oura over 12 months, Dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public developer communication, AI-friendly documentation and integration resources
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Oura maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The motivation states the work funds a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD, with 420,000 ADA plus a 105,000 ADA contingency reserve described before the final fee-inclusive total.
- finding: Claim (technical, supported_in_proposal, high materiality): Oura is described as a Rust-native pipeline tool that connects to Cardano nodes, monitors blockchain events, and routes matching patterns to pluggable outputs.
- finding: Claim (technical, supported_in_proposal, medium materiality): Oura is claimed to support multiple data sources including N2C, N2N, S3, Mithril, and UTxO RPC, and sinks including Kafka, Elasticsearch, AWS services, RabbitMQ, Redis, SQL databases, and webhooks.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Oura has 654 commits, 288 stars, 79 forks, and 58 contributors, and links to the public GitHub repository.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal claims Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
- missing: Independent evidence for: The proposal claims Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
- missing: Independent evidence for: The proposal states Oura was previously funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- missing: Independent evidence for: The proposal states TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 currently under development and on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.43
- missing: line-item budget
- missing: milestone-gated disbursement
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Oura maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal claims Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 540750
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Oura maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe maintenance of established open-source infrastructure, include several independently checkable governance and repository references, and provide concrete fund-management controls; the nudge remains small because key adoption and delivery-history claims are still largely proposer-asserted within the document and the ask draws real treasury funds.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal claims Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
- Claims and evidence missing: Independent evidence for: The proposal states Oura was previously funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `5abd2918598a237f7b5b414be6f0994ec4e2ccd09074a4781ab5eb97fed1f796`
- snapshot_bundle_hash: `6ede283365336291a81f19bf8189e43d7add579b599edf1138c46a97d9c9c0c9`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5017, "NO": 0.2222, "YES": 0.2762}`

