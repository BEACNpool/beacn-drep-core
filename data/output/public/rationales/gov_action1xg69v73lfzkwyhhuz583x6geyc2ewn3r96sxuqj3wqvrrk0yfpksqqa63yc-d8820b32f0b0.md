# Rationale: gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc
Recommendation: **NO**
Score: `-0.2833` (raw `-0.2833` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7908` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit ecosystem infrastructure and includes a narrower scope, milestones, and claimed oversight, but the most material adoption, dependency, and governance claims are mostly proposer-asserted or only externally checkable rather than evidenced in the supplied document. The deterministic treasury and evidence rules appear to capture the main caution points, so no additional nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not meet the higher evidence bar required for spending shared ADA. The proposal had a pinned, replayable anchor and a clear 9-month delivery plan, but key claims about Scalus being an established platform with broad reuse were not independently supported enough to justify the requested withdrawal under elevated treasury scrutiny.

The action requested ₳2,464,844 for Lantr Engineering to continue Scalus work through March 2027, covering maintenance, Dijkstra readiness, JVM and JS/TS interoperability, and early application runtime components. The proposer stated that Scalus has been developed over three years, is reused in Cardano tooling such as MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit, and supports multiple protocols and applications. The proposal itself supported the budget amount, the 9-month schedule, the reduced scope from a prior ₳8.5M proposal, and the three quarterly milestone structure.

The review found some positive evidence: the anchor was available, the requested amount and timeline were clear, and the strongest YES case was that the budget was substantiated and the proposal cleared basic evidence gates. But the claims-and-evidence section remained thin. Independent evidence was still missing for the central claim that Scalus is an established open-source Cardano development platform built over three years of continuous delivery, and for the claim that its components are reused across the named developer tools.

Because this is a treasury withdrawal, BEACN applied elevated scrutiny. The review also noted medium execution risk, a confidence-reducing flag score, missing treasury sustainability path, missing independent assurance, and missing dependency map. With those gaps, the cost and precedent risk outweighed the supported benefits, so BEACN voted NO.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 640
- finding: Expires after epoch: 647
- finding: Treasury request: 2.46M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Fund a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a first scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance including bug fixes, dependency upkeep, security patches, and releases, Dijkstra developer preview with initial Plutus V4 support in the compiler and standard library, Dijkstra ledger rules and transaction-builder updates including new builtins, cost models, nested transactions, accounts, and guard scripts, Improved JS/TS interfaces and documentation for components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin integration including Spring Boot and Ktor examples and cleaner integration with Cardano Client Lib and Yaci, Application runtime foundational components, reactive workers, chain follower, and task scheduler, Reference applications, integration tests, and early-user feedback for the scoped runtime
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, proposer_asserted, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are reused in Cardano developer tooling including MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (adoption, proposer_asserted, high materiality): Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on or use Scalus.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal is a reduced resubmission from a prior ₳8.5M, 12-month proposal, with the standalone L1 node, full L2 integration, and broad formal verification removed from scope.
- finding: Claim (technical, supported_in_proposal, high materiality): Delivery is planned through three quarterly milestones from July 2026 to March 2027, with maintenance running continuously across all milestones.
- missing: Independent evidence for: Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- missing: Independent evidence for: Scalus components are reused in Cardano developer tooling including MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on or use Scalus.
- missing: Independent evidence for: Dijkstra readiness is claimed to be needed because Plutus V4, nested transactions, guard script types, and accounts affect smart contract development, Plutus evaluation, transaction building, ledger rules, testing, and developer workflows.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 2464844
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.86
- missing: sustainability path
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: low
- finding: Technical risk: medium
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal asks for ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 2464844
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal asks for ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- No additional inference.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- Claims and evidence missing: Independent evidence for: Scalus components are reused in Cardano developer tooling including MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `d8820b32f0b052fdc1e0e2ceb693dc90cd8e8974e53c7bb9e53dd19fb22d86f5`
- snapshot_bundle_hash: `c1e32f62dfad02bfe8e0859481f6aeab3bb4875a3ff0fd57a784e238c3b625c8`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2025, "NO": 0.7517, "YES": 0.0458}`

