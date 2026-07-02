# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.9333` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal has meaningful governance and custody details plus checkable references, but the supplied assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal; under the doctrine, treasury stewardship and evidence quality justify a small cautious negative nudge beyond mechanical scoring.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw 3,810,423 ada for Mithril Protocol. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund continued Mithril Protocol development through Intersect on behalf of the vendor.. The recorded treasury amount is 3,810,423. The strongest grounded claim is: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.

A material weak point is that this claim remains proposer-asserted or thinly supported: The proposal states that full node synchronization is slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund continued Mithril Protocol development through Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with project-specific management described for Mithril.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect budget administration, audit, oversight, reporting obligations, and milestone-based disbursement controls
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that full node synchronization is slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal says Mithril strengthens cross-chain interoperability, lowers onboarding friction, and enables tooling for exchanges, wallets, monitoring, bridges, light wallets, full wallets, and light clients.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is 3,699,440 ADA for Mithril Protocol Continuous Development plus a 110,983 ADA Intersect Budget Administration fee, totaling 3,810,423 ADA.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain treasury withdrawal submission under the approved framework.
- finding: Claim (governance, independently_verifiable, high materiality): The requested amount does not, at submission, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713, either alone or in aggregate.
- missing: Independent evidence for: The proposal states that full node synchronization is slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- missing: Independent evidence for: The proposal says Mithril strengthens cross-chain interoperability, lowers onboarding friction, and enables tooling for exchanges, wallets, monitoring, bridges, light wallets, full wallets, and light clients.
- missing: Independent evidence for: Teragone has not previously received direct Cardano treasury or community governance funding, but has worked on Mithril for several years through IOG-funded collaboration.
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
- finding: Requested ADA: 3.81M ADA
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
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that full node synchronization is slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 3.81M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has meaningful governance and custody details plus checkable references, but the supplied assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal; under the doctrine, treasury stewardship and evidence quality justify a small cautious negative nudge beyond mechanical scoring.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow signal is in unsustainable regime (advisory penalty applied).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states that full node synchronization is slow and light clients rely on centralized trust, creating a pressing infrastructure challenge for Cardano.
- Claims and evidence missing: Independent evidence for: The proposal says Mithril strengthens cross-chain interoperability, lowers onboarding friction, and enables tooling for exchanges, wallets, monitoring, bridges, light wallets, full wallets, and light clients.
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
- input_hash: `1c7acf6ad96cebf7464c5e4e30c4912196f94b4f981bca00624796f38d7a4165`
- snapshot_bundle_hash: `b3ba9efa6f04704351e341feeed752164cf65aafd640dbb00fcbca3e0edb602d`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4fbc4829bb6142608e4d32087d1ed0565eaf5b12`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `800`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.164, "NO": 0.7957, "YES": 0.0403}`

