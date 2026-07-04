# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s5z9qdza
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims describe useful open-source infrastructure and some checkable governance and custody controls, but the deterministic assessment is blocked by missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's treasury doctrine, evidence quality and treasury stewardship justify a small cautionary negative nudge rather than a positive lean toward spending.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not clear the evidence bar for spending shared ADA. The proposal describes useful open-source infrastructure, but the review found too many unresolved gaps in budget detail, feasibility, risk, alternatives, failure modes, and community impact.

The action requested 540,750 ada for Year 2 maintenance and enhancement of UTxO RPC by TxPipe. The proposal said this total included 420,000 ada for work, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee. It also described a 12-month part-time maintainer role, maintenance of the protobuf specification and official SDKs, community support, AI-friendly documentation, and milestone-based controls through Intersect budget management smart contracts.

Several core claims were supported in the proposal or independently checkable: the amount requested, the basic maintainer scope, the technical description of UTxO RPC, the open-source repository footprint, the Intersect budget-process support threshold, the Net Change Limit statement, and the planned treasury-management structure. But important adoption and delivery-record claims remained unsupported by independent evidence in the review, including the claim that Amaru, Dingo, and the Haskell Cardano node had adopted UTxO RPC as a query interface, and the claim about TxPipe’s past Catalyst and Intersect delivery record.

Because this is a treasury withdrawal, BEACN applied elevated scrutiny. The pinned anchor was available and the proposal had a defensible YES case on the stated funding breakdown, but the review gates for treasury analysis, risk review, and synthesis were incomplete or blocked. In particular, the review was missing a complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis. On the available evidence, BEACN judged that treasury stewardship and precedent risk outweighed the case for approval.

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
- finding: Requested: Treasury withdrawal to fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2, including maintenance and enhancement plus Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for UTxO RPC over 12 months, Maintenance of the protobuf specification, including compatibility, versioning, and documentation, Maintenance of official SDKs, including dependency updates, performance improvements, and bug fixing, Community support, issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows, Milestone-based disbursement controls through Intersect budget management smart contracts
- finding: Deadline/expiry: 12 months after closure of existing contract; exact dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (economic, supported_in_proposal, high materiality): The funded work is a part-time UTxO RPC maintainer for 12 months at an annual rate of $105,000 USD, beginning after the existing contract closes.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification using Protocol Buffers with SDKs in Rust, Go, Node.js, .NET, Haskell, and Python to standardize interactions with UTxO-based blockchains.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories covering the core specification, language SDKs, documentation, and provider integrations, and is open source under Apache 2.0.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope includes protobuf specification maintenance, official SDK maintenance, community support, and AI-friendly documentation and integration resources.
- missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard.
- missing: Independent evidence for: TxPipe is reported to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule, plus 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims describe useful open-source infrastructure and some checkable governance and custody controls, but the deterministic assessment is blocked by missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's treasury doctrine, evidence quality and treasury stewardship justify a small cautionary negative nudge rather than a positive lean toward spending.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard.
- Claims and evidence missing: Independent evidence for: TxPipe is reported to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development and on schedule, plus 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule.
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
- input_hash: `fc810db8c87911dee8ce37aa2dd4d029269be0119df1d10a8de562338767def2`
- snapshot_bundle_hash: `117fb7a9ed71ef9a7ac0da5a0e0bb9bc83c66e7a06609bd5a97e2e9e2f0fdeb6`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `960`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

