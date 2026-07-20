# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.08` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.0` recorded, not added) | Confidence: `0.74` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show plausible public-benefit infrastructure maintenance and some independently checkable governance/process references, while several key delivery and adoption statements remain proposer-asserted within the document. Because the deterministic engine has already completed treasury, risk, and evidence gates, the doctrine does not justify an additional directional nudge.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

This action requested 540,750 ada to fund Year 2 of Dolos by TxPipe, including 12 months of maintenance, enhancement, community support, documentation, and AI-friendly integration resources. The proposal says 525,000 ada would go to Dolos maintenance and enhancement, with a 15,750 ada Intersect administration fee. It also describes milestone-based disbursement through Intersect treasury tooling and administration via the listed Treasury Reserve Smart Contract stake address.

The review found some claims well supported by the proposal, including the requested amount, budget breakdown, maintainer scope, and planned treasury administration controls. Other claims were only proposer-asserted or thinly evidenced, including key technical claims about what Dolos is, how it connects to Cardano, what it indexes, and which query interfaces it exposes. Adoption and governance context were treated as independently verifiable signals where public references were provided, but they did not remove the treasury-specific evidence requirement.

This is a conservative, evidence-based hold, not a rejection of Dolos. Treasury withdrawals require elevated scrutiny because they spend shared ada and set precedent. A directional vote would be unblocked by pinned, independently verifiable public chain evidence showing the withdrawal does not breach the applicable Net Change Limit, plus stronger replayable evidence for the core technical claims, sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path.

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
- finding: Requested: Fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2, including maintenance, enhancement, community support, and AI-friendly documentation/integration resources over 12 months.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with project administration by Intersect on behalf of TxPipe as vendor
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months at an annual rate of $105,000 USD, Essential maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public developer communication, AI-friendly documentation and integration resources, Milestone-based disbursement controls through Intersect treasury management tooling
- finding: Deadline/expiry: 12 months, beginning after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested maintenance funding includes 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is an open-source lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a traditional full node.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with Cardano-cli and Ogmios.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors, and links to the public GitHub repository.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope covers dependency updates, protocol compatibility, performance improvements, bug fixing, documentation, issue triage, contribution review, ecosystem-feedback enhancements, and AI-friendly documentation and integration resources.
- missing: Independent evidence for: Dolos is an open-source lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a traditional full node.
- missing: Independent evidence for: Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with Cardano-cli and Ogmios.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule, plus 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Dolos is an open-source lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a traditional full node." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: Dolos is an open-source lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a traditional full node.
- Claims and evidence missing: Independent evidence for: Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with Cardano-cli and Ogmios.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `ff984cd206462fa0f1dee333a68d6052fd01aacc345de037f61640385eb8eec6`
- snapshot_bundle_hash: `47f247ef399fd3a6788250d02886159b0a653c847b2956c847e551292274e4f8`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `4be57618f85e778396d883cd24aa46e529b1399c`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.505, "NO": 0.3275, "YES": 0.1675}`

