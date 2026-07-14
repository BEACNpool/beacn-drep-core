# Rationale: 3234567a3f48ace25efc150f1369192615974e232ea06e0251701831d9e4486d#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.56` (raw `-0.56` + doctrine-LLM nudge `+0.0`) | Confidence: `0.82` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show plausible public-benefit infrastructure alignment and a materially reduced ask, but several high-materiality adoption, escrow, oversight, and delivery-record claims remain proposer-asserted or only externally checkable rather than evidenced inside the document. The deterministic assessment already marked the case ready, so the bounded reasoning layer should not add an extra spending-positive or spending-negative adjustment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work.

The proposal requests ₳2,464,844 for a 9-month continuation of Scalus by Lantr Engineering, covering maintenance, Dijkstra readiness, interoperability across JVM/JS/TS tooling, and foundational application runtime components through March 2027. The proposal supported the budget claim: ₳2,464,844 over 9 months, about $394,375 at a $0.16/ADA reference rate, with no contingency. It also supported that this resubmission is smaller than the prior ₳8,503,000 request and excludes larger items such as a production-grade JVM L1 node, full Gummiworm L2 integration, broad formal verification, and advanced devnet expansion.

Several important claims remained only proposer-asserted or thinly evidenced. Independent evidence was missing for the claim that Scalus is an open-source Cardano development platform built over three years of continuous delivery, and for the claim that it is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm. Adoption metrics such as 4,642 commits, 32 releases, 12 contributors, and more than 20,000 monthly Scalus.js downloads were treated as independently verifiable, but the broader claims-and-evidence status was still thin.

The review found a pinned, replayable proposal anchor and recognized a credible strongest YES case around the substantiated budget and reduced scope. But treasury withdrawals require elevated scrutiny because they spend shared ADA and set precedent. The hold would be unblocked by a pinned, independently verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the unsupported Scalus history and adoption claims, a sustainability path, independent assurance, and a dependency map.

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
- finding: Requested: Fund a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, JVM/JS/TS interoperability, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing Scalus maintenance including bug fixes, dependency upkeep, security patches, and releases, Dijkstra developer preview including initial Plutus V4 support in the compiler and standard library, Dijkstra ledger-rule and transaction-builder updates including new builtins, cost models, nested transactions, accounts, and guard scripts with conformance testing, Improved JS/TS interfaces and documentation for Scalus components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin integration including Spring Boot and Ktor examples and cleaner Cardano Java stack integration with CCL and Yaci, Foundational application runtime components including reactive workers, chain follower, and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, proposer_asserted, high materiality): Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate with no contingency.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components for script evaluation, cost calculation, and in-memory Cardano node emulation are embedded in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- finding: Claim (adoption, independently_verifiable, medium materiality): Scalus has had 4,642 commits across 32 releases with 12 contributors, and Scalus.js reaches more than 20,000 downloads per month.
- finding: Claim (economic, supported_in_proposal, high materiality): The resubmission reduces the previous proposal from ₳8,503,000 over 12 months to about ₳2,464,844 over 9 months and reduces FTE from 8.25 to 2.25.
- missing: Independent evidence for: Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- missing: Independent evidence for: Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- missing: Independent evidence for: Scalus components for script evaluation, cost calculation, and in-memory Cardano node emulation are embedded in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- missing: Independent evidence for: Delivery is milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.82
- missing: sustainability path
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
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
- finding: Strongest YES: the proposal substantiates "The proposal asks for ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate with no contingency." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal asks for ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate with no contingency." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
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
- Claims and evidence missing: Independent evidence for: Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- Claims and evidence missing: Independent evidence for: Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `7c3ae7de239b7e9c39c5a26ca22431a6bff400bd17b6cd88c33032745afb08b7`
- snapshot_bundle_hash: `a5ae00add887f4e43b895a13c4f0fc3e041772b532991fbc57ca3eada90ea935`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4158, "NO": 0.5446, "YES": 0.0396}`

