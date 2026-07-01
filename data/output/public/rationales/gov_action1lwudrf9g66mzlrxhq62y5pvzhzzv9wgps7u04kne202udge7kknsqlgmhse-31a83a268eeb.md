# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.8733` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal describes a useful wallet and includes a budget table, repayment concept, public-wallet commitment, and audit timing, but the deterministic assessment says the treasury analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis are incomplete. Under the doctrine, a large treasury withdrawal with thin or unverifiable evidence should receive a cautious negative nudge rather than extra benefit for plausible ecosystem value.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Eternl: Path to Sustainability - v2. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, support, infrastructure, audits/oversight metrics, and continued development while Eternl introduces paid Pro plans.. The recorded treasury amount is 2350000. The strongest grounded claim is: The proposal asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover around $420,000 of annual operating cost.

A material weak point is that this claim remains proposer-asserted or thinly supported: Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: 2.35M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, support, infrastructure, audits/oversight metrics, and continued development while Eternl introduces paid Pro plans.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development, Backend infrastructure and operations, User support, Day-to-day administration and operations, Periodic independent audits of treasury fund use and oversight metrics, Eternl Core rewrite, Eternl Hub, enhanced hardware wallet support, enhanced wallet data export, and governance tooling improvements
- finding: Deadline/expiry: 12-month delivery period from August 2026 to July 2027
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover around $420,000 of annual operating cost.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is allocated as ₳1,292,500 frontend, ₳587,500 backend, ₳117,500 support, ₳305,500 admin, and ₳47,000 audits.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl has an install base of about 100,000 browser-extension installs and about 30,000 Android and iOS installs combined.
- finding: Claim (economic, supported_in_proposal, high materiality): If roughly 5,500 users, or about 4.2% of the install base, buy a Pro plan, Pro-plan income would fully cover the annual $420,000 cost.
- finding: Claim (economic, proposer_asserted, high materiality): The proposer says up to $420,000 worth of Ada will be converted into stablecoins and deposited into a public company wallet, with any Ada above that amount returned to the treasury.
- missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction.
- missing: Independent evidence for: Eternl has an install base of about 100,000 browser-extension installs and about 30,000 Android and iOS installs combined.
- missing: Independent evidence for: The proposer says up to $420,000 worth of Ada will be converted into stablecoins and deposited into a public company wallet, with any Ada above that amount returned to the treasury.
- missing: Independent evidence for: Eternl claims that 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- finding: Requested ADA: 2.35M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unknown (stale snapshot)
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
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover around $420,000 of annual operating cost." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction." — so cost or precedent may outweigh the benefit.
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
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2.35M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover around $420,000 of annual operating cost." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal describes a useful wallet and includes a budget table, repayment concept, public-wallet commitment, and audit timing, but the deterministic assessment says the treasury analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis are incomplete. Under the doctrine, a large treasury withdrawal with thin or unverifiable evidence should receive a cautious negative nudge rather than extra benefit for plausible ecosystem value.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~19 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- Claims and evidence missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction.
- Claims and evidence missing: Independent evidence for: Eternl has an install base of about 100,000 browser-extension installs and about 30,000 Android and iOS installs combined.
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
- input_hash: `31a83a268eebfcf6e60bcb1ede3fecc4f7c7e17ae881f57794373bc6f1040d16`
- snapshot_bundle_hash: `1dc48aead5a5e7416019c03912f5f20d0f3a8a26993efb723518cb413357967c`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `715`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1753, "NO": 0.7831, "YES": 0.0416}`

