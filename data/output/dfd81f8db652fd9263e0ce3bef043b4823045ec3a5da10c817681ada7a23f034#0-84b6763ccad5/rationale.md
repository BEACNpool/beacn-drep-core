# Rationale: dfd81f8db652fd9263e0ce3bef043b4823045ec3a5da10c817681ada7a23f034#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline treasury evidence: the on-chain treasury amount field needed for a Treasury Withdrawal review was missing. This is a conservative, evidence-based hold, not a rejection of the idea.

The proposal requested Phase 1 funding for Bifrost, a Bitcoin-to-Cardano bridge, from FluidTokens and Lantr Engineering. It described about ₳12,332,031 over nine months, including a refundable contingency, to move from testnet toward launch readiness through hardening, audits, formal verification, partner readiness, stewardship, and economic design. The proposal did support some core facts, including that Bifrost is designed as a permissionless Bitcoin-Cardano bridge using Cardano’s SPO ecosystem, and that public rollout plus 24 months of operations are deferred to a later Phase 2 proposal.

However, several important claims remained assertions rather than independently evidenced review findings. The review did not have independent evidence that Phase 1 would end with an audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes, or that BTC custody would be distributed across 400+ Cardano SPOs with threshold control by delegated stake. The treasury review was also missing milestone-gated disbursement and sustainability evidence, while the risk review lacked independent assurance and a rollback or remedy path.

A directional YES or NO would be unblocked by the missing treasury_amount_lovelace field for the withdrawal, plus replayable public evidence for the major technical custody and mainnet-readiness claims, a milestone-gated funding plan, a sustainability path, independent assurance, and a clear rollback or remedy path. Until those baseline items are present, BEACN’s vote remains ABSTAIN.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 640
- finding: Expires after epoch: 647
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Phase 1 of 2 funding to take Bifrost from a working testnet to launch readiness, including hardening, security audits, formal verification, ecosystem and partner readiness, stewardship, and economic foundations for launch.
- finding: Recipient: FluidTokens and Lantr Engineering
- finding: Stated amount: ₳12,332,031 approximate, including a 10% refundable contingency
- finding: Deliverables: Audited bridge running on Cardano mainnet in both custody modes under controlled access, Hardening, security audits, and formal verification, Ecosystem and partner readiness, Stewardship structure, Hardened economic model, SPO/dApp partner pipeline required for public launch
- finding: Deadline/expiry: 9-month delivery period from July 2026 to March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests approximately ₳12,332,031 from the Cardano Treasury for a 9-month Phase 1 delivery period from July 2026 to March 2027.
- finding: Claim (technical, proposer_asserted, high materiality): By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access.
- finding: Claim (technical, proposer_asserted, high materiality): Bifrost custody of locked BTC is distributed across 400+ Cardano SPOs weighted by delegation, and moving funds requires a cryptographic threshold of SPOs representing the majority of delegated stake.
- finding: Claim (technical, proposer_asserted, high materiality): If SPO coordination fails, Bifrost can activate a federated mode as an operational fallback.
- finding: Claim (technical, proposer_asserted, medium materiality): Bifrost smart contracts, off-chain tooling, and SDK are released under Apache 2.0 and can be audited, forked, run, or built on without permission.
- missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access.
- missing: Independent evidence for: Bifrost custody of locked BTC is distributed across 400+ Cardano SPOs weighted by delegation, and moving funds requires a cryptographic threshold of SPOs representing the majority of delegated stake.
- missing: Independent evidence for: If SPO coordination fails, Bifrost can activate a federated mode as an operational fallback.
- missing: Independent evidence for: Bifrost smart contracts, off-chain tooling, and SDK are released under Apache 2.0 and can be audited, forked, run, or built on without permission.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: milestone-gated disbursement
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
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: evidence is too thin for a directional vote while 1 blocker(s) remain open.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access.
- Claims and evidence missing: Independent evidence for: Bifrost custody of locked BTC is distributed across 400+ Cardano SPOs weighted by delegation, and moving funds requires a cryptographic threshold of SPOs representing the majority of delegated stake.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `84b6763ccad5ca51f496819c37e9f945b4797b6f93c457356c9beef5d6af9c35`
- snapshot_bundle_hash: `6959562c5a14ddca390b8ae42dcde5c8b755f5419ef03c5292b16004396a940e`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

