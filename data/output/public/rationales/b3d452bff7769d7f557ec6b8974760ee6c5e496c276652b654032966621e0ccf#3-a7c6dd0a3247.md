# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#3
Recommendation: **YES**
Score: `0.189` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7672` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show relevant public-benefit governance work, budget breakdowns, NCL and voting references, and oversight mechanisms, while the deterministic assessment already marks the evidence, treasury, risk, and synthesis stages complete. No additional doctrine-based nudge is justified beyond the engine's captured gates and scoring.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Withdraw 1,193,000 ada for Intersect Technical Steering Committee Support. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Intersect Technical Steering Committee support activities for 12 months across community engagement, protocol governance, and independent technical review. It asks the treasury for 1193000 ADA. The strongest grounded claim is: Intersect requests $298,250, equivalent to 1,193,000 ADA, to support Technical Steering Committee activities for 12 months.

A residual watch item: this claim remains proposer-asserted rather than independently shown: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.19M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee support activities for 12 months across community engagement, protocol governance, and independent technical review.
- finding: Recipient: Intersect / 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 1193000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including expert attendance at ecosystem events and commissioning technical reports, WP 2: Protocol Governance and Evolution, funding the Parameter Committee, CIP editors, and Hard Fork Working Group, WP 3: Technical Review, establishing a pilot independent technical review programme launching in 2027, Full expenditure accounting with return of unspent funds to the Cardano treasury, Use of Intersect treasury management smart contracts with external oversight and community dashboard tracking
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests $298,250, equivalent to 1,193,000 ADA, to support Technical Steering Committee activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposed budget allocates 256,000 ADA to WP1, 832,000 ADA to WP2, and 105,000 ADA to WP3, totaling 1,193,000 ADA.
- finding: Claim (governance, proposer_asserted, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (governance, proposer_asserted, high materiality): The TSC states that its work provides foundational technical governance capacity needed for Cardano to function effectively as a decentralized ecosystem.
- finding: Claim (technical, supported_in_proposal, high materiality): WP2 funds the Parameter Committee, CIP editors, and Hard Fork Working Group to support evidence-based protocol settings, the CIP pipeline, and safe coordination of protocol upgrades.
- finding: Claim (governance, supported_in_proposal, high materiality): WP3 will establish an independent technical review programme with conflict-of-interest provisions, published recusals, and reviewer selection through an open process against documented criteria.
- missing: Independent evidence for: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- missing: Independent evidence for: The TSC states that its work provides foundational technical governance capacity needed for Cardano to function effectively as a decentralized ecosystem.
- missing: Independent evidence for: Independent audits and assurance for the proposal will be provided by Appold, with possible reviews including deliverable verification, control testing, spend validation, and milestone evidence assessment.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1193000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.55
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
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Intersect requests $298,250, equivalent to 1,193,000 ADA, to support Technical Steering Committee activities for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Execution of the work packages is contingent on approval of the IntersectMBO budget proposal." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1193000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests $298,250, equivalent to 1,193,000 ADA, to support Technical Steering Committee activities for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Directional YES cleared ecosystem benefit, delivery, cost-efficiency, downside-protection, and portfolio-capacity floors.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- Claims and evidence missing: Independent evidence for: The TSC states that its work provides foundational technical governance capacity needed for Cardano to function effectively as a decentralized ecosystem.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `a7c6dd0a3247515eede6471357c071723c45429058d1ed40c1ea872c04bb5428`
- snapshot_bundle_hash: `fb660a0c5bc36b2e68991fb8814ec2c9837fed479e27239b3049f3766e46cafd`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `3e3c343fc0dd14a03a92aad1216ba6620b3d0185`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2241, "NO": 0.0551, "YES": 0.7208}`

