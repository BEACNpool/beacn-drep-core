# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **NEEDS_MORE_INFO**
Score: `0.185` (raw `-0.53` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7662` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe established infrastructure and governance coordination functions, provide a clear budget split, disclose prior treasury funding, and point to independently checkable voting, NCL, smart-contract, audit, and dashboard references. The nudge remains small because several operational-impact claims and the future Appold assurance are still proposer assertions, and the ask is large enough that treasury stewardship should dominate any public-benefit momentum.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action requests 25,400,000 ada for Intersect from June 2026 to June 2027, paid through the 2026 Treasury Reserve Smart Contract stake address. The proposal describes three work packages: 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship, incident response, release coordination, and core repository work, and 600,000 ada for management of critical processes. It also describes milestone-based drawdowns, evidence-backed reporting, transparent disclosures, Appold assurance, and Sundae Labs treasury management smart contracts with named addresses and authorization roles.

Several core facts were strong enough to review: the anchor document was pinned and replayable, the requested amount and budget split were clear, prior treasury funding to Intersect was disclosed, the Intersect budget-process support threshold was presented with references, and the smart-contract administration setup included checkable addresses, documentation, audit references, and a dashboard. But important claims remained unsupported or thin, including the claim that the ask decreased from $7.875M to $6.35M while preserving critical functions, and claims about Intersect’s operational maturity, upgrade coordination, incident response role, and future Appold assurance.

This is a conservative, evidence-based hold, not a rejection of the work described. BEACN would need the Net Change Limit independently verified from public chain evidence, plus stronger independent support for the cost comparison, operational-impact claims, sustainability path, cost-benefit clarity, independent assurance, and dependency map before casting a YES or NO vote.

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
- finding: Requested: Fund Intersect's governance coordination, technical stewardship, incident response, release coordination, repository stewardship, security initiatives, and management of critical processes for June 2026 to June 2027.
- finding: Recipient: Intersect via the 2026 Treasury Reserve Smart Contract stake address
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination including core Cardano repos: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance by Appold, Use of Sundae Labs treasury management smart contracts with specified TRSC and PSSC addresses and multisignature-style authorization roles
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 25,400,000 ADA for three work packages covering operations and ecosystem coordination, technical stewardship and incident response, and management of critical processes.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal states Intersect's overall ask decreased from $7.875M last year to $6.35M while preserving functions it considers critical to Cardano continuity and maturity.
- finding: Claim (adoption, proposer_asserted, high materiality): Intersect says it has matured into a focused operational layer supporting committees and working groups, core Haskell repository stewardship, upgrades, incident response, and administration of community-approved initiatives.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect states it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation, audited results, and an audit report.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states the requested withdrawal does not, at submission, breach the applicable 350M ADA Net Change Limit for Epoch 613 to Epoch 713 and links to the relevant governance action.
- missing: Independent evidence for: The proposal states Intersect's overall ask decreased from $7.875M last year to $6.35M while preserving functions it considers critical to Cardano continuity and maturity.
- missing: Independent evidence for: Intersect says it has matured into a focused operational layer supporting committees and working groups, core Haskell repository stewardship, upgrades, incident response, and administration of community-approved initiatives.
- missing: Independent evidence for: Intersect states it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: The proposal says independent audits and assurance will be provided by Appold, potentially including deliverable verification, control testing, spend validation, and milestone evidence assessment.
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA for three work packages covering operations and ecosystem coordination, technical stewardship and incident response, and management of critical processes." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states Intersect's overall ask decreased from $7.875M last year to $6.35M while preserving functions it considers critical to Cardano continuity and maturity." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA for three work packages covering operations and ecosystem coordination, technical stewardship and incident response, and management of critical processes." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe established infrastructure and governance coordination functions, provide a clear budget split, disclose prior treasury funding, and point to independently checkable voting, NCL, smart-contract, audit, and dashboard references. The nudge remains small because several operational-impact claims and the future Appold assurance are still proposer assertions, and the ask is large enough that treasury stewardship should dominate any public-benefit momentum.
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
- Claims and evidence missing: Independent evidence for: The proposal states Intersect's overall ask decreased from $7.875M last year to $6.35M while preserving functions it considers critical to Cardano continuity and maturity.
- Claims and evidence missing: Independent evidence for: Intersect says it has matured into a focused operational layer supporting committees and working groups, core Haskell repository stewardship, upgrades, incident response, and administration of community-approved initiatives.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `0a3ff07544062d62708c7d0ddcf878ff7681e604a19c1d549987ed393d8d3992`
- snapshot_bundle_hash: `fa92b9c057b5f48714d1462adbf768c82ff2b52bb22e2a8c6a4ece5807b2fec1`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `6`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5115, "NO": 0.0592, "YES": 0.4292}`

