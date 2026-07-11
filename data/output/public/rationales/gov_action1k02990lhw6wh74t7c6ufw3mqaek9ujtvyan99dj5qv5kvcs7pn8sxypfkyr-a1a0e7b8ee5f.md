# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a governance-infrastructure proposal with budget breakdowns, oversight mechanisms, NCL and voting references, and a commitment to return unspent funds; the deterministic assessment already marks claims, treasury analysis, risk review, and synthesis complete, so there is no clear uncaptured evidence-quality or doctrine-alignment factor requiring a score nudge.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal and the applicable Net Change Limit still needs to be pinned and independently verified from public chain evidence before BEACN can make a directional vote.

The action asks to withdraw 1,193,000 ada for 12 months of Intersect Technical Steering Committee support. The proposal says the funds would cover three work packages: 256,000 ada for community-facing technical coordination, 832,000 ada for protocol governance and evolution support, and 105,000 ada for a pilot independent technical review programme launching in 2027. The proposal also says unused funds would be returned to the treasury, and that Intersect treasury management smart contracts, external oversight, and dashboard visibility would be used.

Several core claims were supported by the proposal or independently verifiable evidence: the requested amount and work-package split, the specialist groups covered by WP2, the planned WP3 review programme, the dependency on the IntersectMBO budget proposal, the reported Intersect budget-process support threshold, the stated Net Change Limit position at submission, and the use of the Sundae Labs treasury management framework. But important parts remained thin or unsupported by independent evidence, especially the claim that all expenditure will be fully accounted for with unspent funds returned, and the claim that Appold will provide independent audits and assurance.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by independently verifiable public evidence for the applicable Net Change Limit, stronger evidence for expenditure accounting and return of unspent funds, clearer independent assurance, and better detail on sustainability, cost-benefit clarity, and dependencies.

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
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee support activities for 12 months, including community-facing technical coordination, protocol governance and evolution, and a pilot technical review programme.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination for 256,000 ADA, including expert event attendance and technical reports., WP 2: Protocol Governance and Evolution for 832,000 ADA, including support for the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: Technical Review for 105,000 ADA, establishing a pilot independent technical review programme launching in 2027., Full expenditure accounting and return of any unspent funds to the Cardano treasury., Use of Intersect treasury management smart contracts with external oversight and dashboard visibility.
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect's Technical Steering Committee requests $298,250, stated as 1,193,000 ADA, to support TSC activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal allocates 256,000 ADA to WP1, 832,000 ADA to WP2, and 105,000 ADA to WP3, totaling 1,193,000 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): WP2 will fund three specialist groups: the Parameter Committee, CIP editors, and Hard Fork Working Group.
- finding: Claim (governance, supported_in_proposal, high materiality): WP3 will establish a pilot independent technical review programme launching in 2027, with conflict-of-interest provisions, published recusals, and open reviewer selection against documented criteria.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible review of deliverables, controls, spend validation, and milestone evidence.
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
- finding: Strongest YES: the proposal substantiates "Intersect's Technical Steering Committee requests $298,250, stated as 1,193,000 ADA, to support TSC activities for 12 months." and clears the evidence gates.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1193000
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect's Technical Steering Committee requests $298,250, stated as 1,193,000 ADA, to support TSC activities for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible review of deliverables, controls, spend validation, and milestone evidence.
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
- snapshot_bundle_hash: `bda7fbd039adce42f3e62642b0c24ae4f2cc6331086aace3574d170a00f11079`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

