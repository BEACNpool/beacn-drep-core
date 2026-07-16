# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#3
Recommendation: **YES**
Score: `0.189` (binding treasury composite; advisory raw signal `-0.33`; LLM lean `+0.02` recorded, not added) | Confidence: `0.7672` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show comparatively concrete treasury controls, work-package budgeting, external references for voting and smart-contract administration, and a stated return-of-unspent-funds commitment; this modestly improves evidence quality and treasury stewardship alignment without overriding the deterministic gates.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Withdraw 1,193,000 ada for Intersect Technical Steering Committee Support. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw treasury funds for 12 months of Intersect Technical Steering Committee support covering community engagement, protocol governance, and independent technical review. It asks the treasury for 1193000 ADA. The strongest grounded claim is: The proposal requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support.

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
- finding: Requested: Withdraw treasury funds for 12 months of Intersect Technical Steering Committee support covering community engagement, protocol governance, and independent technical review.
- finding: Recipient: Intersect on behalf of the vendor, with funds directed to the 2026 Treasury Reserve Smart Contract stake address.
- finding: Stated amount: 1193000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including technical expert attendance at major ecosystem events and commissioning technical reports., WP 2: Protocol Governance and Evolution, funding the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: Technical Review, establishing a pilot independent technical review programme launching in 2027.
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support.
- finding: Claim (economic, supported_in_proposal, high materiality): The funded work is divided into WP1 at 256,000 ADA, WP2 at 832,000 ADA, and WP3 at 105,000 ADA, totaling 1,193,000 ADA.
- finding: Claim (governance, proposer_asserted, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal says the Technical Steering Committee has not received Cardano Treasury funding within the past 24 months, while Intersect and its committees received 22,385,000 ADA through listed prior governance actions.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, potentially including deliverable verification, control testing, spend validation, and milestone evidence assessment.
- missing: Independent evidence for: The proposer claims TSC work supports Cardano technical governance, DRep decision-making, protocol upgrade coordination, parameter recommendations, and the 2030 strategy pillars.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests $298,250, equivalent to 1,193,000 ADA, for 12 months of Technical Steering Committee support." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show comparatively concrete treasury controls, work-package budgeting, external references for voting and smart-contract administration, and a stated return-of-unspent-funds commitment; this modestly improves evidence quality and treasury stewardship alignment without overriding the deterministic gates.
- Directional YES cleared ecosystem benefit, delivery, cost-efficiency, downside-protection, and portfolio-capacity floors.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 30% of rolling available capacity.
- Claims and evidence missing: Independent evidence for: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- Claims and evidence missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `138c9555bb355f8a495b24df6d426f1afc056f61e97276dbb36f48469f709ed1`
- snapshot_bundle_hash: `425427f5a07545e7faa96567b153f652056b2da437f927aa45b06196f8582cd7`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2241, "NO": 0.0551, "YES": 0.7208}`

