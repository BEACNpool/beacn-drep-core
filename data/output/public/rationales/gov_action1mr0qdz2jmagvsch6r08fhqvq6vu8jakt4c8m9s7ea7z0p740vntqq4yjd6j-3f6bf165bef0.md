# Rationale: gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7808` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is materially aligned with public-benefit infrastructure and includes concrete deliverables, milestones, budget categories, and some independently verifiable metrics, but the request is large and several important claims about usage, cost reasonableness, prior delivery, and oversight effectiveness remain proposer-asserted within the document. The deterministic treasury and evidence rules appear to capture the main caution and public-good considerations, so no additional nudge is justified.

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Se7en Labs: Daedalus Wallet Maintenance and Improvements 2026-2027. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Daedalus Wallet maintenance and improvements for 2026-2027 as a time-and-materials engagement delivered by Se7en Labs, Inc. It asks the treasury for 1,785,333 ADA. The strongest grounded claim is: The proposal says Daedalus private keys are generated and stored on the user's device, are never transmitted to an external service, and the Apache 2.0 open-source code allows this to be audited.

A material claim remains proposer-asserted or thinly supported: Daedalus is described as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from chain data without third-party APIs or trusted backends. Reason code: VERIFIED_NCL_REQUIRED.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 1.79M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Daedalus Wallet maintenance and improvements for 2026-2027 as a time-and-materials engagement delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc., with administration and disbursement through Intersect as described in the proposal
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including node upgrades, hard fork readiness, and compatible releases at least 2 weeks before each mainnet hard fork, Ecosystem expansion including Keystone and Flex hardware wallet support, CIP-30 dApp connector, and Japanese localisation, User support across GitHub, community forums, direct channels, and Japanese-language support, Maintenance of Windows, macOS x86_64, macOS aarch64, and Linux builds, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: Contract year through Q3 2027 for architecture assessment; other work spans 52 weeks or milestone durations stated in document
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is described as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from chain data without third-party APIs or trusted backends.
- finding: Claim (technical, independently_verifiable, high materiality): The proposal says Daedalus private keys are generated and stored on the user's device, are never transmitted to an external service, and the Apache 2.0 open-source code allows this to be audited.
- finding: Claim (adoption, proposer_asserted, medium materiality): According to opt-in telemetry cited by the proposer, Daedalus has approximately 4,000 monthly active users, while the proposer asserts the true count is meaningfully higher.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs says it assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states the requested 1,785,333 ADA is allocated as 1,666,667 ADA for team labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and 52,000 ADA for Intersect administration.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal states any unspent labor, hardware, or audit budget at contract close will be returned to the treasury.
- missing: Independent evidence for: Daedalus is described as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from chain data without third-party APIs or trusted backends.
- missing: Independent evidence for: According to opt-in telemetry cited by the proposer, Daedalus has approximately 4,000 monthly active users, while the proposer asserts the true count is meaningfully higher.
- missing: Independent evidence for: Se7en Labs says it assumed Daedalus responsibility under an IOG contract in January 2026 and shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization.
- missing: Independent evidence for: The proposal states any unspent labor, hardware, or audit budget at contract close will be returned to the treasury.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1785333
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.62
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
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
- finding: Strongest YES: the proposal substantiates "The proposal says Daedalus private keys are generated and stored on the user's device, are never transmitted to an external service, and the Apache 2.0 open-source code allows this to be audited." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is described as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from chain data without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1785333
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal says Daedalus private keys are generated and stored on the user's device, are never transmitted to an external service, and the Apache 2.0 open-source code allows this to be audited." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
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
- Claims and evidence missing: Independent evidence for: Daedalus is described as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from chain data without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: According to opt-in telemetry cited by the proposer, Daedalus has approximately 4,000 monthly active users, while the proposer asserts the true count is meaningfully higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `3f6bf165bef09c0437ec8ba119e6b340c47839e11f08c1f31bc1322d93a74bcf`
- snapshot_bundle_hash: `e1712c285c1a0c5ad7d1932a7aa20b861a2416fbafbb2e3049b8e35ad4b4ec8b`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

