# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NO**
Score: `-0.2533` (raw `-0.2533` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7833` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal contains a detailed budget split, work-package descriptions, on-chain fund-management details, prior-funding disclosure, and several externally checkable references, so evidence quality is stronger than a thin ask. However, several important benefit claims are strategic or proposer-asserted, and the doctrine already emphasizes treasury stewardship and caution for spending proposals; the deterministic assessment appears to capture the main positives and risks without needing an additional nudge.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not meet the higher evidence bar required for spending shared ADA, especially with material parts of the execution and assurance story still unsupported by independent evidence.

The action requested 1,193,000 ada for 12 months of Intersect Technical Steering Committee support. The proposal described three work packages: community-facing technical coordination, protocol governance and evolution, and a pilot independent technical review programme launching in 2027. It also described milestone-based drawdowns, evidence-backed reporting, transparent disclosures, external assurance by Appold, and use of a treasury management smart contract framework.

Several core claims were supported. The requested amount and budget split were clear: 256,000 ada for WP1, 832,000 ada for WP2, and 105,000 ada for WP3. The proposal supported the role of WP2 in funding the Parameter Committee, CIP editors, and Hard Fork Working Group, and supported the design of WP3 with conflict-of-interest provisions and open reviewer selection. The anchor document was available and replayable, the withdrawal did not breach the stated 350M ada Net Change Limit at submission, and the smart contract administration framework was independently verifiable.

The NO came from the remaining gaps under elevated treasury scrutiny. The review found thin claims-and-evidence coverage, a medium execution risk, a flag score reducing confidence, no sustainability path, unclear cost-benefit case, missing independent assurance evidence, and a missing dependency map. In particular, the claim that the work depends on approval of the IntersectMBO budget proposal was not independently evidenced, and the claimed Appold assurance was also not independently evidenced. For BEACN, those gaps meant the cost and precedent risk outweighed the supported benefits.

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
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee Support for 12 months across community-facing technical coordination, protocol governance and evolution, and technical review.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including attendance of technical experts at major ecosystem events and commissioning technical reports, WP 2: Protocol Governance and Evolution, including support for the Parameter Committee, CIP editors, and Hard Fork Working Group, WP 3: Technical Review, including establishment of a pilot independent technical review programme launching in 2027, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance by Appold, Use of Intersect treasury management smart contract framework with TRSC and one PSSC
- finding: Deadline/expiry: 12 months; WP3 pilot launches in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect's Technical Steering Committee requests $298,250, equal to 1,193,000 ADA, to support activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 256,000 ADA for WP1, 832,000 ADA for WP2, and 105,000 ADA for WP3.
- finding: Claim (governance, proposer_asserted, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (technical, supported_in_proposal, high materiality): WP2 will fund the Parameter Committee, CIP editors, and Hard Fork Working Group to support protocol settings, the CIP pipeline, and safe coordination of protocol upgrades.
- finding: Claim (governance, supported_in_proposal, high materiality): WP3 will establish a pilot independent technical review programme launching in 2027 with conflict-of-interest provisions, recorded and published recusals, and open reviewer selection against documented criteria.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- missing: Independent evidence for: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- missing: Independent evidence for: Independent audits and assurance for the proposal will be provided by Appold, with possible review of deliverables, controls, spend validation, and milestone evidence.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1193000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.76
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Intersect's Technical Steering Committee requests $298,250, equal to 1,193,000 ADA, to support activities for 12 months." and clears the evidence gates.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1193000
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect's Technical Steering Committee requests $298,250, equal to 1,193,000 ADA, to support activities for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- Claims and evidence missing: Independent evidence for: Independent audits and assurance for the proposal will be provided by Appold, with possible review of deliverables, controls, spend validation, and milestone evidence.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `5eb02985c84a820e899ef6d40c4c87074e90a747a9b5a3c67379437dc9f16e1b`
- snapshot_bundle_hash: `48c9a687316a7fdd531225ec205a7aa15f8e21d553336ded38125cab05ae89c1`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2093, "NO": 0.7436, "YES": 0.0471}`

