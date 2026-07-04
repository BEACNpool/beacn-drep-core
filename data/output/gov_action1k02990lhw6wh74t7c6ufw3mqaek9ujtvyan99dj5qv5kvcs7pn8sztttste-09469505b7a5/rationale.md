# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sztttste
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): A small negative nudge is justified because the request is a sizable treasury withdrawal and the assessment says treasury analysis is incomplete and risk review is thin, with missing budget, feasibility, alternatives, and failure-mode analysis. The proposal provides useful implementation and oversight detail, but the doctrine prioritizes treasury stewardship and evidence quality over public-benefit growth when evidence is incomplete.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a sizable treasury withdrawal with an incomplete evidence record: the review found missing budget, feasibility, risk, alternatives, failure-mode, and community impact analysis.

The action requested 540,750 ada for “Dolos by TxPipe: Maintaining Cardano’s Lightweight Data Node, Year 2,” covering 12 months of part-time maintenance, community support, AI-friendly documentation and integration resources, and Intersect administration. The proposal said the funding included 420,000 ada plus a 105,000 ada contingency reserve for a part-time maintainer, with a total budget of 525,000 ada for Dolos work and 15,750 ada for Intersect’s administration fee. Those budget totals were supported in the proposal, and the anchor document was available and replayable.

The proposal also claimed Dolos is a lightweight Rust-based Cardano data node that provides efficient access to chain data and exposes several query interfaces. Those technical claims were treated as proposer assertions, but the review found independent evidence missing for the core claim that Dolos provides resource-efficient chain access without running a full node, and for the claimed network and query-interface capabilities. The proposal did provide useful governance context, including Intersect process support, claimed threshold approval in the Hydra Voting phase, oversight, reporting obligations, and milestone-based controls.

The review passed the basic intake and anchor checks, and it recognized the strongest YES case: the request clearly substantiates funding for a part-time Dolos maintainer over 12 months. But treasury withdrawals require elevated scrutiny because they spend shared ADA and set precedent. Here, the treasury analysis was incomplete, the risk review was thin, execution risk was unknown, and seven review blockers remained open. On that evidence, BEACN concluded the cost and uncertainty outweighed the supported case for approval.

## Review Tree
- overall_status: `blocked`

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2, including part-time maintenance over 12 months and Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe.
- finding: Stated amount: 540,750
- finding: Deliverables: WP1 - Dolos Maintenance and Enhancement, Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, feedback-driven enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows, Intersect budget administration and oversight
- finding: Deadline/expiry: 12 months; new grant period begins after closure of existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget summary totals 540,750 ADA, consisting of 525,000 ADA for Dolos maintenance and enhancement and 15,750 ADA for an Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a full node.
- finding: Claim (technical, proposer_asserted, medium materiality): Dolos is claimed to connect directly to the Cardano network, index ledger primitives, and expose five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros Node-to-Client Unix socket.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal states the work will cover maintenance, community support, and AI-friendly documentation and integration resources.
- missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a full node.
- missing: Independent evidence for: Dolos is claimed to connect directly to the Cardano network, index ledger primitives, and expose five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros Node-to-Client Unix socket.
- missing: Independent evidence for: The proposal states TxPipe has received funding through 30 Project Catalyst proposals, with 26 successfully delivered and 4 under development and on schedule, and that prior Intersect-funded Pallas, Dolos, and UTxO RPC maintenance is being delivered on schedule.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 540.8k ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a full node." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 540.8k ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small negative nudge is justified because the request is a sizable treasury withdrawal and the assessment says treasury analysis is incomplete and risk review is thin, with missing budget, feasibility, alternatives, and failure-mode analysis. The proposal provides useful implementation and oversight detail, but the doctrine prioritizes treasury stewardship and evidence quality over public-benefit growth when evidence is incomplete.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Dolos is described as a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without running a full node.
- Claims and evidence missing: Independent evidence for: Dolos is claimed to connect directly to the Cardano network, index ledger primitives, and expose five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros Node-to-Client Unix socket.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `09469505b7a5d2c8c2f281e9d4afd701ff12c970b5e830f19234233eaf21031f`
- snapshot_bundle_hash: `b226301ae7b9627443b6cf2a26067f505d6e3ef91c6ed168abb7e4d94afb7712`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `960`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

