# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9033` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal includes some concrete treasury controls, audits, and repayment mechanics, but the deterministic assessment identifies thin evidence and incomplete treasury, feasibility, risk, alternatives, and failure-mode analysis for a large non-milestone treasury withdrawal. Under the doctrine, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Eternl: Path to Sustainability - v2. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, support, infrastructure, audits, and improvements while Eternl introduces paid Pro plans.. The recorded treasury amount is 2350000. The strongest grounded claim is: Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover about $420,000 in annual costs for a 12-month period.

A material weak point is that this claim remains proposer-asserted or thinly supported: Eternl states it has about 100,000 browser extension installs and about 30,000 Android and iOS installs, and that about 5,500 Pro plan users would cover the annual $420,000 cost. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, support, infrastructure, audits, and improvements while Eternl introduces paid Pro plans.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development for web, browser extension, iOS, Android, and beta channels, Backend infrastructure and operations including nodes, DBSync/indexers, application servers, metadata aggregation, monitoring, and incident response, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation, User support through Discord ticketing, Telegram, public channels, project support, Wiki updates, and educational videos, Periodic independent audits of treasury fund use and oversight metrics in February 2027 and August 2027
- finding: Deadline/expiry: August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover about $420,000 in annual costs for a 12-month period.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (governance, supported_in_proposal, high materiality): Eternl plans to convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal is not milestone-based and is intended to ensure funds availability for the full 12-month period.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl states it has about 100,000 browser extension installs and about 30,000 Android and iOS installs, and that about 5,500 Pro plan users would cover the annual $420,000 cost.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl states that 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: Eternl states it has about 100,000 browser extension installs and about 30,000 Android and iOS installs, and that about 5,500 Pro plan users would cover the annual $420,000 cost.
- missing: Independent evidence for: Eternl states that 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: Eternl says that without treasury funds it may have to let developers go, scale down to essential maintenance, shift focus outside Cardano, or remove the free option if paid licenses are insufficient.
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
- finding: Strongest YES: the proposal substantiates "Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover about $420,000 in annual costs for a 12-month period." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl states it has about 100,000 browser extension installs and about 30,000 Android and iOS installs, and that about 5,500 Pro plan users would cover the annual $420,000 cost." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover about $420,000 in annual costs for a 12-month period." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal includes some concrete treasury controls, audits, and repayment mechanics, but the deterministic assessment identifies thin evidence and incomplete treasury, feasibility, risk, alternatives, and failure-mode analysis for a large non-milestone treasury withdrawal. Under the doctrine, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~17 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Eternl states it has about 100,000 browser extension installs and about 30,000 Android and iOS installs, and that about 5,500 Pro plan users would cover the annual $420,000 cost.
- Claims and evidence missing: Independent evidence for: Eternl states that 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- input_hash: `7be9d77c15b91373a48f0dbfb359c8193d088e2b0d0a98185f750ff04b9b4aa2`
- snapshot_bundle_hash: `2ab93975353b8399e9c277a3ccc9b4ed24e872afbcdf8305fa2680429ab46afa`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `251`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1675, "NO": 0.792, "YES": 0.0404}`

