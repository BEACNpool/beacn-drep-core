# Rationale: dfd81f8db652fd9263e0ce3bef043b4823045ec3a5da10c817681ada7a23f034#0
Recommendation: **NO**
Score: `-0.1475` (raw `-0.56` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7569` | Readiness: `0.75`
> Reasoning layer (precomputed): The claims describe potentially high public-benefit infrastructure, but the supplied assessment says claims and evidence are thin and the request is large for treasury spending; under the doctrine, weak evidence on a significant treasury ask justifies a small cautionary negative nudge rather than rewarding plausible upside.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Bifrost: Unlocking Bitcoin DeFi on Cardano — Road to Mainnet (Phase 1 of 2). On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund Phase 1 of Bifrost, a Bitcoin-Cardano bridge, to move from working testnet to launch readiness. It asks the treasury for 12332031 ADA. The strongest grounded claim is: Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset.

A material claim remains proposer-asserted or thinly supported: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access.

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
- finding: Requested: Fund Phase 1 of Bifrost, a Bitcoin-Cardano bridge, to move from working testnet to launch readiness.
- finding: Recipient: FluidTokens and Lantr Engineering
- finding: Stated amount: 12332031
- finding: Deliverables: Hardening, Security audits, Formal verification, Ecosystem and partner readiness, Stewardship structure and economic foundations for launch, Audited bridge running on Cardano mainnet in federated and SPO threshold custody modes under controlled access
- finding: Deadline/expiry: March 2027 after a 9-month delivery period from July 2026 to March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳12,332,031, approximately $1,973,125 at 0.16 USD/ADA, including a 10% refundable contingency, for a 9-month delivery period.
- finding: Claim (technical, proposer_asserted, high materiality): By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access.
- finding: Claim (governance, supported_in_proposal, high materiality): Public rollout and 24 months of operations are excluded from this request and planned for a Phase 2 proposal in Q1 2027.
- finding: Claim (technical, proposer_asserted, high materiality): Bifrost custody is described as distributed across 400+ Cardano SPOs weighted by delegation, requiring a cryptographic threshold representing the majority of delegated stake to move funds.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says Bifrost is already live on testnet under Catalyst Fund 14 with working peg-ins and peg-outs and participating SPOs.
- missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access.
- missing: Independent evidence for: Bifrost custody is described as distributed across 400+ Cardano SPOs weighted by delegation, requiring a cryptographic threshold representing the majority of delegated stake to move funds.
- missing: Independent evidence for: The proposal says Bifrost is already live on testnet under Catalyst Fund 14 with working peg-ins and peg-outs and participating SPOs.
- missing: Independent evidence for: Bifrost's smart contracts, off-chain tooling, and SDK are stated to be open source under Apache 2.0.
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
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: The claims describe potentially high public-benefit infrastructure, but the supplied assessment says claims and evidence are thin and the request is large for treasury spending; under the doctrine, weak evidence on a significant treasury ask justifies a small cautionary negative nudge rather than rewarding plausible upside.
- Directional NO is supported by affirmative independent evidence of waste, duplication, excessive cost, or failed delivery — not by missing information.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 50% of rolling available capacity.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access.
- Claims and evidence missing: Independent evidence for: Bifrost custody is described as distributed across 400+ Cardano SPOs weighted by delegation, requiring a cryptographic threshold representing the majority of delegated stake to move funds.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `6af0cf046af4e212dde8563d7c36835febb9ff4dc5a7315a4c83e9da46a544cf`
- snapshot_bundle_hash: `962e7790499caea9fcbcdec4ef928fa4dddb9a2811edf091925873f6dd561bbb`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2254, "NO": 0.6767, "YES": 0.0979}`

