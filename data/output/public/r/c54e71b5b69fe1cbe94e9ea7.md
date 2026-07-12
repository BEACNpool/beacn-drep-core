# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#8
Recommendation: **NEEDS_MORE_INFO**
Score: `0.2084` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7721` | Readiness: `0.75`
> Reasoning layer (precomputed): A small positive nudge is justified because the extracted claims indicate public-benefit core infrastructure with checkable adoption metrics, named downstream users, explicit deliverables, NCL compliance assertions, and independently verifiable treasury-management infrastructure; the nudge remains small because several important execution and prior-delivery claims are still proposer asserted.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Pallas or TxPipe.

The proposal requests 540,750 ada for Year 2 maintenance of Pallas, including core Rust library upkeep, community support, and AI-friendly documentation and integration resources over 12 months. The proposal supports several important claims: the budget total is broken into 420,000 ada, a 105,000 ada contingency reserve, and a 15,750 ada Intersect administration fee; Pallas is described as core Cardano Rust infrastructure; the work scope is clear; and public GitHub, crates.io, voting, audit, and treasury-management references were supplied for verification.

However, some material claims remain unsupported or thinly evidenced. The proposal says Pallas is used by Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others, but that downstream-use claim still needs independent evidence. The proposal also says TxPipe has 30 Project Catalyst proposals, with 26 delivered and 4 on schedule, but that prior-delivery claim remains proposer asserted. The review also found missing or incomplete evidence around a line-item budget, sustainability path, independent assurance, and rollback or remedy path.

The review gates were strong enough to show this proposal is reviewable, has a pinned and replayable anchor document, has low execution risk, and includes a credible strongest-YES case for public-benefit infrastructure. But because treasury actions spend shared ada and require elevated scrutiny, BEACN needs independently pinned Net Change Limit evidence, plus stronger independent support for the unresolved material claims, before casting a YES or NO vote.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 540.8k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Pallas by TxPipe: Maintaining Cardano's Core Rust Libraries, Year 2, including maintenance, community support, and AI-friendly documentation and integration resources over 12 months.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor TxPipe
- finding: Stated amount: 540,750
- finding: Deliverables: Essential maintenance of the Pallas codebase including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation., Community support including issue triage, review of external contributions, enhancements driven by ecosystem feedback, and public communication., Upgrade Pallas compatibility with AI-driven development workflows through AI-friendly documentation and integration resources.
- finding: Deadline/expiry: 12 months; new grant period begins after closure of existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): Pallas is described as a collection of Rust crates re-implementing core Ouroboros and Cardano primitives including CBOR encoding, cryptographic operations, networking, ledger traversal, transaction building, and address handling.
- finding: Claim (adoption, proposer_asserted, high materiality): The document states that Pallas is used by Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC and other ecosystem projects.
- finding: Claim (adoption, independently_verifiable, high materiality): The document reports Pallas has over 649 pull requests, 199 stars, 91 forks, 60 contributors, and 214,446 crates.io downloads, with GitHub and crates.io links supplied for verification.
- finding: Claim (technical, supported_in_proposal, high materiality): The requested work covers maintenance, community support, and AI-friendly documentation and integration resources for Pallas.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting and audit materials.
- missing: Independent evidence for: The document states that Pallas is used by Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC and other ecosystem projects.
- missing: Independent evidence for: The document states TxPipe has received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development and on schedule.
- missing: Independent evidence for: The document states independent oversight will be provided through Intersect and technically capable third parties, including reporting obligations and milestone-based disbursement controls.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.55
- missing: line-item budget
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: low
- finding: Governance risk: medium
- finding: Technical risk: low
- finding: Treasury exposure risk: low
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The document states that Pallas is used by Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC and other ecosystem projects." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 540750
- Risk review: Execution risk: low
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the extracted claims indicate public-benefit core infrastructure with checkable adoption metrics, named downstream users, explicit deliverables, NCL compliance assertions, and independently verifiable treasury-management infrastructure; the nudge remains small because several important execution and prior-delivery claims are still proposer asserted.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The document states that Pallas is used by Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC and other ecosystem projects.
- Claims and evidence missing: Independent evidence for: The document states TxPipe has received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `9c050d8c018198c9096ce54daefa8bb7b53e7219707cfc2d35880f2dfcfc58c7`
- snapshot_bundle_hash: `7d408f5d0c4481df68f6ac95daf05db4f53f59c2e02d8c91529fa910fe4bac25`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5055, "NO": 0.0493, "YES": 0.4452}`

