# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline treasury evidence, specifically the missing `treasury_amount_lovelace` field for a treasury withdrawal. For a request that would consume shared ADA, BEACN treats that as a conservative, evidence-based hold rather than a directional judgment for or against the work.

The action requested 25,400,000 ada for Intersect from June 2026 to June 2027, covering governance coordination, technical stewardship, incident response, release coordination, and management of critical unowned processes. The proposal broke that into 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship and incident response, and 600,000 ada for management of critical processes, with milestone-based drawdowns, reporting, disclosures, and external assurance.

Several basic claims were supported in the proposal itself, including the requested amount, recipient stake address, budget split, prior disclosed treasury receipts, Hydra Voting support references, the Net Change Limit statement, and treasury smart contract arrangements. But important claims still lacked independent evidence in the review, including the operating model’s claimed support for core Cardano functions and the statement that the ask was reduced while preserving critical continuity functions. The treasury analysis was also incomplete, with missing sustainability path and cost-benefit clarity, and the risk review still lacked independent assurance and a rollback or remedy path.

The strongest case for YES was that the proposal did substantiate the 25,400,000 ada request and listed on-chain reward value, but one review blocker remained open. The strongest hold case was decisive: a treasury action without a complete baseline dossier cannot be voted on directionally without pretending certainty. A future directional vote would require the missing treasury amount field, independent evidence for material claims, clearer sustainability and cost-benefit analysis, independent assurance, and a remedy path.

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
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination, technical stewardship, incident response, release coordination, and management of critical unowned processes for June 2026 to June 2027.
- finding: Recipient: Intersect / 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination including core Cardano repos: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 25,400,000 ADA, with the on-chain reward value stated as 25,400,000,000,000 lovelace to the listed 2026 Treasury Reserve Smart Contract stake address.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says Intersect’s 2026-2027 core operating model supports governance coordination, critical unowned processes, technical stewardship, incident response, and release coordination for Cardano.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is divided into 6,000,000 ADA for operations and ecosystem coordination, 18,800,000 ADA for technical stewardship and incident response, and 600,000 ADA for management of critical processes.
- finding: Claim (economic, proposer_asserted, medium materiality): Intersect states its ask has reduced from $7.875M last year to $6.35M this year while preserving the most critical continuity and maturity functions.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation, final audited results, and an audit report.
- missing: Independent evidence for: The proposal says Intersect’s 2026-2027 core operating model supports governance coordination, critical unowned processes, technical stewardship, incident response, and release coordination for Cardano.
- missing: Independent evidence for: Intersect states its ask has reduced from $7.875M last year to $6.35M this year while preserving the most critical continuity and maturity functions.
- missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: The proposal says independent audits and assurance will be provided by Appold, covering possible deliverable verification, control testing, spend validation, and milestone evidence review where appropriate.
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA, with the on-chain reward value stated as 25,400,000,000,000 lovelace to the listed 2026 Treasury Reserve Smart Contract stake address." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal says Intersect’s 2026-2027 core operating model supports governance coordination, critical unowned processes, technical stewardship, incident response, and release coordination for Cardano." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA, with the on-chain reward value stated as 25,400,000,000,000 lovelace to the listed 2026 Treasury Reserve Smart Contract stake address." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: The proposal says Intersect’s 2026-2027 core operating model supports governance coordination, critical unowned processes, technical stewardship, incident response, and release coordination for Cardano.
- Claims and evidence missing: Independent evidence for: Intersect states its ask has reduced from $7.875M last year to $6.35M this year while preserving the most critical continuity and maturity functions.
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
- input_hash: `74b2af96bb4fd330985a542ac0a784202588bad9dec79cbe55d619b9be74a2a3`
- snapshot_bundle_hash: `b49d047c37787cbba4a1a4b4d89fc29143c92209dc03afe774ee3616eabcfa9b`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

