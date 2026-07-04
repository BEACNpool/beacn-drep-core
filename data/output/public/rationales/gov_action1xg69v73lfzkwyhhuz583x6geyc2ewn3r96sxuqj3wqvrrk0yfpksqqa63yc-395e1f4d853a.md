# Rationale: gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc
Recommendation: **NO**
Score: `-0.3033` (raw `-0.2833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7958` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit ecosystem infrastructure and narrows scope from a prior larger ask, but several high-materiality adoption, governance, and track-record claims are asserted in the document rather than evidenced or externally anchored in the supplied text. Given the treasury size and BEACN's caution-first posture for unverifiable treasury upside, a small negative nudge is warranted.

## Plain-language explanation (precomputed)
BEACN voted NO because this is a large treasury withdrawal and several material claims behind the expected public benefit were not independently evidenced in the supplied review record.

The proposal requested ₳2,464,844 for nine months of Scalus work by Lantr Engineering, through March 2027. The requested scope included ongoing maintenance, Dijkstra hard-fork readiness, Plutus V4 support, interoperability work for JS/TS and Java/Kotlin ecosystems, and foundational application runtime components. The proposal also stated that this was a reduced resubmission from a much larger prior request, with the standalone L1 node, full L2 integration, broader formal verification, and advanced devnet expansion removed from scope.

Some parts were well supported in the proposal: the amount, duration, ADA reference rate, lack of contingency, quarterly milestone structure, and the narrowed scope compared with the earlier request. But several high-materiality claims were only proposer assertions in the supplied data, including Scalus’s three-year open-source delivery history, direct use by named projects, reuse in major SDKs, monthly download numbers, and commit/release/contributor history. For a treasury action, proposer assertions alone were not enough to support confidence in the claimed ecosystem upside.

The review found a pinned, replayable anchor document and recognized the strongest YES case: the budget request was clearly stated and the proposal cleared basic evidence gates. But treasury withdrawals require elevated scrutiny because they spend shared ADA and set precedent. The review also noted medium execution risk, thin claims-and-evidence status, missing sustainability path, missing independent assurance, missing dependency map, and an advisory treasury-flow penalty. On balance, BEACN judged that the cost and precedent outweighed the verified evidence available, so the deterministic vote was NO.

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
- finding: Requested: Treasury withdrawal to fund Scalus 2026 maintenance, Dijkstra readiness, interoperability, and a scoped application runtime over 9 months.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing Scalus maintenance including bug fixes, dependency upkeep, security patches, and releases, Dijkstra hard-fork readiness including Plutus V4 support, ledger rules, transaction-builder updates, nested transactions, accounts, guard scripts, cost models, and conformance testing, Improved JS/TS interfaces and documentation for Scalus components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin interoperability including Spring Boot and Ktor examples and cleaner integration with Cardano Client Lib and Yaci, Foundational application runtime components including reactive workers, chain follower, and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, proposer_asserted, high materiality): Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,464,844 for 9 months at a $0.16/ADA reference rate with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal is a reduced resubmission from a prior ₳8,503,000, 12-month proposal, removing the standalone L1 node, full L2 integration, broad formal verification, and advanced devnet expansion from scope.
- finding: Claim (governance, supported_in_proposal, high materiality): The funded work is organized into quarterly milestones from July 2026 through March 2027.
- missing: Independent evidence for: Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- missing: Independent evidence for: Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- missing: Independent evidence for: Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: Delivery will be milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests ₳2,464,844 for 9 months at a $0.16/ADA reference rate with no contingency." and clears the evidence gates.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2464844
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests ₳2,464,844 for 9 months at a $0.16/ADA reference rate with no contingency." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal is aligned with public-benefit ecosystem infrastructure and narrows scope from a prior larger ask, but several high-materiality adoption, governance, and track-record claims are asserted in the document rather than evidenced or externally anchored in the supplied text. Given the treasury size and BEACN's caution-first posture for unverifiable treasury upside, a small negative nudge is warranted.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- Claims and evidence missing: Independent evidence for: Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `395e1f4d853a21bf2b13f9a519d479bcd669d5ce6359102bbce4c2c0e22af008`
- snapshot_bundle_hash: `fa56dd6fc35b594ec71502a1f784cad5f0996e5828c602c6a4ad2d5a789cb08d`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1982, "NO": 0.7569, "YES": 0.0449}`

