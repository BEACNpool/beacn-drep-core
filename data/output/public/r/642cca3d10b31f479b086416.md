# Rationale: 3234567a3f48ace25efc150f1369192615974e232ea06e0251701831d9e4486d#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.56` (binding treasury composite; advisory raw signal `-0.56`; LLM lean `+0.02` recorded, not added) | Confidence: `0.82` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims show a materially reduced ask, narrower scope, no contingency, milestone framing, escrow/oversight language, and open-source public-infrastructure alignment; however, adoption and track-record claims are mostly proposer-asserted in the supplied document, so the adjustment should remain small.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work.

The proposal requests ₳2,464,844 over 9 months for Scalus 2026 maintenance, Dijkstra readiness, interoperability, and a scoped application runtime, with delivery through March 2027 by Lantr Engineering. The proposal’s budget claim is well-supported in the supplied materials: it states the amount, the 9-month term, the $394,375 reference value at $0.16/ADA, and no contingency. The reduced scope versus the prior ₳8.503M request is also supported in the proposal, including the smaller team size and narrower deliverables.

Several important claims were only proposer-asserted or thinly evidenced in the supplied review. These include Scalus having three years of continuous delivery, its direct and indirect adoption by named Cardano projects and tools, and the reported commit, release, contributor, and download figures. The review also notes missing or unresolved treasury and risk information, including a sustainability path, independent assurance, and a dependency map.

The review gates established that the proposal anchor is pinned and replayable, the execution risk is medium, and the best YES case is that the proposal has a materially reduced ask, narrower scope, no contingency, milestone framing, oversight language, and open-source infrastructure alignment. But because treasury actions require elevated scrutiny, BEACN needs the verified Net Change Limit, plus stronger independent evidence for the major technical and adoption claims, before it can cast a directional YES or NO vote.

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
- finding: Requested: Scalus 2026 maintenance, Dijkstra readiness, interoperability, and first scoped application runtime over 9 months
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance: bug fixes, dependency upkeep, security patches, and releases, Dijkstra hard-fork readiness including Plutus V4 support, transaction-building, ledger-rule, emulation, testing, conformance, nested transactions, accounts, guard scripts, and cost-model updates, Improved JS/TS interfaces and documentation for Scalus components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin interoperability with examples for Spring Boot and Ktor and cleaner integration with Cardano Client Lib and Yaci, Application runtime foundational components including reactive workers, chain follower, task scheduler, backend workflows, and recovery-oriented operating capabilities
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, proposer_asserted, high materiality): Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency.
- finding: Claim (technical, supported_in_proposal, high materiality): The funded scope is limited to maintenance, Dijkstra hard-fork readiness, interoperability, and a scoped application runtime, while excluding a standalone L1 node, full L2 integration, broad formal verification, and advanced devnet expansion.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, and indirectly through MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states Scalus has 4,642 commits, 32 releases, 12 contributors, and 20,000+ monthly Scalus.js downloads.
- finding: Claim (economic, supported_in_proposal, high materiality): The resubmission reduces the prior proposal from ₳8.503M over 12 months to about ₳2.465M over 9 months, reduces FTE from 8.25 to 2.25, and removes a 10% contingency.
- missing: Independent evidence for: Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- missing: Independent evidence for: The proposal states that Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, and indirectly through MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: The proposal states Scalus has 4,642 commits, 32 releases, 12 contributors, and 20,000+ monthly Scalus.js downloads.
- missing: Independent evidence for: Delivery is described as milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
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
- finding: Strongest YES: the proposal substantiates "The proposal asks for ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal asks for ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims show a materially reduced ask, narrower scope, no contingency, milestone framing, escrow/oversight language, and open-source public-infrastructure alignment; however, adoption and track-record claims are mostly proposer-asserted in the supplied document, so the adjustment should remain small.
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
- Claims and evidence missing: Independent evidence for: The proposal states that Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, and indirectly through MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `bf0b8a68c385e6a287025fc97776751f525285de53f0a363affdcb2919fd7e56`
- snapshot_bundle_hash: `f41087efe0649870683bdf9ad4dfbea679af1de34e2ac00ecdd4569455fd6b1e`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4158, "NO": 0.5446, "YES": 0.0396}`

