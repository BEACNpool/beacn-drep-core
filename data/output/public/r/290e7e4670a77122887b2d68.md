# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.077` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7392` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit infrastructure maintenance and documented governance/process references, while several important adoption and delivery-history assertions remain proposer-stated rather than evidenced within the document; the deterministic assessment already marked the review ready, so no additional directional nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the project.

The action requests 540,750 ada for year-two UTxO RPC maintenance by TxPipe, submitted by Intersect on behalf of the vendor. The proposal says this covers 525,000 ada for 12 months of maintenance and enhancement, plus a 15,750 ada Intersect administration fee. The funded work would include maintaining the protobuf specification, official SDKs, community support, issue triage, contribution review, public communication, and AI-friendly documentation resources.

Several core facts were well-supported: the requested amount and fee structure, the annual maintenance funding model, the technical description of UTxO RPC, the pinned and replayable proposal anchor, Intersect Budget Process support, and the stated treasury administration setup using Sundae Labs smart contracts. But important claims remained thin or unsupported by independent evidence, including adoption by Amaru, Dingo, and the Haskell Cardano node, and the claim that the project maintains more than 10 Apache 2.0 open-source repositories across the specification, SDKs, documentation, and integrations.

Because this is a treasury withdrawal, BEACN applies a higher evidence bar. The review also noted stressed treasury-flow conditions, missing sustainability and cost-benefit clarity, unknown execution risk, no independent assurance, and no clear rollback or remedy path. A directional vote would be unblocked by pinned, independently verifiable public chain evidence for the Net Change Limit, plus stronger replayable evidence for the adoption and repository claims and clearer treasury-risk mitigations.

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
- finding: Requested: Fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2, including 12 months of part-time maintenance and enhancement plus administration fee.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe/vendor
- finding: Stated amount: 540750
- finding: Deliverables: Maintenance of the protobuf specification, including protocol compatibility, versioning, and documentation, Maintenance of official SDKs, including dependency updates, performance improvements, and bug fixing, Community support, issue triage, contribution review, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months; grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The maintainer funding is described as 420,000 ADA plus a 105,000 ADA contingency reserve for 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification for UTxO-based blockchains using Protocol Buffers and SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem.
- finding: Claim (technical, proposer_asserted, medium materiality): The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission.
- missing: Independent evidence for: The proposer states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem.
- missing: Independent evidence for: The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: The proposer states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem.
- Claims and evidence missing: Independent evidence for: The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `a4de2cad73d186752dd61385ac794e1ad7273184bef2172e90cab90272a12ad9`
- snapshot_bundle_hash: `2aa80de7274f001671ca1d306d3e7a5d04753ad3012ecbd6f11034a7ed63a746`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `3e3c343fc0dd14a03a92aad1216ba6620b3d0185`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5048, "NO": 0.1706, "YES": 0.3246}`

