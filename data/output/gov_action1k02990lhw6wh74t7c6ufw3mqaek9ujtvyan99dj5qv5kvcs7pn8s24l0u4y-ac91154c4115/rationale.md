# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NO**
Score: `-0.2833` (raw `-0.2533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7908` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show meaningful public-benefit infrastructure alignment and several independently verifiable governance and custody references, but the largest budget line lacks stated milestones, acceptance criteria, delivery dates, and detailed cost basis. Under a treasury-withdrawal review, that evidence gap warrants a small cautionary nudge rather than extra confidence in spending.

## Plain-language explanation (precomputed)
BEACN voted NO because the proposal asks for a large treasury withdrawal while the largest work package lacks specific milestones, acceptance criteria, delivery dates, and detailed cost basis.

The action requested 3,810,423 ada for Mithril Protocol continuous development, administered through Intersect and paid to the 2026 Treasury Reserve Smart Contract stake address. The proposal allocated 3,699,440 ada to Mithril development and 110,983 ada to an Intersect administration fee, and it described oversight, reporting obligations, milestone-based disbursement controls, and treasury management smart contracts.

Several parts of the proposal were well-supported. The anchor document was available and replayable. The proposal substantiated Mithril’s technical role in helping securely access and verify Cardano blockchain state using stake-based threshold multi-signatures. It also provided verifiable governance and custody references, including Intersect budget process support, Net Change Limit context, smart contract addresses, oversight structure, audits, repository links, and a public dashboard.

The NO vote came from the treasury review standard: spending shared ADA requires clearer evidence than broad public-benefit claims. The review found unsupported adoption claims around faster sync times reducing onboarding friction and enabling tools for exchanges, wallets, monitoring, bridges, light clients, and related uses. It also found missing treasury and risk evidence, including sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path. Given those gaps, the benefits were not enough to justify the requested withdrawal.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 3.81M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Withdraw treasury funds for Mithril Protocol continuous development with Intersect budget administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Audit and oversight through Intersect and technically capable third-party reporting obligations and milestone-based disbursement controls, Use of TRSC and PSSC treasury management smart contracts for fund administration
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify Cardano state trustlessly.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states that faster sync times enabled by Mithril lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states that Mithril enables community-built bridges, light wallets, full wallets, light clients, and monitoring tools around Cardano.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to the vote, documentation, audited results, and audit report.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal asserts that the requested amount does not, at time of submission, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713 and links to the NCL governance action.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget summary allocates 3,699,440 ada to Mithril Protocol Continuous Development and 110,983 ada to an Intersect Budget Administration fee, totaling 3,810,423 ada.
- missing: Independent evidence for: The proposal states that faster sync times enabled by Mithril lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- missing: Independent evidence for: The proposal states that Mithril enables community-built bridges, light wallets, full wallets, light clients, and monitoring tools around Cardano.
- missing: Independent evidence for: The proposal states that Teragone has not previously received direct Cardano treasury or community governance funding, while IOG has funded its Mithril work to date.
- missing: Independent evidence for: The proposal does not state specific development milestones, acceptance criteria, delivery dates, or a detailed cost basis for the 3,699,440 ada continuous development work package in the anchor text.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 3810423
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.52
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify Cardano state trustlessly." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that faster sync times enabled by Mithril lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring." — so cost or precedent may outweigh the benefit.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 3810423
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state by using stake-based threshold multi-signatures to certify Cardano state trustlessly." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims show meaningful public-benefit infrastructure alignment and several independently verifiable governance and custody references, but the largest budget line lacks stated milestones, acceptance criteria, delivery dates, and detailed cost basis. Under a treasury-withdrawal review, that evidence gap warrants a small cautionary nudge rather than extra confidence in spending.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal states that faster sync times enabled by Mithril lower onboarding friction and unlock tooling for exchanges, wallets, and monitoring.
- Claims and evidence missing: Independent evidence for: The proposal states that Mithril enables community-built bridges, light wallets, full wallets, light clients, and monitoring tools around Cardano.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `ac91154c41150700a6d9793c2917a9179e64e571738fdef42dfb544cb3af95bd`
- snapshot_bundle_hash: `fa7c17ed5d958998fdfbd25eef8287eecc11a3e59e377d310f7fa8e98782689d`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2025, "NO": 0.7517, "YES": 0.0458}`

