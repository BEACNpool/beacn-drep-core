# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#7
Recommendation: **NEEDS_MORE_INFO**
Score: `0.027` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7268` | Readiness: `0.65`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims describe established open-source infrastructure maintenance with concrete scope, custody controls, milestone disbursement, NCL compliance, and several independently checkable governance and repository references. The adjustment remains small because key delivery-history and adoption-impact assertions are largely proposer asserted, and treasury stewardship requires caution on a 540,750 ADA maintenance request.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a Treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action requests 540,750 ada to fund 12 months of Oura by TxPipe maintenance and enhancement. The proposal says this includes 420,000 ada for part-time maintainer work, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. It also claims Oura is a Rust-native Cardano event pipeline tool, with maintenance covering dependency updates, protocol compatibility, performance improvements, bug fixes, documentation, issue triage, external contribution review, ecosystem-feedback enhancements, and AI-friendly integration resources.

Several core claims were supported by the proposal or independently checkable: the requested amount and broad cost structure, Oura’s technical purpose, the stated maintainer scope, repository activity references, Intersect budget-process support, and the statement that the request did not breach the Net Change Limit at submission. But some important claims remained unsupported or thin, including prior Catalyst funding for Oura, TxPipe’s broader Catalyst delivery record, a line-item budget, milestone-gated disbursement detail, independent assurance, and a rollback or remedy path.

This is a conservative, evidence-based hold rather than a rejection. A directional vote would be unblocked by pinned, independently verifiable public chain evidence for the applicable Net Change Limit, plus stronger replayable evidence for the missing delivery-history, budget, milestone, assurance, and remedy-path details.

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
- finding: Requested: Fund Oura by TxPipe maintenance and enhancement for 12 months, including part-time maintainer work, community support, AI-friendly documentation and integration resources, plus Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe/vendor
- finding: Stated amount: 540750
- finding: Deliverables: Essential maintenance of the Oura codebase including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public developer communication, AI-friendly documentation and integration resources for AI-driven development workflows, Milestone-based disbursement controls and reporting obligations through Intersect oversight
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD, with a total withdrawal of 540,750 ADA including a 15,750 ADA Intersect administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Oura is a Rust-native pipeline tool that connects to Cardano nodes, monitors blockchain events, and routes matching patterns to pluggable outputs for processing.
- finding: Claim (technical, supported_in_proposal, medium materiality): Oura supports multiple data sources including N2C, N2N, S3, Mithril, and UTxO RPC, and many output sinks including Kafka, Elasticsearch, AWS services, RabbitMQ, Redis, SQL databases, and webhooks.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states that Oura has 654 commits, 288 stars, 79 forks, and 58 contributors, and identifies its GitHub repository as the source project.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope covers dependency updates, Cardano protocol compatibility, performance improvements, bug fixes, documentation, issue triage, external contribution review, ecosystem-feedback enhancements, public communication, and AI-friendly documentation and integration resources.
- finding: Claim (economic, proposer_asserted, medium materiality): Oura was previously funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- missing: Independent evidence for: Oura was previously funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 successfully delivered and 4 currently under development and on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD, with a total withdrawal of 540,750 ADA including a 15,750 ADA Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Oura was previously funded twice through Project Catalyst in Funds 9 and 13 for feature development." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Oura maintainer over 12 months at an annual rate of $105,000 USD, with a total withdrawal of 540,750 ADA including a 15,750 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims describe established open-source infrastructure maintenance with concrete scope, custody controls, milestone disbursement, NCL compliance, and several independently checkable governance and repository references. The adjustment remains small because key delivery-history and adoption-impact assertions are largely proposer asserted, and treasury stewardship requires caution on a 540,750 ADA maintenance request.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Oura was previously funded twice through Project Catalyst in Funds 9 and 13 for feature development.
- Claims and evidence missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 successfully delivered and 4 currently under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `279377afa43fff70383900a98c0b11515092362f2c735a4545d7b4ebdbb3d58f`
- snapshot_bundle_hash: `95b6cefbe7a8a6dcc668db58a1b1957676091f6d94db0cea019e322711d38a25`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `6`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5017, "NO": 0.2222, "YES": 0.2762}`

