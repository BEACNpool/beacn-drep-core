# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims show plausible public-benefit infrastructure value and several externally checkable governance and smart-contract references, but the deterministic assessment already flags missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN doctrine, treasury stewardship and evidence quality justify only a small cautionary negative nudge beyond the mechanical gates.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal request and the review found too many core gaps in the evidence needed to justify spending shared ada.

The action requested 3,810,423 ada for Mithril Protocol, with 3,699,440 ada described for continuous development and 110,983 ada for Intersect budget administration. The proposal said Intersect submitted the withdrawal on behalf of the vendor, with Teragone identified as the project vendor. It claimed Mithril would improve secure, fast access to Cardano state and support tooling for wallets, exchanges, light clients, bridges, monitoring, and other applications.

Some parts were well-supported or independently checkable: the requested amount and fee split were stated clearly, the proposal anchor was pinned and replayable, the Intersect budget-process support threshold was cited, the Net Change Limit claim was stated, and treasury smart contract addresses and authorization rules were identified. But important technical and public-benefit claims remained only proposer-asserted or lacked independent evidence in the review, including the claim that Mithril certifies Cardano state through stake-based threshold multi-signatures and the claim that it solves a pressing infrastructure problem around full-node sync and light-client trust.

The decisive issue was not that Mithril lacked potential value. The review recognized a plausible public-infrastructure benefit. The NO came from failed or incomplete gates for a treasury action: missing complete proposal summary, missing budget analysis, missing feasibility assessment, missing risk analysis, missing alternatives analysis, missing failure-mode analysis, and missing community impact analysis. Treasury analysis also lacked a line-item budget and milestone-gated disbursement evidence, while risk review lacked mitigation evidence and independent assurance. For a 3.81M ada withdrawal, BEACN’s standard required stronger evidence than was available.

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
- finding: Requested: Withdraw treasury funds for Mithril Protocol continuous development and Intersect budget administration.
- finding: Recipient: The on-chain withdrawal reward address is stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v; Intersect submitted the withdrawal on behalf of the vendor, and Teragone is identified as the project vendor in the rationale.
- finding: Stated amount: 3810423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for an Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril is described as using stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that full node synchronization is slow and light clients rely on centralized trust, making secure access to blockchain state a pressing infrastructure challenge for Cardano.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal claims Mithril can lower onboarding friction and unlock tooling for exchanges, wallets, monitoring, bridges, full wallets, light clients, and other community-built tools.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states the requested withdrawal does not, at submission, breach the applicable 350M ada Net Change Limit covering Epoch 613 to Epoch 713, either alone or in aggregate.
- missing: Independent evidence for: Mithril is described as using stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- missing: Independent evidence for: The proposal states that full node synchronization is slow and light clients rely on centralized trust, making secure access to blockchain state a pressing infrastructure challenge for Cardano.
- missing: Independent evidence for: The proposal claims Mithril can lower onboarding friction and unlock tooling for exchanges, wallets, monitoring, bridges, full wallets, light clients, and other community-built tools.
- missing: Independent evidence for: The proposal states that audit and oversight costs are included in the overhead and administration fee, with independent oversight through Intersect and technically capable third parties plus reporting obligations and milestone-based disbursement controls.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for an Intersect Budget Administration fee." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Mithril is described as using stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for an Intersect Budget Administration fee." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims show plausible public-benefit infrastructure value and several externally checkable governance and smart-contract references, but the deterministic assessment already flags missing budget, feasibility, risk, alternatives, and failure-mode analysis for a large treasury withdrawal. Under BEACN doctrine, treasury stewardship and evidence quality justify only a small cautionary negative nudge beyond the mechanical gates.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Mithril is described as using stake-based threshold multi-signatures to certify Cardano state in a trustless way so nodes and applications can verify state rapidly without relying on the entire chain.
- Claims and evidence missing: Independent evidence for: The proposal states that full node synchronization is slow and light clients rely on centralized trust, making secure access to blockchain state a pressing infrastructure challenge for Cardano.
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
- input_hash: `c024ee05154028885784c6792bcbfb4f789a2df51951b7ff88ff3f63233e97b5`
- snapshot_bundle_hash: `43632f26aff520efa505cf36b5bf33cf495a8f317ac27d8a3935f17245205bb5`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1218`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

