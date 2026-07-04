# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sj72rg72
Recommendation: **NO**
Score: `-0.3833` (raw `-0.3533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5158` | Readiness: `0.0`
> Reasoning layer (precomputed): The proposal has a plausible public-benefit thesis and some checkable governance/process references, but the deterministic assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's hierarchy, treasury stewardship and evidence quality should receive a cautious negative nudge because the ask is large and the document does not provide enough internal detail to validate cost reasonableness or delivery risk.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal request and the review found too many unresolved evidence gaps to justify spending shared ADA. The proposal has a plausible public-benefit case, but BEACN’s treasury standard requires stronger proof on budget, feasibility, risk, alternatives, failure modes, and community impact.

The action requested 1,684,050 ada to fund Tx3 by TxPipe over 12 months, including 1,308,000 ada for the project, a 327,000 ada contingency reserve, and a 49,050 ada Intersect administration fee. The proposal described Tx3 as an open API layer for Cardano dApp protocols, with documentation, multi-language SDKs, live JSON-RPC endpoints, agent-first documentation, protocol skills packaging, an MCP server, and onboarding of 12 additional protocols over four quarters.

Several claims were supported: the amount and fee structure were stated, the technical goal of an open-source protocol interface was documented, the proposal had a pinned and replayable anchor, Tx3 had five protocols live through Catalyst Fund 14, and the action had passed the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase. However, important claims remained unsupported or thin, including the claim that Cardano lacks a common interface mechanism, the strategic-alignment claims, execution risk, mitigation evidence, and independent assurance.

The review gates for treasury diligence, risk review, and synthesis did not clear BEACN’s bar. The dossier was incomplete, the treasury analysis lacked a line-item budget and complete budget analysis, the feasibility and risk assessments were missing, and the synthesis was blocked by missing proposal, alternatives, failure-mode, and community-impact analysis. Because treasury withdrawals require elevated scrutiny, BEACN treated these gaps as decisive and voted NO.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.68M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Tx3 by TxPipe as an open API layer for Cardano dApp protocols.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe.
- finding: Stated amount: 1,684,050
- finding: Deliverables: Open, standardized interface across Cardano on-chain protocols, Documentation, auto-generated multi-language SDKs, and live JSON-RPC endpoints from verified interface definitions, Agent-first documentation, protocol skills packaging operations, and an MCP server for agent discovery and calls, Onboarding of 12 additional protocols over 12 months, three per quarter, with developer and agent coverage
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Tx3 is intended to provide a standard open-source interface to Cardano protocols through documentation, multi-language SDKs, and live RPC endpoints.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says there is currently no common interface mechanism across the Cardano ecosystem, causing each integrator to relearn each protocol and making cross-protocol composability impractical.
- finding: Claim (adoption, independently_verifiable, medium materiality): Through Catalyst Fund 14, TxPipe has already put the developer layer into production with five protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal funds 12 additional protocol onboardings, three per quarter, plus development of the MCP server and skill framework as shared registry infrastructure.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal claims it aligns with Intersect strategic Pillar 2 by improving developer experience and with Pillar 4 by supporting ecosystem growth and market adoption.
- missing: Independent evidence for: The proposal says there is currently no common interface mechanism across the Cardano ecosystem, causing each integrator to relearn each protocol and making cross-protocol composability impractical.
- missing: Independent evidence for: The proposal claims it aligns with Intersect strategic Pillar 2 by improving developer experience and with Pillar 4 by supporting ecosystem growth and market adoption.
- missing: Independent evidence for: TxPipe is said to have received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and four under development and on schedule.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1.68M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." though 7 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal says there is currently no common interface mechanism across the Cardano ecosystem, causing each integrator to relearn each protocol and making cross-protocol composability impractical." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1.68M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." though 7 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has a plausible public-benefit thesis and some checkable governance/process references, but the deterministic assessment identifies missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's hierarchy, treasury stewardship and evidence quality should receive a cautious negative nudge because the ask is large and the document does not provide enough internal detail to validate cost reasonableness or delivery risk.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposal says there is currently no common interface mechanism across the Cardano ecosystem, causing each integrator to relearn each protocol and making cross-protocol composability impractical.
- Claims and evidence missing: Independent evidence for: The proposal claims it aligns with Intersect strategic Pillar 2 by improving developer experience and with Pillar 4 by supporting ecosystem growth and market adoption.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `744f01b9394f6a6044230e795e44d048d141647b61111afe05120e7c783b3673`
- snapshot_bundle_hash: `dbf89476d00250195934db88d0d693e0a6fc24790dc834d0d7086676b8db01a7`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `960`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2207, "NO": 0.7361, "YES": 0.0432}`

