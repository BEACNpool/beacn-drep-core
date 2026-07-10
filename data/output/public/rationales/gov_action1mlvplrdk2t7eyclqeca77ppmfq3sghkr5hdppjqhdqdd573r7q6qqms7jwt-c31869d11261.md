# Rationale: gov_action1mlvplrdk2t7eyclqeca77ppmfq3sghkr5hdppjqhdqdd573r7q6qqms7jwt
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7808` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal describes a potentially public-benefit interoperability project, but the high treasury ask depends on security, adoption, revenue, and SPO-threshold custody claims that are largely asserted in the anchor text while the deterministic assessment already marks claims and evidence as thin. A small negative nudge is justified because treasury stewardship and evidence quality should dominate plausible ecosystem growth when the main benefits and downside controls are not yet strongly evidenced in the supplied claims.

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Bifrost: Unlocking Bitcoin DeFi on Cardano — Road to Mainnet (Phase 1 of 2). This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Phase 1 of 2 funding to take Bifrost from a working testnet to launch readiness, including hardening, security audits, formal verification, ecosystem and partner readiness, and stewardship and economic foundations for launch. It asks the treasury for 12332031 ADA. The strongest grounded claim is: Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset.

A material claim remains proposer-asserted or thinly supported: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO-threshold custody modes under controlled access. Reason code: VERIFIED_NCL_REQUIRED.

## Review Tree
- overall_status: `incomplete`

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
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Phase 1 of 2 funding to take Bifrost from a working testnet to launch readiness, including hardening, security audits, formal verification, ecosystem and partner readiness, and stewardship and economic foundations for launch.
- finding: Recipient: FluidTokens and Lantr Engineering
- finding: Stated amount: 12332031
- finding: Deliverables: Audited bridge running on Cardano mainnet in both custody modes under controlled access, Security audits, Formal verification, Ecosystem and partner readiness, Stewardship structure, Hardened economic model, SPO/dApp partner pipeline required for public launch
- finding: Deadline/expiry: 9-month delivery period from July 2026 to March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳12,332,031, approximately $1,973,125 at 0.16 USD/ADA, including a 10% refundable contingency, for a 9-month delivery period.
- finding: Claim (technical, proposer_asserted, high materiality): By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO-threshold custody modes under controlled access.
- finding: Claim (governance, proposer_asserted, high materiality): Public rollout and 24 months of operations are intentionally deferred to a Phase 2 proposal in Q1 2027 after the bridge has been proven on-chain.
- finding: Claim (technical, independently_verifiable, high materiality): The bridge is already live on testnet under Catalyst Fund 14 with working peg-ins and peg-outs and participating SPOs.
- finding: Claim (adoption, supported_in_proposal, medium materiality): Catalyst Fund 14 funded Bifrost with ₳739,000 for architecture, testnet MVP, and documentation, and the proposal states the timeline from December 2025 to August 2026 is on track.
- missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO-threshold custody modes under controlled access.
- missing: Independent evidence for: Public rollout and 24 months of operations are intentionally deferred to a Phase 2 proposal in Q1 2027 after the bridge has been proven on-chain.
- missing: Independent evidence for: Bifrost custody of locked BTC is described as distributed across 400+ Cardano SPOs weighted by delegation, with fund movement requiring a cryptographic threshold representing the majority of delegated stake.
- missing: Independent evidence for: Bifrost will have no bridge token or founder allocation, and its smart contracts, off-chain tooling, and SDK are released under Apache 2.0.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 12332031
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.78
- missing: milestone-gated disbursement
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: high
- finding: Governance risk: medium
- finding: Technical risk: high
- finding: Treasury exposure risk: high
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
- finding: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO-threshold custody modes under controlled access." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 12332031
- Risk review: Execution risk: high
- Counterargument pass: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal describes a potentially public-benefit interoperability project, but the high treasury ask depends on security, adoption, revenue, and SPO-threshold custody claims that are largely asserted in the anchor text while the deterministic assessment already marks claims and evidence as thin. A small negative nudge is justified because treasury stewardship and evidence quality should dominate plausible ecosystem growth when the main benefits and downside controls are not yet strongly evidenced in the supplied claims.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO-threshold custody modes under controlled access.
- Claims and evidence missing: Independent evidence for: Public rollout and 24 months of operations are intentionally deferred to a Phase 2 proposal in Q1 2027 after the bridge has been proven on-chain.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- delivery controls, milestones, assurance, or remedy path

## Reproducibility
- input_hash: `c31869d1126149cb19b18718209277982ba9989fbc89f038a7523d22c858de31`
- snapshot_bundle_hash: `50c06cd6edab3853b2b839155468bd95cf394a237b3de1289b98cf11b474d8df`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

