# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and the required deep-research dossier was not complete enough to support a directional YES or NO.

The action requested 25,400,000 ada for Intersect from June 2026 to June 2027, covering governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and critical process management. The proposal’s basic request was clear and replayable: 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship and incident coordination, and 600,000 ada for critical process management. It also provided support for some key points, including the total funding request, the proposal anchor, prior treasury funding disclosures, treasury smart contract management details, and references to required budget-process voting and net-change-limit checks.

The hold came from gaps in evidence, not from rejecting the purpose of the work. Several important claims remained unsupported or thinly supported, including the claim that the ask was reduced from $7.875M to $6.35M while preserving continuity, and the claim that Intersect has matured into the operational layer described. The treasury analysis was incomplete because it lacked a line-item budget and sustainability path. The risk review was also incomplete because independent assurance and a rollback or remedy path were missing.

This is a conservative, evidence-based hold. A directional vote would require the missing feasibility assessment, alternatives analysis, and failure-mode analysis, along with stronger independent evidence for the unsupported claims, a clearer line-item budget, a sustainability path, independent assurance, and a defined remedy path if delivery fails.

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
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and critical process management for June 2026 to June 2027.
- finding: Recipient: Intersect via the 2026 Treasury Reserve Smart Contract stake address.
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination including core Cardano repos: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 25,400,000 ADA to fund its core operating model for June 2026 to June 2027.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal says the overall ask has been reduced from $7.875M to $6.35M compared with last year while preserving critical continuity functions.
- finding: Claim (adoption, proposer_asserted, medium materiality): Intersect states it has matured over the past two years into a focused operational layer supporting committees, working groups, core Haskell repositories, upgrades, incident response, and community-approved initiatives.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect states it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal claims funding will retain an open coordination layer, a response mechanism for critical unowned issues, and technical stewardship covering releases, incidents, repository management, and bug bounties.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation, audited results, and an audit report.
- missing: Independent evidence for: The proposal says the overall ask has been reduced from $7.875M to $6.35M compared with last year while preserving critical continuity functions.
- missing: Independent evidence for: Intersect states it has matured over the past two years into a focused operational layer supporting committees, working groups, core Haskell repositories, upgrades, incident response, and community-approved initiatives.
- missing: Independent evidence for: Intersect states it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: Independent audits and assurance for the proposal will be provided by Appold, with possible reviews of deliverables, controls, spend validation, and milestone evidence.
- missing: feasibility assessment
- missing: alternatives analysis
- missing: failure-mode analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 25400000
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: not confirmed
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.60
- missing: line-item budget
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: low
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA to fund its core operating model for June 2026 to June 2027." though 3 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal says the overall ask has been reduced from $7.875M to $6.35M compared with last year while preserving critical continuity functions." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing feasibility assessment
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 25400000
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA to fund its core operating model for June 2026 to June 2027." though 3 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional voting is blocked until dossier quality gates pass.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Dossier completeness not confirmed for this treasury proposal.
- Claims and evidence missing: Independent evidence for: The proposal says the overall ask has been reduced from $7.875M to $6.35M compared with last year while preserving critical continuity functions.
- Claims and evidence missing: Independent evidence for: Intersect states it has matured over the past two years into a focused operational layer supporting committees, working groups, core Haskell repositories, upgrades, incident response, and community-approved initiatives.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: missing feasibility assessment
- Synthesis missing: missing alternatives analysis
- Synthesis status is blocked.

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.
- Missing dossier section: feasibility assessment
- Missing dossier section: alternatives analysis
- Missing dossier section: failure-mode analysis

## Reproducibility
- input_hash: `9ed3b81568ea4f09d56e3e05b0fefce48b46dddc698a8453d277a5bdbf044fd3`
- snapshot_bundle_hash: `ba0b622e3b6db51fec6cd8aadb4bca7b039bedf88a5e3d336e6dee2e1fc2bbb9`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

