# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NO**
Score: `-0.2333` (raw `-0.2533` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7783` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show comparatively concrete treasury controls, budget allocation, on-chain administration details, external assurance, NCL compliance, and governance-process references, while the contingency on the main IntersectMBO budget and several asserted benefits argue against a larger adjustment.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not clear the higher evidence bar for spending shared ADA, especially with important execution dependencies and treasury sustainability concerns left insufficiently supported.

The action requested 1,193,000 ada for 12 months of Intersect Technical Steering Committee support, covering community-facing technical coordination, protocol governance work, and a pilot independent technical review programme. The proposal gave a concrete budget split across the three work packages and provided a pinned, replayable anchor document. It also included on-chain administration details, stated milestone-based reporting, external oversight, full expenditure accounting, and return of unspent funds.

Several claims were well-supported or independently checkable: the requested amount and budget allocation, the Hydra Voting support threshold, compliance with the 350M Net Change Limit at submission, and the stated treasury management smart contract structure. But some material claims remained proposer assertions rather than independently evidenced, including that the work depends on approval of the main IntersectMBO budget proposal, and that all spending will be fully accounted for with unused funds returned.

The review gates found medium execution risk, thin claims-and-evidence status, missing cost-benefit clarity, no clear sustainability path, missing independent assurance, and no dependency map. Because treasury actions require elevated scrutiny and the treasury flow signal was already in an unsustainable regime, BEACN concluded that the cost and precedent risk outweighed the substantiated benefits, despite recognizing the strongest YES case that the proposal had concrete scope, budget, and controls.

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
- finding: Recipient: Intersect, on behalf of the vendor, with funds directed to the 2026 Treasury Reserve Smart Contract stake address stated in the document.
- finding: Stated amount: 1193000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including attendance of technical experts at major ecosystem events and commissioning technical reports., WP 2: Protocol Governance and Evolution, including support for the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: Technical Review, including establishment of a pilot independent technical review programme launching in 2027., Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and full expenditure accounting., Return of any unspent funds to the Cardano treasury.
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect's Technical Steering Committee requests $298,250, equivalent to 1,193,000 ADA, to support activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 256,000 ADA for WP 1, 832,000 ADA for WP 2, and 105,000 ADA for WP 3.
- finding: Claim (governance, proposer_asserted, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (economic, proposer_asserted, high materiality): All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (economic, independently_verifiable, high materiality): The requested amount does not at submission breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713.
- missing: Independent evidence for: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold and may include deliverable verification, control testing, spend validation, and milestone evidence assessment.
- missing: Independent evidence for: The TSC support work is presented as foundational technical governance infrastructure aligned with protocol reliability, DRep decision-making, and treasury stewardship goals.
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
- finding: Strongest YES: the proposal substantiates "Intersect's Technical Steering Committee requests $298,250, equivalent to 1,193,000 ADA, to support activities for 12 months." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect's Technical Steering Committee requests $298,250, equivalent to 1,193,000 ADA, to support activities for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by +0.020 (clamped to ±0.05): A small positive nudge is justified because the extracted claims show comparatively concrete treasury controls, budget allocation, on-chain administration details, external assurance, NCL compliance, and governance-process references, while the contingency on the main IntersectMBO budget and several asserted benefits argue against a larger adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- Claims and evidence missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `98932c84af8b7974d896635388edf301ab03cee90e550ce0c4e9b0e85aa7073d`
- snapshot_bundle_hash: `3fd4124586713dbf32e86efcc9f882058331608e10a46296c5a565bf5951cc47`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.214, "NO": 0.7379, "YES": 0.048}`

