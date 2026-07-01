# Rationale: gov_action19avrmrhm0gqa4qwlgvh4vxj6nwe02ay42h828cva2zt6n0asddfqqtgph5d
Recommendation: **NO**
Score: `-0.3933` (raw `-0.3833` + doctrine-LLM nudge `-0.01`) | Confidence: `0.8833` | Readiness: `0.0`
> Reasoning layer (codex-offline-review): Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), assessment blocked, 7 open blocker(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment -0.010 (clamped to ±0.05).

## Plain-language explanation (codex-offline-review)
BEACN records NO on [OriLife × TonFarm] Identifying 180 Million Durians Without Physical Labels. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: [OriLife × TonFarm] Identifying 180 Million Durians Without Physical Labels. The recorded treasury amount is 2.40M ADA. The strongest grounded claim is: OriLife Alliance proposes 2,400,000 ADA from the Cardano Treasury to deploy tamper-evident traceability across 12,000 hectares of durian in Đắk Lắk, Vietnam — before the December 1, 2026 deadline (Article 15, Circular 11/2026/TT-BCT).

The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: expired
- finding: Proposed epoch: 628
- finding: Expires after epoch: 635
- finding: Treasury request: 2.40M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: [OriLife × TonFarm] Identifying 180 Million Durians Without Physical Labels
- finding: Recipient: 
- finding: Stated amount: 2.40M ADA
- finding: Deliverables: OriLife Alliance proposes 2,400,000 ADA from the Cardano Treasury to deploy tamper-evident traceability across 12,000 hectares of durian in Đắk Lắk, Vietnam — before the December 1, 2026 deadline (Article 15, Circular 11/2026/TT-BCT)., The PoC works today: AI fruit identification is live at orilife.io/demo, VeData batching is verified on Cardano Preprod, and farmers across 46 communes have been onboarded over two harvest seasons (verifiable on TON)., The Alliance self-invested ~$500,000 USD before this GA., The Treasury funds production deployment.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, independently_verifiable, high materiality): OriLife Alliance proposes 2,400,000 ADA from the Cardano Treasury to deploy tamper-evident traceability across 12,000 hectares of durian in Đắk Lắk, Vietnam — before the December 1, 2026 deadline (Article 15, Circular 11/2026/TT-BCT).
- finding: Claim (economic, independently_verifiable, low materiality): The PoC works today: AI fruit identification is live at orilife.io/demo, VeData batching is verified on Cardano Preprod, and farmers across 46 communes have been onboarded over two harvest seasons (verifiable on TON).
- finding: Claim (economic, independently_verifiable, low materiality): The Alliance self-invested ~$500,000 USD before this GA.
- finding: Claim (economic, independently_verifiable, high materiality): The Treasury funds production deployment.
- finding: Claim (economic, independently_verifiable, low materiality): The Problem: A $3.36 Billion Supply Chain Built on Peelable Stickers Vietnam's durian exports to China totaled $3.36 billion USD in 2024 — over 90% of the country's durian export revenue, employing hundreds of thousands of farmers across the Central Highlan...
- finding: Claim (economic, independently_verifiable, low materiality): The entire traceability system underpinning this supply chain rests on physical QR labels — printed paper stickers attached to each fruit — that can be peeled off one fruit and stuck onto another in seconds, with no detection, no audit trail, and no recourse.
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
- finding: Requested ADA: 2.40M ADA
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
- finding: Strongest YES: the proposal substantiates "OriLife Alliance proposes 2,400,000 ADA from the Cardano Treasury to deploy tamper-evident traceability across 12,000 hectares of durian in Đắk Lắk, Vietnam — before the December 1, 2026 deadline (Article 15, Circular 11/2026/TT-BCT)." and clears the evidence gates.
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
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2.40M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "OriLife Alliance proposes 2,400,000 ADA from the Cardano Treasury to deploy tamper-evident traceability across 12,000 hectares of durian in Đắk Lắk, Vietnam — before the December 1, 2026 deadline (Article 15, Circular 11/2026/TT-BCT)." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.010 (clamped to ±0.05): Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), assessment blocked, 7 open blocker(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment -0.010 (clamped to ±0.05).
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

## Reproducibility
- input_hash: `9ab0a841c6c0dec675060cce00f899223b6009f92b14e5b9166c460b1f7cb9ac`
- snapshot_bundle_hash: `1e6fd6135092ac4e625133ac8333a41c5155bd59f0cebc70e673b6f47aa6126c`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `250`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1727, "NO": 0.7861, "YES": 0.0412}`

