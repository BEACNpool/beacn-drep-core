# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.4633` (raw `-0.4633` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal gives a concrete budget, delivery period, repayment formula, and audit schedule, but several decision-critical adoption and usage claims are proposer-asserted and the ask is not milestone-based. Under a treasury withdrawal standard where thin or unverifiable asks receive caution, the evidence quality supports only a small negative nudge despite plausible public-benefit wallet maintenance.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Eternl’s value or of wallet maintenance funding.

The action asks for ₳2,350,000 for 12 months of Eternl operations from August 2026 through July 2027. The proposal says this equals about $420,000, covering 6.0 FTE across 10 contributors, backend infrastructure, operations, monitoring, support, governance tooling improvements, independent treasury-use audits, and public reporting around Pro plan earnings, repayment, and donation transaction hashes. It also describes paid Pro plans and a repayment formula tied to surplus funds and paid plan income.

Several core budget details were well-supported in the proposal: the amount requested, the 12-month delivery period, the stated operating cost, the audit schedule, Pro plan pricing, and the repayment structure. But some decision-critical claims remained proposer-asserted or thinly evidenced, including adoption and usage claims, and the plan for converting Ada into stablecoins, using a public company wallet, returning excess Ada, and keeping pre-conversion Ada undelegated to an SPO and delegated to abstain voting. The review also noted no documented milestone-gated disbursement, missing cost-benefit clarity, missing independent assurance, an unknown execution risk, and a stressed treasury-flow signal.

The evidence that would unblock a directional vote is specific: the relevant Net Change Limit must be pinned and independently verified from public chain evidence. Stronger replayable evidence for the unsupported treasury handling and adoption claims, plus milestone-gated disbursement and independent assurance, would also reduce uncertainty under BEACN’s higher scrutiny standard for treasury withdrawals.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: 2.35M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, and improvements while Eternl introduces paid Pro plans.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: 12 months of frontend and backend maintenance and development, Backend infrastructure, operations, monitoring, and incident response, User support and day-to-day operations, Governance tooling enhancements, Periodic independent audits of treasury fund use and oversight metrics, Public reporting of Pro plan earnings, repayment, and donation transaction hashes
- finding: Deadline/expiry: Delivery period August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $420,000 using an Ada conversion rate of $0.1787, for a 12-month delivery period from August 2026 to July 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states that Eternl's annual operating cost is about $420,000, funding 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (governance, proposer_asserted, high materiality): Eternl says it will convert up to $420,000 worth of Ada into stablecoins, deposit it into a public company wallet, return any Ada above that amount to the treasury, and keep pre-conversion Ada undelegated to an SPO and delegated to abstain voting.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal says the Audits allocation is for periodic independent audits of treasury fund use and oversight metrics, not technical security audits, with audits planned for February 2027 and August 2027 by an unaffiliated party.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl proposes semiannual repayment checks in December and June, using surplus treasury stablecoins plus paid plan income above $420,000 to repay up to the received $420,000 value in Ada, then donating 50% of paid plan income above $420,000 until an additional $210,000 worth of Ada is donated.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states that Eternl will introduce Pro plans priced at $96 per year for Personal and $360 per year for Company, and that about 5,500 users, or 4.2% of its install base, would fully cover the $420,000 annual cost.
- missing: Independent evidence for: Eternl says it will convert up to $420,000 worth of Ada into stablecoins, deposit it into a public company wallet, return any Ada above that amount to the treasury, and keep pre-conversion Ada undelegated to an SPO and delegated to abstain voting.
- missing: Independent evidence for: Eternl claims an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users.
- missing: Independent evidence for: Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: The proposal states that Eternl is a non-custodial Cardano light wallet for web, browser extension, Android, and iOS that users rely on for payments, staking, governance, and DApp interaction.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 2350000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.74
- missing: milestone-gated disbursement
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
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $420,000 using an Ada conversion rate of $0.1787, for a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl says it will convert up to $420,000 worth of Ada into stablecoins, deposit it into a public company wallet, return any Ada above that amount to the treasury, and keep pre-conversion Ada undelegated to an SPO and delegated to abstain voting." — so cost or precedent may outweigh the benefit.
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
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2350000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $420,000 using an Ada conversion rate of $0.1787, for a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: The proposal gives a concrete budget, delivery period, repayment formula, and audit schedule, but several decision-critical adoption and usage claims are proposer-asserted and the ask is not milestone-based. Under a treasury withdrawal standard where thin or unverifiable asks receive caution, the evidence quality supports only a small negative nudge despite plausible public-benefit wallet maintenance.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Eternl says it will convert up to $420,000 worth of Ada into stablecoins, deposit it into a public company wallet, return any Ada above that amount to the treasury, and keep pre-conversion Ada undelegated to an SPO and delegated to abstain voting.
- Claims and evidence missing: Independent evidence for: Eternl claims an install base of about 100,000 browser-extension users and about 30,000 Android and iOS users.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `b13ff24b1c499108ca110632cf2fc7da59cd8ff406880a54cacc7c8527a10b43`
- snapshot_bundle_hash: `73da02893d6bdc04b7ca98a11489489d5cc49fa92cf57918c36724860375d564`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

