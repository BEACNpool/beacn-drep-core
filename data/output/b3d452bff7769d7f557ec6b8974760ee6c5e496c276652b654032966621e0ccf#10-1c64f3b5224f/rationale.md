# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.077` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.01` recorded, not added) | Confidence: `0.7392` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the proposal concerns maintained open-source integration infrastructure, provides a concrete maintenance scope, cites checkable budget-process and treasury-management references, and describes oversight and disbursement controls. The nudge is limited because several important adoption and prior-delivery claims are asserted rather than evidenced inside the document, and the cost case for a part-time maintainer plus contingency is not deeply substantiated against post-AI cost expectations.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action asks to withdraw 540,750 ada for 12 months of Year 2 UTxO RPC maintenance and enhancement by TxPipe, administered through Intersect. The proposal says this includes 525,000 ada for the work and 15,750 ada for Intersect administration. It describes a part-time maintainer, protobuf specification maintenance, SDK maintenance, community support, AI-friendly documentation, and Intersect oversight.

Several core facts were supported in the proposal: the requested amount, the maintenance scope, the description of UTxO RPC as an open Protocol Buffers interface with SDKs across multiple languages, and references to Intersect budget-process and treasury-management materials. However, some material claims were not independently evidenced inside the review record, including adoption by Amaru, Dingo, and the Haskell Cardano node, and TxPipe’s prior Catalyst and Intersect delivery record. The review also found thin claim evidence overall, missing sustainability and cost-benefit clarity, unknown execution risk, no independent assurance, and no clear rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the project. A directional vote would be unblocked by public, replayable evidence verifying the applicable Net Change Limit from chain data, plus stronger independent evidence for the adoption and prior-delivery claims, clearer cost-benefit and sustainability support, and stronger execution assurance and remedy paths.

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
- finding: Requested: Fund Year 2 maintenance and enhancement of UTxO RPC by TxPipe for 12 months, including a part-time maintainer and Intersect administration.
- finding: Recipient: Intersect treasury reserve smart contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, for TxPipe as vendor via Intersect budget administration
- finding: Stated amount: 540750
- finding: Deliverables: UTxO RPC maintenance and enhancement, Maintenance of the protobuf specification including compatibility, versioning, and documentation, Maintenance of official SDKs including dependency updates, performance improvements, and bug fixes, Community support including issue triage, contribution review, feedback-driven enhancements, and public communication, AI-friendly documentation and integration resources, Intersect administration and oversight
- finding: Deadline/expiry: 12 months after closure of the existing contract; exact dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and 15,750 ADA for Intersect administration.
- finding: Claim (economic, supported_in_proposal, high materiality): The motivation states the project funding includes 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification using Protocol Buffers with SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The document says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope includes protobuf specification maintenance, SDK maintenance, community support, and AI-friendly documentation and integration resources.
- finding: Claim (technical, independently_verifiable, medium materiality): The proposal says the project maintains more than 10 repositories and is open source under Apache 2.0.
- missing: Independent evidence for: The document says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- missing: Independent evidence for: TxPipe is said to have received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development and on schedule, plus 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC delivered on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.58
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and 15,750 ADA for Intersect administration." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The document says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and 15,750 ADA for Intersect administration." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.010 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the proposal concerns maintained open-source integration infrastructure, provides a concrete maintenance scope, cites checkable budget-process and treasury-management references, and describes oversight and disbursement controls. The nudge is limited because several important adoption and prior-delivery claims are asserted rather than evidenced inside the document, and the cost case for a part-time maintainer plus contingency is not deeply substantiated against post-AI cost expectations.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The document says UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- Claims and evidence missing: Independent evidence for: TxPipe is said to have received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development and on schedule, plus 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC delivered on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `1c64f3b5224fc3563d949fe31373fd2e9e7929a899298dd4d8f125ca99a903cf`
- snapshot_bundle_hash: `d4ca4a0cdb9b3a40303b9839879edbca0d31cc5dcb5a886d07e3a1fa710510fb`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.1706, "YES": 0.3246}`

