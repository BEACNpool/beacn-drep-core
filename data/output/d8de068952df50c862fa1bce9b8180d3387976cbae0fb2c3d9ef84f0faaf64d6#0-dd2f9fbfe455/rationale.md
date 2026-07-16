# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.56` (binding treasury composite; advisory raw signal `-0.56`; LLM lean `+0.02` recorded, not added) | Confidence: `0.82` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims emphasize maintenance of open-source full-node wallet infrastructure, public deliverables, milestone-based administration, and independently verifiable release/version metrics. The nudge remains modest because several important adoption, cost-efficiency, and prior-delivery claims are proposer-asserted rather than independently evidenced in the supplied claims.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work.

The action asks for 1,785,333 ADA for Se7en Labs’ Daedalus maintenance and improvement work through 2026-2027, with funds administered by Intersect. The proposal covers hard-fork-ready Daedalus releases, backend updates, signed releases, CI maintenance, Japanese translation, Leios and Peras readiness, Keystone and Flex hardware wallet support, CIP-30 dApp connector work, user support, and a public architecture assessment by Q3 2027.

Several parts were supported well enough to matter: the anchor document was pinned and replayable, the budget breakdown was supplied, Intersect was proposed as administrator and milestone verifier, and release/version timing can be checked through public GitHub repositories and the Cardano mainnet chain. The proposal also substantiated prior Daedalus maintenance work under an IOG contract since January 2026, including named shipped improvements. However, important claims remained only proposer-asserted or thinly evidenced, including that Daedalus is Cardano’s only full-node desktop wallet, that it avoids third-party APIs or trusted backends, and that it has about 4,000 monthly active users from opt-in telemetry.

Because this is a treasury withdrawal, BEACN applied elevated scrutiny. The review found medium execution risk, missing sustainability and cost-benefit clarity, missing independent assurance, and no clear rollback or remedy path. The evidence that would unblock a directional vote is independently pinned public-chain verification of the relevant Net Change Limit, plus stronger replayable evidence for the key product, adoption, cost-efficiency, assurance, and remedy claims.

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
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027, including protocol maintenance, ecosystem expansion, user support, hardware wallet support, CIP-30, Japanese localisation, and architecture assessment.
- finding: Recipient: Se7en Labs, Inc., with funds administered by Intersect
- finding: Stated amount: 1785333
- finding: Deliverables: Compatible Daedalus stable releases at least 2 weeks before each mainnet hard fork, Continuous cardano-node and cardano-wallet backend updates, signed releases, CI maintenance, and Japanese translation coverage for 52 weeks, Leios and Peras compatible node readiness ahead of testnet or mainnet activation, Keystone and Flex hardware wallet support in a stable release, CIP-30 dApp connector implementation with documentation and dApp interoperability, Ongoing user support via GitHub, community forums, direct channels, and Japanese-language support, Public architecture assessment by Q3 2027
- finding: Deadline/expiry: contract year through 2026-2027; architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, high materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be higher because privacy-conscious users may not opt in.
- finding: Claim (technical, supported_in_proposal, high materiality): Se7en Labs has maintained Daedalus under an IOG contract since January 2026 and says it shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization.
- finding: Claim (technical, independently_verifiable, high materiality): The proposal commits to releases compatible with each mainnet hard fork at least 2 weeks before activation, with release timing and version-currency metrics independently verifiable from public GitHub repositories and the Cardano mainnet chain.
- finding: Claim (governance, proposer_asserted, high materiality): All funded outputs are described as public assets under the Apache License 2.0, including source code, build tooling, documentation, and release artifacts.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget totals 1,785,333 ADA, consisting of 1,666,667 ADA for labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be higher because privacy-conscious users may not opt in.
- missing: Independent evidence for: All funded outputs are described as public assets under the Apache License 2.0, including source code, build tooling, documentation, and release artifacts.
- missing: Independent evidence for: Any unspent labor, hardware, or audit budget is stated to be returned to the treasury at contract close.
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
- finding: Strongest YES: the proposal substantiates "Se7en Labs has maintained Daedalus under an IOG contract since January 2026 and says it shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Se7en Labs has maintained Daedalus under an IOG contract since January 2026 and says it shipped Mithril Snapshot Bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims emphasize maintenance of open-source full-node wallet infrastructure, public deliverables, milestone-based administration, and independently verifiable release/version metrics. The nudge remains modest because several important adoption, cost-efficiency, and prior-delivery claims are proposer-asserted rather than independently evidenced in the supplied claims.
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
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be higher because privacy-conscious users may not opt in.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `dd2f9fbfe455ae0ab07b5e7af83d86d77ec43a8fa77b464984ac566a86d0c3a8`
- snapshot_bundle_hash: `fcd006c62aa3d3b464e44706f97bf074bac3ed36fa122d2bbef900229419e46d`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4158, "NO": 0.5446, "YES": 0.0396}`

