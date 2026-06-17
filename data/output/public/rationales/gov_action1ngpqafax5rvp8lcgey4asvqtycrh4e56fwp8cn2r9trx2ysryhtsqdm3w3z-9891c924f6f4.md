# Rationale: gov_action1ngpqafax5rvp8lcgey4asvqtycrh4e56fwp8cn2r9trx2ysryhtsqdm3w3z
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` | Confidence: `0.2` | Readiness: `0`

## Plain-language explanation (codex-offline-review)
BEACN records NEEDS_MORE_INFO on Eternl: Path to Sustainability (2026-2027). This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Eternl: Path to Sustainability (2026-2027). The recorded treasury amount is 1.68M ADA. The strongest grounded claim is: Eternl is a non-custodial Cardano light wallet for the web, browser extension, Android, and iOS.

A material weak point is that this claim remains proposer-asserted or thinly supported: Budget and Budget Breakdown The Path to Sustainability Eternl will introduce a Pro plan for personal and company use. The blocking questions are: missing budget analysis; missing feasibility assessment; missing alternatives analysis. Reason code: DEEP_RESEARCH_REQUIRED.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 631
- finding: Expires after epoch: unknown
- finding: Treasury request: 1.68M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Eternl: Path to Sustainability (2026-2027)
- finding: Recipient: 
- finding: Stated amount: 1.68M ADA
- finding: Deliverables: Eternl is a non-custodial Cardano light wallet for the web, browser extension, Android, and iOS., Users rely on Eternl for payments, staking, governance, and DApp interaction., This proposal enables 12 months of operations, maintenance, and improvements., It includes frontend and backend maintenance and development, backend infrastructure, user support, and day-to-day operations.[^1] The goal is to keep Eternl secure, compatible, stable, and available as Cardano keeps evolving.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, low materiality): Eternl is a non-custodial Cardano light wallet for the web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, medium materiality): Users rely on Eternl for payments, staking, governance, and DApp interaction.
- finding: Claim (economic, supported_in_proposal, low materiality): This proposal enables 12 months of operations, maintenance, and improvements.
- finding: Claim (technical, supported_in_proposal, low materiality): It includes frontend and backend maintenance and development, backend infrastructure, user support, and day-to-day operations.[^1] The goal is to keep Eternl secure, compatible, stable, and available as Cardano keeps evolving.
- finding: Claim (economic, proposer_asserted, high materiality): Budget and Budget Breakdown The Path to Sustainability Eternl will introduce a Pro plan for personal and company use.
- finding: Claim (economic, supported_in_proposal, low materiality): | Plan | Price | |----------|--------------------------:| | Personal | $96/year ($8/month) | | Company | $384/year ($32/month)[^2] | Eternl has an install base of about 100,000 on the browser extension and about 30,000 across Android and iOS.
- missing: Independent evidence for: Budget and Budget Breakdown The Path to Sustainability Eternl will introduce a Pro plan for personal and company use.
- missing: budget analysis
- missing: feasibility assessment
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1680000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unsustainable
- finding: Financial confidence: 0.55
- missing: milestone-gated disbursement
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: low
- finding: Governance risk: low
- finding: Technical risk: low
- finding: Treasury exposure risk: low
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: not confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: rollback/remedy path
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet for the web, browser extension, Android, and iOS." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Budget and Budget Breakdown The Path to Sustainability Eternl will introduce a Pro plan for personal and company use." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1680000
- Risk review: Execution risk: low
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet for the web, browser extension, Android, and iOS." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional voting is blocked until dossier quality gates pass.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Dossier completeness not confirmed for this treasury proposal.
- Claims and evidence missing: Independent evidence for: Budget and Budget Breakdown The Path to Sustainability Eternl will introduce a Pro plan for personal and company use.
- Claims and evidence missing: budget analysis
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.
- Missing dossier section: budget analysis
- Missing dossier section: feasibility assessment
- Missing dossier section: alternatives analysis
- Missing dossier section: failure-mode analysis
- Missing dossier section: community impact analysis

## Reproducibility
- input_hash: `9891c924f6f4cc140fbc49ce4b5e0d28e9f6cc69d68f16988c5a28533f755271`
- snapshot_bundle_hash: `1e4bb0122a1505e68e43143c2df7f131e48a9640da6d45103f6682572d6733b7`
- soul_commit: `6bf4a7d7baa636417ad929e543cfb8be8fae1f03`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1a7b2a06eb1757aad5065883cf73f8066d2dc3a6`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

