# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.5333` (raw `-0.5033` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): A small negative nudge is justified because the ask is large, the deterministic assessment marks claims and evidence as thin, and several material premises for treasury stewardship rely on proposer assertions rather than reproducible evidence, even though the proposal includes repayment, audit, and transparency commitments.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal, and the evidence did not meet the higher bar needed for spending shared ADA. The proposal included useful transparency, audit, and repayment commitments, but important cost and adoption claims still relied on proposer assertions rather than independent, replayable evidence.

The action requested ₳2,350,000 for 12 months of Eternl operations from August 2026 through July 2027, covering frontend and backend work, infrastructure, support, administration, audits, governance tooling, Eternl Core, Eternl Hub, hardware wallet support, and wallet data export improvements. The proposer said Eternl costs about $420,000 per year, funds 6.0 FTE across 10 contributors, has about 100,000 browser-extension installs plus about 30,000 mobile installs, and handles 10-18% of Cardano mainnet transactions.

Several claims were well-supported in the proposal itself: the requested amount and funding period, the plan to convert up to $420,000 worth of ADA into stablecoins, public-wallet custody, refunding excess ADA, independent audits in February and August 2027, semiannual repayment checks, and planned Pro plan pricing. However, the review found thin evidence overall, with missing independent support for the annual cost and staffing claim, the install figures, and other material premises.

The review gates passed enough to make the proposal reviewable: the pinned anchor document was available, the action type and basic request were clear, and the strongest YES case was considered. But treasury scrutiny is elevated, and key gaps remained: no milestone-gated disbursement was documented, cost-benefit clarity was missing, execution risk was unknown, independent assurance was incomplete, and no dependency map was provided. On balance, BEACN concluded that the cost and precedent risk outweighed the supported benefits, so the evidence-based vote was NO.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, improvements, infrastructure, support, administration, and audits/oversight.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development, Backend infrastructure and operations, User support, Administrative operations, Periodic independent audits of treasury fund use and oversight metrics, Governance tooling enhancements, Planned Eternl Core, Eternl Hub, hardware wallet support, and wallet data export improvements
- finding: Deadline/expiry: August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month delivery period from August 2026 to July 2027.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states Eternl costs around $420,000 per year and funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans to introduce Pro plans priced at $96 per year for personal users and $360 per year for companies, and says about 5,500 paying users would fully cover the annual $420,000 cost.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer states Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposer commits to convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal says independent audits by a party unaffiliated with Tastenkunst GmbH or the Eternl team will occur in February 2027 and August 2027 and review custody, conversion, spending, balances, Pro plan income relevant to repayment, and treasury refunds or repayments.
- missing: Independent evidence for: The proposal states Eternl costs around $420,000 per year and funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- missing: Independent evidence for: The proposer states Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- missing: Independent evidence for: The proposer claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 2350000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states Eternl costs around $420,000 per year and funds 6.0 FTE across 10 contributors at $70,000 per FTE." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small negative nudge is justified because the ask is large, the deterministic assessment marks claims and evidence as thin, and several material premises for treasury stewardship rely on proposer assertions rather than reproducible evidence, even though the proposal includes repayment, audit, and transparency commitments.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: The proposal states Eternl costs around $420,000 per year and funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- Claims and evidence missing: Independent evidence for: The proposer states Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `509a0b5e35ba327a75adfc11f62afd8edc8dd70653fe8e230b87aeaf6f48d00b`
- snapshot_bundle_hash: `7d08940cb62deeb21ee83c9854f98f71b2337593dedcad57b7109b7694d94caa`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1758, "NO": 0.7845, "YES": 0.0397}`

