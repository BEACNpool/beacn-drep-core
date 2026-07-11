# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#3
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.08` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.77` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show alignment with protocol safety and governance quality through specialist technical groups, hard fork coordination, independent review design, NCL disclosure, and smart-contract oversight. The nudge remains small because several important controls, including expenditure return and assurance execution, are still largely proposer commitments rather than completed evidence.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal and the applicable Net Change Limit still needs to be pinned and independently verified from public chain evidence before a directional vote is justified.

The action asks to withdraw 1,193,000 ada for 12 months of Intersect Technical Steering Committee support. The proposal breaks that into 256,000 ada for community-facing technical coordination, 832,000 ada for protocol governance and evolution through the Parameter Committee, CIP editors, and Hard Fork Working Group, and 105,000 ada for a pilot independent technical review programme launching in 2027. The proposal also says the work is contingent on approval of the IntersectMBO budget proposal.

Several parts were well-supported in the proposal: the requested amount and work-package budget split, the specialist groups funded under WP2, the design of the WP3 independent review programme, the stated contingency on the IntersectMBO budget, and the use of treasury management smart contracts with oversight details. Other important controls were not independently evidenced enough for a treasury vote: the commitment to fully account for all spending and return unspent funds, and the proposed Appold audits and assurance. The review also flagged missing sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by replayable public evidence that pins and verifies the applicable Net Change Limit from chain data, plus stronger independent evidence for spending accountability, return of unspent funds, audit or assurance execution, and remedies if delivery or controls fall short.

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
- finding: Requested: Withdraw treasury funds to support Intersect Technical Steering Committee activities for 12 months across community engagement, protocol governance, and independent technical review.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination for 256,000 ADA, including expert attendance at ecosystem events and commissioned technical reports., WP 2: Protocol Governance and Evolution for 832,000 ADA, funding the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: Technical Review for 105,000 ADA, establishing a pilot independent technical review programme launching in 2027.
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests $298,250, stated as 1,193,000 ADA, to support TSC activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The work packages are budgeted at 256,000 ADA for WP1, 832,000 ADA for WP2, and 105,000 ADA for WP3, totaling 1,193,000 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): WP2 funds three specialist groups: the Parameter Committee, CIP editors, and Hard Fork Working Group.
- finding: Claim (governance, supported_in_proposal, high materiality): WP3 will establish a pilot independent technical review programme in 2027 with conflict-of-interest provisions, recorded and published recusals, and open reviewer selection against documented criteria.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that all expenditure will be fully accounted for and unspent funds returned to the Cardano treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews including deliverable verification, control testing, spend validation, and milestone evidence assessment.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests $298,250, stated as 1,193,000 ADA, to support TSC activities for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that all expenditure will be fully accounted for and unspent funds returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests $298,250, stated as 1,193,000 ADA, to support TSC activities for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show alignment with protocol safety and governance quality through specialist technical groups, hard fork coordination, independent review design, NCL disclosure, and smart-contract oversight. The nudge remains small because several important controls, including expenditure return and assurance execution, are still largely proposer commitments rather than completed evidence.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews including deliverable verification, control testing, spend validation, and milestone evidence assessment.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `26c95d8794ea3172d2544a1a8fd4c79c0988d1be1d646f68a40c0c736ee6d239`
- snapshot_bundle_hash: `19028084b266f0313f0d6e73782d8116fd7455571f61afe748d1c40fcf497a91`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5125, "NO": 0.3238, "YES": 0.1638}`

