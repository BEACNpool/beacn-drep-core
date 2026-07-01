# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sgx6wlxf
Recommendation: **NO**
Score: `-0.3133` (raw `-0.2833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.8333` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal contains meaningful governance and custody details plus checkable references, but for a large treasury withdrawal the extracted claims still leave key diligence gaps already identified in the assessment, including incomplete budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN doctrine, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw 25,400,000 ada for Intersect: Governance coordination and technical .... The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Intersect governance coordination and technical stewardship for the Cardano ecosystem from June 2026 to June 2027.. The recorded treasury amount is 25,400,000. The strongest grounded claim is: Intersect states the proposal funds its core operating model for June 2026 to June 2027, including governance coordination, critical unowned processes, technical stewardship, incident response, and release coordination.

A material weak point is that this claim remains proposer-asserted or thinly supported: Intersect claims its overall ask decreased from $7.875M last year to $6.35M while preserving functions critical to Cardano continuity and maturity. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination and technical stewardship for the Cardano ecosystem from June 2026 to June 2027.
- finding: Recipient: Intersect via the 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v.
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination, including core Cardano repositories: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Intersect states the proposal funds its core operating model for June 2026 to June 2027, including governance coordination, critical unowned processes, technical stewardship, incident response, and release coordination.
- finding: Claim (economic, proposer_asserted, high materiality): Intersect claims its overall ask decreased from $7.875M last year to $6.35M while preserving functions critical to Cardano continuity and maturity.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and links to voting, documentation, and audited-result references.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal claims the requested amount does not, at submission, breach the applicable 350M ADA Net Change Limit covering Epoch 613 to Epoch 713.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal discloses that Intersect and its committees received 22,385,000 ADA from listed Cardano Treasury governance actions within the prior 24 months.
- missing: Independent evidence for: Intersect claims its overall ask decreased from $7.875M last year to $6.35M while preserving functions critical to Cardano continuity and maturity.
- missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: Independent audits and assurance for this proposal are stated to be provided by Appold, potentially including deliverable verification, control testing, spend validation, and milestone-evidence assessment.
- missing: Independent evidence for: The proposal says all milestones will be outlined within metadata when funds are transferred to the Project-Specific Smart Contract.
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
- finding: Six-month treasury flow regime: unknown (stale snapshot)
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
- finding: Strongest YES: the proposal substantiates "Intersect states the proposal funds its core operating model for June 2026 to June 2027, including governance coordination, critical unowned processes, technical stewardship, incident response, and release coordination." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Intersect claims its overall ask decreased from $7.875M last year to $6.35M while preserving functions critical to Cardano continuity and maturity." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect states the proposal funds its core operating model for June 2026 to June 2027, including governance coordination, critical unowned processes, technical stewardship, incident response, and release coordination." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal contains meaningful governance and custody details plus checkable references, but for a large treasury withdrawal the extracted claims still leave key diligence gaps already identified in the assessment, including incomplete budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN doctrine, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~18 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Intersect claims its overall ask decreased from $7.875M last year to $6.35M while preserving functions critical to Cardano continuity and maturity.
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
- input_hash: `0eaa3177ec3620d84137de6de061ef10ee0acc8eb0a5c8253dc07ffb9a618be1`
- snapshot_bundle_hash: `f6e96234a87b218078b4dd3eac00884b7a47eee20b02e23224135314c2ec7dca`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `659`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1914, "NO": 0.7642, "YES": 0.0443}`

