# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was missing baseline evidence needed to make a responsible directional vote on a large treasury withdrawal. This is a conservative, evidence-based hold, not a rejection of the stated work.

The proposal requested 25,400,000 ada for Intersect from June 2026 to June 2027, covering governance coordination, operations, technical stewardship, incident response, release coordination, repository management, security initiatives, and management of critical processes. The proposal split the request across three work packages: 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship and incident response, and 600,000 ada for critical process management. It also described milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance as part of the operating model.

Several claims were supported or independently verifiable in the proposal record, including the three-part funding split, governance support through committees and working groups, the 2026 Intersect Budget Process Hydra Voting threshold, prior disclosed treasury receipts, the Net Change Limit statement, and use of Sundae Labs treasury management smart contracts. But important claims remained only proposer-asserted or lacked independent evidence in the review, including the reduced-budget comparison to last year and the claims about prior network upgrade coordination and the November 2025 chain partition incident.

The deciding issue was that key review gates were not complete. The intake was blocked because `treasury_amount_lovelace` was missing for a treasury withdrawal, claims and evidence were thin, treasury analysis was incomplete, and risk review was thin. A directional vote would require the missing baseline fields, a complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, community impact analysis, and stronger evidence for mitigation and independent assurance.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination, core operating model, technical stewardship, incident response, release coordination, repository management, security initiatives, and critical process management for June 2026 to June 2027.
- finding: Recipient: Intersect via the listed 2026 Treasury Reserve Smart Contract stake address.
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination, including core Cardano repos: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance are described as part of the operating model
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 25,400,000 ADA split across three work packages: operations and ecosystem coordination, technical stewardship and incident response, and management of critical processes.
- finding: Claim (economic, proposer_asserted, medium materiality): Intersect states its current ask is reduced from last year's $7.875M to $6.35M while preserving the functions it considers most critical to Cardano continuity and maturity.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect states it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states Intersect supports Cardano governance through committees, working groups, proposal development, budgeting processes, and ecosystem strategy discussions.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and links to voting, documentation, audit, and final-results references.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states the requested withdrawal does not breach the applicable 350M ADA Net Change Limit for Epoch 613 to Epoch 713 at the moment of submission and links to the relevant governance action.
- missing: Independent evidence for: Intersect states its current ask is reduced from last year's $7.875M to $6.35M while preserving the functions it considers most critical to Cardano continuity and maturity.
- missing: Independent evidence for: Intersect states it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: Independent audits and assurance for this proposal are stated to be provided by Appold, with reviews potentially covering deliverable verification, controls, spend validation, and milestone evidence.
- missing: Independent evidence for: The proposal states an Oversight Committee of Sundae Labs, Cardano Foundation, Dquadrant, NMKR, Sundial, and Eternl will independently verify key administrative actions using on-chain logic without discretion over governance decisions.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA split across three work packages: operations and ecosystem coordination, technical stewardship and incident response, and management of critical processes." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Intersect states its current ask is reduced from last year's $7.875M to $6.35M while preserving the functions it considers most critical to Cardano continuity and maturity." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA split across three work packages: operations and ecosystem coordination, technical stewardship and incident response, and management of critical processes." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: Intersect states its current ask is reduced from last year's $7.875M to $6.35M while preserving the functions it considers most critical to Cardano continuity and maturity.
- Claims and evidence missing: Independent evidence for: Intersect states it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `b7590854fa834fea01cca266bd30f0de82efbde8cdf69a36685f4a0db4e7f7d3`
- snapshot_bundle_hash: `53d9b272de6404fb2634636d2940c2dd487aa39c94282d8e00bc972569b34d94`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

