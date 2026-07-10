# Rationale: gov_action1mlvplrdk2t7eyclqeca77ppmfq3sghkr5hdppjqhdqdd573r7q6qqms7jwt
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7808` | Readiness: `0.8`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit growth and some checkable Catalyst/testnet context, but the request is large, the assessment says claims and evidence are thin, and several high-materiality claims about mainnet readiness, security fallback, revenue return, adoption targets, and open-source status are asserted rather than evidenced in the supplied document. A small negative nudge is warranted for treasury stewardship and evidence quality without overriding the deterministic assessment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for ₳12,332,031 for Phase 1 of Bifrost, a 9-month effort from July 2026 to March 2027 to move a Bitcoin-Cardano bridge from testnet toward launch readiness. The requested work includes hardening, audits, formal verification, partner readiness, stewardship planning, an economic model, and a mainnet bridge under controlled access. The proposer says Bifrost would bring BTC to Cardano as native fBTC, use Cardano SPOs for threshold custody, and defer public rollout plus 24 months of operations to a Phase 2 proposal in Q1 2027.

Several core claims were supported well enough for review: the anchor document was pinned and replayable, the basic design and funding request were stated clearly, the SPO-threshold custody model was described, and Catalyst Fund 14 context was independently verifiable. But several high-materiality claims remained asserted rather than independently evidenced, including the claim that Phase 1 will end with an audited mainnet bridge in both federated and SPO threshold custody modes, and the claim that federated mode can safely serve as the fallback if SPO coordination fails.

This is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would be unblocked by pinned, independently verifiable Net Change Limit evidence, stronger independent assurance for the mainnet bridge and fallback design, clearer milestone-gated disbursement, and a defined rollback or remedy path if execution or security assumptions fail.

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
- finding: Requested: Phase 1 of 2 funding to take Bifrost from working testnet to launch readiness, including hardening, security audits, formal verification, ecosystem and partner readiness, stewardship, and economic foundations for launch.
- finding: Recipient: FluidTokens and Lantr Engineering
- finding: Stated amount: 12332031
- finding: Deliverables: Audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access, Hardening, security audits, and formal verification, Ecosystem and partner readiness, Stewardship structure determined for launch, Hardened economic model and SPO/dApp partner pipeline, Public rollout and 24 months of operations deferred to Phase 2 in Q1 2027
- finding: Deadline/expiry: 9-month delivery period from July 2026 to March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as native fBTC.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳12,332,031, approximately $1,973,125 at 0.16 USD/ADA, including a 10% refundable contingency, for a 9-month Phase 1 delivery period.
- finding: Claim (technical, proposer_asserted, high materiality): By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access.
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost custody of locked BTC is proposed to be distributed across 400+ Cardano SPOs weighted by delegation, with movement of funds requiring a threshold representing the majority of delegated stake.
- finding: Claim (technical, proposer_asserted, high materiality): If SPO coordination fails, Bifrost will use a federated mode as an operational fallback.
- finding: Claim (technical, proposer_asserted, medium materiality): Bifrost smart contracts, off-chain tooling, and SDK are released under Apache 2.0 and can be audited, forked, run, or built on without permission.
- missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access.
- missing: Independent evidence for: If SPO coordination fails, Bifrost will use a federated mode as an operational fallback.
- missing: Independent evidence for: Bifrost smart contracts, off-chain tooling, and SDK are released under Apache 2.0 and can be audited, forked, run, or built on without permission.
- missing: Independent evidence for: The proposer targets 1,200 BTC TVL, about 600,000 annual transactions, and 3,000 fBTC-holding wallets by Q2 2029 as Bifrost contributions to Cardano 2030 KPIs.
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
- finding: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as native fBTC." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as native fBTC." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show plausible public-benefit growth and some checkable Catalyst/testnet context, but the request is large, the assessment says claims and evidence are thin, and several high-materiality claims about mainnet readiness, security fallback, revenue return, adoption targets, and open-source status are asserted rather than evidenced in the supplied document. A small negative nudge is warranted for treasury stewardship and evidence quality without overriding the deterministic assessment.
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
- Claims and evidence missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access.
- Claims and evidence missing: Independent evidence for: If SPO coordination fails, Bifrost will use a federated mode as an operational fallback.
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
- snapshot_bundle_hash: `22dabba0c90314047251ca9e9bc923c05e2d4f4c52c291626d765a73469fcfe2`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

