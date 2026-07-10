# Rationale: dfd81f8db652fd9263e0ce3bef043b4823045ec3a5da10c817681ada7a23f034#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was missing baseline evidence needed to make a responsible treasury decision. This is a conservative, evidence-based hold, not a rejection of the idea.

The proposal requested about ₳12,332,031 for Phase 1 of taking Bifrost from testnet toward launch readiness over nine months, from July 2026 to March 2027. The requested work included bridge hardening, audits, formal verification, ecosystem and partner readiness, stewardship structure, economic foundations, and a partner pipeline for public launch. The proposal supported the basic description of Bifrost as a permissionless Bitcoin-Cardano bridge that would bring BTC to Cardano as native fBTC, and it supported the stated funding period and several design claims, including SPO-based custody and open-source licensing.

However, several important claims were still only proposer assertions, including that Bifrost is currently on testnet with working peg-ins and outs and participating SPOs, and that Phase 1 will result in an audited mainnet bridge operating in both custody modes under controlled access. For a treasury withdrawal, BEACN also required stronger budget and risk evidence than was available. The review found the intake blocked, treasury analysis incomplete, claims and evidence thin, and risk review thin.

A directional vote would require the missing baseline evidence: the treasury amount in lovelace, a complete proposal summary, line-item budget, milestone-gated disbursement plan, feasibility assessment, risk and mitigation evidence, independent assurance, alternatives analysis, failure-mode analysis, and community impact analysis. Without that dossier, BEACN could not vote YES or NO without pretending to have more certainty than the evidence supported.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 640
- finding: Expires after epoch: 647
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Phase 1 of 2 work to take Bifrost from working testnet to launch readiness, including hardening, security audits, formal verification, ecosystem and partner readiness, and stewardship and economic foundations for launch.
- finding: Recipient: FluidTokens and Lantr Engineering
- finding: Stated amount: ₳12,332,031 approximately, including a 10% refundable contingency
- finding: Deliverables: Audited bridge running on Cardano mainnet in both custody modes under controlled access, Hardened security and formal verification work, Ecosystem and partner readiness, Independent stewardship structure or equivalent determined in Phase 1, Hardened economic model, SPO/dApp partner pipeline required for public launch
- finding: Deadline/expiry: 9-month delivery period from July 2026 to March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's SPO ecosystem that brings BTC onto Cardano as native fBTC.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposers request ₳12,332,031 for a 9-month Phase 1 delivery period from July 2026 to March 2027.
- finding: Claim (adoption, proposer_asserted, high materiality): Bifrost is currently on testnet under Catalyst Fund 14, with working peg-ins/outs and participating SPOs.
- finding: Claim (economic, supported_in_proposal, medium materiality): The Catalyst Fund 14 grant for Bifrost was ₳739,000 and covered architecture, testnet MVP, and documentation from December 2025 to August 2026.
- finding: Claim (technical, proposer_asserted, high materiality): By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO-threshold custody modes under controlled access.
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost custody is described as distributed across 400+ Cardano SPOs weighted by delegation, with fund movement requiring a cryptographic threshold representing the majority of delegated stake.
- missing: Independent evidence for: Bifrost is currently on testnet under Catalyst Fund 14, with working peg-ins/outs and participating SPOs.
- missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO-threshold custody modes under controlled access.
- missing: Independent evidence for: The proposal projects a base Q2 2029 target of 1,200 BTC TVL, about 600,000 annual transactions, and 3,000 fBTC-holding wallets.
- missing: Independent evidence for: Bridge fee surplus is claimed to return to the Cardano Treasury in fBTC after operations and SPO incentives.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: milestone-gated disbursement
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
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's SPO ecosystem that brings BTC onto Cardano as native fBTC." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Bifrost is currently on testnet under Catalyst Fund 14, with working peg-ins/outs and participating SPOs." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: evidence is too thin for a directional vote while 1 blocker(s) remain open.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's SPO ecosystem that brings BTC onto Cardano as native fBTC." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: Bifrost is currently on testnet under Catalyst Fund 14, with working peg-ins/outs and participating SPOs.
- Claims and evidence missing: Independent evidence for: By the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in federated and SPO-threshold custody modes under controlled access.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `f2ba64852251ea3052ec781005f83911bbc3528aadfbe39d732c3edfd90fe30b`
- snapshot_bundle_hash: `f1b4424767d0c5f4305f90d326391c471195b1a5115eadadc43e4f579ffdfb68`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

