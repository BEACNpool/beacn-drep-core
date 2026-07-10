# Rationale: gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7808` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is materially more bounded than the prior version and gives concrete milestone themes, exclusions, budget, and governance mechanisms, but several key adoption, delivery-record, and assurance claims are asserted rather than evidenced inside the anchor text. Given the large treasury withdrawal and BEACN's emphasis on evidence quality and treasury stewardship, the bounded lean should apply a small cautionary nudge rather than reward plausible ecosystem upside.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal requests ₳2,464,844 over 9 months for Scalus 2026 work by Lantr Engineering, covering maintenance, Dijkstra hard-fork readiness, JVM and JS/TS interoperability, runtime foundations, ledger-rule and transaction-builder updates, conformance testing, and integration examples, with delivery organized into three quarterly milestones through March 2027. The proposer says this is a reduced resubmission from a prior ₳8.503M proposal, with several larger items removed from scope, and that the work would use milestone-based treasury administration with oversight and assurance.

Several parts of the case were strong enough to review: the anchor document was pinned and replayable, the budget and timeline were stated, the proposal clearly described a narrower scope than the prior version, and the claim that Scalus is an established open-source Cardano development platform built over three years was supported in the proposal. But key adoption and assurance claims were still not independently evidenced in the supplied review, including claims that Scalus is used by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, and that Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by pinned, independently verifiable Net Change Limit evidence from public chain data, plus stronger replayable evidence for the major adoption and reuse claims, the sustainability path, independent assurance, and the dependency map.

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
- finding: Requested: Scalus 2026 maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS, and a scoped application runtime continuation over 9 months.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance: bug fixes, dependency upkeep, security patches, and releases, Dijkstra developer preview with initial Plutus V4 support in the compiler and standard library, Improved interfaces and documentation for JS/TS components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Runtime foundational components and reactive workers, Dijkstra ledger rules and transaction-builder updates including new builtins, cost models, nested transactions, accounts, and guard scripts with conformance testing, Java/Kotlin integration examples for Spring Boot and Ktor and cleaner integration paths with Cardano Client Lib and Yaci, Runtime chain follower and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus is used directly by projects including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for ₳2,464,844 over 9 months, approximately $394,375 at a $0.16/ADA reference rate, with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): This proposal is a reduced resubmission from a prior ₳8.503M 12-month proposal, removing the standalone L1 node, full L2 integration, broad formal verification, and advanced devnet expansion from scope.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js has more than 20,000 downloads per month.
- missing: Independent evidence for: Scalus is used directly by projects including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- missing: Independent evidence for: Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: Delivery is described as milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- missing: Independent evidence for: Lantr Engineering says every prior Scalus milestone was delivered on time and commits to public reporting, open community sessions, and on-time milestone delivery for treasury-funded work.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 2464844
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest NO: a material claim is unsupported — "Scalus is used directly by projects including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal is materially more bounded than the prior version and gives concrete milestone themes, exclusions, budget, and governance mechanisms, but several key adoption, delivery-record, and assurance claims are asserted rather than evidenced inside the anchor text. Given the large treasury withdrawal and BEACN's emphasis on evidence quality and treasury stewardship, the bounded lean should apply a small cautionary nudge rather than reward plausible ecosystem upside.
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
- Claims and evidence missing: Independent evidence for: Scalus is used directly by projects including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- Claims and evidence missing: Independent evidence for: Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `b02a109afc6b522ac3daf4dc1c28c8ed8e5ab931ffdfa33f0317fef319c49fb4`
- snapshot_bundle_hash: `5e168cf538a48178048693c2c9adad25b3bd2c52c79f4de3e8ad2389023d9d9a`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

