# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#7
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.08` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.0` recorded, not added) | Confidence: `0.74` | Readiness: `0.65`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit infrastructure maintenance and some independently verifiable governance, NCL, repository, and voting references, while key adoption and prior delivery claims remain largely proposer-asserted within the document. The deterministic assessment is ready, and the remaining evidence-quality tradeoff appears already captured, so no additional nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal and the applicable Net Change Limit still needs to be pinned and independently verified from public chain evidence before a directional vote is justified.

The action asks to withdraw 540,750 ada for 12 months of Oura by TxPipe maintenance and enhancement. The proposal describes part-time maintenance, community support, documentation, protocol compatibility, bug fixing, performance improvements, and AI-friendly documentation and integration resources. It says 525,000 ada would fund the work, including 420,000 ada plus a 105,000 ada contingency reserve for a part-time maintainer at a stated annual rate of $105,000 USD, with a 15,750 ada Intersect Budget Administration fee.

Several core claims were reviewable from the proposal or independent evidence. The anchor document was available, pinned, and replayable. The proposal supported the requested budget structure, described Oura as a Rust-native Cardano event pipeline tool, and provided technical details about data sources and outputs. Independent checks supported Oura’s repository activity and the fact that the proposal passed the required 67% Intersect Budget Process Hydra Voting threshold. However, other claims were not independently verified, including prior Project Catalyst funding in Funds 9 and 13 and broad ecosystem use for indexing, monitoring, analytics, and real-time event processing.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by public, replayable verification of the applicable Net Change Limit, stronger independent evidence for the unsupported adoption and funding-history claims, and clearer treasury-risk details such as a line-item budget, milestone-gated disbursement, independent assurance, and a rollback or remedy path.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: ratified
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
- finding: Requested: Fund Oura by TxPipe maintenance and enhancement over 12 months, including part-time maintenance, community support, documentation, protocol compatibility, bug fixing, performance improvements, and AI-friendly documentation/integration resources.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor TxPipe
- finding: Stated amount: 540,750
- finding: Deliverables: WP1 - Oura Maintenance and Enhancement, Essential maintenance of the codebase including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The total requested withdrawal is 540,750 ADA, consisting of 525,000 ADA for Oura maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Oura is a Rust-native pipeline tool that connects to Cardano nodes, monitors blockchain events, and routes matching patterns to pluggable outputs.
- finding: Claim (technical, supported_in_proposal, medium materiality): Oura supports multiple data sources including N2C, N2N, S3, Mithril, and UTxO RPC, and multiple sinks including Kafka, Elasticsearch, AWS Lambda/S3/SQS, RabbitMQ, Redis, SQL databases, and webhooks.
- finding: Claim (adoption, independently_verifiable, medium materiality): Oura has 654 commits, 288 stars, 79 forks, and 58 contributors, and is the most starred project in the TxPipe portfolio.
- finding: Claim (economic, proposer_asserted, medium materiality): Oura has been funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- missing: Independent evidence for: Oura has been funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- missing: Independent evidence for: The proposer states that Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Oura has been funded twice through Project Catalyst in Funds 9 and 13 for feature development." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Directional treasury voting is blocked until this action is ranked against competing active proposals and verified NCL capacity.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Oura has been funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- Claims and evidence missing: Independent evidence for: The proposer states that Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `b68e572b5f4a1ddbcbaa366f8f0fc7630ca7b079ae3fa35b479248c0cc044684`
- snapshot_bundle_hash: `533edcf11156adcb5f643d19d51b21454bf1d324190844aca55299ab6b6c279a`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `199e0465f8eabf20be3ce768498dd41ae56148a9`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.505, "NO": 0.3275, "YES": 0.1675}`

