# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.8733` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims include useful budget structure, repayment commitments, and audit intentions, but the deterministic assessment already found thin evidence and incomplete treasury, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's hierarchy, a large treasury withdrawal with material adoption and sustainability assumptions that are mostly asserted rather than evidenced warrants a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Eternl: Path to Sustainability - v2. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, and improvements, including frontend and backend work, infrastructure, user support, administration, and audits/oversight.. The recorded treasury amount is 2350000. The strongest grounded claim is: The proposal requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual costs for 12 months.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, and improvements, including frontend and backend work, infrastructure, user support, administration, and audits/oversight.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development for Chrome extension, web/PWA, iOS, Android, beta channel, CIPs, hardfork features, multisig, dApp interoperability, app store compliance, and hardware wallet support, Backend infrastructure and operations including multi-region servers, Cardano nodes, DBSync indexers, application servers, metadata aggregation, Hub backend services, monitoring, alerting, and incident response, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation tooling, User support through Discord ticketing, Telegram, public channels, ecosystem project support, wiki maintenance, and educational videos, Day-to-day operations including release management, hardware wallet vendor coordination, dApp/CIP coordination, code review, and security practices, Periodic independent audits of treasury fund use and implementation of oversight metrics
- finding: Deadline/expiry: 12-month delivery period, August 2026 to July 2027
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual costs for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is allocated as 55% frontend, 25% backend, 5% support, 13% admin, and 2% audits.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce Pro plans priced at $96/year for personal users and $360/year for company users, and asserts that roughly 5,500 users, about 4.2% of its install base, would fully cover the $420,000 annual cost.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl states it has about 100,000 browser-extension installs and about 30,000 Android/iOS installs.
- missing: Independent evidence for: Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS used for payments, staking, governance, and DApp interaction.
- missing: Independent evidence for: Eternl states it has about 100,000 browser-extension installs and about 30,000 Android/iOS installs.
- missing: Independent evidence for: Eternl asserts that 10-18% of Cardano mainnet transactions are conducted via Eternl and that Eternl has provided multi-platform access with basically zero downtime for over five years.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual costs for 12 months." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual costs for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims include useful budget structure, repayment commitments, and audit intentions, but the deterministic assessment already found thin evidence and incomplete treasury, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's hierarchy, a large treasury withdrawal with material adoption and sustainability assumptions that are mostly asserted rather than evidenced warrants a small cautionary nudge rather than a positive adjustment.
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
- Claims and evidence missing: Independent evidence for: Eternl states it has about 100,000 browser-extension installs and about 30,000 Android/iOS installs.
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
- input_hash: `0f23c076d370c993ee634edb54b22b728f376cb95b3108895b7847a8b595bda0`
- snapshot_bundle_hash: `dc418873f9ef1516d6b1ba5a3638b4dce13f3ebf3beb75e736f27ed203dc35ff`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `643`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1753, "NO": 0.7831, "YES": 0.0416}`

