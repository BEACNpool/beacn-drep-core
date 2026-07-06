# Rationale: gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc
Recommendation: **NO**
Score: `-0.3033` (raw `-0.2833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7958` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit developer infrastructure and includes a reduced scope, exclusions, milestones, and oversight mechanisms, but several high-materiality adoption, governance, and execution claims remain proposer-asserted or only externally checkable rather than evidenced inside the anchor text. Given the large treasury ask and BEACN's caution around spending when evidence is incomplete, a small negative nudge is warranted.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and the evidence record was too thin for several material claims. The proposal had a pinned, replayable anchor and a clear funding request, but treasury spending requires a higher bar because it consumes shared ADA and sets precedent.

The action requested ₳2,464,844 for Lantr Engineering to fund nine months of Scalus work from July 2026 through March 2027. The scope covered maintenance, Dijkstra hard-fork readiness, Java/Kotlin and JS/TS interoperability, documentation, and scoped application runtime components. The proposer also said the scope had been reduced from a prior ₳8.5M proposal, with fewer FTEs and no contingency.

The strongest supported point was the budget itself: the amount, timeframe, reference ADA rate, reduced scope, exclusions, milestone framing, and oversight approach were stated in the proposal. Some adoption figures and ecosystem reuse claims were presented as independently checkable. But important claims remained proposer-asserted or insufficiently evidenced in the review record, including that Scalus is an established open-source platform built over three years of continuous delivery, and that the named Dijkstra changes materially affect the listed developer workflows.

Several gates passed: the proposal could be reviewed, the anchor was available, and the counterargument review found a defensible YES case around the clearly stated budget and scope. But the treasury and risk review remained concerning: the action had medium execution risk, missing sustainability-path analysis, missing independent assurance, missing dependency mapping, and an unsustainable treasury-flow signal. On balance, BEACN judged that the cost and precedent risk outweighed the evidenced benefits, so the vote was NO.

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
- finding: Requested: Fund Scalus 2026 maintenance, Dijkstra hard-fork readiness, interoperability, and a scoped application runtime as shared Cardano infrastructure.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance: bug fixes, dependency upkeep, security patches, and releases, Dijkstra readiness including Plutus V4 support, ledger rules, transaction-builder updates, conformance testing, nested transactions, accounts, and guard scripts, Improved JS/TS interfaces and documentation for components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin interoperability including Spring Boot and Ktor examples and cleaner integration with Cardano Client Lib and Yaci, Scoped application runtime components including foundational components, reactive workers, chain follower, and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,464,844 for a 9-month Scalus continuation from July 2026 to March 2027 with no contingency, using a $0.16/ADA reference rate.
- finding: Claim (technical, proposer_asserted, high materiality): Scalus is described as an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, independently_verifiable, high materiality): The document says Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js has more than 20,000 monthly downloads.
- finding: Claim (adoption, independently_verifiable, high materiality): The proposer states Scalus is used by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, and that its components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal says the 2026 scope was reduced from a prior ₳8.5M 12-month proposal to ₳2.464844M over 9 months, with FTE reduced from 8.25 to 2.25 and contingency reduced from 10% to 0%.
- finding: Claim (technical, supported_in_proposal, medium materiality): The funded scope excludes a standalone L1 node, full L2 integration, broad formal verification, and advanced devnet expansion.
- missing: Independent evidence for: Scalus is described as an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- missing: Independent evidence for: The proposer claims Dijkstra changes such as Plutus V4 support, nested transactions, guard script types, and accounts affect smart contract development, Plutus evaluation, transaction building, ledger rules, testing, and developer workflows.
- missing: Independent evidence for: Delivery is described as milestone-based, administered through audited SundaeSwap treasury contracts with an independent oversight board, third-party assurance, public reporting, and open community sessions.
- missing: Independent evidence for: Lantr Engineering states it has six senior engineers and identifies Alexander Nemish and Oleksii Khodakivskyi as accountable leads with relevant technical and execution backgrounds.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests ₳2,464,844 for a 9-month Scalus continuation from July 2026 to March 2027 with no contingency, using a $0.16/ADA reference rate." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Scalus is described as an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests ₳2,464,844 for a 9-month Scalus continuation from July 2026 to March 2027 with no contingency, using a $0.16/ADA reference rate." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal is aligned with public-benefit developer infrastructure and includes a reduced scope, exclusions, milestones, and oversight mechanisms, but several high-materiality adoption, governance, and execution claims remain proposer-asserted or only externally checkable rather than evidenced inside the anchor text. Given the large treasury ask and BEACN's caution around spending when evidence is incomplete, a small negative nudge is warranted.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Scalus is described as an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- Claims and evidence missing: Independent evidence for: The proposer claims Dijkstra changes such as Plutus V4 support, nested transactions, guard script types, and accounts affect smart contract development, Plutus evaluation, transaction building, ledger rules, testing, and developer workflows.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `a8199f9038b89f9272854888571a85377b395332fa283a35e902454390ff8767`
- snapshot_bundle_hash: `f45cfe4ace695173bf74ce59ed5637b57a95a8c2e5c9f8e33950825dd2caeb8b`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1982, "NO": 0.7569, "YES": 0.0449}`

