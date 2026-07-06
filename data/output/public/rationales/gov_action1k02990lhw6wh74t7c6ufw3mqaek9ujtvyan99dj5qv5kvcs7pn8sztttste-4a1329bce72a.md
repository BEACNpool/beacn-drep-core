# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sztttste
Recommendation: **NO**
Score: `-0.2533` (raw `-0.2533` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7833` | Readiness: `0.85`
> Reasoning layer (precomputed): The supplied claims show plausible public-benefit infrastructure alignment and some independently verifiable governance/process evidence, but the request is still a sizable treasury withdrawal for maintenance work and several performance, delivery-history, and cost-effectiveness claims remain proposer-asserted. The deterministic treasury and evidence rules appear to capture the key positives and cautions, so no additional nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not meet the higher evidence bar expected for spending shared ADA. The proposal had a pinned, replayable anchor and some well-supported budget details, but a core technical claim about Dolos being a lightweight Cardano data node built in Rust with lower overhead than traditional full nodes lacked independent evidence in the review.

The action requested 540,750 ada for Year 2 maintenance of Dolos by TxPipe, paid to the listed 2026 Treasury Reserve Smart Contract stake address. The work was described as 12 months of part-time maintenance and enhancement, including dependency updates, Cardano protocol compatibility, performance improvements, bug fixes, documentation, community support, AI-friendly integration resources, and Intersect budget administration. The proposer stated that the amount included 525,000 ada for Dolos work and a 15,750 ada Intersect administration fee, with the underlying budget framed as 420,000 ada plus a 105,000 ada contingency reserve.

The review found several claims well-supported or independently checkable, including the requested amount, the Intersect administration fee, the described oversight and milestone controls, Dolos repository activity figures, Hydra Voting support, and the claim that the request did not breach the applicable Net Change Limit. However, the evidence picture was still thin for a treasury vote. Independent evidence was missing for the core technical value claim about Dolos, for TxPipe’s stated Catalyst delivery history, and for important treasury and risk questions including sustainability path, cost-benefit clarity, independent assurance, and a rollback or remedy path.

Because treasury withdrawals consume shared resources and set precedent, BEACN applies elevated scrutiny. The strongest YES case was that the maintenance budget itself was clearly described and passed evidence gates. The strongest NO case was that an important benefit claim remained unsupported, while treasury-flow sustainability was already in an unsustainable advisory regime. On balance, that made the cost and precedent risk outweigh the supported case, so BEACN voted NO.

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
- finding: Requested: Treasury withdrawal to fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 540750
- finding: Deliverables: WP1 - Dolos Maintenance and Enhancement, Part-time maintainer for Dolos over 12 months, Essential codebase maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows, Intersect budget administration and oversight
- finding: Deadline/expiry: 12 months; exact deadline not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The total requested withdrawal is 540,750 ADA, consisting of 525,000 ADA for Dolos maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Dolos is a lightweight Cardano data node built in Rust that provides efficient chain-data access without the overhead of traditional full nodes.
- finding: Claim (technical, supported_in_proposal, medium materiality): Dolos exposes five query interfaces, including Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and an Ouroboros N2C Unix socket compatible with Cardano-cli, Ogmios, and other tooling.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposer states that Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors.
- finding: Claim (governance, independently_verifiable, high materiality): The proposer states that Dolos achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- missing: Independent evidence for: Dolos is a lightweight Cardano data node built in Rust that provides efficient chain-data access without the overhead of traditional full nodes.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development on schedule.
- missing: Independent evidence for: The proposal states that TxPipe's prior Intersect-funded open-source maintenance for Pallas, Dolos, and UTxO RPC is being delivered on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.68
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Dolos is a lightweight Cardano data node built in Rust that provides efficient chain-data access without the overhead of traditional full nodes." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 540750
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: Dolos is a lightweight Cardano data node built in Rust that provides efficient chain-data access without the overhead of traditional full nodes.
- Claims and evidence missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals from Funds 9 through 14, with 26 delivered and 4 under development on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `4a1329bce72a47594d23f98caa03ddd89fbb5a69a98a3022f66410c8a98f1644`
- snapshot_bundle_hash: `d27014baf1f8982494781364afbe9c098f966c7c69dfc4d163d4913062f7d89d`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2093, "NO": 0.7436, "YES": 0.0471}`

