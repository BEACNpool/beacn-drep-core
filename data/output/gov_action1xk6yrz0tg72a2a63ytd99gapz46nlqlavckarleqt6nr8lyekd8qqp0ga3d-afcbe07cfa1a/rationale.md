# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.52` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims include a detailed budget, milestones, repayment structure, and some independently checkable addresses and future metric commitments, but the highest-materiality benefits depend on proposer assertions about live deployment, user base, contracted anchor demand, projected transaction volume, and NCL compliance. Given the deterministic assessment is blocked for missing complete treasury, feasibility, risk, alternatives, and failure-mode analysis, the evidence quality does not justify a positive nudge for a large treasury withdrawal.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large Treasury withdrawal request, and the review found too many material gaps for shared ADA to be released with confidence.

The proposal asked for 4,969,231 ada to fund Phase 2 of a Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency. It said the work would include a secondary ticket marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent smart-contract audit, launch activity, public metrics, and governance reporting over 8 months. The proposal did substantiate the requested amount, the approximate dollar value, the 8-month schedule, and the stated repayment mechanism of 25% of fees until reimbursement and 5% afterward.

However, several of the most important adoption claims were still only proposer assertions in the supplied review. That includes the claim that Phase 1 is already live on Cardano mainnet and self-funded with over $130,000, the claim that Sellout has 200,000+ registered users and has issued 250,000+ tickets, and the claim of a contracted Yellowstone Club deployment projected to move over $6 million through Cardano in year one. For a Treasury action, BEACN requires stronger replayable evidence for claims that carry the main public benefit case.

The review also found decisive blockers: missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis. Treasury analysis was incomplete, risk review was thin, and the dossier lacked mitigation evidence and independent assurance. Even though the strongest YES case recognized a real funding request with milestones and a repayment structure, the open blockers outweighed that support, so BEACN voted NO.

## Review Tree
- overall_status: `blocked`

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, security audit, and launch campaign.
- finding: Recipient: not stated in document
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace for listing, pricing, and reselling tickets with on-chain settlement, Smart-contract royalty enforcement for artists and venues, Configurable per-event anti-scalping controls, Custodial wallet onboarding inside Sellout's existing flow, Organizer dashboard and ticket lifecycle tools, Independent third-party smart-contract security audit with published report and remediation, Public launch campaign and three trade-show activations, Public metrics dashboard and governance reporting
- finding: Deadline/expiry: 8 months
- finding: Claim (adoption, proposer_asserted, high materiality): Phase 1 of the Sellout ticketing platform is already live on Cardano mainnet and was funded entirely by Sellout with over $130,000 invested.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursement.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 will deliver a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, and launch amplification.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 concert series is a contracted anchor deployment projected to move over $6 million through Cardano in year one.
- finding: Claim (economic, supported_in_proposal, high materiality): The team commits to repay $1,093,231 to the Cardano Treasury through a revenue-share mechanism using 25% of all fees until full reimbursement and 5% thereafter.
- missing: Independent evidence for: Phase 1 of the Sellout ticketing platform is already live on Cardano mainnet and was funded entirely by Sellout with over $130,000 invested.
- missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is a contracted anchor deployment projected to move over $6 million through Cardano in year one.
- missing: Independent evidence for: The requested amount does not breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713 at the moment of submission.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 4.97M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursement." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Phase 1 of the Sellout ticketing platform is already live on Cardano mainnet and was funded entirely by Sellout with over $130,000 invested." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 4.97M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursement." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims include a detailed budget, milestones, repayment structure, and some independently checkable addresses and future metric commitments, but the highest-materiality benefits depend on proposer assertions about live deployment, user base, contracted anchor demand, projected transaction volume, and NCL compliance. Given the deterministic assessment is blocked for missing complete treasury, feasibility, risk, alternatives, and failure-mode analysis, the evidence quality does not justify a positive nudge for a large treasury withdrawal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Phase 1 of the Sellout ticketing platform is already live on Cardano mainnet and was funded entirely by Sellout with over $130,000 invested.
- Claims and evidence missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `afcbe07cfa1a5c8ed29a47e5ab388b9baa9e8aa258b95d41efc0265a3a1c584e`
- snapshot_bundle_hash: `42ba43302bb34cca872b0dda33c103a72237377e8b3123bb8d33973dc96bb059`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `959`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2146, "NO": 0.7433, "YES": 0.0421}`

