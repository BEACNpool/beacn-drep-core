# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show meaningful alignment with protocol safety, governance support, and treasury oversight, but several important benefits and controls remain proposer-asserted while the ask spends real treasury funds and depends on a separate IntersectMBO budget approval. A small cautionary negative nudge is warranted because treasury stewardship and evidence quality should dominate plausible public-benefit growth when some key assurances are not yet evidenced in the document itself.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action requested 1,193,000 ada for 12 months of Intersect Technical Steering Committee support. The stated work covers community-facing technical coordination, protocol governance and evolution, and a pilot independent technical review programme launching in 2027. The proposal says the budget is split into 256,000 ada for WP1, 832,000 ada for WP2, and 105,000 ada for WP3, and that execution depends on approval of the IntersectMBO budget proposal.

Several basic facts were supported by the proposal and its pinned, replayable anchor: the amount requested, the 12-month scope, the work package budget split, the dependency on the IntersectMBO budget proposal, and references to Intersect budget-process voting and treasury-management arrangements. But some important claims remained only asserted by the proposer or lacked independent evidence in this review, including that all spending would be fully accounted for, unspent funds returned, and that this support is foundational technical governance capacity. The review also flagged missing cost-benefit clarity, no sustainability path, missing independent assurance, and an incomplete dependency map.

This is a conservative, evidence-based hold, not a rejection of the stated goals. A directional vote would be unblocked by public, independently verifiable chain evidence pinning the applicable Net Change Limit, plus stronger evidence for the treasury controls, return-of-unspent-funds commitment, independent assurance, dependencies, sustainability path, and cost-benefit case.

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
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee support for 12 months across community engagement, protocol governance, and independent technical review activities.
- finding: Recipient: Intersect / 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including expert attendance at major ecosystem events and commissioning technical reports., WP 2: Protocol Governance and Evolution, funding the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: Technical Review, establishing a pilot independent technical review programme launching in 2027.
- finding: Deadline/expiry: 12 months; WP3 pilot launches in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 1,193,000 ADA, stated as $298,250, to support Technical Steering Committee activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 256,000 ADA for WP1, 832,000 ADA for WP2, and 105,000 ADA for WP3.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, supported_in_proposal, medium materiality): The proposal states that WP3 independent technical reviews will use formal conflict-of-interest provisions, published recusals, and open reviewer selection against documented criteria.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal claims the TSC support is foundational technical governance capacity needed for Cardano to function effectively as a decentralized ecosystem.
- missing: Independent evidence for: The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: The proposal claims the TSC support is foundational technical governance capacity needed for Cardano to function effectively as a decentralized ecosystem.
- missing: Independent evidence for: The proposal says independent audits and assurance will be provided by Appold, with possible reviews of deliverables, controls, spend validation, and milestone evidence.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1193000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 1,193,000 ADA, stated as $298,250, to support Technical Steering Committee activities for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 1,193,000 ADA, stated as $298,250, to support Technical Steering Committee activities for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims show meaningful alignment with protocol safety, governance support, and treasury oversight, but several important benefits and controls remain proposer-asserted while the ask spends real treasury funds and depends on a separate IntersectMBO budget approval. A small cautionary negative nudge is warranted because treasury stewardship and evidence quality should dominate plausible public-benefit growth when some key assurances are not yet evidenced in the document itself.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: The proposal claims the TSC support is foundational technical governance capacity needed for Cardano to function effectively as a decentralized ecosystem.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `a1a0e7b8ee5f6b277cc25b92a0f4ff804b66463cac60b4b96ad4897e7a523048`
- snapshot_bundle_hash: `ab6bfa03cd593f9bd709658b7adfad55232650790ae43f9770f8780cbf6700c8`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

