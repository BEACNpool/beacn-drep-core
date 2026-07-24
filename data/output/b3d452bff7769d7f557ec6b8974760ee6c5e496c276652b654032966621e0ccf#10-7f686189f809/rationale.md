# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.08` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.74` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show public-benefit infrastructure maintenance, cited governance-process references, NCL compliance claims, and described multi-party treasury controls; however, several adoption and delivery-history claims remain proposer-asserted, so the adjustment should stay modest.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal needs an independently verified Net Change Limit check before a directional vote is justified. The proposal may describe useful public infrastructure work, but BEACN treats treasury spending conservatively because it uses shared ADA and sets precedent.

The action requested 540,750 ada for 12 months of part-time UTxO RPC maintenance and enhancement by TxPipe, including protobuf specification maintenance, SDK updates, community support, and AI-friendly documentation. The proposal states that 525,000 ada is for the work and 15,750 ada is an Intersect administration fee, with funds managed through Intersect’s 2026 Treasury Reserve and project-specific smart contracts. The anchor document was available, pinned, and replayable.

Several claims were supported well enough for review: the requested amount and fee structure, the existence of UTxO RPC’s protobuf specification and SDK scope, the open-source repository footprint, the Intersect budget-process support claim, and the described treasury-control structure. Other material claims remained thinner or proposer-asserted, including the uninterrupted 12-month maintainer need, adoption by Amaru, Dingo, and the Haskell Cardano node, prior delivery history, and the status of earlier maintenance funding. The review also found missing clarity on sustainability, cost-benefit, independent assurance, and rollback or remedy paths.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by public, independently verifiable chain evidence confirming that the applicable Net Change Limit is pinned and not breached, plus stronger replayable evidence for the maintainer-scope, adoption, delivery, sustainability, cost-benefit, assurance, and remedy claims.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
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
- finding: Requested: Fund UTxO RPC by TxPipe for 12 months of part-time maintenance and enhancement, including specification, SDK maintenance, community support, and AI-friendly documentation resources.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect on behalf of the vendor TxPipe
- finding: Stated amount: 540,750
- finding: Deliverables: Maintain the protobuf specification, including protocol compatibility, versioning, and documentation., Maintain official SDKs with dependency updates, performance improvements, and bug fixes., Provide community support through issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public communication., Upgrade UTxO RPC compatibility with AI-driven development workflows through AI-friendly documentation and integration resources.
- finding: Deadline/expiry: 12 months; grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement plus a 15,750 ADA Intersect budget administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): The project scope is a 12-month part-time maintainer for UTxO RPC after the existing contract closes, intended to provide uninterrupted maintenance coverage.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC defines common methods, data structures, and communication patterns using Protocol Buffers and provides SDKs for Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories for the core specification, language SDKs, documentation, and provider integrations under the Apache 2.0 open-source license.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and links to voting and audit references.
- missing: Independent evidence for: The project scope is a 12-month part-time maintainer for UTxO RPC after the existing contract closes, intended to provide uninterrupted maintenance coverage.
- missing: Independent evidence for: The proposer states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- missing: Independent evidence for: Prior Intersect 2025 open-source maintenance funding for Pallas, Dolos, and UTxO RPC is stated to be on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement plus a 15,750 ADA Intersect budget administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The project scope is a 12-month part-time maintainer for UTxO RPC after the existing contract closes, intended to provide uninterrupted maintenance coverage." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement plus a 15,750 ADA Intersect budget administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show public-benefit infrastructure maintenance, cited governance-process references, NCL compliance claims, and described multi-party treasury controls; however, several adoption and delivery-history claims remain proposer-asserted, so the adjustment should stay modest.
- Directional treasury voting is blocked until this action is ranked against competing active proposals and verified NCL capacity.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The project scope is a 12-month part-time maintainer for UTxO RPC after the existing contract closes, intended to provide uninterrupted maintenance coverage.
- Claims and evidence missing: Independent evidence for: The proposer states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `7f686189f809ff94f5adf3341acb3f0183639498e30f48d366a835ad93bc619f`
- snapshot_bundle_hash: `bd88187d3b454aef3bbb2b58f33ed45b111921774f757babef4f69e32356c5f0`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `2d4ca1500b8dba4c613121f0e0daabae335dbd3a`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.505, "NO": 0.3275, "YES": 0.1675}`

