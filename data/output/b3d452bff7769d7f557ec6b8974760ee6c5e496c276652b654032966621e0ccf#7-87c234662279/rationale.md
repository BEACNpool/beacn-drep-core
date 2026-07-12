# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#7
Recommendation: **NEEDS_MORE_INFO**
Score: `0.127` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7517` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe established open-source infrastructure maintenance, public repository verifiability, process references, NCL compliance, and structured disbursement oversight. The adjustment remains modest because several adoption and prior-delivery claims are proposer-stated rather than independently evidenced inside the document, and treasury stewardship still requires caution on ongoing maintenance spend.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal requested 540,750 ada for 12 months of Oura maintenance and enhancement by TxPipe, submitted through Intersect. The work package covers a part-time maintainer, dependency updates, Cardano protocol compatibility, performance improvements, bug fixes, documentation, issue triage, review of outside contributions, ecosystem-feedback improvements, public developer communication, and AI-friendly integration resources. The proposal also described Oura as a Rust-native Cardano event pipeline tool and provided public GitHub references for repository activity.

Several claims were well-supported inside the review: the funding structure, the on-chain withdrawal amount including Intersect’s administration fee, the technical description of Oura, the pinned and replayable proposal anchor, Intersect Budget Process support references, stated Net Change Limit references, and the structured treasury management arrangement. Other material claims remained weaker because they were proposer-stated rather than independently evidenced in the review, including broad ecosystem usage of Oura and TxPipe’s prior Project Catalyst delivery record.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by pinned, independently verified public chain evidence for the applicable Net Change Limit, plus stronger independent evidence for the key adoption and delivery claims, clearer treasury sustainability and cost-benefit analysis, and better risk coverage around independent assurance and rollback or remedy paths.

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
- finding: Requested: Withdraw treasury funds to maintain and enhance Oura, a Cardano event pipeline tool, over 12 months.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe as vendor
- finding: Stated amount: 540750
- finding: Deliverables: WP1 - Oura Maintenance and Enhancement, Part-time maintainer for Oura over 12 months, Dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Issue triage, review of external contributions, ecosystem-feedback enhancements, and public developer communication, AI-friendly documentation and integration resources
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The on-chain withdrawal amount is 540,750 ADA, consisting of 525,000 ADA for Oura maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Oura is described as a Rust-native Cardano pipeline tool that connects to Cardano nodes, monitors blockchain events, and routes matching patterns to pluggable outputs.
- finding: Claim (technical, supported_in_proposal, medium materiality): Oura supports multiple data sources including N2C, N2N, S3, Mithril, and UTxO RPC, and supports sinks including Kafka, Elasticsearch, AWS services, RabbitMQ, Redis, SQL databases, and webhooks.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states that Oura has 654 commits, 288 stars, 79 forks, and 58 contributors, and links to the public GitHub repository for verification.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
- missing: Independent evidence for: The proposer states that Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
- missing: Independent evidence for: The proposal states that TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.63
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe established open-source infrastructure maintenance, public repository verifiability, process references, NCL compliance, and structured disbursement oversight. The adjustment remains modest because several adoption and prior-delivery claims are proposer-stated rather than independently evidenced inside the document, and treasury stewardship still requires caution on ongoing maintenance spend.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposer states that Oura is used across the ecosystem for indexing, monitoring, analytics, and real-time event processing.
- Claims and evidence missing: Independent evidence for: The proposal states that TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `87c23466227972e63560f3a0c1acbfbd7571290143af0919635e63a1827738cb`
- snapshot_bundle_hash: `13cd96ce8bce14e79700cab2b0947fc62bbb01b1c119a6bddc2886789dc61d01`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5079, "NO": 0.119, "YES": 0.373}`

