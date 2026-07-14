# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#3
Recommendation: **YES**
Score: `0.189` (raw `-0.33` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7672` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show comparatively strong treasury-stewardship evidence: a work-package budget, prior-funding disclosure, NCL statement, external assurance, smart-contract controls, oversight thresholds, and public tracking references. The nudge remains small because several strategic-benefit claims are still proposer asserted and the work is contingent on a separate IntersectMBO budget approval.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Withdraw 1,193,000 ada for Intersect Technical Steering Committee Support. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Technical Steering Committee support activities for 12 months, spanning community engagement, protocol governance, and independent technical review. It asks the treasury for 1,193,000 ADA. The strongest grounded claim is: Intersect requests 1,193,000 ADA, stated as $298,250, to fund Technical Steering Committee support for 12 months.

A residual watch item: this claim remains proposer-asserted rather than independently shown: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.

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
- finding: Requested: Technical Steering Committee support activities for 12 months, spanning community engagement, protocol governance, and independent technical review.
- finding: Recipient: Intersect / 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: community-facing technical coordination, including technical expert attendance at major ecosystem events and commissioning technical reports., WP 2: protocol governance and evolution support for the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: establishment of a pilot independent technical review programme launching in 2027.
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 1,193,000 ADA, stated as $298,250, to fund Technical Steering Committee support for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is divided into 256,000 ADA for WP1, 832,000 ADA for WP2, and 105,000 ADA for WP3.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states that the Technical Steering Committee has not received Cardano Treasury funding within the past 24 months, while Intersect and its committees received 22,385,000 ADA through listed prior governance actions.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation and audited results.
- missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: The proposal claims the TSC work supports Cardano strategy pillars including uptime, DRep participation, governance capture resistance, adoption, and treasury stewardship.
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 1,193,000 ADA, stated as $298,250, to fund Technical Steering Committee support for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 1,193,000 ADA, stated as $298,250, to fund Technical Steering Committee support for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show comparatively strong treasury-stewardship evidence: a work-package budget, prior-funding disclosure, NCL statement, external assurance, smart-contract controls, oversight thresholds, and public tracking references. The nudge remains small because several strategic-benefit claims are still proposer asserted and the work is contingent on a separate IntersectMBO budget approval.
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
- Claims and evidence missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: The proposal claims the TSC work supports Cardano strategy pillars including uptime, DRep participation, governance capture resistance, adoption, and treasury stewardship.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `71c7f46d2a402b9326983d53ea12129c2594b49470eb1a3d8d08656e897e8700`
- snapshot_bundle_hash: `3c99e1afa5f13a45c9c58743edfdced7fe8b2cdc6a5d7fa267ce94f5b948f0db`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2241, "NO": 0.0551, "YES": 0.7208}`

