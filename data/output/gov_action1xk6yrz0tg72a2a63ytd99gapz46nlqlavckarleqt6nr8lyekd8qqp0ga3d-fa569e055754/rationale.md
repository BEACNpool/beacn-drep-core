# Rationale: gov_action1xk6yrz0tg72a2a63ytd99gapz46nlqlavckarleqt6nr8lyekd8qqp0ga3d
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.52` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal has substantial public-benefit upside if its adoption and repayment claims hold, and it provides a detailed budget and milestone structure, but the deterministic assessment is blocked for missing treasury, feasibility, risk, alternatives, and failure-mode analysis. Under the doctrine's preference for treasury stewardship and evidence quality over plausible but thin ecosystem growth, the bounded lean should apply a small cautionary nudge rather than reward the spend.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury request did not clear the evidence bar for a 4,969,231 ada withdrawal. The proposal has a pinned, replayable anchor and describes a potentially useful Cardano-native ticketing platform, but the review found too many missing diligence pieces for a directional YES, especially around budget, feasibility, risk, alternatives, and failure modes.

The action asked to fund Phase 2 of a Sellout.io ticketing platform built by Anvil Development Agency, with Intersect as budget administrator. The requested work includes a secondary ticket marketplace, on-chain settlement, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, a third-party smart-contract audit, launch activity, public metrics, quarterly reporting, and a revenue-share repayment mechanism.

Some claims were supported by the proposal itself: the requested amount, the 8-month milestone structure, the Phase 2 deliverables, and the stated repayment mechanism of 25% of fees until reimbursement and 5% afterward. Other important claims were only proposer-asserted or lacked independent evidence in the review, including that Phase 1 is already live on Cardano mainnet, that Sellout funded more than $130,000 itself, and that Sellout has 200,000+ registered users, 250,000+ tickets issued, and 350+ events annually.

Because this is a treasury withdrawal, BEACN applied elevated scrutiny. The review found the claims-and-evidence record thin, treasury analysis incomplete, risk review thin, and synthesis blocked. The strongest YES case was that the proposal clearly states the funding amount, dollar estimate, timeline, and milestone-gated structure, but seven blockers remained open. On that record, BEACN judged that approving the withdrawal would require more certainty than the supplied evidence supports.

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
- finding: Requested: Fund Phase 2 of a production Cardano-native ticketing platform operated by Sellout.io and built by Anvil Development Agency, including a secondary marketplace, royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, audit, and launch campaign.
- finding: Recipient: Anvil Development Agency, Inc. / Intersect as budget administrator
- finding: Stated amount: 4,969,231
- finding: Deliverables: Secondary marketplace for listing, pricing, and reselling tickets with on-chain settlement, Smart-contract-enforced royalty splits, Per-event anti-scalping controls including price ceilings, transfer limits, identity-binding, and time restrictions, Custodial wallet onboarding inside Sellout's existing flow, Organizer dashboard and tools, Independent third-party smart-contract security audit with published remediation, Public launch campaign and trade-show activations, Public metrics dashboard and quarterly reporting, Revenue-share repayment mechanism to reimburse the Treasury
- finding: Deadline/expiry: 8 months over five milestones
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 4,969,231 ada, approximately $1,093,231 at $0.22 per ADA, over 8 months with milestone-gated disbursement.
- finding: Claim (technical, proposer_asserted, high materiality): Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 2 will deliver a secondary marketplace, smart-contract royalty enforcement, anti-scalping controls, wallet onboarding, organizer tools, an independent audit, and launch amplification.
- finding: Claim (adoption, proposer_asserted, high materiality): Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- finding: Claim (adoption, proposer_asserted, high materiality): The Yellowstone Club 2026 concert series is presented as the anchor deployment and is projected to move over $6,000,000 through Cardano in Year 1.
- missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital.
- missing: Independent evidence for: Sellout has 200,000+ registered users, has issued 250,000+ tickets to date, and currently supports 350+ events annually.
- missing: Independent evidence for: The proposal targets 200+ events on-chain, 75,000+ CIP-68 NFT tickets, 150,000+ on-chain interactions, $6,000,000+ ticket revenue on-chain, and 20,000+ new wallets within 12 months from launch.
- missing: Independent evidence for: The Yellowstone Club 2026 concert series is presented as the anchor deployment and is projected to move over $6,000,000 through Cardano in Year 1.
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
- finding: Strongest NO: a material claim is unsupported — "Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital." — so cost or precedent may outweigh the benefit.
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
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has substantial public-benefit upside if its adoption and repayment claims hold, and it provides a detailed budget and milestone structure, but the deterministic assessment is blocked for missing treasury, feasibility, risk, alternatives, and failure-mode analysis. Under the doctrine's preference for treasury stewardship and evidence quality over plausible but thin ecosystem growth, the bounded lean should apply a small cautionary nudge rather than reward the spend.
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
- Claims and evidence missing: Independent evidence for: Phase 1 of the ticketing platform is already live on Cardano mainnet and was funded by Sellout with over $130,000 of its own capital.
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
- input_hash: `fa569e05575479fccb98a7f4fff78cbc8b610588ca8152239ab52efd93b24792`
- snapshot_bundle_hash: `a09980feec0aa3038ec079bd5e80ed36ee78f29ee0490b6cb403645a7a2c37cc`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1217`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2146, "NO": 0.7433, "YES": 0.0421}`

