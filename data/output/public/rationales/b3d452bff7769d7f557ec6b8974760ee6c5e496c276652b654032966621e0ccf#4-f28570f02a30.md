# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **NEEDS_MORE_INFO**
Score: `0.185` (binding treasury composite; advisory raw signal `-0.53`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7662` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims include high-materiality public-benefit and protocol-continuity assertions, but the deterministic assessment is already ready and the strongest due-diligence questions around treasury stewardship, verification, and NCL compliance are mechanical or independently checkable rather than suitable for an extra discretionary nudge.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the proposal.

The action asks to withdraw 25,400,000 ada for Intersect’s June 2026 to June 2027 operating model, including governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and management of critical processes. The funds would go to the 2026 Treasury Reserve Smart Contract stake address. The proposal also describes milestone-based drawdowns, evidence-backed reporting, transparent disclosures, external assurance, and use of the Sundae Labs treasury management smart contract framework.

Some core claims were supported or independently verifiable: the requested amount and purpose were clear, the anchor document was pinned and replayable, prior treasury funding was disclosed, the proposal referenced Intersect budget-process voting documentation, and the treasury smart contract structure included addresses, documentation, repository references, and audits. Other claims remained unsupported or thin, including the claimed budget reduction from last year, the preservation of critical functions, details on Intersect’s operational work, sustainability path, cost-benefit clarity, independent assurance, and dependency mapping.

Because this is a treasury withdrawal, BEACN applies elevated scrutiny. The review found that claims must be tied to replayable public evidence, and proposer assertions alone are not enough. A YES or NO vote would be unblocked by independently pinned public-chain evidence showing the applicable Net Change Limit status, plus stronger evidence for the unresolved budget, delivery, assurance, sustainability, and dependency questions.

## Review Tree
- overall_status: `incomplete`

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
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and management of critical processes for June 2026 to June 2027.
- finding: Recipient: Intersect, with funds directed to the 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v.
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination, including core Cardano repos: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance process, Use of Sundae Labs treasury management smart contract framework with TRSC and PSSC structure
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 25,400,000 ADA for its core operating model covering June 2026 to June 2027.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal states the budget is reduced from last year's $7.875M ask to $6.35M while preserving functions critical to Cardano continuity and maturity.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect says it supports committees and working groups, stewards core Haskell repositories, coordinates upgrades and incident response, and administers community-approved initiatives.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect states it has already coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation, audited results, and an audit report.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal claims the requested amount does not, at submission, breach the applicable 350M ADA Net Change Limit covering Epoch 613 to Epoch 713 and links to the relevant governance action.
- missing: Independent evidence for: The proposal states the budget is reduced from last year's $7.875M ask to $6.35M while preserving functions critical to Cardano continuity and maturity.
- missing: Independent evidence for: Intersect says it supports committees and working groups, stewards core Haskell repositories, coordinates upgrades and incident response, and administers community-approved initiatives.
- missing: Independent evidence for: Intersect states it has already coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews of deliverables, controls, spend validation, and milestone evidence.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 25400000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.62
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
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA for its core operating model covering June 2026 to June 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states the budget is reduced from last year's $7.875M ask to $6.35M while preserving functions critical to Cardano continuity and maturity." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 25400000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA for its core operating model covering June 2026 to June 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 50% of rolling available capacity.
- Claims and evidence missing: Independent evidence for: The proposal states the budget is reduced from last year's $7.875M ask to $6.35M while preserving functions critical to Cardano continuity and maturity.
- Claims and evidence missing: Independent evidence for: Intersect says it supports committees and working groups, stewards core Haskell repositories, coordinates upgrades and incident response, and administers community-approved initiatives.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `f28570f02a3057c888f9d7fe060acc6225690d292fdb5c2904f809edde51e7df`
- snapshot_bundle_hash: `826baf7adb757ddcffa14312ba051fa22771b54d08bfb8c4eafee72c0d0816d3`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5115, "NO": 0.0592, "YES": 0.4292}`

