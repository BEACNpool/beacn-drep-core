# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sgx6wlxf
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims show meaningful public-benefit and protocol-continuity alignment, plus some independently verifiable governance, NCL, prior-funding, and contract-management references. However, the deterministic assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a very large treasury withdrawal, so the conservative nudge is toward treasury stewardship and evidence caution rather than additional spending confidence.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a very large treasury withdrawal and the review found too many unresolved evidence gaps around budget detail, feasibility, risk, alternatives, failure modes, and community impact.

The proposal requested 25,400,000 ada for Intersect’s June 2026 to June 2027 operating model. It described three work packages: 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship, incident response, release coordination, and core repository work, and 600,000 ada for management of critical processes. It also proposed smart-contract-based budget administration, milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance by Appold.

Several basic facts were supported or independently checkable: the anchor document was available, the requested amount and work package split were stated in the proposal, the proposal referenced the 2026 Intersect Budget Process Hydra Voting result, said the withdrawal did not breach the applicable Net Change Limit, disclosed prior Cardano Treasury funding to Intersect and its committees, and described treasury contract tooling and oversight arrangements. But other important claims remained unsupported or thin, including the claim that the ask was more focused than last year while preserving continuity, and the claim that Intersect had matured into a focused operational layer across committees, repositories, upgrades, incident response, and community-approved initiatives.

The strongest case for YES was that the proposal clearly substantiated the basic funding request and described public-benefit continuity work. However, treasury withdrawals require elevated scrutiny because they spend shared ada and set precedent. With the treasury diligence dossier incomplete, execution risk unknown, missing budget and risk analysis, thin evidence status, and seven decisive blockers still open, BEACN judged that the cost and uncertainty outweighed the supported benefits and voted NO.

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
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, operations, ecosystem coordination, and management of critical processes for June 2026 to June 2027.
- finding: Recipient: Intersect via the 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 25400000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination including core Cardano repositories: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Use of a Treasury Reserve Smart Contract and one Project-Specific Smart Contract for budget administration, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance by Appold
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 25,400,000 ADA for its core operating model covering June 2026 to June 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 6,000,000 ADA for operations and ecosystem coordination, 18,800,000 ADA for technical stewardship, incident response and coordination, and 600,000 ADA for management of critical processes.
- finding: Claim (economic, proposer_asserted, medium materiality): Intersect says the proposal is more focused than last year and reduces the overall ask from $7.875M to $6.35M while preserving critical continuity functions.
- finding: Claim (adoption, proposer_asserted, medium materiality): Intersect states it has matured over the past two years into a focused operational layer supporting committees and working groups, core Haskell repository stewardship, upgrades, incident response, and administration of community-approved initiatives.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal claims it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and references voting documentation, final audited results, and an audit report.
- missing: Independent evidence for: Intersect says the proposal is more focused than last year and reduces the overall ask from $7.875M to $6.35M while preserving critical continuity functions.
- missing: Independent evidence for: Intersect states it has matured over the past two years into a focused operational layer supporting committees and working groups, core Haskell repository stewardship, upgrades, incident response, and administration of community-approved initiatives.
- missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews of deliverables, controls, spend validation, and milestone evidence.
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA for its core operating model covering June 2026 to June 2027." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Intersect says the proposal is more focused than last year and reduces the overall ask from $7.875M to $6.35M while preserving critical continuity functions." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA for its core operating model covering June 2026 to June 2027." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims show meaningful public-benefit and protocol-continuity alignment, plus some independently verifiable governance, NCL, prior-funding, and contract-management references. However, the deterministic assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a very large treasury withdrawal, so the conservative nudge is toward treasury stewardship and evidence caution rather than additional spending confidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Intersect says the proposal is more focused than last year and reduces the overall ask from $7.875M to $6.35M while preserving critical continuity functions.
- Claims and evidence missing: Independent evidence for: Intersect states it has matured over the past two years into a focused operational layer supporting committees and working groups, core Haskell repository stewardship, upgrades, incident response, and administration of community-approved initiatives.
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
- input_hash: `01529d6898ec92f7338c3f052f003dbacb40d0f2f02a4bfdd855c4c05be34897`
- snapshot_bundle_hash: `6ef1e75020cce31b97dbc77cad40c02d565c5fd785a06f6b785328768e21529c`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `960`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

