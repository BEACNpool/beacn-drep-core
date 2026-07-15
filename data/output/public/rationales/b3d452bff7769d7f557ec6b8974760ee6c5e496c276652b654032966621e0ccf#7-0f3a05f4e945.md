# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#7
Recommendation: **NEEDS_MORE_INFO**
Score: `0.027` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7268` | Readiness: `0.65`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit infrastructure maintenance and some independently verifiable governance and repository evidence, but the deterministic assessment is already ready and the document still relies on proposer assertions for ecosystem usage and delivery history; no additional doctrine-based nudge is justified beyond the engine result.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal depends on a verified Net Change Limit, and that public chain evidence was not pinned and independently verified. This is a conservative, evidence-based hold, not a rejection of Oura or TxPipe.

The action requests 540,750 ada for 12 months of Oura maintenance and enhancement, submitted by Intersect on behalf of the vendor. The proposal says this includes 525,000 ada for the work and a 15,750 ada Intersect administration fee. It also describes Oura as a Rust-native Cardano event pipeline tool, with maintenance covering dependency updates, protocol compatibility, performance improvements, bug fixes, documentation, issue triage, contribution review, ecosystem-driven enhancements, public developer communication, and AI-friendly integration resources.

Several basics were reviewable: the proposal anchor was pinned and replayable, the requested amount was clear, and the proposal provided support for the budget total and technical description. Some claims were weaker. The claim that Oura is widely used across the ecosystem was not independently evidenced, prior Catalyst funding claims were not independently evidenced, the claims-and-evidence record was thin, and the review was missing a line-item budget, milestone-gated disbursement detail, independent assurance, and a rollback or remedy path. Execution risk remained unknown.

Because this is a treasury withdrawal, BEACN applies a higher bar: spending shared ADA requires replayable evidence, clear controls, and verified compliance with treasury limits. A directional vote would be unblocked by pinned, independently verified public chain evidence for the applicable Net Change Limit, plus stronger independent evidence for the material adoption and funding claims and clearer treasury controls.

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
- finding: Requested: Treasury withdrawal to fund Oura by TxPipe maintenance over 12 months, submitted by Intersect on behalf of the vendor.
- finding: Recipient: stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for Oura over 12 months, Dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public developer communication, AI-friendly documentation and integration resources, Milestone-based disbursement controls and reporting obligations
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Oura maintenance and enhancement plus a 15,750 ADA Intersect administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The motivation states the underlying maintenance request is 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time maintainer at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): Oura is described as a Rust-native pipeline tool that connects to Cardano nodes, monitors blockchain events, and routes matching patterns to pluggable outputs.
- finding: Claim (technical, supported_in_proposal, medium materiality): The proposal says Oura supports multiple sources including N2C, N2N, S3, Mithril, and UTxO RPC and many sinks including Kafka, Elasticsearch, AWS services, RabbitMQ, Redis, SQL databases, and webhooks.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Oura has 654 commits, 288 stars, 79 forks, and 58 contributors, and links to the public GitHub repository.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal claims Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
- missing: Independent evidence for: The proposal claims Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
- missing: Independent evidence for: The proposal states Oura was previously funded through Project Catalyst Funds 9 and 13 for feature development.
- missing: Independent evidence for: The proposal states TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Oura maintenance and enhancement plus a 15,750 ADA Intersect administration fee." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Oura maintenance and enhancement plus a 15,750 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
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
- Claims and evidence missing: Independent evidence for: The proposal states Oura was previously funded through Project Catalyst Funds 9 and 13 for feature development.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `0f3a05f4e945c7d5d24f123e79954add7af26daecbf20ada53ac3cca96794504`
- snapshot_bundle_hash: `efe443e348de40c73ebad969698cfa14f1cf59110a6b6a676acec12c160d7234`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `880436a840989202a38cccce66fd8f1cbf15004d`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5017, "NO": 0.2222, "YES": 0.2762}`

