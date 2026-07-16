# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1359` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.754` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims describe ongoing open-source infrastructure maintenance, concrete deliverables, public repositories and governance references, and structured oversight for fund administration; the nudge remains small because several material delivery and prior-performance claims are proposer-asserted rather than independently verified within the supplied text.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal needs independently verified Net Change Limit evidence before BEACN can cast a directional vote. This is a conservative, evidence-based hold: treasury actions spend shared ADA, so BEACN requires the applicable limit to be pinned and checked from public chain evidence, not just asserted in the proposal.

The action asks to withdraw 540,750 ada to fund Year 2 maintenance of Dolos by TxPipe, a lightweight Cardano data node. The proposal says this includes 525,000 ada for maintenance and enhancement plus a 15,750 ada Intersect administration fee. It describes 12 months of part-time maintenance after the current contract closes, including dependency updates, protocol compatibility, performance improvements, bug fixes, documentation, issue triage, review of outside contributions, ecosystem-feedback improvements, public developer communication, and AI-friendly integration resources.

Several core claims were supported well enough for review: the requested amount and fee split were stated clearly, the technical description of Dolos and its maintenance scope was supported in the proposal, the GitHub activity figures were tied to a checkable repository link, the Intersect budget-process support claim had referenced voting and audit materials, and the fund administration plan included smart-contract addresses, oversight, audit references, and a dashboard. Other claims remained thinner: the alignment with Pillar 2 developer experience and TxPipe’s prior delivery record were proposer-asserted rather than independently verified in the supplied review.

The proposal passed intake because the pinned anchor document was available and replayable, and it had a credible strongest-YES case around the defined amount, scope, and evidence gates. But the treasury review applied a higher bar, with stressed treasury-flow conditions noted, no sustainability path or cost-benefit clarity supplied, execution risk unknown, and no independent assurance or rollback/remedy path identified. A directional YES or NO would be unblocked by pinned, independently verified public chain evidence that the withdrawal fits within the applicable Net Change Limit, along with stronger independent support for the currently asserted alignment, prior-performance, treasury-sustainability, and risk-mitigation claims.

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
- finding: Requested: Treasury withdrawal to fund Dolos by TxPipe for maintaining Cardano's lightweight data node for Year 2.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor TxPipe
- finding: Stated amount: 540,750
- finding: Deliverables: 12 months of part-time Dolos maintenance after the existing contract closes, Dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public developer communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months; exact dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The motivation describes the project funding as 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): Dolos is described as a lightweight Cardano data node in Rust that connects directly to the Cardano network, indexes ledger primitives, and exposes multiple query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and Ouroboros N2C compatibility.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposer states that Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors, and provides the Dolos GitHub repository link as a checkable source.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope includes codebase maintenance, protocol compatibility, performance work, bug fixing, documentation, community support, contribution review, and AI-friendly documentation and integration resources.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer states that Dolos aligns with Pillar 2 focus area A.3 Developer Experience by maintaining open-source Cardano infrastructure and improving resource-efficient access to chain data.
- missing: Independent evidence for: The proposer states that Dolos aligns with Pillar 2 focus area A.3 Developer Experience by maintaining open-source Cardano infrastructure and improving resource-efficient access to chain data.
- missing: Independent evidence for: The proposal says TxPipe previously received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development on schedule, and also received 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC that is being delivered on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that Dolos aligns with Pillar 2 focus area A.3 Developer Experience by maintaining open-source Cardano infrastructure and improving resource-efficient access to chain data." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims describe ongoing open-source infrastructure maintenance, concrete deliverables, public repositories and governance references, and structured oversight for fund administration; the nudge remains small because several material delivery and prior-performance claims are proposer-asserted rather than independently verified within the supplied text.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposer states that Dolos aligns with Pillar 2 focus area A.3 Developer Experience by maintaining open-source Cardano infrastructure and improving resource-efficient access to chain data.
- Claims and evidence missing: Independent evidence for: The proposal says TxPipe previously received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development on schedule, and also received 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC that is being delivered on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `0a0f9fea2f835e599e499eb03b14b030fe10fab4c3d8b804416b824ce35f9f59`
- snapshot_bundle_hash: `d9a536d40b98b5c103a99be58661ab650d9fe8d9c9b367649c81774c8df07507`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5085, "NO": 0.1099, "YES": 0.3816}`

