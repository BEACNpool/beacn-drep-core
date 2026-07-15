# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1359` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.754` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show an open-source infrastructure maintenance proposal with checkable repository, voting, NCL, smart-contract, and dashboard references, plus concrete maintenance and oversight scope. The nudge remains small because several high-materiality delivery and prior-performance claims are still proposer-asserted, and treasury stewardship under the doctrine requires caution for real spending.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Dolos or the requested work.

The proposal asks for 540,750 ada for Year 2 maintenance of Dolos by TxPipe: 420,000 ada for the work, 105,000 ada as contingency, and 15,750 ada for Intersect administration. The requested scope includes 12 months of part-time maintenance, dependency updates, protocol compatibility, performance work, bug fixes, documentation, issue triage, contribution review, community communication, and AI-friendly documentation and integration resources. The proposal also says funds would be administered through Intersect with milestone controls, smart-contract treasury management, reporting obligations, and public auditability.

Several parts were well supported or independently checkable. The funding breakdown was clear. The proposal anchor was pinned and replayable. The proposal provided references for Intersect budget-process support, repository activity, NCL status at submission, treasury administration, voting records, audited results, contract addresses, and dashboard-based oversight. But some material technical and delivery claims remained only proposer-asserted or thinly evidenced, including independent evidence that Dolos is a lightweight Rust Cardano data node, that it provides the stated interfaces and network functions, and that execution risk, cost-benefit clarity, sustainability path, independent assurance, and rollback or remedy paths are adequately covered.

Because shared treasury ada is being requested, BEACN applies a higher evidence bar. The specific evidence that would unblock a directional vote is independently pinned public-chain verification of the applicable Net Change Limit, plus stronger replayable evidence for the material Dolos technical claims and the missing treasury and risk-review items. Until then, NEEDS_MORE_INFO avoids overstating certainty while leaving room for a YES or NO once the evidence is complete.

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
- finding: Requested: Funding for Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2, including maintenance, enhancement, community support, and AI-friendly documentation/integration resources over 12 months.
- finding: Recipient: Intersect treasury reserve smart contract stake address for administration on behalf of the vendor TxPipe
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months after the existing contract closes, Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixes, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public developer communication, Upgrades for AI-driven development workflows through AI-friendly documentation and integration resources, Milestone-based disbursement controls and reporting obligations through Intersect oversight
- finding: Deadline/expiry: 12-month grant period beginning after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a traditional full node.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is said to connect directly to the Cardano network, index ledger primitives, and expose five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with existing tooling.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors, with a GitHub repository link provided for verification.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed maintainer scope includes dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, documentation, issue triage, contribution review, community communication, and AI-friendly documentation and integration resources.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal states Dolos aligns with Intersect Strategic Pillar 2 focus area A.3 for Developer Experience and open-source incentives.
- missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a traditional full node.
- missing: Independent evidence for: Dolos is said to connect directly to the Cardano network, index ledger primitives, and expose five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with existing tooling.
- missing: Independent evidence for: The proposal states Dolos aligns with Intersect Strategic Pillar 2 focus area A.3 for Developer Experience and open-source incentives.
- missing: Independent evidence for: The proposal states TxPipe has received 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development on schedule, and that prior Intersect 2025 maintenance funding for Pallas, Dolos, and UTxO RPC is being delivered on schedule.
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
- finding: Financial confidence: 0.68
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a traditional full node." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show an open-source infrastructure maintenance proposal with checkable repository, voting, NCL, smart-contract, and dashboard references, plus concrete maintenance and oversight scope. The nudge remains small because several high-materiality delivery and prior-performance claims are still proposer-asserted, and treasury stewardship under the doctrine requires caution for real spending.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a traditional full node.
- Claims and evidence missing: Independent evidence for: Dolos is said to connect directly to the Cardano network, index ledger primitives, and expose five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with existing tooling.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `a9980c09e0158d138b442c1f352a139c14a4cddf36fae0911c3efebb1c6c7718`
- snapshot_bundle_hash: `f2f1c2cf6f855948bd60474871ac5e32f4ddea39caae796355c807063859f3d0`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `d68b33ee7989803aaecd7edc03d77c134a98a7f1`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5085, "NO": 0.1099, "YES": 0.3816}`

