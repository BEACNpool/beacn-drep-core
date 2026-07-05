# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s5z9qdza
Recommendation: **NO**
Score: `-0.2733` (raw `-0.2533` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7883` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit developer infrastructure and includes governance/process references, budget line items, and oversight mechanics, but several decision-critical value claims are asserted rather than evidenced in the anchor text, including adoption, repository scope, prior delivery record, and current schedule status. Given the doctrine's priority for treasury stewardship and evidence quality, the appropriate bounded nudge is mildly cautious rather than supportive of spending.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not clear the evidence bar for spending shared ADA. The proposal had a replayable anchor and a clear funding request, but several value-critical claims were asserted rather than independently evidenced, especially the claim that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a standard query interface.

The action requested 540,750 ada for Year 2 maintenance of UTxO RPC by TxPipe, submitted by Intersect on behalf of the vendor. The funds were described as 525,000 ada for maintenance and enhancement, including a 420,000 ada maintainer budget plus 105,000 ada contingency reserve, and 15,750 ada for Intersect budget administration. The proposed work covered protobuf specification maintenance, SDK updates, bug fixes, community support, AI-friendly documentation, and administration over 12 months.

BEACN recognized several supported points: the amount and budget structure were clear, UTxO RPC was described as an open Protocol Buffers interface with multiple SDKs, the proposal passed the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase, and the withdrawal did not breach the applicable Net Change Limit at submission. The proposal also described treasury management controls, milestone-based disbursement, oversight, and a public dashboard.

The NO vote came from treasury stewardship and evidence quality. Treasury actions require elevated scrutiny because they spend shared funds and set precedent. The review found thin evidence for adoption, repository scope, prior delivery record, and current schedule status; it also lacked a sustainability path, cost-benefit clarity, independent assurance, and a rollback or remedy path. With treasury flow already flagged as unsustainable in the review, BEACN concluded that the cost and precedent risk outweighed the supported case for funding.

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
- finding: Requested: Treasury withdrawal to fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2, including part-time maintenance over 12 months and Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe/vendor
- finding: Stated amount: 540750
- finding: Deliverables: WP1 - UTxO RPC Maintenance and Enhancement, Maintenance of the protobuf specification, including protocol compatibility, versioning, and documentation, Maintenance of official SDKs, including dependency updates, performance improvements, and bug fixing, Community support including issue triage, review of external contributions, enhancements from ecosystem feedback, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows, Intersect Budget Administration fee
- finding: Deadline/expiry: 12 months; new grant period begins after closure of existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The total withdrawal is 540,750 ADA, consisting of 525,000 ADA for UTxO RPC Maintenance and Enhancement and 15,750 ADA for the Intersect Budget Administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is an open interface specification using Protocol Buffers with SDKs in Rust, Go, Node.js, .NET, Haskell, and Python to standardize interactions with UTxO-based blockchains.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem.
- finding: Claim (technical, proposer_asserted, medium materiality): The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission under the approved Budget Process Framework.
- missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem.
- missing: Independent evidence for: The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- missing: Independent evidence for: TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 successfully delivered and 4 currently under development and on schedule.
- missing: Independent evidence for: TxPipe received open-source maintenance funding through Intersect's 2025 budget cycle for Pallas, Dolos, and UTxO RPC, all of which the proposal says are being delivered on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.66
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for a part-time UTxO RPC maintainer over 12 months at an annual rate of $105,000 USD." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal is aligned with public-benefit developer infrastructure and includes governance/process references, budget line items, and oversight mechanics, but several decision-critical value claims are asserted rather than evidenced in the anchor text, including adoption, repository scope, prior delivery record, and current schedule status. Given the doctrine's priority for treasury stewardship and evidence quality, the appropriate bounded nudge is mildly cautious rather than supportive of spending.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as a standard across the ecosystem.
- Claims and evidence missing: Independent evidence for: The project maintains more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `7b684fe32cab1cf55510df9f2cae690440733554541543e9b87598653a9cf812`
- snapshot_bundle_hash: `c201a7459bca8a6252563e253126bb8fe5b12b943dc5c088f22f15e86fb8c416`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2047, "NO": 0.7491, "YES": 0.0462}`

