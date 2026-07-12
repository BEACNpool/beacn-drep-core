# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.0` | Readiness: `0`


## Plain-language explanation (deterministic-template)
BEACN's autonomous DRep recorded ABSTAIN on "Withdraw 25,400,000 ada for Intersect: Governance coordination and technical ..." (TreasuryWithdrawals). This is a conservative, evidence-based hold rather than opposition. The action requests 25.40M ADA from the treasury. A key material claim lacks independent support: "Intersect states that its overall ask has decreased from $7.875M last year to $6.35M this year while preserving functions it considers critical to Cardano continuity and maturity.". Open questions before a directional vote: freshness gate failed. Reason code: STALE_DATA. (Plain-language summary generated deterministically; a model-written explanation appears here when the reasoning layer is enabled.)

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
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, ecosystem coordination, and management of critical processes.
- finding: Recipient: Intersect, with withdrawal directed to the 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination, including core Cardano repositories: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance by Appold
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (governance, supported_in_proposal, high materiality): Intersect says the proposal funds its core operating model for June 2026 to June 2027, including governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and critical unowned processes.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is 25,400,000 ADA, allocated as 6,000,000 ADA for operations and ecosystem coordination, 18,800,000 ADA for technical stewardship and incident response, and 600,000 ADA for critical process management.
- finding: Claim (economic, proposer_asserted, medium materiality): Intersect states that its overall ask has decreased from $7.875M last year to $6.35M this year while preserving functions it considers critical to Cardano continuity and maturity.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and links to voting records, documentation, audited results, and an audit report.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states the requested amount does not, alone or in aggregate at submission time, breach the 350M ADA Net Change Limit covering Epoch 613 to Epoch 713 and links to the relevant governance action.
- missing: Independent evidence for: Intersect states that its overall ask has decreased from $7.875M last year to $6.35M this year while preserving functions it considers critical to Cardano continuity and maturity.
- missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
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
- finding: Strongest YES: the proposal substantiates "Intersect says the proposal funds its core operating model for June 2026 to June 2027, including governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and critical unowned processes." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Intersect states that its overall ask has decreased from $7.875M last year to $6.35M this year while preserving functions it considers critical to Cardano continuity and maturity." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: freshness gate failed
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Data freshness check failed: data is 91636s old, max allowed is 21600s
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect says the proposal funds its core operating model for June 2026 to June 2027, including governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and critical unowned processes." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce reliable recommendation with stale data.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- All scoring suspended until fresh data is available.
- Claims and evidence missing: Independent evidence for: Intersect states that its overall ask has decreased from $7.875M last year to $6.35M this year while preserving functions it considers critical to Cardano continuity and maturity.
- Claims and evidence missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: freshness gate failed
- Synthesis status is blocked.

## Reproducibility
- input_hash: `2a5bd02b8f6e26c596c39274cf6ed4adcdba008505472fbd099ed6698791b731`
- snapshot_bundle_hash: `4b81b99ad906f4d9b5aaf49c88ffec50a600e42297f04673ea70375839557d87`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `eec0908e48c56be13e86e06ac5d9440d0cac813a`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `91636`
- uncertainty_band: `LOW`
- evidence_depth_score: `2`
- decision_probs: `{"ABSTAIN": 0.32, "NO": 0.34, "YES": 0.34}`

- **DATA STALE**: age exceeded threshold

