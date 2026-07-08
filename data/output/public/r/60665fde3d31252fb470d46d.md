# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NO**
Score: `-0.3133` (raw `-0.2833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7983` | Readiness: `0.9`
> Reasoning layer (precomputed): The proposal has detailed milestones, budget lines, and oversight structure, but several high-materiality adoption and repayment claims remain proposer-asserted, and the repayment terms are not fully defined until M1 contracting. Under the doctrine, plausible ecosystem growth should not outweigh treasury stewardship and evidence quality when a large withdrawal depends on future commercial uptake and partially unresolved reimbursement terms.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large Treasury withdrawal, and several material claims needed to justify that spending were not backed by independent, replayable evidence.

The proposal requested 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency. It described work on a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent smart-contract audit, launch activity, public reporting, and a revenue-share repayment mechanism. The proposal did substantiate the requested amount, estimated at about $1,093,231 at $0.22 per ada, including a 3% Intersect administration fee, and it provided detailed milestones, budget lines, and an oversight structure.

However, some of the most important adoption and execution claims remained proposer-asserted rather than independently evidenced. The review found missing independent evidence that Phase 1 is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification. It also found missing independent evidence for the claim that Sellout invested over $130,000 of its own capital into Phase 1. The repayment commitment was positive, but the exact revenue base and payment cadence were still to be finalized later during M1 contracting.

Because this action would spend shared Treasury ada, BEACN applied elevated scrutiny. The anchor document was available and the proposal was reviewable, but the claims-and-evidence status was thin, execution risk was medium, and the risk review lacked independent assurance and a dependency map. The strongest YES case was that the amount and intended Phase 2 scope were clearly stated, but that was not enough to overcome the unsupported material claims and unresolved repayment details.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 4.97M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, security audit, and launch campaign.
- finding: Recipient: not stated in document
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace with on-chain settlement, Smart-contract royalty enforcement, Per-event anti-scalping controls, Custodial wallet onboarding in Sellout flow, Organizer dashboard and tools, Independent third-party smart-contract audit with published remediation, Public launch campaign and trade-show activations, Public metrics dashboard and quarterly reporting, Revenue-share repayment mechanism to reimburse the Treasury
- finding: Deadline/expiry: 8 months over five milestones
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 of the Sellout ticketing system is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- finding: Claim (economic, proposer_asserted, medium materiality): Sellout has invested over $130,000 of its own capital into Phase 1.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, equivalent to about $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 is planned to deliver a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, and a launch campaign.
- finding: Claim (economic, supported_in_proposal, high materiality): The team commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism, with 25% of fees paid until reimbursement and 5% thereafter.
- finding: Claim (governance, supported_in_proposal, high materiality): The exact revenue-base definition and payment cadence for the repayment mechanism will be finalized during M1 contracting with the oversight committee.
- missing: Independent evidence for: Phase 1 of the Sellout ticketing system is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- missing: Independent evidence for: Sellout has invested over $130,000 of its own capital into Phase 1.
- missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- missing: Independent evidence for: The Yellowstone Club 2026 deployment is projected to move more than $6 million through Cardano in year one, based on $5.88 million in 2025 historical volume.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 4969231
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.74
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, equivalent to about $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 of the Sellout ticketing system is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 4969231
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, equivalent to about $1,093,231 at $0.22 per ADA, including a 3% Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has detailed milestones, budget lines, and oversight structure, but several high-materiality adoption and repayment claims remain proposer-asserted, and the repayment terms are not fully defined until M1 contracting. Under the doctrine, plausible ecosystem growth should not outweigh treasury stewardship and evidence quality when a large withdrawal depends on future commercial uptake and partially unresolved reimbursement terms.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 of the Sellout ticketing system is already live on Cardano mainnet with on-chain event creation, CIP-68 ticket minting, transfers, and attendance verification.
- Claims and evidence missing: Independent evidence for: Sellout has invested over $130,000 of its own capital into Phase 1.
- Claims and evidence status is thin.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `6b0c013556ee0118b6f09090423749cc3bbc725dbafffb72a07335fcbe2412ad`
- snapshot_bundle_hash: `45a67c9e06ca71caee71406c4dbbe6a2be7f030e0f4cce3505276d49d289e465`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1961, "NO": 0.7594, "YES": 0.0445}`

