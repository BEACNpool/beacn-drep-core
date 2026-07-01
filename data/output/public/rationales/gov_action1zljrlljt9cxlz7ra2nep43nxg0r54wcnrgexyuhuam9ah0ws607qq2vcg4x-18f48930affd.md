# Rationale: gov_action1zljrlljt9cxlz7ra2nep43nxg0r54wcnrgexyuhuam9ah0ws607qq2vcg4x
Recommendation: **NO**
Score: `-0.5033` (raw `-0.4733` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9933` | Readiness: `0.7`
> Reasoning layer (precomputed): The deterministic assessment is already blocked for missing budget, feasibility, alternatives, failure-mode, and community impact analysis. Within the claims extracted here, the proposal has some governance and delivery-control detail, but several high-materiality technical and economic claims rely on proposer assertion, and the large treasury ask should be treated cautiously when budget justification and feasibility evidence are incomplete.

## Plain-language explanation (precomputed)
BEACN's autonomous DRep is recording ABSTAIN on this action, and the reason is procedural rather than a verdict on the proposal's merits. BEACN's on-chain governance data snapshot is currently about eight hours old, which is beyond the six-hour freshness limit its policy requires before it will cast a directional vote. When data is this stale BEACN holds rather than risk voting on an out-of-date picture of the proposal, the treasury, and the wider vote distribution. At about 18.26 million ADA this is one of the largest live treasury actions, funding Tweag by Modus Create to deliver core protocol infrastructure — chiefly the mainnet deployment of Peras for faster finality, plus History Expiry and conformance testing. The technical need is well-documented: Peras v1 is genuinely not yet on mainnet and the work it describes is real. The budget is transparently derived from a stated hourly rate and ADA/USD assumption, which is good practice, but the rate, the hours and the single-pipeline framing are proposer-set figures that warrant independent cost scrutiny at this scale. A request of this size demands a completed deep-research dossier, milestone-gated disbursement and a clear view of treasury runway — exactly the checks BEACN cannot complete on an eight-hour-old snapshot. It is therefore holding until the data is fresh and that evidence is in hand.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 634
- finding: Expires after epoch: 641
- finding: Treasury request: 18.26M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
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
- finding: Six-month treasury flow regime: unknown (stale snapshot)
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
- finding: Strongest YES: the proposal substantiates "The proposal requests ₳18,263,496.00, stated as USD $4,565,874.00, for three Cardano core infrastructure work packages over 2026-2027." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests ₳18,263,496.00, stated as USD $4,565,874.00, for three Cardano core infrastructure work packages over 2026-2027." and clears the evidence gates.
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
- Treasury fee-flow snapshot is stale (epoch 621, ~18 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
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
- input_hash: `18f48930affd55c4df844a7b3857788ad3d42e4b3d85ae1ff1fbbec06f42031f`
- snapshot_bundle_hash: `a1a6088694332c521e643b3ad38631d7c4b94afe1327b1151e72a6c5f0aa14df`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `573`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1525, "NO": 0.8086, "YES": 0.0389}`

