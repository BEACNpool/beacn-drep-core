# Rationale: gov_action1zljrlljt9cxlz7ra2nep43nxg0r54wcnrgexyuhuam9ah0ws607qq2vcg4x
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Tweag Core Cardano Infrastructure: Treasury Withdrawal 2026–2027. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Tweag by Modus Create's delivery of three Cardano core infrastructure work packages over 2026-2027. It asks the treasury for 18263496.00 ADA. The strongest grounded claim is: The proposal requests ₳18,263,496.00, stated as USD $4,565,874.00, for three Cardano core infrastructure work packages over 2026-2027.

A material claim remains proposer-asserted or thinly supported: Peras v1 is described as enabling faster finality of approximately 2 minutes compared with approximately 12 minutes today. BEACN's own independent diligence is also incomplete — before this vote could move to YES, BEACN's published review still needs budget analysis; feasibility assessment; alternatives analysis. Reason code: DEEP_RESEARCH_REQUIRED.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 634
- finding: Expires after epoch: 641
- finding: Treasury request: 18.26M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Tweag by Modus Create's delivery of three Cardano core infrastructure work packages over 2026-2027.
- finding: Recipient: Tweag by Modus Create, administered through Intersect and Cardano Development Holdings contract structures
- finding: Stated amount: 18263496.00
- finding: Deliverables: Peras v1 production cryptography, KillSwitch, mainnet readiness, support, and maintenance, History Expiry partial-history nodes to reduce SPO storage costs, Conformance Testing CTC framework extended for Peras and Leios
- finding: Deadline/expiry: 2026-2027 delivery period; specific milestone dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳18,263,496.00, stated as USD $4,565,874.00, for three Cardano core infrastructure work packages over 2026-2027.
- finding: Claim (technical, proposer_asserted, high materiality): Peras v1 is described as enabling faster finality of approximately 2 minutes compared with approximately 12 minutes today.
- finding: Claim (technical, supported_in_proposal, high materiality): History Expiry is intended to enable partial-history nodes and reduce SPO storage costs as throughput increases.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal asserts that Leios throughput could cause SPO disk usage to surge to approximately 1 GB per hour at 100-1000 TPS without History Expiry.
- finding: Claim (adoption, proposer_asserted, medium materiality): Tweag states it has been engaged on Cardano core infrastructure since January 2018, including consensus and ledger leadership, Ouroboros Genesis implementation, and Peras design contributions.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is based on an average market rate of $176 per hour for senior Cardano infrastructure engineers and an ADA/USD conversion rate of 0.25 based on a five-year average.
- missing: Independent evidence for: Peras v1 is described as enabling faster finality of approximately 2 minutes compared with approximately 12 minutes today.
- missing: Independent evidence for: The proposal asserts that Leios throughput could cause SPO disk usage to surge to approximately 1 GB per hour at 100-1000 TPS without History Expiry.
- missing: Independent evidence for: Tweag states it has been engaged on Cardano core infrastructure since January 2018, including consensus and ledger leadership, Ouroboros Genesis implementation, and Peras design contributions.
- missing: budget analysis
- missing: feasibility assessment
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 18263496
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.40
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: low
- finding: Technical risk: high
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: unknown
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: not confirmed
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests ₳18,263,496.00, stated as USD $4,565,874.00, for three Cardano core infrastructure work packages over 2026-2027." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Peras v1 is described as enabling faster finality of approximately 2 minutes compared with approximately 12 minutes today." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 18263496
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests ₳18,263,496.00, stated as USD $4,565,874.00, for three Cardano core infrastructure work packages over 2026-2027." though 5 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: Peras v1 is described as enabling faster finality of approximately 2 minutes compared with approximately 12 minutes today.
- Claims and evidence missing: Independent evidence for: The proposal asserts that Leios throughput could cause SPO disk usage to surge to approximately 1 GB per hour at 100-1000 TPS without History Expiry.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
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
- input_hash: `ca61cc65c321448febaa581848968f6f837c086b0d44380f22d8129abd91ac8d`
- snapshot_bundle_hash: `8bf592edede1ae3d6cb1b41cb3b9d7d6836397e20c4ffe52c6c1b02778f630de`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `5`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

