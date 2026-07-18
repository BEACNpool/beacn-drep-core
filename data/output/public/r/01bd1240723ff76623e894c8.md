# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#6
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.33` (binding treasury composite; advisory raw signal `-0.33`; LLM lean `+0.0` recorded, not added) | Confidence: `0.8025` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims include meaningful public-benefit and infrastructure-continuity arguments, and the proposal gives some checkable references for voting process, benchmarks, NCL compliance, prior funding, and custody controls. The main value questions around adoption magnitude and migration risk are still largely proposer-asserted, and the doctrine already prioritizes treasury stewardship and evidence quality, so no additional nudge beyond the deterministic assessment is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks to withdraw 1,162,746 ada for annual maintenance and enhancement of Plutarch and Ply, including compatibility work, bug fixes, optimizations, documentation, examples, technical blog posts, and developer-experience improvements. The proposer says the amount includes 1,128,880 ada for the work itself and 33,866 ada for Intersect budget administration. The proposal also says Plutarch and Ply are Cardano smart contract tooling, that prior funding exists, that the action passed the 2026 Intersect Budget Process Hydra Voting threshold, and that oversight would come through Intersect and technically capable third parties with milestone-based controls.

Several basic review gates passed: the anchor document was available, pinned, and replayable; the requested amount was clear; the tool descriptions and budget split were supported in the proposal; and the Intersect process and Net Change Limit claims were treated as independently verifiable in principle. But the evidence base was still thin for a treasury decision. The adoption claim was not independently supported, including the stated count of at least 26 teams and the separate conservative count of at least 15 teams. The proposal’s claims about maintenance being crucial, migration risk if the tools fall behind, sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path also remained insufficiently evidenced.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by pinned public chain evidence for the applicable Net Change Limit, stronger independent evidence for adoption and ecosystem need, and clearer treasury-risk support around sustainability, cost-benefit, assurance, and remedies if delivery problems arise.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.16M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Annual funding for maintenance and enhancement of Plutarch and Ply, including compatibility work, bug fixes, optimizations, documentation, examples, technical blog posts, and developer-experience improvements.
- finding: Recipient: Intersect treasury reserve smart contract stake address for MLabs Core Tool Maintenance & Enhancement: Plutarch and Ply
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience, Critical breakages and serious vulnerabilities addressed as first priority, Protocol-era and hard-fork compatibility, including Dijkstra era if relevant changes land during the funding period, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements
- finding: Deadline/expiry: annual funding period; specific dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,162,746 ada, consisting of 1,128,880 ada for Plutarch and Ply maintenance and 33,866 ada for an Intersect Budget Administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Plutarch is described as a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply is described as helping serialize Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, proposer_asserted, high materiality): MLabs says a recent internal audit counted at least 26 teams using Plutarch and Ply, while the rationale section separately says it conservatively counted at least 15 teams.
- finding: Claim (technical, independently_verifiable, medium materiality): MLabs states that its public cross-language benchmarks show Plutarch scripts rank among the smallest in the benchmark suite while requiring comparatively low on-chain compute and memory.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that continued maintenance is crucial for teams needing smart contract tooling that tracks Cardano ledger, Plutus, and UPLC evolution.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that if Plutarch and Ply fall behind protocol evolution, existing adopters may face friction, migration risk, bespoke workarounds, avoidable rewrites, or expensive smart contract stack migrations.
- missing: Independent evidence for: MLabs says a recent internal audit counted at least 26 teams using Plutarch and Ply, while the rationale section separately says it conservatively counted at least 15 teams.
- missing: Independent evidence for: The proposal states that continued maintenance is crucial for teams needing smart contract tooling that tracks Cardano ledger, Plutus, and UPLC evolution.
- missing: Independent evidence for: The proposal states that if Plutarch and Ply fall behind protocol evolution, existing adopters may face friction, migration risk, bespoke workarounds, avoidable rewrites, or expensive smart contract stack migrations.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1162746
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.58
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,162,746 ada, consisting of 1,128,880 ada for Plutarch and Ply maintenance and 33,866 ada for an Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "MLabs says a recent internal audit counted at least 26 teams using Plutarch and Ply, while the rationale section separately says it conservatively counted at least 15 teams." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1162746
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,162,746 ada, consisting of 1,128,880 ada for Plutarch and Ply maintenance and 33,866 ada for an Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Proposal clears individual quality floors but is not currently portfolio-eligible: insufficient remaining NCL capacity after higher-ranked proposals.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 30% of rolling available capacity.
- Claims and evidence missing: Independent evidence for: MLabs says a recent internal audit counted at least 26 teams using Plutarch and Ply, while the rationale section separately says it conservatively counted at least 15 teams.
- Claims and evidence missing: Independent evidence for: The proposal states that continued maintenance is crucial for teams needing smart contract tooling that tracks Cardano ledger, Plutus, and UPLC evolution.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `d963d60c2578babab34eba9a8aedb6a96f211e3e1dea116512c11998e1df1fd3`
- snapshot_bundle_hash: `303fbd2a2e11c03b0f38685cfb5e7f3158c499f241b886bb7871466322410f72`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `71c55fc4938e0c692e52f6c0b4a1c4d9d8926c12`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4566, "NO": 0.4996, "YES": 0.0438}`

