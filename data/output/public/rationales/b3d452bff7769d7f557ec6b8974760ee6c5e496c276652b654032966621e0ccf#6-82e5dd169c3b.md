# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#6
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.33` (binding treasury composite; advisory raw signal `-0.33`; LLM lean `+0.0` recorded, not added) | Confidence: `0.8025` | Readiness: `0.85`
> Reasoning layer (precomputed): The document contains meaningful governance-process references, a budget breakdown, prior-funding disclosures, and a concrete disbursement framework, while the main technical adoption and counterfactual-risk claims remain partly asserted and include an internal inconsistency between 26 and 15 counted teams. The deterministic assessment is already ready, and these evidence-quality mixed signals do not justify a directional nudge beyond the mechanical rules.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal needs independently verified Net Change Limit evidence before a directional vote. This is a conservative, evidence-based hold, not a rejection of the work.

The action requested 1,162,746 ada for annual maintenance and enhancement of MLabs’ Plutarch and Ply tooling, with 1,128,880 ada for the work package and 33,866 ada for Intersect administration. The proposal says Intersect submitted it on behalf of MLabs, with funds going to the 2026 Treasury Reserve Smart Contract stake address. The requested work covers maintenance, compatibility, bug fixes, optimizations, documentation, examples, blog posts, and developer-experience improvements, but the document did not state a deadline.

Several claims were supported well enough for review: the amount and fee breakdown were clear, the proposal anchor was pinned and replayable, the tool descriptions were supported in the proposal, and the Intersect Budget Process support claim had independently verifiable references. But important claims were still thin or unsupported, including the adoption count discrepancy of at least 26 teams in one section versus at least 15 in another, future compatibility needs around ledger, Plutus, tooling, and possible Dijkstra-era changes, and the broader cost-benefit and sustainability case. The review also found missing independent assurance and no clear rollback or remedy path.

The gate that blocks a YES or NO vote is the need to pin and independently verify the applicable Net Change Limit from public chain evidence. BEACN would need that verified NCL evidence, plus stronger independent support for the adoption and execution-risk claims, to move from this hold to a directional treasury vote.

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
- finding: Requested: Treasury withdrawal to fund annual maintenance and enhancement of MLabs Core Tool Maintenance & Enhancement: Plutarch and Ply.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor MLabs
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience, Critical breakages and serious vulnerabilities, Protocol-era and hard-fork compatibility, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,162,746 ada, consisting of 1,128,880 ada for Plutarch and Ply maintenance, compatibility, and developer experience plus a 33,866 ada Intersect administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Plutarch is described as a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, while Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says MLabs counted at least 26 teams using Plutarch and Ply in the motivation section, while the rationale separately says the count was at least 15 teams.
- finding: Claim (technical, independently_verifiable, medium materiality): The proposal states that Plutarch scripts rank among the smallest in MLabs' public cross-language benchmark suite while requiring comparatively low on-chain compute and memory, and links to the benchmark page.
- finding: Claim (technical, proposer_asserted, high materiality): The next funding period is expected to cover ongoing Cardano ledger, Plutus, and tooling evolution, including possible Dijkstra-era compatibility if relevant changes land during the funding period.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal claims that if Plutarch and Ply fall behind ledger and Plutus/UPLC evolution, existing adopters may face more friction, migration risk, bespoke workarounds, or avoidable rewrites.
- missing: Independent evidence for: The proposal says MLabs counted at least 26 teams using Plutarch and Ply in the motivation section, while the rationale separately says the count was at least 15 teams.
- missing: Independent evidence for: The next funding period is expected to cover ongoing Cardano ledger, Plutus, and tooling evolution, including possible Dijkstra-era compatibility if relevant changes land during the funding period.
- missing: Independent evidence for: The proposal claims that if Plutarch and Ply fall behind ledger and Plutus/UPLC evolution, existing adopters may face more friction, migration risk, bespoke workarounds, or avoidable rewrites.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,162,746 ada, consisting of 1,128,880 ada for Plutarch and Ply maintenance, compatibility, and developer experience plus a 33,866 ada Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says MLabs counted at least 26 teams using Plutarch and Ply in the motivation section, while the rationale separately says the count was at least 15 teams." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,162,746 ada, consisting of 1,128,880 ada for Plutarch and Ply maintenance, compatibility, and developer experience plus a 33,866 ada Intersect administration fee." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: The proposal says MLabs counted at least 26 teams using Plutarch and Ply in the motivation section, while the rationale separately says the count was at least 15 teams.
- Claims and evidence missing: Independent evidence for: The next funding period is expected to cover ongoing Cardano ledger, Plutus, and tooling evolution, including possible Dijkstra-era compatibility if relevant changes land during the funding period.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `82e5dd169c3b16111222792a4da2a5c1e58d95c55dca3e4e07ada2ae822a6bff`
- snapshot_bundle_hash: `00026863c669f7382cb93dc4e9319559d4f7386272ef3c48c48bc725321a9aaf`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4566, "NO": 0.4996, "YES": 0.0438}`

