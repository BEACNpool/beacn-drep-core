# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.077` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7392` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show plausible public infrastructure value and some independently checkable governance and oversight references, while key adoption and delivery-history claims remain mostly proposer-asserted in the supplied document. Because the deterministic assessment is already ready and hard gates have handled eligibility, the evidence mix does not justify an additional directional nudge beyond the mechanical score.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the project.

The action requests 540,750 ada for Year 2 maintenance of UTxO RPC by TxPipe. The proposal says this includes 420,000 ada for work, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. It would fund a part-time maintainer for 12 months, maintenance of the protobuf specification and SDKs, community support, documentation, and AI-friendly integration resources. The anchor document was available, pinned, and replayable, and the basic budget claim was well-supported in the proposal.

Several claims were treated as useful but not fully proven for voting confidence. The review found independent support that the project is open source under Apache 2.0 and spans more than 10 repositories, and it noted the proposal’s claim that the action passed the required 67% Intersect Budget Process Hydra Voting threshold. But adoption claims, including use by Amaru, Dingo, and the Haskell Cardano node, still lacked independent evidence in the review. The claims about TxPipe’s Catalyst delivery record and 2025 Intersect-funded work were also proposer assertions rather than independently verified evidence.

The review gates showed enough information to review the proposal, but not enough to cast a YES or NO responsibly. Treasury scrutiny was elevated because shared ada would be spent, execution risk remained unknown, the evidence record was thin, and the review was missing a sustainability path, clearer cost-benefit analysis, independent assurance, and a rollback or remedy path. A directional vote would be unblocked by pinned, independently verifiable public-chain evidence for the Net Change Limit, plus stronger independent evidence for the material adoption and delivery claims.

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
- finding: Requested: Treasury withdrawal to fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for UTxO RPC over 12 months, Maintenance of the protobuf specification including compatibility, versioning, and documentation, Maintenance of official SDKs including dependency updates, performance improvements, and bug fixes, Community support including issue triage, review of contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months after closure of the existing contract; exact dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve, with a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested funding covers a part-time maintainer for UTxO RPC over 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification that standardizes interactions with UTxO-based blockchains using Protocol Buffers and SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The document states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories covering the core specification, language SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: The document states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- missing: Independent evidence for: TxPipe received 2025 Intersect open-source maintenance funding for Pallas, Dolos, and UTxO RPC, and the document states all are being delivered on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve, with a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The document states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve, with a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: The document states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- Claims and evidence missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `52507d9481f7cb6f8a4d81d797fecbedc0a2e94d747c56bc139d309dbc24498c`
- snapshot_bundle_hash: `ff28dd81663c0196481ffba0f4ff4189356f76802158c973c43c9136ee00f885`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.1706, "YES": 0.3246}`

