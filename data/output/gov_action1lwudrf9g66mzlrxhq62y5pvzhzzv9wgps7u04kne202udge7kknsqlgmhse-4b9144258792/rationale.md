# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (codex-offline-review)
BEACN records NEEDS_MORE_INFO on Eternl: Path to Sustainability - v2. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, improvements, infrastructure, support, administration, and audit/oversight activities.. The recorded treasury amount is 2350000. The strongest grounded claim is: Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual operating costs for 12 months.

A material weak point is that this claim remains proposer-asserted or thinly supported: The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment. Reason code: DEEP_RESEARCH_REQUIRED.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, improvements, infrastructure, support, administration, and audit/oversight activities.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development, Backend infrastructure and operations, User support, Day-to-day administration and operations, Periodic independent audits of treasury fund use and oversight metrics, Development of Eternl Core, Eternl Hub, hardware wallet support, wallet data export, and governance tooling
- finding: Deadline/expiry: Delivery period August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual operating costs for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as ₳1,292,500 frontend, ₳587,500 backend, ₳117,500 support, ₳305,500 admin, and ₳47,000 audits.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs, and about 5,500 Pro users would fully cover the annual $420,000 cost.
- finding: Claim (economic, supported_in_proposal, high materiality): After withdrawal, the proposer says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, supported_in_proposal, medium materiality): Independent audits by an unaffiliated party are planned for February 2027 and August 2027 to review custody, conversion, spending, balances, Pro plan income relevant to repayment, and refunds or repayments.
- missing: Independent evidence for: The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- missing: Independent evidence for: Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs, and about 5,500 Pro users would fully cover the annual $420,000 cost.
- missing: Independent evidence for: Eternl states that 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: If treasury funds are not received and paid licenses are insufficient beyond August, the proposer says it may let developers go, scale down to essential maintenance, focus outside Cardano, or remove the free option.
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
- finding: Six-month treasury flow regime: unsustainable
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
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual operating costs for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE." — so cost or precedent may outweigh the benefit.
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
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2.35M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 of annual operating costs for 12 months." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- Claims and evidence missing: Independent evidence for: Eternl has about 100,000 browser extension installs and about 30,000 Android and iOS installs, and about 5,500 Pro users would fully cover the annual $420,000 cost.
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

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.
- Missing dossier section: complete proposal summary
- Missing dossier section: budget analysis
- Missing dossier section: feasibility assessment
- Missing dossier section: risk analysis
- Missing dossier section: alternatives analysis
- Missing dossier section: failure-mode analysis
- Missing dossier section: community impact analysis

## Reproducibility
- input_hash: `4b9144258792b67831dd10811a5d34394998a767f498f3f0097959d243f72931`
- snapshot_bundle_hash: `ee40841448b2b8d94e2f46a2e4bdc89ded2115dfb21144ca10b66b5f244780c0`
- soul_commit: `6bf4a7d7baa636417ad929e543cfb8be8fae1f03`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `693efb97d136543a3565ea51fab80f1cada41b23`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `339`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

