# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#1
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1359` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.754` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show a public-benefit open-source infrastructure maintenance ask with concrete scope, budget breakdown, checkable governance-process references, NCL compliance assertions, and fund-control mechanisms; the nudge stays small because several delivery-history and strategic-alignment claims remain proposer-asserted and the maintainer deliverables are broad.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal requests 540,750 ada for Year 2 of Dolos by TxPipe: 525,000 ada for 12 months of part-time maintenance and enhancement, plus 15,750 ada for Intersect budget administration. The proposal describes Dolos as a lightweight Cardano data node with several query interfaces, and its maintenance scope includes protocol compatibility, dependency updates, performance improvements, bug fixes, documentation, community support, and AI-friendly integration resources. The budget breakdown, technical scope, public GitHub metrics, Intersect voting references, stated NCL compliance, and fund-control design were treated as checkable or well-supported from the proposal materials.

The hold is conservative and evidence-based, not a rejection of Dolos. Several items still need stronger independent support, including the claimed alignment with Intersect Strategic Pillar 2, TxPipe’s delivery-history claims, a clearer sustainability path, stronger cost-benefit clarity, independent assurance, and a rollback or remedy path. Execution risk was also marked unknown, and treasury withdrawals receive elevated scrutiny because they spend shared ada and set precedent.

A directional YES or NO would be unblocked by pinned, independently verifiable public chain evidence for the applicable Net Change Limit, plus stronger independent evidence for the remaining strategic-alignment, delivery-history, risk, sustainability, and remedy questions. Until then, BEACN’s vote remains NEEDS_MORE_INFO to avoid overstating certainty.

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
- finding: Requested: Fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2, including 12 months of part-time maintenance and enhancement plus Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, for TxPipe/Dolos via Intersect budget administration
- finding: Stated amount: 540,750
- finding: Deliverables: WP1 - Dolos Maintenance and Enhancement for 525,000 ADA, Essential maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows, Intersect Budget Administration fee for 15,750 ADA
- finding: Deadline/expiry: 12 months; new grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement and 15,750 ADA for Intersect budget administration.
- finding: Claim (economic, supported_in_proposal, high materiality): The motivation states the grant covers 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): Dolos is described as a lightweight Cardano data node in Rust that provides chain-data access without full-node overhead and exposes multiple query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C socket.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors, and links to the public GitHub repository for verification.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope includes dependency updates, protocol compatibility, performance improvements, bug fixes, documentation, issue triage, contribution review, community communication, and AI-friendly documentation and integration resources.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal asserts Dolos aligns with Intersect Strategic Pillar 2 focus area A.3 for Developer Experience and open-source infrastructure maintenance.
- missing: Independent evidence for: The proposal asserts Dolos aligns with Intersect Strategic Pillar 2 focus area A.3 for Developer Experience and open-source infrastructure maintenance.
- missing: Independent evidence for: The proposal states TxPipe previously received funding through 30 Project Catalyst proposals, with 26 delivered and 4 currently under development and on schedule, plus 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement and 15,750 ADA for Intersect budget administration." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal asserts Dolos aligns with Intersect Strategic Pillar 2 focus area A.3 for Developer Experience and open-source infrastructure maintenance." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement and 15,750 ADA for Intersect budget administration." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show a public-benefit open-source infrastructure maintenance ask with concrete scope, budget breakdown, checkable governance-process references, NCL compliance assertions, and fund-control mechanisms; the nudge stays small because several delivery-history and strategic-alignment claims remain proposer-asserted and the maintainer deliverables are broad.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal asserts Dolos aligns with Intersect Strategic Pillar 2 focus area A.3 for Developer Experience and open-source infrastructure maintenance.
- Claims and evidence missing: Independent evidence for: The proposal states TxPipe previously received funding through 30 Project Catalyst proposals, with 26 delivered and 4 currently under development and on schedule, plus 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `46f4090b255f88cc079e2b6d3e6c4cd13cb4e43e3b960ea815c93c38dbfeb612`
- snapshot_bundle_hash: `492965c746f99cd8cb8d2e48c327504b8be3632243a86d1e746ec6aafa8bd5a9`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5085, "NO": 0.1099, "YES": 0.3816}`

