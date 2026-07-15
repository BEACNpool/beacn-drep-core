# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **NEEDS_MORE_INFO**
Score: `0.185` (binding treasury composite; advisory raw signal `-0.53`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7662` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show comparatively strong alignment with protocol safety, governance operations, treasury controls, and reproducible oversight mechanisms through referenced voting results, NCL checkability, prior funding disclosure, external assurance, smart-contract controls, and a public dashboard. The nudge is small because several central delivery-history and operational-importance claims remain proposer asserted rather than independently established within the supplied text, and the deterministic engine has already handled hard evidence and treasury gates.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large Treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action requests 25,400,000 ada for Intersect’s June 2026 to June 2027 operating model, covering governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, operations, ecosystem coordination, and management of critical processes. The proposal breaks this into 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship and incident response, and 600,000 ada for management of critical processes, with milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance.

Several important claims were supported in the supplied review: the requested amount and budget split were stated in the proposal, the anchor document was pinned and replayable, the proposal passed the required Intersect Budget Process Hydra Voting threshold, prior Treasury funding was disclosed, Appold assurance was identified, and the use of a Sundae Labs treasury management smart contract framework with oversight and a public dashboard was independently verifiable. However, some central claims remained only proposer asserted, including the claimed reduction from last year’s budget while preserving critical functions, and Intersect’s claimed delivery history around two network upgrades, preparation for a third, and coordination during the November 2025 chain partition incident.

This is a conservative, evidence-based hold, not a rejection of the work described. The review gates found enough structure to review the action, but Treasury votes require elevated scrutiny because they spend shared ada and create precedent. BEACN would need the Net Change Limit pinned and independently verified from public chain evidence, plus stronger independent evidence for the unsupported delivery-history and budget-comparison claims, clearer sustainability and cost-benefit analysis, independent assurance detail, and a dependency map before moving from NEEDS_MORE_INFO to a directional yes or no.

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
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, operations, ecosystem coordination, and management of critical processes for June 2026 to June 2027.
- finding: Recipient: Intersect via the 2026 Treasury Reserve Smart Contract stake address stated in the document
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination, including core Cardano repositories: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance process
- finding: Deadline/expiry: June 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 25,400,000 ADA for its core operating model covering June 2026 to June 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 6,000,000 ADA for operations and ecosystem coordination, 18,800,000 ADA for technical stewardship and incident response, and 600,000 ADA for management of critical processes.
- finding: Claim (economic, proposer_asserted, medium materiality): Intersect states that its current ask reduced from last year's $7.875M to $6.35M while preserving the most critical functions for Cardano continuity and maturity.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal claims Intersect provides technical coordination for network upgrades, incident response, security coordination, repository stewardship, and operational coordination around critical Cardano components.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission under the approved Budget Process Framework.
- missing: Independent evidence for: Intersect states that its current ask reduced from last year's $7.875M to $6.35M while preserving the most critical functions for Cardano continuity and maturity.
- missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
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
- finding: Strongest NO: a material claim is unsupported — "Intersect states that its current ask reduced from last year's $7.875M to $6.35M while preserving the most critical functions for Cardano continuity and maturity." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show comparatively strong alignment with protocol safety, governance operations, treasury controls, and reproducible oversight mechanisms through referenced voting results, NCL checkability, prior funding disclosure, external assurance, smart-contract controls, and a public dashboard. The nudge is small because several central delivery-history and operational-importance claims remain proposer asserted rather than independently established within the supplied text, and the deterministic engine has already handled hard evidence and treasury gates.
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
- Claims and evidence missing: Independent evidence for: Intersect states that its current ask reduced from last year's $7.875M to $6.35M while preserving the most critical functions for Cardano continuity and maturity.
- Claims and evidence missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `f6e8d6c4ce71082f37902512d318dc7ceceec52efd06fd2ba8ff31cee2ffcad9`
- snapshot_bundle_hash: `3be4f2473808b8cf3812eeec8d0dec3f573ef1f958712962efc0b94197f86335`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5115, "NO": 0.0592, "YES": 0.4292}`

