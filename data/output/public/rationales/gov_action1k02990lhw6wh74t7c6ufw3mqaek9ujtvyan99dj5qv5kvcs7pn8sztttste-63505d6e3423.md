# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sztttste
Recommendation: **NO**
Score: `-0.3733` (raw `-0.3533` + doctrine-LLM nudge `-0.02`) | Confidence: `0.6633` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has meaningful public-benefit alignment and several independently checkable governance and on-chain references, but the treasury analysis is marked incomplete and the budget justification is thin relative to the requested amount, especially because the maintenance labor rate and contingency are asserted without detailed cost breakdown or milestone pricing. A small cautionary negative adjustment is warranted for treasury stewardship and evidence quality, without overriding the deterministic gates.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not meet the higher evidence bar for spending shared ADA: the budget justification and treasury analysis were incomplete, and key claims remained unsupported.

The action requested 540,750 ada to fund Year 2 maintenance of Dolos by TxPipe: 420,000 ada for maintenance, 105,000 ada as contingency, and 15,750 ada for Intersect administration. The proposal described 12 months of part-time maintenance, including dependency updates, Cardano protocol compatibility, performance improvements, bug fixes, documentation, issue triage, contribution review, public communication, and AI-friendly integration resources. It also included oversight and milestone-based disbursement controls through Intersect administration, third-party oversight, and the Sundae Labs treasury management smart contract framework.

Several points were well-supported: the pinned anchor document was available, the requested amount was clear, Dolos’ listed interfaces and maintenance scope were supported in the proposal, and governance/on-chain process claims had independently checkable references. The proposal also had evidence that Dolos is open-source and has public development activity. However, important claims were not independently supported, including the claim that Dolos provides resource-efficient access to chain data without the overhead of traditional full nodes, and claims about TxPipe’s past Catalyst delivery record and 2025 maintenance delivery status.

The review gates raised treasury-specific concerns. Treasury actions require elevated scrutiny, and this review found the treasury diligence dossier incomplete, missing a sustainability path and clear cost-benefit justification. The risk review was also incomplete, with missing independent assurance and no clear rollback or remedy path. Even though the strongest YES case was acknowledged, BEACN’s evidence-based process judged that the unsupported claims, thin cost justification, incomplete treasury review, and broader treasury sustainability signal outweighed the case for approval.

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
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe as vendor.
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months after the existing contract closes., Essential maintenance of the codebase including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation., Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public communication., AI-friendly documentation and integration resources for AI-driven development workflows.
- finding: Deadline/expiry: 12 months; exact start and end dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without the overhead of traditional full nodes.
- finding: Claim (technical, supported_in_proposal, high materiality): Dolos connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with existing tooling.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer will perform dependency updates, Cardano protocol compatibility work, performance improvements, bug fixes, documentation, issue triage, contribution review, ecosystem-feedback enhancements, public communication, and AI-friendly integration resources.
- finding: Claim (adoption, independently_verifiable, medium materiality): Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors, and remains fully open-source.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission under the approved Budget Process Framework.
- missing: Independent evidence for: Dolos is a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without the overhead of traditional full nodes.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule, and its 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC is being delivered on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.68
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Dolos is a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without the overhead of traditional full nodes." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 540750
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has meaningful public-benefit alignment and several independently checkable governance and on-chain references, but the treasury analysis is marked incomplete and the budget justification is thin relative to the requested amount, especially because the maintenance labor rate and contingency are asserted without detailed cost breakdown or milestone pricing. A small cautionary negative adjustment is warranted for treasury stewardship and evidence quality, without overriding the deterministic gates.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Dolos is a lightweight Cardano data node built in Rust that provides resource-efficient access to chain data without the overhead of traditional full nodes.
- Claims and evidence missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule, and its 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC is being delivered on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `63505d6e34235734c8e2eabe5bcdc77a1dec03e02175dfce2e280a0cf2584bdc`
- snapshot_bundle_hash: `d7fc081cae2a0d923f0e874875bab398c02ef30925237ab401c6e68d2b4fd627`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `31`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2033, "NO": 0.7538, "YES": 0.0429}`

