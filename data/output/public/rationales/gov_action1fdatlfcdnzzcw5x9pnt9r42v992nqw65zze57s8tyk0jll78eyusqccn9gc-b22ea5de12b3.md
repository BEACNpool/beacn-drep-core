# Rationale: gov_action1fdatlfcdnzzcw5x9pnt9r42v992nqw65zze57s8tyk0jll78eyusqccn9gc
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.3433` (raw `-0.3433` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7758` | Readiness: `0.75`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims show relatively concrete governance controls, KPI alignment, prior operating history, milestone-administered disbursement, and an independently checkable repayment transaction, while the adjustment remains limited because several high-materiality track-record claims are still proposer-asserted and the detailed milestone and budget contents are only referenced rather than included in the anchor text.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a 20,000,000 ADA treasury request, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks the Cardano Treasury to fund the Cardano Builder DAO as a smart contract-governed, KPI-driven funding mechanism for builders. It says funded projects would track monthly active users, TVL, and on-chain transactions; that an independent council and multisig administrator would oversee funds and milestone validation; and that unused or unallocated DAO treasury funds would be returned to the Treasury. The proposal also states that 354,790 ADA was returned after earlier rounds and provides an AdaStat transaction link, which gives that repayment claim independent support.

Several important governance design claims were supported in the proposal itself, including the DAO funding model, KPI requirements, named administrator structure, separate auditable accounts, no stake pool delegation, and abstain voting delegation for administrator-held ADA. But other material claims remained proposer-asserted rather than independently verified, including the KPI dashboard’s progress toward live on-chain data and the claim that 11.1M ADA had already been distributed across 34 proposals. The review also found missing treasury and risk details, including a line-item budget, sustainability path, independent assurance, and dependency map.

This is a conservative, evidence-based hold, not a rejection of the idea. The proposal showed meaningful structure and some checkable evidence, but treasury withdrawals require a higher bar because they spend shared ADA and set precedent. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the material track-record claims and the missing budget, sustainability, assurance, and dependency details.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 20.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to continue and expand the Cardano Builder DAO as a smart contract-governed, KPI-driven funding mechanism for Cardano builders.
- finding: Recipient: Cardano Builder DAO
- finding: Stated amount: 20000000
- finding: Deliverables: Allocate capital to builders expected to improve monthly active users, monthly on-chain transactions, and TVL., Require funded projects to track core KPIs including monthly active users, TVL, and on-chain transactions., Continue development of KPI tracking toward live on-chain Cardano data., Use an independent council and multisig administrator to hold funds, validate milestones, and oversee disbursement., Return unused or unallocated DAO treasury funds to the Cardano Treasury.
- finding: Deadline/expiry: not stated in document
- finding: Claim (governance, supported_in_proposal, high materiality): The Cardano Builder DAO is proposed as an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Vision 2030 KPIs.
- finding: Claim (adoption, supported_in_proposal, high materiality): The proposal says funded projects will be required to track monthly active users, TVL, and on-chain transactions.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposer states that KPI dashboard Version 1 enabled public self-reported KPI tracking and Version 2 moved toward KPI tracking tied to live on-chain Cardano data.
- finding: Claim (economic, proposer_asserted, high materiality): The Cardano Builder DAO has already distributed 11.1M ADA across 34 proposals in two funding rounds.
- finding: Claim (governance, proposer_asserted, high materiality): Round 1 is described as funding 20 companies with 38 voting members, 27 requesting members, 83% governance participation, and 5,541,335 ADA distributed through a smart contract-governed process.
- finding: Claim (governance, proposer_asserted, medium materiality): Round 2 is described as adding 18 new members, funding 14 companies, and achieving 88% member participation after review, debate, temperature checks, and final voting.
- missing: Independent evidence for: The proposer states that KPI dashboard Version 1 enabled public self-reported KPI tracking and Version 2 moved toward KPI tracking tied to live on-chain Cardano data.
- missing: Independent evidence for: The Cardano Builder DAO has already distributed 11.1M ADA across 34 proposals in two funding rounds.
- missing: Independent evidence for: Round 1 is described as funding 20 companies with 38 voting members, 27 requesting members, 83% governance participation, and 5,541,335 ADA distributed through a smart contract-governed process.
- missing: Independent evidence for: Round 2 is described as adding 18 new members, funding 14 companies, and achieving 88% member participation after review, debate, temperature checks, and final voting.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 20000000
- finding: Budget granularity: unknown
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.48
- missing: line-item budget
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The Cardano Builder DAO is proposed as an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Vision 2030 KPIs." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that KPI dashboard Version 1 enabled public self-reported KPI tracking and Version 2 moved toward KPI tracking tied to live on-chain Cardano data." — so cost or precedent may outweigh the benefit.
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
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 20000000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The Cardano Builder DAO is proposed as an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Vision 2030 KPIs." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims show relatively concrete governance controls, KPI alignment, prior operating history, milestone-administered disbursement, and an independently checkable repayment transaction, while the adjustment remains limited because several high-materiality track-record claims are still proposer-asserted and the detailed milestone and budget contents are only referenced rather than included in the anchor text.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer states that KPI dashboard Version 1 enabled public self-reported KPI tracking and Version 2 moved toward KPI tracking tied to live on-chain Cardano data.
- Claims and evidence missing: Independent evidence for: The Cardano Builder DAO has already distributed 11.1M ADA across 34 proposals in two funding rounds.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `b22ea5de12b32ab50dc3a4850dfa63d02d6a0d278497e4d9507b3ab5bee09a5c`
- snapshot_bundle_hash: `76f752585187de6b11d219bc0ea317e1e9199981a8e7d889a518d8f6fd73bf6d`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4468, "NO": 0.5097, "YES": 0.0435}`

