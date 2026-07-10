# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims include a clear budget breakdown, externally checkable Hydra voting and NCL references, disclosed smart-contract custody controls, and planned assurance, which improve evidence quality and treasury stewardship beyond a thin ask. The adjustment remains small because the document still relies on proposer assertions for strategic impact and because execution is contingent on another IntersectMBO budget approval.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a Treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work.

The proposal requests 1,193,000 ada for 12 months of Intersect Technical Steering Committee support, covering community-facing technical coordination, protocol governance work, and a pilot independent technical review programme. The proposer gives a clear budget split: 256,000 ada for WP1, 832,000 ada for WP2, and 105,000 ada for WP3. The review found several stronger points: the proposal anchor is available and replayable, the requested amount does not appear to breach the stated 350M ada Net Change Limit at submission, the Hydra voting support claim is externally checkable, and the custody setup through Sundae Labs smart contracts is disclosed.

The hold comes from the evidence gaps that still matter for a Treasury vote. Some claims remain proposer assertions rather than independently supported facts, including that all spending will be fully accounted for and unspent funds returned, and that the TSC work will deliver the claimed strategic benefits for uptime, DRep participation, governance quality, and ecosystem resilience. The review also flagged thin claims-and-evidence status, missing sustainability and cost-benefit clarity, missing independent assurance, and an incomplete dependency map.

To unblock a directional vote, BEACN would need the applicable Net Change Limit pinned and independently verified from public chain evidence. Stronger independent evidence for spending accountability, return of unspent funds, assurance, dependencies, and cost-benefit clarity would also reduce uncertainty.

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
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee Support for 12 months across community engagement, protocol governance, and independent technical review.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor
- finding: Stated amount: 1193000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including technical expert attendance at major ecosystem events and commissioned technical reports, WP 2: Protocol Governance and Evolution, funding the Parameter Committee, CIP editors, and Hard Fork Working Group, WP 3: Technical Review, establishing a pilot independent technical review programme launching in 2027, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect's Technical Steering Committee requests 1,193,000 ADA, described as $298,250, for 12 months of support activities.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 256,000 ADA for WP1, 832,000 ADA for WP2, and 105,000 ADA for WP3.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation, audited results, and an audit report.
- finding: Claim (economic, independently_verifiable, high materiality): The requested amount does not, at submission, breach the 350M ADA Net Change Limit covering Epoch 613 to Epoch 713.
- missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: The proposal claims TSC work is foundational technical governance capacity that supports Cardano's strategy pillars, including uptime, DRep participation, governance quality, and ecosystem resilience.
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
- finding: Strongest YES: the proposal substantiates "Intersect's Technical Steering Committee requests 1,193,000 ADA, described as $298,250, for 12 months of support activities." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect's Technical Steering Committee requests 1,193,000 ADA, described as $298,250, for 12 months of support activities." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by +0.020 (clamped to ±0.05): A small positive nudge is justified because the claims include a clear budget breakdown, externally checkable Hydra voting and NCL references, disclosed smart-contract custody controls, and planned assurance, which improve evidence quality and treasury stewardship beyond a thin ask. The adjustment remains small because the document still relies on proposer assertions for strategic impact and because execution is contingent on another IntersectMBO budget approval.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: The proposal claims TSC work is foundational technical governance capacity that supports Cardano's strategy pillars, including uptime, DRep participation, governance quality, and ecosystem resilience.
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
- snapshot_bundle_hash: `1b31f5d522c8744ebcc7086b078ac2f24be72725551971a8e65346604fda7c66`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

