# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.8733` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show a concrete budget and some stated oversight mechanisms, but the deterministic assessment identifies thin evidence and missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN doctrine, treasury stewardship and evidence quality outweigh plausible ecosystem value, so the bounded adjustment should lean cautiously negative rather than reward asserted repayment and adoption claims.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Eternl: Path to Sustainability - v2. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12 months of operations, maintenance, and improvements for the Eternl non-custodial Cardano light wallet, including frontend and backend maintenance and development, backend infrastructure, user support, day-to-day operations, audits, and oversight metrics.. The recorded treasury amount is 2350000. The strongest grounded claim is: Eternl requests ₳2,350,000 at about $0.1787 per Ada to fund a 12-month operating period from August 2026 to July 2027.

A material weak point is that this claim remains proposer-asserted or thinly supported: Eternl says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: 12 months of operations, maintenance, and improvements for the Eternl non-custodial Cardano light wallet, including frontend and backend maintenance and development, backend infrastructure, user support, day-to-day operations, audits, and oversight metrics.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development, Backend infrastructure and operations, User support, Administration and day-to-day operations, Periodic independent audits of treasury fund use and oversight metrics, Eternl Pro plan rollout, Governance tooling enhancements, Eternl Core rewrite, Eternl Hub, hardware wallet support, and wallet data export improvements
- finding: Deadline/expiry: 12-month delivery period from August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000 at about $0.1787 per Ada to fund a 12-month operating period from August 2026 to July 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states Eternl's annual operating cost is about $420,000, funding 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget allocates 55% to frontend, 25% to backend, 5% to support, 13% to admin, and 2% to audits.
- finding: Claim (economic, proposer_asserted, high materiality): Eternl says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, proposer_asserted, high materiality): Eternl says independent fund-use audits will be performed in February 2027 and August 2027 by a party unaffiliated with Tastenkunst GmbH or the Eternl team.
- finding: Claim (economic, proposer_asserted, high materiality): Eternl states it will assess repayment every December and June and use surplus treasury stablecoins plus paid plan income above $420,000 to repay the treasury until $420,000 in Ada has been repaid.
- missing: Independent evidence for: Eternl says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- missing: Independent evidence for: Eternl says independent fund-use audits will be performed in February 2027 and August 2027 by a party unaffiliated with Tastenkunst GmbH or the Eternl team.
- missing: Independent evidence for: Eternl states it will assess repayment every December and June and use surplus treasury stablecoins plus paid plan income above $420,000 to repay the treasury until $420,000 in Ada has been repaid.
- missing: Independent evidence for: Eternl claims it has about 100,000 browser extension installs and about 30,000 Android and iOS installs combined.
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
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000 at about $0.1787 per Ada to fund a 12-month operating period from August 2026 to July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000 at about $0.1787 per Ada to fund a 12-month operating period from August 2026 to July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show a concrete budget and some stated oversight mechanisms, but the deterministic assessment identifies thin evidence and missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN doctrine, treasury stewardship and evidence quality outweigh plausible ecosystem value, so the bounded adjustment should lean cautiously negative rather than reward asserted repayment and adoption claims.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~19 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- Claims and evidence missing: Independent evidence for: Eternl says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- Claims and evidence missing: Independent evidence for: Eternl says independent fund-use audits will be performed in February 2027 and August 2027 by a party unaffiliated with Tastenkunst GmbH or the Eternl team.
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
- input_hash: `92026a67255fb20eec5928dec5650e070b57441e885a6605739739254b477d89`
- snapshot_bundle_hash: `12b7265b0c8f1716443613c017e19ac5506f277cb627ed33911a79d41ca7be46`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `651`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1753, "NO": 0.7831, "YES": 0.0416}`

