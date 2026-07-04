# Rationale: gov_action1fdatlfcdnzzcw5x9pnt9r42v992nqw65zze57s8tyk0jll78eyusqccn9gc
Recommendation: **NO**
Score: `-0.5133` (raw `-0.4833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.64` | Readiness: `0.75`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit ecosystem growth and includes some governance controls such as milestone validation, independent multisig administration, and a repayment commitment, but several high-materiality track-record and KPI claims are asserted rather than evidenced in the anchor text, and the deterministic assessment marks treasury analysis as incomplete. Under BEACN doctrine, that evidence gap warrants a small cautionary nudge against spending rather than a positive lean.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal request for 20,000,000 ADA, and the evidence package did not meet the higher bar required for spending shared treasury funds.

The proposal asked for funding to continue and expand the Cardano Builder DAO as a smart contract-governed, KPI-driven funding mechanism for Cardano builders. It said funded projects would track monthly active users, TVL, and on-chain transactions, and that funds would be disbursed through milestones overseen by an independent dRep DAO council and multisig administrator. Those governance and KPI-tracking commitments were supported in the proposal, and the pinned anchor document was available for review.

The weaker part was the evidence behind several material claims. The proposer asserted that the DAO is an ecosystem-wide mechanism advancing Cardano Vision 2030 KPIs, that it had already distributed 11.1 million ADA across 34 proposals, and that prior impact was measured through public KPI dashboards. The review found the claims-and-evidence status thin, with independent evidence missing for key track-record and ecosystem-impact claims. The proposer also stated that 354,790 ADA had been returned to the treasury and provided an AdaStat transaction URL, which was treated as independently verifiable at medium strength.

The main review gates did not all clear. The anchor and basic intake gates were sufficient, and the counterargument review found a credible YES case around KPI tracking. But treasury analysis was incomplete, with no line-item budget or sustainability path, and the risk review was missing independent assurance and a dependency map. Because treasury actions require elevated scrutiny, and because this request came with incomplete treasury diligence, unknown execution risk, and an unsustainable treasury flow signal, BEACN concluded that the cost and precedent risk outweighed the supported benefits.

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
- finding: Deep research dossier: required
- finding: Requested: Cardano Builder DAO requests treasury funding to continue and expand a smart contract-governed, KPI-driven funding mechanism for Cardano builders.
- finding: Recipient: Cardano Builder DAO
- finding: Stated amount: 20000000
- finding: Deliverables: Allocate capital to builders expected to advance Cardano KPI outcomes including monthly active users, monthly on-chain transactions, and TVL., Require funded projects to track core KPIs including monthly active users, TVL, and on-chain transactions., Use a DAO process for proposal evaluation, feedback coordination, transparent fund distribution, and results tracking., Disburse funds through milestones overseen by an independent dRep DAO council and multisig administrator.
- finding: Deadline/expiry: not stated in document
- finding: Claim (adoption, proposer_asserted, high materiality): The Cardano Builder DAO is proposed as an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal says funded projects will be required to track monthly active users, TVL, and on-chain transactions.
- finding: Claim (economic, proposer_asserted, high materiality): The proposer states the DAO has already distributed 11.1 million ADA across 34 proposals in two funding rounds.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer states Round 1 funded 20 companies, involved 38 voting members and 27 requesting members, distributed 5,541,335 ADA, and achieved 83% governance participation.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer states Round 2 funded 14 companies, added 18 new members, and achieved 88% member participation.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal says prior DAO impact was measured through public KPI dashboards, including a move from self-reported tracking toward live on-chain Cardano data.
- missing: Independent evidence for: The Cardano Builder DAO is proposed as an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs.
- missing: Independent evidence for: The proposer states the DAO has already distributed 11.1 million ADA across 34 proposals in two funding rounds.
- missing: Independent evidence for: The proposer states Round 1 funded 20 companies, involved 38 voting members and 27 requesting members, distributed 5,541,335 ADA, and achieved 83% governance participation.
- missing: Independent evidence for: The proposer states Round 2 funded 14 companies, added 18 new members, and achieved 88% member participation.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 20000000
- finding: Budget granularity: unknown
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "The proposal says funded projects will be required to track monthly active users, TVL, and on-chain transactions." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The Cardano Builder DAO is proposed as an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal says funded projects will be required to track monthly active users, TVL, and on-chain transactions." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal is aligned with public-benefit ecosystem growth and includes some governance controls such as milestone validation, independent multisig administration, and a repayment commitment, but several high-materiality track-record and KPI claims are asserted rather than evidenced in the anchor text, and the deterministic assessment marks treasury analysis as incomplete. Under BEACN doctrine, that evidence gap warrants a small cautionary nudge against spending rather than a positive lean.
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
- Claims and evidence missing: Independent evidence for: The Cardano Builder DAO is proposed as an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs.
- Claims and evidence missing: Independent evidence for: The proposer states the DAO has already distributed 11.1 million ADA across 34 proposals in two funding rounds.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `97c582c07a4c19ac99e32dbcab7334e4eb9e8e6ad39f653eaff0d9160e771384`
- snapshot_bundle_hash: `5a49880e9158794890f6fbca2d87642ad7631f13df0f28c656e9f8d912b17166`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `31`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

