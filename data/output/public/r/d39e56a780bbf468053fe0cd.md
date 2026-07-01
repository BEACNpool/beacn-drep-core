# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sj72rg72
Recommendation: **NO**
Score: `-0.3133` (raw `-0.2833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.8333` | Readiness: `0.0`
> Reasoning layer (precomputed): The document presents plausible public-benefit infrastructure and some checkable governance and registry references, but the deterministic assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN's hierarchy, that evidence gap warrants a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw 1,684,050 ada for Tx3 by TxPipe: Open API Layer for Cardano's dApp P.... The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Tx3 by TxPipe, described as an open API layer for Cardano dApp protocols.. The recorded treasury amount is 1,684,050. The strongest grounded claim is: The proposal requests 1,684,050 ADA total, consisting of 1,635,000 ADA for the Open API Layer for Cardano Protocols and a 49,050 ADA Intersect Budget Administration fee.

A material weak point is that this claim remains proposer-asserted or thinly supported: Tx3 is intended to let developers and AI agents discover, integrate, and compose Cardano protocols through a single consistent interface surface. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.68M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Tx3 by TxPipe, described as an open API layer for Cardano dApp protocols.
- finding: Recipient: Intersect 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 1,684,050
- finding: Deliverables: Open, standardized interface across Cardano on-chain protocols, 12 additional protocol onboardings over 12 months, Developer and agent coverage for onboarded protocols, MCP server, Protocol skills framework, Agent-first documentation, Auto-generated SDKs in multiple languages, Live JSON-RPC endpoints
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,684,050 ADA total, consisting of 1,635,000 ADA for the Open API Layer for Cardano Protocols and a 49,050 ADA Intersect Budget Administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The underlying vendor work is described as 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months.
- finding: Claim (technical, proposer_asserted, high materiality): Tx3 is intended to let developers and AI agents discover, integrate, and compose Cardano protocols through a single consistent interface surface.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that Tx3 produces documentation, auto-generated multi-language SDKs, and live JSON-RPC endpoints from verified protocol interface definitions.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states that Catalyst Fund 14 has already put the Tx3 developer layer into production with 5 protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal funds 12 additional protocol onboardings, at 3 per quarter, with full developer and agent coverage.
- missing: Independent evidence for: Tx3 is intended to let developers and AI agents discover, integrate, and compose Cardano protocols through a single consistent interface surface.
- missing: Independent evidence for: The proposal states that Tx3 produces documentation, auto-generated multi-language SDKs, and live JSON-RPC endpoints from verified protocol interface definitions.
- missing: Independent evidence for: The proposal claims there is currently no common interface mechanism across the Cardano ecosystem, forcing integrators to relearn each protocol from scratch.
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
- finding: Requested ADA: 1.68M ADA
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
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,684,050 ADA total, consisting of 1,635,000 ADA for the Open API Layer for Cardano Protocols and a 49,050 ADA Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Tx3 is intended to let developers and AI agents discover, integrate, and compose Cardano protocols through a single consistent interface surface." — so cost or precedent may outweigh the benefit.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1.68M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,684,050 ADA total, consisting of 1,635,000 ADA for the Open API Layer for Cardano Protocols and a 49,050 ADA Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The document presents plausible public-benefit infrastructure and some checkable governance and registry references, but the deterministic assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN's hierarchy, that evidence gap warrants a small cautionary nudge rather than a positive adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~19 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Tx3 is intended to let developers and AI agents discover, integrate, and compose Cardano protocols through a single consistent interface surface.
- Claims and evidence missing: Independent evidence for: The proposal states that Tx3 produces documentation, auto-generated multi-language SDKs, and live JSON-RPC endpoints from verified protocol interface definitions.
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
- input_hash: `4c99ed1d295265c36b7a47868fa29d2425f336fca2c3017795481458710bd675`
- snapshot_bundle_hash: `6f62ec2e7665e0fbee8e8095183f20fb8f1b53468084215d537d79b31fa697c3`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `715`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1914, "NO": 0.7642, "YES": 0.0443}`

