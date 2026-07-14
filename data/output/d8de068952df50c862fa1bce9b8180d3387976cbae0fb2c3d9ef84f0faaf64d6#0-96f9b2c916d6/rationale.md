# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.56` (raw `-0.56` + doctrine-LLM nudge `+0.02`) | Confidence: `0.82` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe maintenance of established open-source wallet infrastructure with public deliverables, independently verifiable release/version metrics, milestone administration, and some downside protection through returned unspent funds. The nudge remains small because several important adoption and historical-performance claims are proposer-asserted rather than independently evidenced in the supplied document, and the treasury amount is substantial.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for 1,785,333 ADA for Se7en Labs, Inc. to maintain and improve Daedalus over a 52-week contract, with Intersect administering funds and verifying milestones. The scope includes protocol and node compatibility, wallet backend updates, hard fork readiness, signed releases, Nix build maintenance, security and dependency updates, hardware wallet support, CIP-30, Japanese localisation, user support, and an architecture assessment by Q3 2027.

Several parts of the proposal were well-supported in the supplied review. Se7en Labs’ recent Daedalus work under an IOG contract, the proposed technical scope, the release-timing commitments, the budget breakdown, return of unspent funds, and Intersect’s administration role were all treated as supported by the proposal or independently verifiable where stated. But important claims remained unsupported in the supplied evidence, including that Daedalus is Cardano’s only full-node desktop wallet using chain-derived wallet and governance data without third-party APIs, and that Daedalus has about 4,000 monthly active users with a meaningfully higher true count.

This is a conservative, evidence-based hold, not a rejection of the work. The review found a pinned and replayable proposal anchor, medium execution risk, and a credible strongest-YES case, but treasury withdrawals require a higher bar because they spend shared ADA. A directional vote would be unblocked by pinned, independently verifiable Net Change Limit evidence from the public chain, plus stronger public evidence for the unsupported product and adoption claims, sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path.

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
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027 delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc., with Intersect serving as administrator and milestone verifier
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including node upgrades, wallet backend updates, hard fork readiness, and compatible releases at least 2 weeks before each mainnet hard fork, Ecosystem expansion including Keystone and Flex hardware wallet support and a CIP-30 dApp connector, Japanese localisation and user support across GitHub, community forums, and direct channels, Maintenance of reproducible Nix build infrastructure, dependency updates, security patches, platform compatibility, and signed releases, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: 52-week contract period, with architecture assessment published by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, high materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting the true count is meaningfully higher.
- finding: Claim (technical, supported_in_proposal, high materiality): Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM Backend, Apple Silicon builds, a release CLI, and Nix build modernization since then.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed scope includes maintaining Cardano protocol compatibility, release engineering, security and dependency maintenance, four platform builds, Japanese localisation, hardware wallet support, CIP-30, user support, and an architecture assessment.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to compatible stable Daedalus releases at least 2 weeks before every mainnet hard fork and cardano-node being no more than 2 major versions behind mainnet recommended at any time.
- finding: Claim (governance, independently_verifiable, medium materiality): All release-timing and version-currency success metrics are stated to be independently verifiable from public GitHub repositories and the Cardano mainnet chain.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting the true count is meaningfully higher.
- missing: Independent evidence for: Se7en Labs states it has not received ada from the Cardano Treasury within the last 24 months and that its prior Daedalus maintenance work was funded by a direct IOG contract ending August 31, 2026.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1785333
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
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
- finding: Strongest YES: the proposal substantiates "Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM Backend, Apple Silicon builds, a release CLI, and Nix build modernization since then." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1785333
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM Backend, Apple Silicon builds, a release CLI, and Nix build modernization since then." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe maintenance of established open-source wallet infrastructure with public deliverables, independently verifiable release/version metrics, milestone administration, and some downside protection through returned unspent funds. The nudge remains small because several important adoption and historical-performance claims are proposer-asserted rather than independently evidenced in the supplied document, and the treasury amount is substantial.
- Proposal clears individual quality floors but is not currently portfolio-eligible: insufficient remaining NCL capacity after higher-ranked proposals.
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
- Claims and evidence missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting the true count is meaningfully higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `96f9b2c916d61502d8877c54a9ec855e5d6f0151e301f990a85474f7beaadaea`
- snapshot_bundle_hash: `a474ab02d43a24593076c41b2a6f8342593f3c57240d02e2b64be3ee79d7e882`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4158, "NO": 0.5446, "YES": 0.0396}`

