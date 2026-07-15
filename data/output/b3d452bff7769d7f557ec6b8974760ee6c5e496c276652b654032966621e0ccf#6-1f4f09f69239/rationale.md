# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#6
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.33` (binding treasury composite; advisory raw signal `-0.33`; LLM lean `+0.0` recorded, not added) | Confidence: `0.8025` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show plausible public-benefit open-source infrastructure maintenance and some independently checkable governance, benchmark, NCL, and smart-contract administration references, but key adoption and cost-value claims remain largely proposer-asserted and the deterministic assessment is already ready; no additional doctrine-based nudge is justified beyond the mechanical score.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks to withdraw 1,162,746 ada for annual maintenance and enhancement of Plutarch and Ply, with 1,128,880 ada for the work and 33,866 ada for Intersect budget administration. The requested work includes compatibility updates, critical breakage and vulnerability response, bug fixes, correctness improvements, optimizations, documentation, examples, technical blog posts, and developer-experience improvements. Funds would be administered through Intersect using milestone-based smart-contract disbursement controls.

Several basic claims were supported in the proposal: the amount requested, the split between project funding and administration fee, the descriptions of Plutarch and Ply, prior related MLabs funding, and the stated Intersect-administered treasury process. Some claims were only proposer assertions or still needed stronger independent support, including the adoption claim that at least 26 or 15 teams use the tools, and the possible need for future protocol-era compatibility work such as Dijkstra-era changes. The review also found thin claims-and-evidence coverage, unknown execution risk, and missing detail on sustainability, cost-benefit clarity, independent assurance, and rollback or remedy paths.

This is a conservative, evidence-based hold, not a rejection of the tools or the maintenance work. A directional vote would be unblocked by pinned, independently verifiable public chain evidence for the relevant Net Change Limit, plus stronger independent evidence for the material adoption and technical-need claims and clearer treasury-risk information around sustainability, value for cost, assurance, and remedies if delivery problems occur.

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
- finding: Requested: Annual funding for maintenance and enhancement of Plutarch and Ply, including compatibility, bug fixes, optimizations, documentation, examples, technical blog posts, and developer-experience improvements.
- finding: Recipient: Intersect treasury reserve smart contract stake address for project administration on behalf of MLabs/vendor
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1: Plutarch and Ply Maintenance, Compatibility & Developer Experience, Critical breakages and serious vulnerabilities, Protocol-era and hard-fork compatibility, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements, Milestone-based disbursement controls through Intersect-administered smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,162,746 ADA, consisting of 1,128,880 ADA for Plutarch and Ply maintenance, compatibility, and developer experience plus a 33,866 ADA Intersect budget administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Plutarch is described as a Haskell eDSL for creating efficient Cardano smart contracts through controlled compilation into UPLC, and Ply is described as tooling for serializing Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, proposer_asserted, high materiality): MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, citing an internal audit count of at least 26 teams in the motivation and at least 15 teams in the rationale.
- finding: Claim (technical, independently_verifiable, medium materiality): The proposal states that Plutarch scripts rank among the smallest in MLabs' public cross-language benchmark suite while requiring comparatively low on-chain compute and memory.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal says the next funding period may include protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land during the funding period.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer argues that failure to maintain Plutarch and Ply could create friction, migration risk, bespoke workarounds, or avoidable rewrites for existing adopters.
- missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, citing an internal audit count of at least 26 teams in the motivation and at least 15 teams in the rationale.
- missing: Independent evidence for: The proposal says the next funding period may include protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land during the funding period.
- missing: Independent evidence for: The proposer argues that failure to maintain Plutarch and Ply could create friction, migration risk, bespoke workarounds, or avoidable rewrites for existing adopters.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,162,746 ADA, consisting of 1,128,880 ADA for Plutarch and Ply maintenance, compatibility, and developer experience plus a 33,866 ADA Intersect budget administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, citing an internal audit count of at least 26 teams in the motivation and at least 15 teams in the rationale." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,162,746 ADA, consisting of 1,128,880 ADA for Plutarch and Ply maintenance, compatibility, and developer experience plus a 33,866 ADA Intersect budget administration fee." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, citing an internal audit count of at least 26 teams in the motivation and at least 15 teams in the rationale.
- Claims and evidence missing: Independent evidence for: The proposal says the next funding period may include protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land during the funding period.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `1f4f09f69239c9c84b6f593315ae6f7ece613caf8a925f37cf70bb8a681a7845`
- snapshot_bundle_hash: `2f70e21919e5f56ca24db642383c30eff2027ee94784f413706353f7df7fc747`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4566, "NO": 0.4996, "YES": 0.0438}`

