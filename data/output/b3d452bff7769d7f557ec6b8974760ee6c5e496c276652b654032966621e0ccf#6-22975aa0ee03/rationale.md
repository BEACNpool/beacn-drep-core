# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#6
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.33` (raw `-0.33` + doctrine-LLM nudge `+0.0`) | Confidence: `0.8025` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit infrastructure value and some independently checkable governance and oversight references, but the document also relies on proposer assertions for adoption impact and migration risk and contains inconsistent team-count figures. The deterministic engine has already marked the assessment ready, and the remaining evidence-quality concerns are adequately captured without an additional advisory nudge.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work or the proposer.

The action asks to withdraw 1,162,746 ada for annual MLabs maintenance and enhancement of Plutarch and Ply, submitted by Intersect on behalf of MLabs. The proposal says this includes 1,128,880 ada for maintenance, compatibility, bug fixes, optimizations, documentation, examples, technical blog posts, and developer-experience work, plus a 33,866 ada Intersect Budget Administration fee. It also says funds would be administered through Sundae Labs treasury management smart contracts with reserve and project-specific addresses, role-based approvals, oversight, milestone controls, and a public dashboard.

Several claims were well-supported in the proposal: the requested amount and budget split, the description of Plutarch and Ply, the planned work priorities, prior related funding disclosures, Intersect budget-process support, and the statement that the request did not breach the stated 350M Net Change Limit at submission. But some material claims remained unsupported by independent evidence, including the claimed level of ecosystem adoption and the asserted migration or rewrite risks if maintenance is not funded. The review also found thin evidence overall, unknown execution risk, no stated deadline, missing sustainability path, missing cost-benefit clarity, missing independent assurance, and no clear rollback or remedy path.

For BEACN to move from NEEDS_MORE_INFO to a directional vote, the review would need pinned, independently verifiable public chain evidence for the applicable Net Change Limit, plus stronger independent support for the adoption and risk claims, clearer treasury sustainability and cost-benefit evidence, and better assurance around execution and remedies. Until then, abstaining avoids overstating certainty on a treasury withdrawal that would consume shared ada and set precedent.

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
- finding: Requested: Annual funding for MLabs Core Tool Maintenance & Enhancement: Plutarch and Ply, including maintenance, compatibility, bug fixes, optimizations, documentation, examples, technical blog posts, and developer-experience improvements.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor MLabs
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience, Critical breakages and serious vulnerabilities, Protocol-era and hard-fork compatibility, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,162,746 ada, consisting of 1,128,880 ada for Plutarch and Ply maintenance, compatibility and developer experience plus a 33,866 ada Intersect Budget Administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Plutarch is described as a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply is described as helping serialize Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, proposer_asserted, high materiality): MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem and reports at least 26 teams in the motivation section and at least 15 teams in the rationale section building with the tools.
- finding: Claim (technical, independently_verifiable, medium materiality): MLabs states that Plutarch scripts rank among the smallest in its public cross-language benchmark suite while requiring comparatively low on-chain compute and memory, and provides a benchmark URL.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal says the next funding period will prioritize critical breakages and serious vulnerabilities, protocol-era and hard-fork compatibility, bug fixes and optimizations, then documentation and developer-experience improvements.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer argues that without continued maintenance, existing adopters could face more friction, migration risk, bespoke workarounds, avoidable rewrites, or expensive smart contract stack migrations.
- missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem and reports at least 26 teams in the motivation section and at least 15 teams in the rationale section building with the tools.
- missing: Independent evidence for: The proposer argues that without continued maintenance, existing adopters could face more friction, migration risk, bespoke workarounds, avoidable rewrites, or expensive smart contract stack migrations.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,162,746 ada, consisting of 1,128,880 ada for Plutarch and Ply maintenance, compatibility and developer experience plus a 33,866 ada Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem and reports at least 26 teams in the motivation section and at least 15 teams in the rationale section building with the tools." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,162,746 ada, consisting of 1,128,880 ada for Plutarch and Ply maintenance, compatibility and developer experience plus a 33,866 ada Intersect Budget Administration fee." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem and reports at least 26 teams in the motivation section and at least 15 teams in the rationale section building with the tools.
- Claims and evidence missing: Independent evidence for: The proposer argues that without continued maintenance, existing adopters could face more friction, migration risk, bespoke workarounds, avoidable rewrites, or expensive smart contract stack migrations.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `22975aa0ee035a0239e7d9d2668a4ade863a6de8db8ef728feeac8eb07cc07bc`
- snapshot_bundle_hash: `b81aeae3d83a80d2efa1468834201f63d9f64efd25de8a97b22f13390dbe5d3e`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4566, "NO": 0.4996, "YES": 0.0438}`

