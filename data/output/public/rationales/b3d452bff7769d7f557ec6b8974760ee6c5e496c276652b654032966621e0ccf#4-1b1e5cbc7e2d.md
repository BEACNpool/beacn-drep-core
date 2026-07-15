# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **NEEDS_MORE_INFO**
Score: `0.185` (raw `-0.08` + doctrine-LLM nudge `-0.01`) | Confidence: `0.7662` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has meaningful public-benefit and protocol-continuity alignment, and it provides checkable governance, NCL, prior-funding, and smart-contract references; however, the large treasury ask, reliance on several proposer assertions about past operational performance, and limited detail in the anchor about concrete milestones and cost justification warrant a small cautionary nudge under treasury stewardship and evidence quality.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the proposal’s purpose.

The action requested 25,400,000 ada for Intersect’s June 2026 to June 2027 governance coordination and technical stewardship work. The proposal says this would fund Intersect operations and ecosystem coordination, technical stewardship and incident response including core Cardano repositories, and management of critical processes. It also claims the ask is lower than last year, that Intersect has coordinated major network work and incident response, and that the withdrawal fits within the relevant 350M ada Net Change Limit.

Several parts were reviewable and supported: the anchor document was pinned and replayable, the proposal described the operating model and work packages, disclosed prior treasury funding, linked to Intersect budget-process materials, and described treasury smart-contract administration and oversight roles. But other important claims remained unsupported by independent evidence, including the reduced-cost comparison, the claimed past operational performance, sustainability path, cost-benefit clarity, independent assurance, and dependency map.

Because this is a large treasury withdrawal, BEACN applies elevated scrutiny. The review found meaningful public-benefit and protocol-continuity alignment, but treasury stewardship requires replayable public evidence before committing shared ada. A directional vote would be unblocked by independently verifiable public-chain confirmation of the applicable Net Change Limit, plus stronger evidence for the unsupported cost, performance, assurance, sustainability, and dependency claims.

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
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination and technical stewardship for June 2026 to June 2027.
- finding: Recipient: Intersect, via the 2026 Treasury Reserve Smart Contract stake address stated in the document.
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination including core Cardano repos: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA
- finding: Deadline/expiry: June 2027
- finding: Claim (governance, supported_in_proposal, high materiality): Intersect says the proposal funds its core operating model for June 2026 to June 2027, including governance coordination, reserved capacity for critical unowned processes, and technical stewardship.
- finding: Claim (economic, proposer_asserted, medium materiality): Intersect says the total ask has decreased from $7.875M last year to $6.35M while preserving functions critical to Cardano continuity and maturity.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and links to voting results and audit materials.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states the requested amount does not breach the applicable 350M ADA Net Change Limit covering Epoch 613 to Epoch 713 at submission time and links to the referenced governance action.
- finding: Claim (governance, proposer_asserted, medium materiality): The document states independent audits and assurance for the proposal will be provided by Appold, including possible deliverable verification, control testing, spend validation, and milestone evidence assessment.
- missing: Independent evidence for: Intersect says the total ask has decreased from $7.875M last year to $6.35M while preserving functions critical to Cardano continuity and maturity.
- missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: The document states independent audits and assurance for the proposal will be provided by Appold, including possible deliverable verification, control testing, spend validation, and milestone evidence assessment.
- missing: Independent evidence for: The proposal states all TRSC and PSSC instances cannot be staked with an SPO and are delegated to the auto-abstain predefined DRep.
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
- finding: Strongest YES: the proposal substantiates "Intersect says the proposal funds its core operating model for June 2026 to June 2027, including governance coordination, reserved capacity for critical unowned processes, and technical stewardship." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Intersect says the total ask has decreased from $7.875M last year to $6.35M while preserving functions critical to Cardano continuity and maturity." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect says the proposal funds its core operating model for June 2026 to June 2027, including governance coordination, reserved capacity for critical unowned processes, and technical stewardship." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.010 (display cap ±0.05) and had zero influence on the binding score: The proposal has meaningful public-benefit and protocol-continuity alignment, and it provides checkable governance, NCL, prior-funding, and smart-contract references; however, the large treasury ask, reliance on several proposer assertions about past operational performance, and limited detail in the anchor about concrete milestones and cost justification warrant a small cautionary nudge under treasury stewardship and evidence quality.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Intersect says the total ask has decreased from $7.875M last year to $6.35M while preserving functions critical to Cardano continuity and maturity.
- Claims and evidence missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `1b1e5cbc7e2d22b4dbcfab78278abc3b560abca2922579fb04c333e146a41250`
- snapshot_bundle_hash: `96fded2f1bb4106960e0f17b6c581909a7a4922816f4ce2e0c5ad612249e86b9`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `afd630a34be9d7440e2fac020ac552cde501098f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5115, "NO": 0.0592, "YES": 0.4292}`

