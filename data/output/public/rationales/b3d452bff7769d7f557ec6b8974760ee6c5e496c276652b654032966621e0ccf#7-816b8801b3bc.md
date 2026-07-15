# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#7
Recommendation: **NEEDS_MORE_INFO**
Score: `0.027` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7268` | Readiness: `0.65`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims describe maintenance of established open-source Cardano infrastructure, include concrete budget components, identify operational scope, and point to independently verifiable governance, NCL, repository, smart-contract, audit, and dashboard sources. The nudge remains small because several delivery-history and schedule claims are proposer-asserted, and treasury stewardship still depends on the deterministic engine's verified dossier and cost analysis.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action requests 540,750 ada for 12 months of Oura maintenance and enhancement by TxPipe, submitted by Intersect on behalf of the vendor. The proposal says this includes 525,000 ada for Oura work and a 15,750 ada Intersect administration fee, with the Oura budget described as 420,000 ada plus a 105,000 ada contingency reserve for a part-time maintainer. The work would cover dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, documentation, community support, AI-friendly integration resources, and milestone-based disbursement and reporting through Intersect oversight.

Several important claims were supported well enough for review: the proposal anchor was pinned and replayable, Oura’s technical role as a Rust-native Cardano event pipeline was supported, repository activity and adoption signals were independently verifiable, and the proposal’s passage through the 2026 Intersect Budget Process Hydra Voting phase was independently verifiable. The review also found that the requested amount did not breach the stated 350M ada Net Change Limit at submission, and that Intersect would administer funds through treasury management smart contracts with oversight, authorization thresholds, reporting, milestone controls, and a public dashboard.

This is a conservative, evidence-based hold, not a rejection of Oura. The review found thin evidence in some areas: independent evidence was missing for the Project Catalyst funding-history claims, the line-item budget was missing, milestone-gated disbursement evidence was missing from treasury analysis, and the risk review lacked independent assurance plus a rollback or remedy path. The specific evidence that would unblock a directional vote is pinned, independently verifiable public chain evidence for the applicable Net Change Limit, with stronger support for the missing budget, milestone, assurance, and remedy details.

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
- finding: Requested: Treasury withdrawal to fund Oura by TxPipe maintenance and enhancement for 12 months, submitted by Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Oura over 12 months, Essential maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows, Milestone-based disbursement controls and reporting obligations through Intersect oversight
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time maintainer for Oura over 12 months at an annual rate of $105,000 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The on-chain withdrawal amount is 540,750 ADA, consisting of 525,000 ADA for Oura maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Oura is a Rust-native pipeline tool that connects to Cardano nodes, monitors blockchain events, and routes matching patterns to pluggable outputs.
- finding: Claim (technical, supported_in_proposal, medium materiality): Oura supports multiple data sources including N2C, N2N, S3, Mithril, and UTxO RPC and many sinks including Kafka, Elasticsearch, AWS services, RabbitMQ, Redis, SQL databases, and webhooks.
- finding: Claim (adoption, independently_verifiable, medium materiality): Oura has 654 commits, 288 stars, 79 forks, and 58 contributors and is the most starred project in the TxPipe portfolio.
- finding: Claim (economic, proposer_asserted, medium materiality): Oura has been funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- missing: Independent evidence for: Oura has been funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time maintainer for Oura over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time maintainer for Oura over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims describe maintenance of established open-source Cardano infrastructure, include concrete budget components, identify operational scope, and point to independently verifiable governance, NCL, repository, smart-contract, audit, and dashboard sources. The nudge remains small because several delivery-history and schedule claims are proposer-asserted, and treasury stewardship still depends on the deterministic engine's verified dossier and cost analysis.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Oura has been funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- Claims and evidence missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `816b8801b3bca2331273e12e7db0b555d661ed6d216dec3b25fab1258d9b37b0`
- snapshot_bundle_hash: `c4e7fe1a4c193561b31e58263733ff2340a47fb9241e0b4c007660f1347e4d49`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `3e3c343fc0dd14a03a92aad1216ba6620b3d0185`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5017, "NO": 0.2222, "YES": 0.2762}`

