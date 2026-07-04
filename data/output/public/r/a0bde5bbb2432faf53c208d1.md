# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sztttste
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal describes a plausible public-benefit open-source infrastructure maintenance effort and includes budget, scope, governance-process references, and smart-contract oversight mechanics, but the deterministic assessment identifies missing budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis. Given the large treasury withdrawal and BEACN's caution-first treasury doctrine, the evidence quality does not justify a positive nudge beyond the engine's captured blockers.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and the review left too many core diligence gaps unresolved, especially around budget analysis, feasibility, risk, alternatives, failure modes, and community impact.

The action requested 540,750 ada to fund Year 2 maintenance and enhancement of TxPipe’s Dolos project through a 12-month part-time maintainer arrangement. The proposal said the withdrawal included 525,000 ada for Dolos maintenance and enhancement, plus a 15,750 ada Intersect administration fee. It described work on dependency updates, Cardano protocol compatibility, performance improvements, bug fixes, documentation, issue triage, contribution review, public developer communication, and AI-friendly integration resources.

Several claims were supported by the proposal or independently checkable context. The requested amount, the stated maintainer rate, the maintenance scope, the Intersect budget process support threshold, and the fact that the withdrawal did not breach the applicable net change limit were all treated as supported or verifiable. But important technical claims about what Dolos is and how it works were still treated as proposer assertions without independent evidence in the review. The claims-and-evidence section was thin, the risk review was thin, and the treasury analysis was incomplete.

The strongest case for YES was that the proposal did substantiate its basic funding request for a part-time maintainer. But treasury actions require elevated scrutiny because they spend shared ada and set precedent. In this review, seven blockers remained open: missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis. With those gaps still present, BEACN’s conservative treasury standard led to a NO vote.

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
- finding: Requested: Treasury withdrawal to fund Dolos by TxPipe maintenance and enhancement for Year 2, submitted by Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months, Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, feedback-driven enhancements, and public developer communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months; new grant period begins after closure of existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The total treasury withdrawal is 540,750 ADA, consisting of 525,000 ADA for Dolos Maintenance and Enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C Unix socket compatible with Cardano-cli and Ogmios.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposer states that Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed maintenance scope includes dependency updates, protocol compatibility, performance improvements, bug fixing, documentation, issue triage, contribution review, feedback-driven enhancements, public communication, and AI-friendly documentation and integration resources.
- missing: Independent evidence for: Dolos is a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- missing: Independent evidence for: Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C Unix socket compatible with Cardano-cli and Ogmios.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 successfully delivered and 4 currently under development and on schedule.
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
- finding: Strongest NO: a material claim is unsupported — "Dolos is a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes." — so cost or precedent may outweigh the benefit.
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
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal describes a plausible public-benefit open-source infrastructure maintenance effort and includes budget, scope, governance-process references, and smart-contract oversight mechanics, but the deterministic assessment identifies missing budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis. Given the large treasury withdrawal and BEACN's caution-first treasury doctrine, the evidence quality does not justify a positive nudge beyond the engine's captured blockers.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Dolos is a lightweight Cardano data node built in Rust that provides efficient access to chain data without the overhead of traditional full nodes.
- Claims and evidence missing: Independent evidence for: Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C Unix socket compatible with Cardano-cli and Ogmios.
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
- input_hash: `322f535ead770120b0fe241372630462da3b70e2d35c40755a3cb752d1fe0d2a`
- snapshot_bundle_hash: `a8b6668bf2256690ba054b4505e650154bbf3cce7cf2643377892b9b37c06ab8`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1217`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

