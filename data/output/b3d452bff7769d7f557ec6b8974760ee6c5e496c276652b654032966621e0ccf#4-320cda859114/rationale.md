# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#4
Recommendation: **NEEDS_MORE_INFO**
Score: `0.185` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7662` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive adjustment is justified because the extracted claims show strong alignment with protocol safety and governance continuity, and several high-materiality controls are externally checkable, including Hydra voting references, NCL compliance, prior funding disclosures, smart-contract addresses, audit references, and dashboard/on-chain traceability. The adjustment remains small because several core performance claims, including prior upgrade and incident coordination, are proposer asserted in the anchor text and the requested amount is large.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

This action requested 25,400,000 ada for Intersect’s June 2026 to June 2027 operating model, covering governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, operations, ecosystem coordination, and critical-process management. The proposal also described milestone-based drawdowns, evidence-backed reporting, transparent disclosures, Appold assurance, and Sundae Labs treasury management smart contracts.

Several important claims were supported in the proposal or described as independently verifiable, including the core funding purpose, alignment with governance and ecosystem resilience, prior Intersect budget-process support, prior treasury funding disclosures, smart-contract administration details, and public dashboard/on-chain traceability. However, some material claims remained unsupported by independent evidence in the review, including the stated reduction in Intersect’s overall ask and claims about prior network-upgrade coordination and the November 2025 chain partition response. The review also found thin claims-and-evidence coverage, missing sustainability and cost-benefit clarity, unknown execution risk, and missing detail on independent assurance and dependency mapping.

This is a conservative, evidence-based hold, not a rejection of the proposal’s goals. A directional vote would be unblocked by independently pinned, public chain evidence verifying the applicable Net Change Limit, plus stronger replayable evidence for the material cost, performance, assurance, sustainability, and dependency claims.

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
- finding: Requested: Withdraw treasury funds for Intersect governance coordination, technical stewardship, incident response, release coordination, repository management, security initiatives, operations, ecosystem coordination, and management of critical processes for June 2026 to June 2027.
- finding: Recipient: Intersect via the 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination, including core Cardano repos: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance by Appold, Use of Sundae Labs treasury management smart contracts with TRSC and PSSC addresses and specified authorization thresholds
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Intersect states that this withdrawal funds its core operating model for June 2026 to June 2027, including ecosystem coordination, reserved capacity for critical unowned processes, technical stewardship, incident response, and release coordination.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal says Intersect's overall ask decreased from $7.875M last year to $6.35M while preserving functions it considers critical to Cardano continuity and maturity.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has already coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, supported_in_proposal, medium materiality): The proposal claims primary alignment with infrastructure and research excellence, governance, and ecosystem sustainability and resilience, with secondary alignment to adoption and community growth.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to the voting proposal, documentation, final audited results, and audit materials.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states that the requested 25,400,000 ADA does not, at submission alone or in aggregate, breach the applicable 350M Net Change Limit for Epoch 613 to Epoch 713.
- missing: Independent evidence for: The proposal says Intersect's overall ask decreased from $7.875M last year to $6.35M while preserving functions it considers critical to Cardano continuity and maturity.
- missing: Independent evidence for: Intersect claims it has already coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
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
- finding: Strongest YES: the proposal substantiates "Intersect states that this withdrawal funds its core operating model for June 2026 to June 2027, including ecosystem coordination, reserved capacity for critical unowned processes, technical stewardship, incident response, and release coordination." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says Intersect's overall ask decreased from $7.875M last year to $6.35M while preserving functions it considers critical to Cardano continuity and maturity." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect states that this withdrawal funds its core operating model for June 2026 to June 2027, including ecosystem coordination, reserved capacity for critical unowned processes, technical stewardship, incident response, and release coordination." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive adjustment is justified because the extracted claims show strong alignment with protocol safety and governance continuity, and several high-materiality controls are externally checkable, including Hydra voting references, NCL compliance, prior funding disclosures, smart-contract addresses, audit references, and dashboard/on-chain traceability. The adjustment remains small because several core performance claims, including prior upgrade and incident coordination, are proposer asserted in the anchor text and the requested amount is large.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal says Intersect's overall ask decreased from $7.875M last year to $6.35M while preserving functions it considers critical to Cardano continuity and maturity.
- Claims and evidence missing: Independent evidence for: Intersect claims it has already coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `320cda8591141c437f6cf92849f5770ae3355ccc490ed14e954236d2a338c2d4`
- snapshot_bundle_hash: `f0aa4b91641f1a4305ed0548141e091b3d78df54b99f3b5c4a88f8e6a8f0a08a`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `880436a840989202a38cccce66fd8f1cbf15004d`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5115, "NO": 0.0592, "YES": 0.4292}`

