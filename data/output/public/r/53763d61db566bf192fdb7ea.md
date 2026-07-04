# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sgx6wlxf
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): The anchor includes useful public-benefit and governance-alignment claims, budget categories, voting references, prior funding disclosure, and custody mechanics, but the deterministic assessment remains blocked because core treasury diligence is incomplete, including budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's hierarchy, a large treasury withdrawal with incomplete evidence warrants a small cautionary negative nudge rather than rewarding plausible ecosystem value.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large 25,400,000 ada treasury withdrawal and the review found the core treasury diligence incomplete. The proposal had a pinned, replayable anchor and described public-benefit work, but the evidence package did not meet the higher bar BEACN applies when shared treasury funds are being spent.

The action requested funding for Intersect from June 2026 to June 2027, covering governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and critical process management. The proposal broke the ask into 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship and incident response, and 600,000 ada for critical processes. It also described milestone-based drawdowns, Appold assurance, transparent reporting, and use of Sundae Labs treasury management smart contracts.

Several basic claims were supported in the proposal: the amount requested, the work packages, the intended recipient address, prior treasury funding disclosures, and the custody mechanics. Some claims were presented as independently verifiable, including Intersect budget-process voting support and the claim that the request did not breach the applicable 350M Net Change Limit. But important claims remained unsupported or thin, including the claimed year-over-year budget reduction and Intersect’s claimed role in prior network upgrades and the November 2025 chain partition incident.

The decisive issue was not that the work was unimportant; it was that the review gates were not complete. BEACN found missing or incomplete budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, community impact analysis, mitigation evidence, and independent assurance. Treasury flow was also in an unsustainable regime, adding caution. With seven review blockers still open, BEACN judged that the cost, precedent, and incomplete evidence outweighed the substantiated case for funding, so the vote was NO.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 25.40M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and management of critical processes for June 2026 to June 2027.
- finding: Recipient: Intersect via the 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v.
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination, including core Cardano repositories: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, External assurance by Appold, Milestone-based drawdowns, evidence-backed reporting, and transparent disclosures, Use of Sundae Labs treasury management smart contract framework with TRSC and PSSC addresses
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 25,400,000 ADA for its core operating model covering governance coordination, technical stewardship, incident response, release coordination, and critical unowned processes from June 2026 to June 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 6,000,000 ADA for operations and ecosystem coordination, 18,800,000 ADA for technical stewardship and incident response, and 600,000 ADA for management of critical processes.
- finding: Claim (economic, proposer_asserted, medium materiality): Intersect states that this year's ask is reduced from $7.875M to $6.35M compared with the previous year while preserving functions critical to Cardano continuity and maturity.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and links to voting documentation, audited results, and an audit report.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal claims the requested amount does not, at submission and either alone or in aggregate, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713.
- missing: Independent evidence for: Intersect states that this year's ask is reduced from $7.875M to $6.35M compared with the previous year while preserving functions critical to Cardano continuity and maturity.
- missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
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
- finding: Requested ADA: 25.40M ADA
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA for its core operating model covering governance coordination, technical stewardship, incident response, release coordination, and critical unowned processes from June 2026 to June 2027." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Intersect states that this year's ask is reduced from $7.875M to $6.35M compared with the previous year while preserving functions critical to Cardano continuity and maturity." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 25.40M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA for its core operating model covering governance coordination, technical stewardship, incident response, release coordination, and critical unowned processes from June 2026 to June 2027." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The anchor includes useful public-benefit and governance-alignment claims, budget categories, voting references, prior funding disclosure, and custody mechanics, but the deterministic assessment remains blocked because core treasury diligence is incomplete, including budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's hierarchy, a large treasury withdrawal with incomplete evidence warrants a small cautionary negative nudge rather than rewarding plausible ecosystem value.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Intersect states that this year's ask is reduced from $7.875M to $6.35M compared with the previous year while preserving functions critical to Cardano continuity and maturity.
- Claims and evidence missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
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
- input_hash: `6a43f7a13e1c669c9f99e39800bcb2795c5abb59fa6f57121aee90d4bd491ed6`
- snapshot_bundle_hash: `88d63ee0b62d6e506fa7bab49f56cda4f8925ec3448fc0b75051b0453dbd3480`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1218`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

