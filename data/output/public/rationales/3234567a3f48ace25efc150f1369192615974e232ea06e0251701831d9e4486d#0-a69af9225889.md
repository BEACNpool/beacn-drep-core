# Rationale: 3234567a3f48ace25efc150f1369192615974e232ea06e0251701831d9e4486d#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.56` (raw `-0.56` + doctrine-LLM nudge `+0.02`) | Confidence: `0.82` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims show a narrowed resubmission, explicit exclusions of higher-risk scope, milestone-based delivery controls, and a public-infrastructure framing with claimed ecosystem reuse; however, the nudge remains small because key adoption, governance, and prior-delivery claims are mostly proposer-asserted rather than evidenced inside the document.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work.

The proposal asks for ₳2,464,844 to fund a 9-month continuation of Scalus through March 2027, covering maintenance, Dijkstra readiness, interoperability across JVM and JS/TS ecosystems, and foundational application runtime components. The proposal is narrowed from a prior larger request, excludes several higher-risk scope items, and describes milestone-based delivery controls. It also substantiates that Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.

The review found several important claims were still not independently supported inside the available evidence. In particular, the claimed reuse of Scalus components in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit needs replayable independent evidence. The same is true for claims that protocols and applications such as Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus. The review also noted thin claims-and-evidence coverage, missing treasury sustainability-path analysis, and missing risk evidence for independent assurance and the dependency map.

Because this is a treasury withdrawal, BEACN applies elevated scrutiny: spending shared ADA requires stronger public evidence than ordinary proposer assertions. A directional vote would be unblocked by a pinned, independently verified Net Change Limit from public chain evidence, plus independent evidence for the major adoption and reuse claims and clearer support for the missing treasury and risk-review items.

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
- finding: Requested: Fund a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance including bug fixes, dependency upkeep, security patches, and releases, Dijkstra developer preview with initial Plutus V4 support in the compiler and standard library, Dijkstra ledger rules and transaction-builder updates including new builtins, cost models, nested transactions, accounts, and guard scripts with conformance testing, Improved JS/TS interfaces and documentation for Scalus components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin integration including Spring Boot and Ktor examples and cleaner integration paths with Cardano Client Lib and Yaci, Application runtime foundational components, reactive workers, chain follower, and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (adoption, proposer_asserted, high materiality): Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js reaches more than 20,000 downloads per month.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is ₳2,464,844 for 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): This resubmission reduces the previous proposal from ₳8,503,000 over 12 months to about ₳2,464,844 over 9 months and reduces FTE from 8.25 to 2.25.
- missing: Independent evidence for: Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- missing: Independent evidence for: Delivery is described as milestone-based through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- missing: Independent evidence for: Lantr Engineering says every prior milestone was delivered on time and commits to public reporting, open community sessions, and on-time milestone delivery for treasury-funded work.
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
- finding: Strongest YES: the proposal substantiates "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims show a narrowed resubmission, explicit exclusions of higher-risk scope, milestone-based delivery controls, and a public-infrastructure framing with claimed ecosystem reuse; however, the nudge remains small because key adoption, governance, and prior-delivery claims are mostly proposer-asserted rather than evidenced inside the document.
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
- Claims and evidence missing: Independent evidence for: Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- Claims and evidence missing: Independent evidence for: Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `a69af9225889e6bc92f1f54fb0810dd1e7d18b3a6cadb20f848cc6b9cf063416`
- snapshot_bundle_hash: `0dd015e76a179a00786275f4fd90be341c59fa3dcedd743f760f06c7473a41a6`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4158, "NO": 0.5446, "YES": 0.0396}`

