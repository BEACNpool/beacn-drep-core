# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s5z9qdza
Recommendation: **NO**
Score: `-0.2733` (raw `-0.2533` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7883` | Readiness: `0.85`
> Reasoning layer (precomputed): The document provides useful governance structure, addresses, external references, and a concrete maintenance scope, but several high-materiality adoption and delivery-history claims are asserted rather than evidenced in the anchor, and the cost basis for a part-time maintainer plus contingency is not strongly justified against treasury stewardship. The small negative nudge reflects caution on evidence quality and cost justification rather than a hard blocker.

## Plain-language explanation (precomputed)
BEACN voted NO because the action asks to withdraw 540,750 ada from the treasury, and the evidence package did not justify that cost strongly enough under the higher scrutiny required for treasury spending.

The proposal requested 12 months of Year 2 funding for TxPipe’s UTxO RPC maintenance and enhancement work. It covered a part-time maintainer, protobuf specification maintenance, official SDK upkeep, community support, ecosystem-feedback improvements, public communication, and AI-friendly documentation. The proposer stated the total was 525,000 ada for the work plus a 15,750 ada Intersect administration fee, with a $105,000 annual maintainer rate and a 105,000 ada contingency reserve.

Several parts were well-supported: the requested amount, the budget administration fee, the broad maintenance scope, the existence of a pinned proposal anchor, the Intersect budget-process support signal, and the proposed treasury administration structure. But some material claims were still thin or only asserted in the proposal, especially adoption by Amaru, Dingo, and the Haskell Cardano node, the claim that more than 10 related repositories are maintained under Apache 2.0, and the delivery-history claims around prior Project Catalyst awards.

The review gates allowed the proposal to be assessed, and the strongest YES case was that the amount and basic scope were clear and the proposal included governance structure and public tracking. The NO case carried more weight: this is a treasury withdrawal, treasury conditions were flagged as unsustainable, cost-benefit clarity and sustainability path were missing, execution risk remained unknown, and there was no independent assurance or rollback/remedy path. BEACN’s vote is therefore a treasury-stewardship NO, based on insufficient evidence for the spending level rather than a rejection of UTxO RPC itself.

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
- finding: Requested: Fund UTxO RPC by TxPipe for maintenance and enhancement over a 12-month Year 2 period.
- finding: Recipient: Intersect treasury reserve smart contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for UTxO RPC over 12 months, Maintenance of the protobuf specification including protocol compatibility, versioning, and documentation, Maintenance of official SDKs including dependency updates, performance improvements, and bug fixing, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect budget administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The motivation states the funding covers a part-time maintainer at an annual rate of $105,000 USD and includes a 105,000 ADA contingency reserve.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC is described as an open interface specification using Protocol Buffers with SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface.
- finding: Claim (technical, proposer_asserted, medium materiality): The project is said to maintain more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations under the Apache 2.0 license.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation and audited results.
- missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface.
- missing: Independent evidence for: The project is said to maintain more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations under the Apache 2.0 license.
- missing: Independent evidence for: The proposal says TxPipe has received 30 Project Catalyst awards across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect budget administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect budget administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The document provides useful governance structure, addresses, external references, and a concrete maintenance scope, but several high-materiality adoption and delivery-history claims are asserted rather than evidenced in the anchor, and the cost basis for a part-time maintainer plus contingency is not strongly justified against treasury stewardship. The small negative nudge reflects caution on evidence quality and cost justification rather than a hard blocker.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface.
- Claims and evidence missing: Independent evidence for: The project is said to maintain more than 10 repositories covering the core specification, language-specific SDKs, documentation, and provider integrations under the Apache 2.0 license.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `a7086ba046f7931142857b1c5118fc1e7ce70c590574c689279df5ca62725444`
- snapshot_bundle_hash: `ed53e8767e13d9fdbeb755a2be190eba779f0cb9d072ecc3c031d10a8e2a0c09`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2047, "NO": 0.7491, "YES": 0.0462}`

