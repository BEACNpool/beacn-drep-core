# Rationale: dfd81f8db652fd9263e0ce3bef043b4823045ec3a5da10c817681ada7a23f034#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.15` (binding treasury composite; advisory raw signal `-0.15`; LLM lean `-0.02` recorded, not added) | Confidence: `0.7575` | Readiness: `0.75`
> Reasoning layer (precomputed): The claims describe potentially high public-benefit infrastructure, but the deterministic assessment says evidence is thin and overall status is incomplete; under the doctrine, large treasury spending with incomplete independently verified diligence should be nudged cautiously rather than toward spending.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and the applicable Net Change Limit was not pinned and independently verified from public chain evidence. That blocks a directional treasury vote under BEACN’s review rules, regardless of whether the proposal may have public value.

The proposal asks for ₳12,332,031 for Phase 1 of Bifrost, a permissionless Bitcoin-to-Cardano bridge, over a 9-month period from July 2026 to March 2027. The proposer describes work toward an audited mainnet bridge, hardening, security audits, formal verification, partner readiness, stewardship design, economic foundations, and SPO/dApp launch preparation. Some core claims were supported in the proposal, including the design goal of bringing BTC to Cardano as a native Cardano asset, the requested amount and timeline, the use of Cardano SPOs in the custody model, and the plan for open-source public infrastructure with no bridge token or founder allocation.

Other important claims were not independently supported enough for BEACN to treat them as settled. In particular, the review lacked independent evidence that Phase 1 will end with an audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access. The review also found thin claims-and-evidence status, unknown execution risk, missing milestone-gated disbursement details, missing sustainability-path analysis, missing independent assurance, and no clear rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the mainnet audited-bridge claim, milestone-gated disbursement, sustainability path, independent assurance, and rollback or remedy plan.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: expired
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
- finding: Requested: Phase 1 of 2 for Bifrost, a permissionless Bitcoin-Cardano bridge, covering launch-readiness work including hardening, security audits, formal verification, ecosystem and partner readiness, and stewardship and economic foundations.
- finding: Recipient: FluidTokens and Lantr Engineering
- finding: Stated amount: 12332031
- finding: Deliverables: Audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access, Hardening and security audits, Formal verification, Ecosystem and partner readiness, Stewardship structure, Hardened economic model, SPO/dApp partner pipeline required for public launch
- finding: Deadline/expiry: 9-month delivery period from July 2026 to March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳12,332,031, approximately $1,973,125 at 0.16 USD/ADA, including a 10% refundable contingency, for a 9-month Phase 1 delivery period from July 2026 to March 2027.
- finding: Claim (technical, proposer_asserted, high materiality): By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access.
- finding: Claim (governance, proposer_asserted, high materiality): Public rollout and 24 months of operations are intentionally separated into a Phase 2 proposal planned for Q1 2027 after the bridge has been proven on-chain.
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost custody of locked BTC is described as distributed across 400+ Cardano SPOs weighted by delegation, with funds moved by a cryptographic threshold of SPOs representing the majority of delegated stake.
- finding: Claim (technical, proposer_asserted, high materiality): If SPO coordination fails, Bifrost includes a federated mode as an operational fallback continuity layer.
- missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access.
- missing: Independent evidence for: Public rollout and 24 months of operations are intentionally separated into a Phase 2 proposal planned for Q1 2027 after the bridge has been proven on-chain.
- missing: Independent evidence for: If SPO coordination fails, Bifrost includes a federated mode as an operational fallback continuity layer.
- missing: Independent evidence for: Bifrost is already live on testnet under Catalyst Fund 14, with working peg-ins and peg-outs and participating SPOs.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access." — so cost or precedent may outweigh the benefit.
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
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims describe potentially high public-benefit infrastructure, but the deterministic assessment says evidence is thin and overall status is incomplete; under the doctrine, large treasury spending with incomplete independently verified diligence should be nudged cautiously rather than toward spending.
- Directional treasury voting is blocked until this action is ranked against competing active proposals and verified NCL capacity.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.14 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access.
- Claims and evidence missing: Independent evidence for: Public rollout and 24 months of operations are intentionally separated into a Phase 2 proposal planned for Q1 2027 after the bridge has been proven on-chain.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `6ff1b2d7352973e8f298f03a90daf72956bb61a6d8cf89805b287259b6a1e231`
- snapshot_bundle_hash: `001f56851ddcc0570d713ba06eca5a93acefff982ddf6fee3427e4a2b410d664`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `ef85d07c90c6bede6f4999502ba5fb3296da465c`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5094, "NO": 0.3953, "YES": 0.0953}`

