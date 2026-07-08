# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#6
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was missing baseline evidence needed to responsibly judge a treasury withdrawal. This is a conservative, evidence-based hold, not a rejection of the tools or the proposer’s goals.

The action requested 1,162,746 ada in annual treasury funding for MLabs Core Tool Maintenance & Enhancement, covering Plutarch and Ply maintenance, compatibility work, bug fixes, optimizations, documentation, and developer-experience improvements. The proposal said Plutarch is a Haskell eDSL for efficient Cardano smart contracts and that Ply handles CIP-57 blueprint-style artifacts; that technical description was supported. It also claimed broad ecosystem use, Cardano 2030 alignment, budget-process support, Net Change Limit compliance, prior funding disclosures, and smart-contract-based administration through Intersect-related treasury controls.

The review found some claims supported or independently verifiable, including the technical description of Plutarch and Ply, the broad quarterly maintenance model, the stated total budget split, and the proposal anchor being pinned and replayable. But key claims were still unsupported or thin, including independent evidence for adoption numbers and for the governance-alignment claim. More importantly, required review areas were incomplete: the treasury amount in lovelace was missing for a treasury withdrawal, and the review lacked a complete proposal summary, budget analysis, feasibility assessment, risk analysis, alternatives analysis, failure-mode analysis, and community impact analysis.

Because this spends shared treasury ada and creates precedent, BEACN would need the missing baseline fields, a complete line-item budget, milestone-gated disbursement evidence, mitigation evidence, independent assurance, and the missing analyses before casting a directional YES or NO vote. Without that, voting either way would require pretending to have confidence the review did not support.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Annual treasury funding for MLabs Core Tool Maintenance & Enhancement covering Plutarch and Ply maintenance, compatibility, and developer-experience work.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v for administration on behalf of the vendor MLabs.
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience, Critical breakage and serious vulnerability response, Protocol-era and hard-fork compatibility work, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, proposer_asserted, high materiality): MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, with a recent internal audit counting at least 26 teams in the motivation section and at least 15 teams in the rationale section.
- finding: Claim (technical, independently_verifiable, medium materiality): MLabs says public cross-language benchmarks show Plutarch scripts rank among the smallest in the benchmark suite while requiring comparatively low on-chain compute and memory.
- finding: Claim (technical, supported_in_proposal, high materiality): The requested work is organized around a quarterly maintenance model prioritizing critical breakages, protocol-era compatibility, bug fixes and optimizations, then documentation and developer-experience improvements.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal states it aligns with Cardano 2030 Pillar 2: Adoption & Utility by supporting developer experience and maintenance of open-source SDKs, frameworks, and infrastructure.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, with a recent internal audit counting at least 26 teams in the motivation section and at least 15 teams in the rationale section.
- missing: Independent evidence for: The proposal states it aligns with Cardano 2030 Pillar 2: Adoption & Utility by supporting developer experience and maintenance of open-source SDKs, frameworks, and infrastructure.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.64
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, with a recent internal audit counting at least 26 teams in the motivation section and at least 15 teams in the rationale section." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: MLabs says Plutarch and Ply have been extensively used in the Cardano ecosystem, with a recent internal audit counting at least 26 teams in the motivation section and at least 15 teams in the rationale section.
- Claims and evidence missing: Independent evidence for: The proposal states it aligns with Cardano 2030 Pillar 2: Adoption & Utility by supporting developer experience and maintenance of open-source SDKs, frameworks, and infrastructure.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `1d381a937296828f683af6685a898d8b206b68b71b5cb8d1cbb46f580720b32c`
- snapshot_bundle_hash: `21caecc4458c5b193a3fd0270765cf1dd52bba05ab03441c1f7b43e109a33722`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `2`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

