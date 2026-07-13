# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **NEEDS_MORE_INFO**
Score: `0.185` (raw `-0.53` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7662` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a large treasury request with meaningful governance and protocol-continuity alignment, plus checkable references for voting, NCL, prior funding, and smart-contract custody. The deterministic assessment already marks the dossier ready, and the remaining evidence-quality concerns, such as several operational-performance claims being proposer asserted, are already the kind of treasury stewardship and evidence issues the mechanical review is designed to capture, so no additional nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large Treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action requests 25,400,000 ada for Intersect’s June 2026 to June 2027 work: governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, ecosystem coordination, and management of critical processes. The proposal breaks this into 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship and incident response, and 600,000 ada for management of critical processes, with milestone-based drawdowns, evidence-backed reporting, disclosures, external assurance, and Sundae Labs treasury management smart contracts.

Several core facts were supported in the proposal: the anchor document was pinned and replayable, the requested amount and work packages were clear, Intersect disclosed prior Treasury funding, and the proposal provided references for voting documentation, audited results, smart contract infrastructure, audit reports, and a tracking dashboard. But some material claims still lacked independent evidence in the review, including the claim that this year’s proposal is more focused and lower cost than last year while preserving continuity, and the claim that Intersect coordinated two network upgrades, is preparing a third, and led coordination during the November 2025 chain partition incident.

This is a conservative, evidence-based hold, not a rejection of the work. The review gates recognized a strong YES case around funding Intersect’s core operating model and continuity functions, but Treasury votes require a higher bar because they spend shared ada and set precedent. A directional vote would be unblocked by pinned, independently verifiable public chain evidence for the Net Change Limit, plus stronger independent support for the thin claims, sustainability path, cost-benefit clarity, independent assurance, and dependency map.

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
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, ecosystem coordination, and management of critical processes for June 2026 to June 2027.
- finding: Recipient: Intersect, paid to the 2026 Treasury Reserve Smart Contract stake address stated in the document.
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination, including core Cardano repos: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance process, Use of Sundae Labs treasury management smart contract framework with TRSC and PSSC configuration
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (governance, supported_in_proposal, high materiality): Intersect states the proposal funds its core operating model from June 2026 to June 2027, including governance coordination, critical unowned processes, and technical stewardship for Cardano.
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect says the total ask is 25,400,000 ADA, allocated as 6,000,000 ADA for operations and ecosystem coordination, 18,800,000 ADA for technical stewardship and incident response, and 600,000 ADA for management of critical processes.
- finding: Claim (economic, proposer_asserted, medium materiality): Intersect asserts its current proposal is more focused than last year and that the overall ask decreased from $7.875M to $6.35M while preserving critical continuity functions.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation, audited results, and an audit report.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal claims the requested amount does not, alone or in aggregate at submission, breach the 350M Net Change Limit for Epoch 613 to Epoch 713 and links to the relevant governance action.
- missing: Independent evidence for: Intersect asserts its current proposal is more focused than last year and that the overall ask decreased from $7.875M to $6.35M while preserving critical continuity functions.
- missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: The proposal says independent audits and assurance will be provided by Appold, with possible reviews of deliverables, controls, spend validation, and milestone evidence.
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
- finding: Strongest YES: the proposal substantiates "Intersect states the proposal funds its core operating model from June 2026 to June 2027, including governance coordination, critical unowned processes, and technical stewardship for Cardano." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Intersect asserts its current proposal is more focused than last year and that the overall ask decreased from $7.875M to $6.35M while preserving critical continuity functions." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect states the proposal funds its core operating model from June 2026 to June 2027, including governance coordination, critical unowned processes, and technical stewardship for Cardano." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: Intersect asserts its current proposal is more focused than last year and that the overall ask decreased from $7.875M to $6.35M while preserving critical continuity functions.
- Claims and evidence missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `790721f3e81428ee75b28df0eb930c830f48dc47aceedf72ea1b6b9967911a57`
- snapshot_bundle_hash: `1e67acf5552271afe4b55841ff1705a90805e84ba2d4448688ddf62588c4d0fe`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4d394ccfc21657ebcbf2e1dbb3e210682b5ea383`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5115, "NO": 0.0592, "YES": 0.4292}`

