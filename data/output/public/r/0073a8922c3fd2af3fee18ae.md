# Rationale: gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc
Recommendation: **NO**
Score: `-0.4033` (raw `-0.3833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.67` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is detailed, scoped down from a larger prior ask, and frames public-benefit developer infrastructure with milestone delivery, but several high-materiality adoption and governance claims are asserted rather than evidenced inside the anchor text, and the deterministic assessment marks treasury analysis incomplete. Under a treasury-stewardship standard, this supports only a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury request asks for a large withdrawal of shared ADA while several material adoption and governance claims were not independently evidenced in the review record, and the treasury analysis was incomplete.

The action requested ₳2,464,844 for a 9-month continuation of Scalus by Lantr Engineering, covering maintenance, Dijkstra readiness, JVM and JS/TS interoperability, and initial application runtime work through March 2027. The proposal described Scalus as an established open-source Cardano development platform with three years of continuous delivery, and that core claim was treated as well-supported. It also stated that the request was reduced from a prior ₳8,503,000 over 12 months to about ₳2,464,844 over 9 months, with the team reduced from 8.25 to 2.25 FTE.

The concern was not that the proposal lacked substance. The review found a pinned, replayable anchor document, a clearer scoped-down request, and a credible YES case around Scalus as public-benefit developer infrastructure. But several high-materiality claims remained proposer-asserted rather than independently supported in the supplied evidence, including claimed use by or support for Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, and claimed reuse across MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.

Because this is a treasury withdrawal, BEACN applied elevated scrutiny. The review marked execution risk as medium, the claims-and-evidence record as thin, treasury analysis as incomplete, and noted missing items including a sustainability path, independent assurance, and a dependency map. With those gaps, plus the advisory treasury-flow penalty, the evidence did not clear the bar for spending this amount of shared ADA, so BEACN voted NO.

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
- finding: Deep research dossier: required
- finding: Requested: Funding for a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a first scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance: bug fixes, dependency upkeep, security patches, and releases, Initial Plutus V4 support in the compiler and standard library, Improved interfaces and documentation for JS/TS components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Foundational runtime components and reactive workers, Dijkstra ledger rules and transaction-builder updates for new builtins, cost models, nested transactions, accounts, and guard scripts, Conformance testing for Dijkstra changes, Java/Kotlin integration including Spring Boot and Ktor examples, Cleaner integration paths with Cardano Client Lib and Yaci, Runtime chain follower and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says Scalus is used by or underpins Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal states Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js has more than 20,000 monthly downloads.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested funding is ₳2,464,844 for 9 months, stated as approximately $394,375 at a $0.16/ADA reference rate with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal says this resubmission reduces the prior request from ₳8,503,000 over 12 months to about ₳2,464,844 over 9 months and reduces FTE from 8.25 to 2.25.
- missing: Independent evidence for: The proposal says Scalus is used by or underpins Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- missing: Independent evidence for: The proposal says Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: The proposal says Dijkstra readiness is needed because Plutus V4, nested transactions, guard script types, and accounts affect smart contract development, Plutus evaluation, transaction building, ledger rules, testing, and developer workflows.
- missing: Independent evidence for: Delivery is described as milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
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
- finding: Strongest NO: a material claim is unsupported — "The proposal says Scalus is used by or underpins Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
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
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal is detailed, scoped down from a larger prior ask, and frames public-benefit developer infrastructure with milestone delivery, but several high-materiality adoption and governance claims are asserted rather than evidenced inside the anchor text, and the deterministic assessment marks treasury analysis incomplete. Under a treasury-stewardship standard, this supports only a small cautionary nudge rather than a positive adjustment.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal says Scalus is used by or underpins Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- Claims and evidence missing: Independent evidence for: The proposal says Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `72dd61f0bcfdeb62eeea86b209fd6ace09342b1e26ed0bdf582e6319e7437144`
- snapshot_bundle_hash: `b5370aa8f2d1631e837cd257b07f4909431f37be11c2641d34c680343919c6cb`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `30`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1974, "NO": 0.7609, "YES": 0.0418}`

