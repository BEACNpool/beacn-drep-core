# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#8
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1559` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `-0.02` recorded, not added) | Confidence: `0.759` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit infrastructure value and several independently verifiable governance and adoption references, but the budget justification is thin relative to treasury stewardship: the document states a large contingency reserve and total ADA request without detailed exchange-rate, labor allocation, or contingency-use rationale. Because the doctrine prioritizes treasury stewardship and evidence quality ahead of ecosystem growth, only a small cautionary negative nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Pallas or TxPipe.

The action requests 540,750 ada to fund Year 2 of Pallas maintenance by TxPipe: 420,000 ada for maintenance, 105,000 ada as contingency, and 15,750 ada for Intersect administration. The proposal describes Pallas as core Rust infrastructure for Cardano primitives, and the requested work includes dependency updates, protocol compatibility, performance improvements, bug fixing, documentation, issue triage, contribution review, community communication, and AI-friendly documentation and integration resources. It also says Intersect would administer funds through milestone-based controls, oversight, reporting obligations, and Sundae Labs treasury management smart contracts.

Several claims were supported or independently checkable, including the total budget breakdown, the technical scope of Pallas, public repository and crates.io metrics, Intersect budget-process support, and the proposal’s assertion that the withdrawal does not breach the 350M ada Net Change Limit for Epoch 613 to Epoch 713. Other material claims remained thin or unsupported by independent evidence in the review, including the claim that Pallas is shared infrastructure used by named ecosystem projects and the claim about TxPipe’s Project Catalyst delivery history. The review also flagged missing clarity on sustainability, cost-benefit justification, independent assurance, and rollback or remedy paths.

Because this is a treasury withdrawal, BEACN applies elevated scrutiny: shared ada would be spent and precedent would be set. The proposal anchor was available and replayable, execution risk was assessed as medium, and the strongest YES case was that the budget request and maintenance scope cleared evidence gates. But BEACN needs the Net Change Limit independently pinned and verified from public chain evidence before it can responsibly vote YES or NO.

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
- finding: Requested: Fund Pallas by TxPipe: Maintaining Cardano's Core Rust Libraries, Year 2, including maintenance, community support, and AI-friendly documentation/integration resources.
- finding: Recipient: Intersect treasury reserve smart contract stake address for subsequent project-specific smart contract administration on behalf of TxPipe as vendor
- finding: Stated amount: 540,750
- finding: Deliverables: 12 months of part-time maintainer coverage for Pallas after the existing contract closes, Essential maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback enhancements, and public communication, AI-friendly documentation and integration resources for AI-driven development workflows, Milestone-based disbursement controls and reporting obligations through Intersect oversight
- finding: Deadline/expiry: 12 months; exact dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for Pallas maintenance, and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA.
- finding: Claim (technical, supported_in_proposal, high materiality): Pallas is described as a collection of Rust crates implementing core Ouroboros and Cardano primitives including CBOR encoding, cryptography, networking mini-protocols, ledger traversal, transaction building, and address handling.
- finding: Claim (adoption, proposer_asserted, high materiality): The document says Pallas is shared infrastructure used by projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others.
- finding: Claim (adoption, independently_verifiable, high materiality): The document reports Pallas has over 649 pull requests, 199 stars, 91 forks, 60 contributors, and 214,446 crates.io downloads, with links to GitHub and crates.io for verification.
- finding: Claim (technical, supported_in_proposal, high materiality): The maintainer scope includes dependency updates, protocol compatibility, performance improvements, bug fixing, documentation, issue triage, contribution review, community communication, and AI-friendly documentation resources.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal states it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain treasury withdrawal submission.
- missing: Independent evidence for: The document says Pallas is shared infrastructure used by projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others.
- missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals in Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.63
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for Pallas maintenance, and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The document says Pallas is shared infrastructure used by projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve for Pallas maintenance, and a 15,750 ADA Intersect administration fee, totaling 540,750 ADA." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show plausible public-benefit infrastructure value and several independently verifiable governance and adoption references, but the budget justification is thin relative to treasury stewardship: the document states a large contingency reserve and total ADA request without detailed exchange-rate, labor allocation, or contingency-use rationale. Because the doctrine prioritizes treasury stewardship and evidence quality ahead of ecosystem growth, only a small cautionary negative nudge is justified.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The document says Pallas is shared infrastructure used by projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others.
- Claims and evidence missing: Independent evidence for: TxPipe is stated to have received funding through 30 Project Catalyst proposals in Funds 9 through 14, with 26 delivered and 4 under development and on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `b77c3dabcda2821c355145c47c3fec764b7ac39d7e2d202316a8f46e47f1da9d`
- snapshot_bundle_hash: `7e6bc8cc353a342929f2a6a1a2ea7279a4669cfc3fc7601f5ba0a6808e39eaf6`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5098, "NO": 0.0892, "YES": 0.401}`

