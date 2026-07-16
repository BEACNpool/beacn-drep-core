# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#7
Recommendation: **NEEDS_MORE_INFO**
Score: `0.027` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7268` | Readiness: `0.65`
> Reasoning layer (precomputed): The extracted claims show a maintenance proposal for existing open-source Cardano infrastructure with defined work areas, public repositories and governance-process references, NCL compliance claims, and smart-contract oversight details. The modest positive nudge is based on alignment with public-benefit ecosystem growth and evidence quality for an established infrastructure dependency, while remaining small because adoption and delivery claims still rely partly on proposer assertions and the treasury amount is material.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action asks for 540,750 ada over 12 months for Oura by TxPipe, administered through Intersect. The proposal says this includes 420,000 ada for the work, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. The stated work covers part-time maintenance, dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, documentation, community support, developer communication, AI-friendly integration resources, and milestone-based oversight through Intersect.

Several core claims were well-supported in the review: the anchor document was available and replayable, the requested amount was clearly stated, Oura’s technical role was described, and the proposal provided governance-process and treasury-management references, including Intersect Budget Process support and smart-contract oversight details. However, some claims remained unsupported or thin, including independent evidence for prior Project Catalyst funding and broad ecosystem use. The review also flagged missing or uncertain areas around line-item budget detail, milestone-gated disbursement evidence, independent assurance, execution risk, and rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of Oura or of maintenance funding. The vote could be unblocked by independently pinned public-chain evidence for the applicable Net Change Limit, plus stronger replayable evidence for the unsupported adoption and funding-history claims and clearer treasury-risk materials such as line-item budgeting, milestone controls, independent assurance, and remedy paths.

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
- finding: Requested: Treasury withdrawal to fund Oura by TxPipe maintenance and enhancement over 12 months, submitted by Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, for Oura by TxPipe via Intersect administration.
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for Oura over 12 months, Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public developer communication, AI-friendly documentation and integration resources, Milestone-based disbursement controls and reporting obligations through Intersect oversight
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, for a total withdrawal of 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): Oura is described as a Rust-native pipeline tool that connects to Cardano nodes, monitors blockchain events, and routes matching patterns to pluggable outputs.
- finding: Claim (technical, supported_in_proposal, medium materiality): Oura supports multiple data sources including N2C, N2N, S3, Mithril, and UTxO RPC, and multiple sinks including Kafka, Elasticsearch, AWS services, RabbitMQ, Redis, SQL databases, and webhooks.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document states that Oura has 654 commits, 288 stars, 79 forks, and 58 contributors, and is the most starred project in the TxPipe portfolio.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal states that Oura has previously been funded twice through Project Catalyst, in Funds 9 and 13, for feature development.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope covers codebase maintenance, community support, and AI-driven development workflow compatibility resources.
- missing: Independent evidence for: The proposal states that Oura has previously been funded twice through Project Catalyst, in Funds 9 and 13, for feature development.
- missing: Independent evidence for: The proposal claims Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, for a total withdrawal of 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Oura has previously been funded twice through Project Catalyst, in Funds 9 and 13, for feature development." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, for a total withdrawal of 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a maintenance proposal for existing open-source Cardano infrastructure with defined work areas, public repositories and governance-process references, NCL compliance claims, and smart-contract oversight details. The modest positive nudge is based on alignment with public-benefit ecosystem growth and evidence quality for an established infrastructure dependency, while remaining small because adoption and delivery claims still rely partly on proposer assertions and the treasury amount is material.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal states that Oura has previously been funded twice through Project Catalyst, in Funds 9 and 13, for feature development.
- Claims and evidence missing: Independent evidence for: The proposal claims Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `119472b771d5b81895ddfe73f79dad595ea9aa518e72ba0c46f2d19c67cddefa`
- snapshot_bundle_hash: `589209046e7d88839364f2d9132f15d7ba21c51d351c8237abeae82232fdd82d`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5017, "NO": 0.2222, "YES": 0.2762}`

