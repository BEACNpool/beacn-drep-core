# Rationale: gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc
Recommendation: **NO**
Score: `-0.3033` (raw `-0.2833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7958` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit ecosystem growth through open-source infrastructure and has a narrower, milestone-based scope than the prior version, but several high-materiality adoption, governance, and delivery-record claims are asserted rather than evidenced inside the supplied document. Given the substantial treasury request, the doctrine favors a small cautionary nudge where treasury stewardship and evidence quality remain only partly supported.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury request and several material claims about adoption, governance, and delivery support were asserted rather than independently evidenced in the supplied review.

The action requested ₳2,464,844 for a 9-month continuation of Scalus by Lantr Engineering, covering maintenance, Dijkstra readiness, JVM and JS/TS interoperability, and a scoped application runtime, with a March 2027 deadline. The proposal framed Scalus as established Apache 2.0 open-source Cardano infrastructure, said it has been built over three years of continuous delivery, and stated that the new scope was narrower than a prior ₳8.5M proposal by removing items such as a production-grade JVM L1 node, full L2 integration, broad formal verification, and advanced devnet expansion.

The review found some important claims well-supported in the proposal: the basic scope, budget, open-source framing, Dijkstra-related work, maintenance plan, and the fact that Scalus is an established Cardano development platform. It also found a pinned, replayable anchor document, which allowed the proposal to be reviewed. But high-materiality adoption claims were not independently evidenced in the supplied data, including claims that Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems, and that components are embedded in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.

Because this is a treasury withdrawal, BEACN applied a higher evidence bar. The review also noted medium execution risk, thin claims-and-evidence status, missing sustainability-path analysis, missing independent assurance, and a missing dependency map. The strongest YES case was that Scalus appears to be real, open-source infrastructure with a narrower milestone-based scope than before. But for this amount of shared ADA, BEACN’s evidence standard required stronger independent support for the adoption and risk-control claims, so the final vote was NO.

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
- finding: Requested: Funding for a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, JVM and JS/TS interoperability, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance including bug fixes, dependency upkeep, security patches, and releases, Initial Plutus V4 support in the compiler and standard library for a Dijkstra developer preview, Improved interfaces and documentation for JS/TS components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Runtime foundational components and reactive workers, Dijkstra ledger rules and transaction-builder updates including new builtins, cost models, nested transactions, accounts, and guard scripts, Conformance testing for Dijkstra changes, Java/Kotlin integration with Spring Boot and Ktor examples, Cleaner integration paths with Cardano Client Lib and Yaci, Runtime chain follower and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are embedded in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js receives more than 20,000 downloads per month.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is ₳2,464,844 for 9 months, based on a $0.16/ADA reference rate and no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): This resubmission reduces the prior proposal from ₳8.5M over 12 months to about ₳2.464M over 9 months and removes the standalone L1 node, full L2 integration, and broad formal verification from scope.
- missing: Independent evidence for: Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems.
- missing: Independent evidence for: Scalus components are embedded in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- missing: Independent evidence for: The proposal says delivery will be milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- missing: Independent evidence for: Lantr Engineering says it previously delivered every Scalus milestone on time and commits to public reporting, community sessions, and on-time milestone delivery for this treasury-funded work.
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
- finding: Strongest YES: the proposal substantiates "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal is aligned with public-benefit ecosystem growth through open-source infrastructure and has a narrower, milestone-based scope than the prior version, but several high-materiality adoption, governance, and delivery-record claims are asserted rather than evidenced inside the supplied document. Given the substantial treasury request, the doctrine favors a small cautionary nudge where treasury stewardship and evidence quality remain only partly supported.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems.
- Claims and evidence missing: Independent evidence for: Scalus components are embedded in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `f35b25e1d29c7195fa785462822a7e4a0ec4e065736ca9d0d7cba7f342e7bc91`
- snapshot_bundle_hash: `da9ec186b6f5dfaf27f8651d9b531871a620287579ed3fed3e37319f17bf73e1`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1982, "NO": 0.7569, "YES": 0.0449}`

