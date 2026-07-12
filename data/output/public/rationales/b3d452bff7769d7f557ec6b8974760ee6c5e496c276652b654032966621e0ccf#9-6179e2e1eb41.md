# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#9
Recommendation: **NEEDS_MORE_INFO**
Score: `0.007` (raw `-0.08` + doctrine-LLM nudge `+0.01`) | Confidence: `0.7218` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show concrete deliverables, a fixed 12-month scope, some independently checkable adoption and governance-process references, and structured treasury controls, which modestly improves evidence quality and public-benefit alignment beyond a generic infrastructure ask. The nudge is small because the request is large and the doctrine prioritizes treasury stewardship and verified evidence over plausible ecosystem growth.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the project.

The action requests 1,684,050 ada to fund Tx3 by TxPipe over 12 months as an open API layer for Cardano dApp protocols. The proposal claims this would provide standardized protocol interfaces, documentation, auto-generated SDKs, live JSON-RPC endpoints, agent-facing documentation, an MCP server, shared registry infrastructure, and 12 additional protocol onboardings at 3 per quarter. The proposal also states that the withdrawal includes 1,308,000 ada for work, a 327,000 ada contingency reserve, and a 49,050 ada Intersect administration fee.

Several items were supported in the proposal or independently verifiable: the anchor document was pinned and replayable, the budget structure was substantiated, Catalyst Fund 14 was stated to have 5 protocols live on the Tx3 Protocol Registry, the proposal was stated to have passed the 67% Intersect Budget Process Hydra Voting threshold, and the funds were described as administered through Intersect with treasury smart contracts, authorization rules, oversight, milestone controls, and a public dashboard. But important claims remained thin or unsupported by independent evidence, including the central claim that Tx3 will deliver a common open interface across leading Cardano protocols and the claim that Cardano currently lacks such a common interface mechanism.

Because this is a treasury withdrawal, BEACN applies elevated scrutiny. The review found missing or incomplete evidence around sustainability, cost-benefit clarity, independent assurance, execution risk, and a rollback or remedy path. The specific evidence that would unblock a directional vote is public, independently verifiable chain evidence pinning the applicable Net Change Limit for this withdrawal, along with stronger independent support for the core technical and ecosystem-benefit claims.

## Review Tree
- overall_status: `incomplete`

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
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Fund Tx3 by TxPipe as an open API layer for Cardano dApp protocols, including developer and agent-facing infrastructure.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe.
- finding: Stated amount: 1684050
- finding: Deliverables: Open standardized interface across Cardano on-chain protocols, Documentation, auto-generated SDKs in multiple languages, and live JSON-RPC endpoints from verified interface definitions, Agent-first documentation, Protocol skills packaging operations, MCP server for agents to discover and call published protocols, 12 additional protocol onboardings over 12 months, described as 3 per quarter, Shared infrastructure for all protocols on the Tx3 Protocol Registry
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): The stated purpose is to deliver an open, standardized interface across leading Cardano on-chain protocols so developers and AI agents can discover, integrate, and compose them through one consistent surface.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer says Cardano currently lacks a common interface mechanism across protocols, causing integrators to relearn protocols, rebuild understanding, and face higher integration costs.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposer says Tx3 describes each protocol once with a verified interface definition that produces documentation, multi-language SDKs, and live JSON-RPC endpoints.
- finding: Claim (adoption, independently_verifiable, high materiality): The document states that Catalyst Fund 14 has already put the Tx3 developer layer into production with 5 protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to funding 12 additional protocol onboardings, at 3 per quarter, with full developer and agent coverage.
- missing: Independent evidence for: The stated purpose is to deliver an open, standardized interface across leading Cardano on-chain protocols so developers and AI agents can discover, integrate, and compose them through one consistent surface.
- missing: Independent evidence for: The proposer says Cardano currently lacks a common interface mechanism across protocols, causing integrators to relearn protocols, rebuild understanding, and face higher integration costs.
- missing: Independent evidence for: The proposer says the work aligns with Intersect Pillar 2 for Adoption and Utility through developer experience and open-source incentives.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.62
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The stated purpose is to deliver an open, standardized interface across leading Cardano on-chain protocols so developers and AI agents can discover, integrate, and compose them through one consistent surface." — so cost or precedent may outweigh the benefit.
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
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.010 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show concrete deliverables, a fixed 12-month scope, some independently checkable adoption and governance-process references, and structured treasury controls, which modestly improves evidence quality and public-benefit alignment beyond a generic infrastructure ask. The nudge is small because the request is large and the doctrine prioritizes treasury stewardship and verified evidence over plausible ecosystem growth.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The stated purpose is to deliver an open, standardized interface across leading Cardano on-chain protocols so developers and AI agents can discover, integrate, and compose them through one consistent surface.
- Claims and evidence missing: Independent evidence for: The proposer says Cardano currently lacks a common interface mechanism across protocols, causing integrators to relearn protocols, rebuild understanding, and face higher integration costs.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `6179e2e1eb41a7c45fd05c327c245f821346e31c2be7b3298038c472eaac9fc7`
- snapshot_bundle_hash: `0ccec393bfafd9fcad9f303eb27a52daafb691398ac49659605e0bf2f2e9a996`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5005, "NO": 0.2428, "YES": 0.2568}`

