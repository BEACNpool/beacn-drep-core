# Rationale: gov_action1zljrlljt9cxlz7ra2nep43nxg0r54wcnrgexyuhuam9ah0ws607qq2vcg4x
Recommendation: **NO**
Score: `-0.6033` (raw `-0.5733` + doctrine-LLM nudge `-0.03`) | Confidence: `0.64` | Readiness: `0.7`
> Reasoning layer (precomputed): The deterministic assessment is already blocked for missing budget, feasibility, alternatives, failure-mode, and community impact analysis. Within the claims extracted here, the proposal has some governance and delivery-control detail, but several high-materiality technical and economic claims rely on proposer assertion, and the large treasury ask should be treated cautiously when budget justification and feasibility evidence are incomplete.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Tweag Core Cardano Infrastructure: Treasury Withdrawal 2026–2027. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Tweag by Modus Create's delivery of three Cardano core infrastructure work packages over 2026-2027. It asks the treasury for 18263496.00 ADA. The strongest grounded claim is: The proposal requests ₳18,263,496.00, stated as USD $4,565,874.00, for three Cardano core infrastructure work packages over 2026-2027.

A material claim remains proposer-asserted or thinly supported: Peras v1 is described as enabling faster finality of approximately 2 minutes compared with approximately 12 minutes today. BEACN's own independent diligence is also incomplete — before this vote could move to YES, BEACN's published review still needs budget analysis; feasibility assessment; alternatives analysis.

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
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 18263496
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests ₳18,263,496.00, stated as USD $4,565,874.00, for three Cardano core infrastructure work packages over 2026-2027." though 5 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The deterministic assessment is already blocked for missing budget, feasibility, alternatives, failure-mode, and community impact analysis. Within the claims extracted here, the proposal has some governance and delivery-control detail, but several high-materiality technical and economic claims rely on proposer assertion, and the large treasury ask should be treated cautiously when budget justification and feasibility evidence are incomplete.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- No milestone-gated disbursement documented.
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

## Reproducibility
- input_hash: `8bcecb2e52e10624469dc352b109dd1c4f260ccc41e6b00fad26302be5f233d1`
- snapshot_bundle_hash: `35fc58a90b16ddb9267628f9f25397a520629ee1476d2924ae4fcededbdf9032`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

