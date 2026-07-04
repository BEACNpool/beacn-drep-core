# Rationale: gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.52` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims show plausible public-benefit infrastructure and a materially reduced ask, but the deterministic assessment is blocked for missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis. Under BEACN's hierarchy, treasury stewardship and evidence quality outweigh ecosystem-growth upside when the ask is large and much of the adoption, governance, and execution record is proposer-asserted rather than fully evidenced in the supplied record.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury request was large and the review record did not clear BEACN’s evidence bar for spending shared ADA. The proposal showed plausible public benefit, but key diligence areas were incomplete or blocked, including budget analysis, feasibility, risk, alternatives, failure modes, and community impact.

The action requested ₳2,464,844 for a 9-month continuation of Scalus by Lantr Engineering, covering maintenance, Dijkstra hard-fork readiness, JVM/JS/TS interoperability, and a scoped application runtime by March 2027. The proposer claimed Scalus is an established Apache 2.0 open-source Cardano development platform with three years of delivery, a reduced scope compared with a prior ₳8.5M proposal, and measurable public activity including 4,642 commits, 32 releases, 12 contributors, and more than 20,000 monthly Scalus.js downloads. Those points were supported in the supplied record.

Other important adoption and governance claims were not independently evidenced in the supplied review. The record did not independently verify that Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit, or that projects such as Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus. The treasury analysis was also incomplete, with missing line-item budget and milestone-gated disbursement evidence, while the risk review was thin and lacked mitigation evidence and independent assurance.

BEACN recognized the strongest YES case: Scalus appears to be established open-source infrastructure with a materially reduced ask and a pinned, replayable anchor document. But treasury withdrawals require elevated scrutiny, the treasury flow signal was in an unsustainable regime, execution risk was unknown, and seven review blockers remained open. On the supplied evidence, stewardship of the treasury outweighed the upside case, so BEACN voted NO.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 640
- finding: Expires after epoch: 647
- finding: Treasury request: 2.46M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Funding for a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, JVM/JS/TS interoperability, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Maintenance of existing Scalus stack and supported export targets, Dijkstra hard-fork readiness across smart contracts, transaction building, emulation, and testing, Improved interoperability with existing Cardano tooling and the broader JVM ecosystem, A first scoped application runtime validated through reference applications, integration tests, and early-user feedback
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,464,844 over 9 months at a $0.16/ADA reference rate with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The current proposal reduces the previous Scalus proposal from ₳8.5M over 12 months to about ₳2.46M over 9 months and removes the L1 node, full L2 integration, and broad formal verification from scope.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (adoption, proposer_asserted, high materiality): Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- finding: Claim (adoption, independently_verifiable, medium materiality): Scalus has had 4,642 commits across 32 releases, 12 contributors, and Scalus.js reaches more than 20,000 downloads per month.
- missing: Independent evidence for: Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- missing: Independent evidence for: Dijkstra readiness is needed because Plutus V4, nested transactions, guard script types, and accounts affect smart contract development, Plutus evaluation, transaction building, ledger rules, testing, and developer workflows.
- missing: Independent evidence for: Delivery is milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
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
- finding: Requested ADA: 2.46M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 2.46M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims show plausible public-benefit infrastructure and a materially reduced ask, but the deterministic assessment is blocked for missing complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, and failure-mode analysis. Under BEACN's hierarchy, treasury stewardship and evidence quality outweigh ecosystem-growth upside when the ask is large and much of the adoption, governance, and execution record is proposer-asserted rather than fully evidenced in the supplied record.
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
- Claims and evidence missing: Independent evidence for: Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- Claims and evidence missing: Independent evidence for: Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
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
- input_hash: `b6b739f35e1d0f0f71cce7aa65df9df153ddff029fc698b332a34a72e05fec6b`
- snapshot_bundle_hash: `e6c2b6348af3d8aba576c66d6df318fbf17d40dc541c64d13afe7b35aba8d693`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `959`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2146, "NO": 0.7433, "YES": 0.0421}`

