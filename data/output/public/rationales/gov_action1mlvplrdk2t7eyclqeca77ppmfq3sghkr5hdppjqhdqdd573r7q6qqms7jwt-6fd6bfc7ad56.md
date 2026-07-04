# Rationale: gov_action1mlvplrdk2t7eyclqeca77ppmfq3sghkr5hdppjqhdqdd573r7q6qqms7jwt
Recommendation: **NO**
Score: `-0.4133` (raw `-0.3833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.52` | Readiness: `0.0`
> Reasoning layer (precomputed): The claims show plausible public-benefit ecosystem growth and some alignment with open infrastructure, but the deterministic assessment identifies thin evidence, incomplete treasury analysis, and missing feasibility and risk analysis for a large bridge-related treasury ask. Under BEACN doctrine, treasury stewardship and evidence quality outweigh speed or prospective growth, so a small cautionary negative adjustment is warranted.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large Treasury withdrawal request with too many unresolved evidence gaps, especially around budget detail, feasibility, risk, and the main Phase 1 delivery claim.

The proposal requested ₳12,332,031 for a 9-month Phase 1 effort to move Bifrost from working testnet toward launch readiness, including hardening, audits, formal verification, stewardship work, partner readiness, and economic foundations. The proposer claimed Bifrost would become an audited Bitcoin-Cardano bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access, while public rollout and 24 months of operations would be deferred to a Phase 2 proposal in Q1 2027.

Several claims were supported in the proposal itself: Bifrost is presented as a permissionless Bitcoin-Cardano bridge, the requested amount and timeline were stated, a federated fallback mode was described, and the proposal says there is no bridge token or founder allocation. The Catalyst Fund 14 history was also listed as independently verifiable at a medium level. But key claims remained unsupported by independent evidence, including the end-of-Phase-1 mainnet bridge outcome and the claim that testnet peg-ins, peg-outs, and participating SPOs are already working.

The review passed the basic anchor check because the pinned proposal document was available, but the Treasury, risk, and synthesis gates were not strong enough for a YES. Missing items included a complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, community impact analysis, line-item budget, milestone-gated disbursement, mitigation evidence, and independent assurance. For a Treasury action of this size, BEACN’s standard is conservative: public-benefit potential is not enough when the evidence package is thin and the use of shared ADA creates precedent.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 640
- finding: Expires after epoch: 647
- finding: Treasury request: 12.33M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Phase 1 of 2 funding to take Bifrost from working testnet to launch readiness, including hardening, security audits, formal verification, ecosystem and partner readiness, stewardship, and economic foundations for launch.
- finding: Recipient: FluidTokens and Lantr Engineering
- finding: Stated amount: 12332031
- finding: Deliverables: Audited bridge running on Cardano mainnet in both custody modes under controlled access, Hardening, security audits, and formal verification, Stewardship structure and hardened economic model, SPO/dApp partner pipeline required for public launch, Public rollout and 24 months of operations deferred to Phase 2 in Q1 2027
- finding: Deadline/expiry: 9-month delivery period from July 2026 to March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳12,332,031, approximately $1,973,125 at 0.16 USD/ADA, including a 10% refundable contingency, for a 9-month Phase 1 delivery period.
- finding: Claim (technical, proposer_asserted, high materiality): By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access.
- finding: Claim (adoption, proposer_asserted, high materiality): Bifrost is already live on testnet under Catalyst Fund 14 with working peg-ins and peg-outs and participating SPOs.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document states Catalyst Fund 14 funded Bifrost with ₳739,000 for architecture, testnet MVP, and documentation, with 585 votes and approved milestones for at least M1 and M2.
- finding: Claim (technical, proposer_asserted, high materiality): Bifrost custody is described as distributed across 400+ Cardano SPOs weighted by delegation, with fund movement requiring a cryptographic threshold representing the majority of delegated stake.
- missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access.
- missing: Independent evidence for: Bifrost is already live on testnet under Catalyst Fund 14 with working peg-ins and peg-outs and participating SPOs.
- missing: Independent evidence for: Bifrost custody is described as distributed across 400+ Cardano SPOs weighted by delegation, with fund movement requiring a cryptographic threshold representing the majority of delegated stake.
- missing: Independent evidence for: The document targets 1,200 BTC, about 600,000 annual transactions, 3,000 fBTC-holding wallets by Q2 2029, and fee surplus returning to the Cardano Treasury.
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
- finding: Requested ADA: 12.33M ADA
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
- finding: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 12.33M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims show plausible public-benefit ecosystem growth and some alignment with open infrastructure, but the deterministic assessment identifies thin evidence, incomplete treasury analysis, and missing feasibility and risk analysis for a large bridge-related treasury ask. Under BEACN doctrine, treasury stewardship and evidence quality outweigh speed or prospective growth, so a small cautionary negative adjustment is warranted.
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
- Claims and evidence missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access.
- Claims and evidence missing: Independent evidence for: Bifrost is already live on testnet under Catalyst Fund 14 with working peg-ins and peg-outs and participating SPOs.
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
- input_hash: `6fd6bfc7ad56036a0d3d4c315d19bd5eb4ef4cbd69f976738ff34449544508f1`
- snapshot_bundle_hash: `2bc46e26c4c400a5338dff721698f379a9471b5f55ad31c62df1e70a2e2ae7a7`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ab8e09e5364b5442ce388bbe8feecaf73d9bf04a`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `1217`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2146, "NO": 0.7433, "YES": 0.0421}`

