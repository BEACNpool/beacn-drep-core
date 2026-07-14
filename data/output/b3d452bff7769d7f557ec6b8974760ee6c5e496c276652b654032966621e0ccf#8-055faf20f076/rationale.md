# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#8
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1559` (raw `-0.08` + doctrine-LLM nudge `+0.02`) | Confidence: `0.759` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe established shared infrastructure, concrete maintenance deliverables, public repositories or dashboards for several verification points, and structured oversight for disbursement. The adjustment remains modest because several adoption and prior-delivery claims are proposer asserted, and treasury stewardship still requires caution on a 540,750 ADA spend.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the proposal.

The action asks to withdraw 540,750 ada for Year 2 maintenance of Pallas by TxPipe, submitted by Intersect on behalf of the vendor. The proposal says this includes 525,000 ada for maintenance and enhancement plus a 15,750 ada Intersect administration fee, funding a part-time maintainer for 12 months after the current contract closes. The work described includes dependency updates, Cardano protocol compatibility, performance improvements, bug fixes, documentation, community support, and AI-friendly integration resources, with milestone-based disbursement through Intersect treasury management smart contracts.

Several important claims were supported in the proposal or had public references: the amount requested, the maintainer rate and period, the technical scope of Pallas, the proposed maintenance work, the Intersect voting threshold, the stated Net Change Limit position at submission, and the treasury administration structure. But some material claims still lacked independent evidence in the review, including that Pallas is used as shared infrastructure by the named ecosystem projects, and that TxPipe’s prior Catalyst and Intersect-funded work has the delivery record claimed.

The review passed the basic intake and anchor checks, recognized the pinned proposal document as replayable, and found a credible strongest case for YES. But treasury withdrawals require a higher bar because they spend shared ada, and the review still flagged thin evidence, stressed treasury-flow conditions, missing sustainability and cost-benefit clarity, missing independent assurance, and no clear rollback or remedy path. The evidence that would unblock a directional vote is independently pinned Net Change Limit verification from public chain evidence, plus stronger independent support for the material adoption and delivery-history claims.

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
- finding: Requested: Withdraw treasury funds for Pallas by TxPipe: Maintaining Cardano's Core Rust Libraries, Year 2.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor
- finding: Stated amount: 540,750
- finding: Deliverables: Part-time maintainer for Pallas over 12 months after closure of the existing contract, Essential maintenance including dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Community support including issue triage, review of external contributions, ecosystem-feedback-driven enhancements, and public developer communication, AI-friendly documentation and integration resources for AI-driven development workflows, Milestone-based disbursement controls through Intersect treasury management smart contracts
- finding: Deadline/expiry: 12 months; exact dates not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Pallas maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested funding is for a part-time Pallas maintainer over 12 months at an annual rate of $105,000 USD, with the new grant period beginning after the existing contract closes.
- finding: Claim (technical, supported_in_proposal, high materiality): Pallas is a collection of Rust crates implementing core Ouroboros and Cardano primitives including CBOR encoding, cryptographic operations, mini-protocol networking, ledger traversal, transaction building, and address handling.
- finding: Claim (adoption, proposer_asserted, high materiality): The document states that Pallas is used as shared infrastructure by projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document reports Pallas has over 649 pull requests, 199 stars, 91 forks, 60 contributors, and 214,446 crates.io downloads, with GitHub and crates.io links provided for verification.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed work includes essential maintenance, community support, and AI-friendly documentation and integration resources.
- missing: Independent evidence for: The document states that Pallas is used as shared infrastructure by projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others.
- missing: Independent evidence for: The document states TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development on schedule, plus Intersect 2025 maintenance funding for Pallas, Dolos, and UTxO RPC that is being delivered on schedule.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Pallas maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The document states that Pallas is used as shared infrastructure by projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Pallas maintenance and enhancement and a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe established shared infrastructure, concrete maintenance deliverables, public repositories or dashboards for several verification points, and structured oversight for disbursement. The adjustment remains modest because several adoption and prior-delivery claims are proposer asserted, and treasury stewardship still requires caution on a 540,750 ADA spend.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The document states that Pallas is used as shared infrastructure by projects including Aiken, Dolos, Lucid, Oura, Mithril, Amaru, UTxO-RPC, and others.
- Claims and evidence missing: Independent evidence for: The document states TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 delivered and 4 under development on schedule, plus Intersect 2025 maintenance funding for Pallas, Dolos, and UTxO RPC that is being delivered on schedule.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `055faf20f076481ce84c9b98281873638ad9d6c589fee5cc921493209977a6b6`
- snapshot_bundle_hash: `e86bab12b5ef24f6fdcb879e602fed70a8a309681dcf424b3a2c33f8ea3f98e0`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5098, "NO": 0.0892, "YES": 0.401}`

