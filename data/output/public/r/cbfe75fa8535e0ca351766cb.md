# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s5z9qdza
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show some checkable governance and smart-contract oversight references, but the deterministic assessment is blocked for missing proposal summary, budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's treasury stewardship and evidence-quality priorities, that supports a small cautionary negative nudge rather than a positive adjustment for ecosystem utility claims that remain partly proposer-asserted.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not clear the evidence bar for spending 540,750 ada from shared funds. The proposal had a pinned, replayable anchor and some verifiable governance and smart-contract administration details, but the review still found major gaps in the budget, feasibility, risk, alternatives, failure modes, and community impact analysis.

The request was to fund UTxO RPC by TxPipe for 12 months of open-source maintenance and enhancement, including a part-time maintainer, SDK upkeep, protobuf specification maintenance, community support, AI-friendly documentation, and Intersect administration. The proposal clearly supported the total amount requested: 525,000 ada for UTxO RPC work plus a 15,750 ada Intersect Budget Administration fee. It also supported technical basics about UTxO RPC, including its protobuf-based interface and SDKs across several languages. Intersect budget-process approval, the Net Change Limit check, and the smart-contract administration framework were treated as independently verifiable or supported.

The weaker side was diligence. The review found thin or missing independent evidence for the stated maintainer funding structure, the adoption claims involving Amaru, Dingo, and the Haskell Cardano node, and several key treasury controls. It specifically lacked a line-item budget, a complete budget analysis, a feasibility assessment, risk mitigation evidence, independent assurance, alternatives analysis, failure-mode analysis, and community impact analysis. Execution risk was marked unknown, and a flag score reduced confidence.

Because this was a treasury withdrawal, BEACN applied elevated scrutiny. The strongest YES case was that the proposal did substantiate the total amount and included Intersect oversight, but seven review blockers remained open. With the treasury diligence dossier incomplete and the broader treasury flow signal in an unsustainable regime, BEACN judged that the cost and precedent risk outweighed the supported case and voted NO.

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
- finding: Requested: Fund UTxO RPC by TxPipe for open-source maintenance and enhancement over 12 months, including a part-time maintainer and Intersect administration.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe
- finding: Stated amount: 540,750
- finding: Deliverables: Maintenance of the protobuf specification, including protocol compatibility, versioning, and documentation., Maintenance of official SDKs, including dependency updates, performance improvements, and bug fixing., Community support, including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication., AI-friendly documentation and integration resources for AI-driven development workflows.
- finding: Deadline/expiry: 12 months after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (economic, proposer_asserted, high materiality): The motivation text describes the core request as 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC defines common methods, data structures, and communication patterns using Protocol Buffers and provides SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface, validating it as an ecosystem standard.
- finding: Claim (technical, proposer_asserted, medium materiality): The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission.
- missing: Independent evidence for: The motivation text describes the core request as 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD.
- missing: Independent evidence for: The proposal states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface, validating it as an ecosystem standard.
- missing: Independent evidence for: The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The motivation text describes the core request as 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show some checkable governance and smart-contract oversight references, but the deterministic assessment is blocked for missing proposal summary, budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's treasury stewardship and evidence-quality priorities, that supports a small cautionary negative nudge rather than a positive adjustment for ecosystem utility claims that remain partly proposer-asserted.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The motivation text describes the core request as 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD.
- Claims and evidence missing: Independent evidence for: The proposal states that UTxO RPC has been adopted by Amaru, Dingo, and the Haskell Cardano node as a query interface, validating it as an ecosystem standard.
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
- input_hash: `69f3a0e901db3ab4b391f3febcfea7f2a17a9cc2e4806f81c85899eefb755404`
- snapshot_bundle_hash: `efe0f9a3f3a1d74840d74d8eb150d35f2ba72e7920ef2fefc1dc7bfcf4ae9d33`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1218`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

