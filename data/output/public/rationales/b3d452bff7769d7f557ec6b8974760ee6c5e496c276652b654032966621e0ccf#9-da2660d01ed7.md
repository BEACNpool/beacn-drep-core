# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#9
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.08` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.0` recorded, not added) | Confidence: `0.74` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit alignment through open-source developer infrastructure and agent-facing access, and the document gives concrete budget, deliverable, governance-process, and oversight details. However, several core need and impact claims remain proposer-asserted rather than evidenced in the anchor text, so the deterministic assessment should not receive an additional directional nudge.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal needs independently pinned public-chain evidence for the applicable Net Change Limit before a directional vote is justified. This is a conservative, evidence-based hold, not a rejection of the project.

The action requests 1,684,050 ada to fund Tx3 by TxPipe over 12 months: 1,308,000 ada for the program, a 327,000 ada contingency reserve, and a 49,050 ada Intersect administration fee. The proposal says Tx3 would provide an open interface layer for Cardano dApp protocols, onboard 12 more protocols at 3 per quarter, develop an MCP server and skill framework, and provide documentation, SDKs, and live JSON-RPC endpoints. Several core facts were supported: the anchor document was available and replayable, Tx3’s existing production use with 5 live protocols was independently verifiable, the proposal passed the required 67% Intersect Budget Process Hydra Voting threshold, and the requested amount was reported as not breaching the 350M ada Net Change Limit at submission.

However, BEACN could not complete the treasury standard for a directional vote. Treasury withdrawals get elevated scrutiny because they spend shared ada and set precedent. The review found thin evidence in some areas: the claim that Cardano lacks a common interface mechanism was not independently supported, the AI-agent risk claim was proposer-asserted rather than independently verified, and the review was missing a sustainability path, clearer cost-benefit analysis, independent assurance, and a rollback or remedy path.

A YES vote would be supported by the clear budget structure, stated deliverables, prior Tx3 production evidence, and Intersect process support. A NO vote would rest on unsupported material claims and unresolved treasury-risk questions. BEACN held at NEEDS_MORE_INFO because the directional blocker is specific: the applicable Net Change Limit must be pinned and independently verified from public chain evidence, with stronger replayable evidence for the unsupported claims and risk controls.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
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
- finding: Requested: Treasury withdrawal to fund Tx3 by TxPipe, an open API layer for Cardano dApp protocols with developer and agent-facing infrastructure.
- finding: Recipient: Intersect 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of TxPipe
- finding: Stated amount: 1,684,050
- finding: Deliverables: Deliver an open, standardized interface across Cardano's leading on-chain protocols over 12 months., Onboard 12 additional protocols, 3 per quarter, with full developer and agent coverage., Develop an MCP server and skill framework as shared infrastructure for protocols on the Tx3 registry., Provide documentation, auto-generated SDKs in multiple languages, and live JSON-RPC endpoints for published protocol interfaces.
- finding: Deadline/expiry: 12 months
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): Tx3 is intended to provide a standard open-source interface to Cardano protocols, including documentation, multi-language SDKs, and live RPC endpoints.
- finding: Claim (adoption, independently_verifiable, high materiality): TxPipe has already put the Tx3 developer layer into production through Catalyst Fund 14 with 5 protocols live on the Tx3 Protocol Registry.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal will fund 12 additional protocol onboardings at a rate of 3 per quarter with developer and agent coverage.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal will develop an MCP server, protocol skills packaging operations, agent-first documentation, and a skill framework for protocols on the registry.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer states there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and increasing integration costs.
- missing: Independent evidence for: The proposer states there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and increasing integration costs.
- missing: Independent evidence for: The proposer states AI agents create a need for auditable intent expression and deterministic transaction generation to reduce the risk of irreversible hallucinated on-chain transactions.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1684050
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.48
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
- finding: Strongest NO: a material claim is unsupported — "The proposer states there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and increasing integration costs." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1684050
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,308,000 ADA plus a 327,000 ADA contingency reserve over 12 months, with a total withdrawal of 1,684,050 ADA including a 49,050 ADA Intersect administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Directional treasury voting is blocked until this action is ranked against competing active proposals and verified NCL capacity.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposer states there is currently no common interface mechanism across the Cardano ecosystem, causing integrators to relearn each protocol and increasing integration costs.
- Claims and evidence missing: Independent evidence for: The proposer states AI agents create a need for auditable intent expression and deterministic transaction generation to reduce the risk of irreversible hallucinated on-chain transactions.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `da2660d01ed7cc541e648028431d2e7ac73c001dbe7886c9a127534e92538f5b`
- snapshot_bundle_hash: `740974cf844dc7ffe72c841a6bf8cd218132f3b53e550db6a2a87a984009ae99`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `2d4ca1500b8dba4c613121f0e0daabae335dbd3a`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.505, "NO": 0.3275, "YES": 0.1675}`

