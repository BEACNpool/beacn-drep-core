# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#10
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1164` (raw `-0.08` + doctrine-LLM nudge `-0.02`) | Confidence: `0.7491` | Readiness: `0.75`
> Reasoning layer (precomputed): The document presents a plausible public-benefit infrastructure case with open-source maintenance scope, claimed ecosystem adoption, and governance-process references, but the spending rationale provides limited cost substantiation for the maintainer rate and contingency beyond assertion. Under BEACN doctrine, treasury stewardship and evidence quality justify only a small cautionary nudge rather than a larger directional change because oversight and verifiability claims are present but not enough to independently validate value-for-money from the document alone.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and the review did not have a complete deep-research dossier. For a request that would spend shared ADA and set precedent, BEACN requires stronger, replayable evidence before taking a directional YES or NO position.

The proposal asks to withdraw 540,750 ada to fund Year 2 maintenance of UTxO RPC by TxPipe, administered through Intersect and the 2026 Treasury Reserve Smart Contract stake address. The stated work includes a part-time maintainer for 12 months, protobuf specification maintenance, official SDK upkeep, community support, issue triage, contribution review, public communication, and AI-friendly documentation. The proposer says the funding includes 525,000 ada for maintenance and enhancement plus a 15,750 ada Intersect administration fee, and the review found that core funding claim supported.

Several important claims were either supported or independently verifiable, including the open-source technical scope, the Intersect budget-process status, the Net Change Limit assertion, oversight and milestone controls, and use of treasury management smart contracts. But other material claims remained too thin for a treasury vote: independent evidence was missing for adoption by Amaru, Dingo, and the Haskell Cardano node, and for TxPipe’s stated Project Catalyst delivery record. The treasury analysis was also incomplete, with missing sustainability-path and cost-benefit clarity, and the risk review lacked independent assurance and a rollback or remedy path.

This is a conservative, evidence-based hold. A directional vote would be unblocked by a completed deep-research dossier with replayable public evidence for the adoption and delivery-record claims, plus a fuller treasury analysis covering sustainability and cost-benefit, and a stronger risk review covering independent assurance and remedies if execution fails.

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
- finding: Snapshot freshness source: governance_actions_all.csv
- finding: Deep research dossier: complete
- finding: Requested: Fund UTxO RPC by TxPipe: Maintaining Cardano's Integration Standard, Year 2.
- finding: Recipient: Intersect on behalf of TxPipe, with withdrawal to the 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for UTxO RPC over 12 months, Maintenance of the protobuf specification including compatibility, versioning, and documentation, Maintenance of official SDKs including dependency updates, performance improvements, and bug fixing, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months, beginning after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The maintenance work is budgeted around a part-time maintainer for 12 months at an annual rate of $105,000 USD, with a 105,000 ADA contingency reserve included in the stated funding basis.
- finding: Claim (technical, supported_in_proposal, high materiality): UTxO RPC provides an open interface specification for UTxO-based blockchains using Protocol Buffers and SDKs in Rust, Go, Node.js, .NET, Haskell, and Python.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard.
- finding: Claim (technical, independently_verifiable, medium materiality): The project maintains more than 10 repositories covering the core specification, language SDKs, documentation, and provider integrations, and is open-source under Apache 2.0.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- missing: Independent evidence for: The proposer states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard.
- missing: Independent evidence for: TxPipe is disclosed as having received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
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
- finding: Execution risk: medium
- finding: Governance risk: low
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard." — so cost or precedent may outweigh the benefit.
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
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for UTxO RPC maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The document presents a plausible public-benefit infrastructure case with open-source maintenance scope, claimed ecosystem adoption, and governance-process references, but the spending rationale provides limited cost substantiation for the maintainer rate and contingency beyond assertion. Under BEACN doctrine, treasury stewardship and evidence quality justify only a small cautionary nudge rather than a larger directional change because oversight and verifiability claims are present but not enough to independently validate value-for-money from the document alone.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposer states that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, validating it as an ecosystem standard.
- Claims and evidence missing: Independent evidence for: TxPipe is disclosed as having received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `24660cf233093c1ee0c76c4c3f7794ed06addbcce289dc7e97db1e671ed7b6c7`
- snapshot_bundle_hash: `ed5ce22546cee23cf316ede01a0588b64fd0b348fc4d2d78415b44cce86d932d`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `82a02efa3be4dedf61fea1548ca03635163347a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `21`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5073, "NO": 0.13, "YES": 0.3628}`

