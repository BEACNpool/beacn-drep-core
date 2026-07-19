# Rationale: 17e43ffe4b2e0df1787d54f21ac66643c74abb131a326272fceecbdbbdd0d3fc#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (binding treasury composite; advisory raw signal `0.0`; LLM lean `+0.0` recorded, not added) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Tweag Core Cardano Infrastructure: Treasury Withdrawal 2026–2027. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Tweag Core Cardano Infrastructure: Treasury Withdrawal 2026–2027. It asks the treasury for 18.26M ADA. The strongest grounded claim is: This treasury withdrawal requests ₳18,263,496.00 (USD $4,565,874.00) to fund Tweag by Modus Create's delivery of 3 work packages across core infrastructure areas for the Cardano ecosystem over 2026–2027.

BEACN's own independent diligence is also incomplete — before this vote could move to YES, BEACN's published review still needs complete proposal summary; budget analysis; feasibility assessment. Reason code: DEEP_RESEARCH_REQUIRED.

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
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Tweag Core Cardano Infrastructure: Treasury Withdrawal 2026–2027
- finding: Recipient: 
- finding: Stated amount: 18.26M ADA
- finding: Deliverables: This treasury withdrawal requests ₳18,263,496.00 (USD $4,565,874.00) to fund Tweag by Modus Create's delivery of 3 work packages across core infrastructure areas for the Cardano ecosystem over 2026–2027., The primary focus is the mainnet deployment of Peras (faster finality: ~2 min vs., ~12 min today), alongside improvements to resilience, scalability, developer tooling, and network observability., Work packages include: - Peras v1 – production cryptography, KillSwitch, mainnet readiness and further support and maintenance - History Expiry – partial-history nodes to reduce SPO storage costs - Conformance Testing – CTC framework extended for Peras and...
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, independently_verifiable, high materiality): This treasury withdrawal requests ₳18,263,496.00 (USD $4,565,874.00) to fund Tweag by Modus Create's delivery of 3 work packages across core infrastructure areas for the Cardano ecosystem over 2026–2027.
- finding: Claim (economic, independently_verifiable, high materiality): The primary focus is the mainnet deployment of Peras (faster finality: ~2 min vs.
- finding: Claim (economic, independently_verifiable, low materiality): ~12 min today), alongside improvements to resilience, scalability, developer tooling, and network observability.
- finding: Claim (technical, independently_verifiable, low materiality): Work packages include: - Peras v1 – production cryptography, KillSwitch, mainnet readiness and further support and maintenance - History Expiry – partial-history nodes to reduce SPO storage costs - Conformance Testing – CTC framework extended for Peras and...
- finding: Claim (technical, independently_verifiable, high materiality): Problem Statement Cardano's next growth phase depends on two critical protocol upgrades: Peras (faster finality) and Leios (higher throughput).
- finding: Claim (economic, independently_verifiable, low materiality): Together they unlock significantly higher transaction volume, staking rewards, and TVL.
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
- finding: Requested ADA: 18.26M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "This treasury withdrawal requests ₳18,263,496.00 (USD $4,565,874.00) to fund Tweag by Modus Create's delivery of 3 work packages across core infrastructure areas for the Cardano ecosystem over 2026–2027." though 7 review blocker(s) remain open.
- finding: Strongest NO: an unresolved blocker (missing complete proposal summary) means costs or weak controls may outweigh the claimed benefit.
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
- Treasury analysis: Requested ADA: 18.26M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This treasury withdrawal requests ₳18,263,496.00 (USD $4,565,874.00) to fund Tweag by Modus Create's delivery of 3 work packages across core infrastructure areas for the Cardano ecosystem over 2026–2027." though 7 review blocker(s) remain open.
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
- Claims and evidence missing: complete proposal summary
- Claims and evidence missing: budget analysis
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
- input_hash: `a6bc756d1a84385d0474586baa774a5308d4ad751096de43bfc98fe978d4c383`
- snapshot_bundle_hash: `af8255665b4e75048bdd3b45508d9e524029c7213eac68063b2edc1944b91ea8`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `646629824e42aafea23488c5eeef5362c697d560`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

