# Rationale: gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7808` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit developer infrastructure and includes a narrower scope, milestone framing, and some independently checkable adoption indicators, but several high-materiality claims about direct usage, governance controls, and prior delivery are asserted rather than evidenced inside the document. Given the large treasury request and BEACN's caution around evidence quality and treasury stewardship, a small negative nudge is warranted rather than a positive spending lean.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for ₳2,464,844 to fund nine more months of Scalus work by Lantr Engineering, covering maintenance, Dijkstra hard-fork readiness, JVM and JS/TS interoperability, and a scoped application runtime through March 2027. The proposer says Scalus is an established open-source Cardano development platform with three years of delivery, a reduced scope compared with the prior ₳8.503 million request, milestone-based delivery, public reporting, and ecosystem use across several projects and libraries.

Some parts were well supported in the review: the action has a pinned, replayable proposal anchor; the budget, duration, reduced scope, and core technical purpose were clear; and the strongest case for support is that Scalus appears to be established open-source developer infrastructure. But several high-materiality claims were still only asserted rather than independently evidenced inside the review, including direct usage by named projects, reuse in named ecosystem libraries, the governance controls around audited SundaeSwap treasury contracts and oversight, and the record of prior on-time delivery.

This is a conservative, evidence-based hold, not a rejection of the work. To unblock a directional vote, BEACN would need the applicable Net Change Limit pinned and independently verified from public chain evidence, plus stronger replayable evidence for the major adoption and governance-control claims, along with clearer treasury sustainability, independent assurance, and dependency-map information.

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
- finding: Requested: Funding for a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance: bug fixes, dependency upkeep, security patches, and releases, Dijkstra readiness including Plutus V4 support, ledger rules, transaction-builder updates, conformance testing, nested transactions, accounts, and guard scripts, Improved JS/TS interfaces and documentation for components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin interoperability including Spring Boot and Ktor examples and cleaner integration with Cardano Client Lib and Yaci, Foundational runtime components including reactive workers, chain follower, and task scheduler, Reference applications, integration tests, early-user feedback, public reporting, third-party assurance, and milestone-based delivery
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, and its components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,464,844 for 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal is a reduced resubmission of a prior Scalus proposal, cutting the ask from ₳8.503 million to about ₳2.465 million, reducing duration from 12 to 9 months, reducing FTE from 8.25 to 2.25, and removing the standalone L1 node, full L2 integration, and broad formal verification from scope.
- finding: Claim (governance, proposer_asserted, high materiality): Delivery is proposed to be milestone-based through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal says Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js reaches more than 20,000 monthly downloads.
- missing: Independent evidence for: Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, and its components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: Delivery is proposed to be milestone-based through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- missing: Independent evidence for: Dijkstra readiness is presented as necessary because the hard fork introduces Plutus V4 support, nested transactions, guard script types, and accounts affecting smart contract development, evaluation, transaction building, ledger rules, testing, and workflows.
- missing: Independent evidence for: Lantr Engineering says it has delivered every prior Scalus milestone on time and commits to public reporting, open community sessions, and on-time milestone delivery for treasury-funded work.
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
- finding: Strongest NO: a material claim is unsupported — "Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, and its components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit." — so cost or precedent may outweigh the benefit.
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
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal is aligned with public-benefit developer infrastructure and includes a narrower scope, milestone framing, and some independently checkable adoption indicators, but several high-materiality claims about direct usage, governance controls, and prior delivery are asserted rather than evidenced inside the document. Given the large treasury request and BEACN's caution around evidence quality and treasury stewardship, a small negative nudge is warranted rather than a positive spending lean.
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
- Claims and evidence missing: Independent evidence for: Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, and its components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- Claims and evidence missing: Independent evidence for: Delivery is proposed to be milestone-based through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `b02a109afc6b522ac3daf4dc1c28c8ed8e5ab931ffdfa33f0317fef319c49fb4`
- snapshot_bundle_hash: `8a20183e25f7d5eba24d637ddcee30d298eba12cce959dc5903e092df5b6f72e`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

