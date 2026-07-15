# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **NEEDS_MORE_INFO**
Score: `0.185` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7662` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show comparatively strong alignment with protocol safety and governance continuity, including technical stewardship, incident response, release coordination, budget-process references, NCL compliance references, prior-funding disclosure, smart-contract controls, and public auditability. The nudge remains small because several important operational-performance claims and the future Appold assurance arrangement are proposer assertions rather than verified results in the supplied text.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large Treasury withdrawal and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal requests 25,400,000 ada for Intersect from June 2026 to June 2027, covering governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and critical unowned process capacity. The budget is presented as 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship and incident response, and 600,000 ada for management of critical processes, with milestone-based drawdowns, reporting, disclosures, and external assurance.

Several core facts were reviewable: the anchor document was pinned and replayable, the requested amount and work packages were clear, prior Treasury funding of 22,385,000 ada was disclosed, and the proposal referenced Hydra voting support, NCL compliance, treasury smart-contract controls, role-based approvals, oversight, and public auditability. But important claims remained unsupported by independent evidence in the supplied review, including the claim that the ask decreased from $7.875M to $6.35M while preserving critical functions, and the claim that Intersect has matured into the described operational layer. The review also found thin claims-and-evidence status, unknown execution risk, missing sustainability path, missing cost-benefit clarity, missing independent assurance, and no dependency map.

This is a conservative, evidence-based hold, not a rejection of the work described. A directional vote would be unblocked by pinned, independently verifiable public chain evidence for the Net Change Limit, plus stronger independent evidence for the material operational and budget claims, clearer sustainability and cost-benefit analysis, and completed assurance and dependency evidence.

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
- finding: Requested: Treasury withdrawal for Intersect governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, and critical unowned process capacity for June 2026 to June 2027.
- finding: Recipient: Intersect via the 2026 Treasury Reserve Smart Contract stake address stated in the on-chain rewards field.
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination, including core Cardano repos: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance process
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 25,400,000 ADA to fund its core operating model from June 2026 to June 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 6,000,000 ADA for operations and ecosystem coordination, 18,800,000 ADA for technical stewardship and incident response, and 600,000 ADA for management of critical processes.
- finding: Claim (economic, proposer_asserted, medium materiality): Intersect states the overall ask has decreased from $7.875M last year to $6.35M while preserving the most critical continuity and maturity functions.
- finding: Claim (adoption, proposer_asserted, medium materiality): Intersect states it has matured over two years into a focused operational layer supporting committees and working groups, core Haskell repository stewardship, upgrades, incident response, and administration of community-approved initiatives.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect states it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation and audited results.
- missing: Independent evidence for: Intersect states the overall ask has decreased from $7.875M last year to $6.35M while preserving the most critical continuity and maturity functions.
- missing: Independent evidence for: Intersect states it has matured over two years into a focused operational layer supporting committees and working groups, core Haskell repository stewardship, upgrades, incident response, and administration of community-approved initiatives.
- missing: Independent evidence for: Intersect states it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews of deliverables, controls, spending, and milestone evidence.
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA to fund its core operating model from June 2026 to June 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Intersect states the overall ask has decreased from $7.875M last year to $6.35M while preserving the most critical continuity and maturity functions." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA to fund its core operating model from June 2026 to June 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show comparatively strong alignment with protocol safety and governance continuity, including technical stewardship, incident response, release coordination, budget-process references, NCL compliance references, prior-funding disclosure, smart-contract controls, and public auditability. The nudge remains small because several important operational-performance claims and the future Appold assurance arrangement are proposer assertions rather than verified results in the supplied text.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Intersect states the overall ask has decreased from $7.875M last year to $6.35M while preserving the most critical continuity and maturity functions.
- Claims and evidence missing: Independent evidence for: Intersect states it has matured over two years into a focused operational layer supporting committees and working groups, core Haskell repository stewardship, upgrades, incident response, and administration of community-approved initiatives.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `760de4e17a41ffda90754c7299b0c323271460a8519c357092c981f1e39cdbec`
- snapshot_bundle_hash: `99fab6aae946a0e82db1bda36e2ba7b093c3cda6149ef84045c7e8214adef5d5`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3d9c2c9681f9060eff076f9ca8f4e36a1ddb67a2`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5115, "NO": 0.0592, "YES": 0.4292}`

