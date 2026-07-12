# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.1515` (raw `-0.11` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7579` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a public-good maintenance proposal for established wallet infrastructure with concrete deliverables, oversight, return-of-unspent-funds commitments, and some independently verifiable success metrics. The nudge is small because several important adoption, uniqueness, and cost-efficiency claims remain proposer-asserted, and treasury stewardship cautions against giving much extra weight beyond the deterministic assessment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal requests 1,785,333 ADA for Daedalus Wallet maintenance and improvements in 2026-2027, delivered by Se7en Labs and administered through Intersect with monthly milestone-based disbursements. The work includes protocol and backend maintenance, hard fork readiness, stable releases before mainnet hard forks, hardware wallet support, CIP-30 dApp connector work, user support including Japanese-language support, translation work, and an architecture assessment by Q3 2027.

Several parts of the case were supported well enough to take seriously. The review found a pinned, replayable proposal anchor, concrete deliverables, Intersect administration and milestone controls, and independently verifiable release-timing and version-currency commitments. It also found support for the claim that Se7en Labs assumed Daedalus responsibility under an IOG contract in January 2026 and has shipped specific improvements since then. But other important claims remained unsupported or only proposer-asserted, including that Daedalus is Cardano’s only full-node desktop wallet, that it avoids third-party APIs or trusted backends, and that it has about 4,000 monthly active users with a higher true count.

This is a conservative, evidence-based hold, not a rejection of the work. Treasury withdrawals require elevated scrutiny because they spend shared ADA and set precedent. A directional vote would be unblocked by independently pinned public-chain evidence showing the action does not breach the applicable Net Change Limit, along with stronger independent evidence for the unsupported wallet-uniqueness, adoption, sustainability, cost-benefit, assurance, and remedy-path questions.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 1.79M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Daedalus Wallet maintenance and improvements for 2026-2027 as a time-and-materials engagement delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc., administered through Intersect with milestone-based monthly disbursement controls.
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance, node and wallet backend updates, hard fork readiness, and compatible stable releases at least 2 weeks before each mainnet hard fork, Keystone and Flex hardware wallet support, plus newer hardware wallet models as they emerge during the contract period, CIP-30 dApp connector implementation within Daedalus with documentation and interoperability verification, Responsive user support, including Japanese-language support and full Japanese translation across shipped features, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: Contract year through 2026-2027; Architecture assessment by Q3 2027; IOG contract noted as closing August 31, 2026
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, high materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting the true count is higher.
- finding: Claim (technical, supported_in_proposal, high materiality): Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril snapshot bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization since then.
- finding: Claim (technical, independently_verifiable, high materiality): The proposal commits to stable Daedalus releases at least 2 weeks before each mainnet hard fork and to keeping cardano-node no more than 2 major versions behind the mainnet recommendation.
- finding: Claim (technical, independently_verifiable, high materiality): All release-timing and version-currency metrics are claimed to be independently verifiable from public GitHub repositories and the Cardano mainnet chain.
- finding: Claim (economic, supported_in_proposal, high materiality): The work package total is 1,785,333 ADA, consisting of 1,666,667 ADA for maintenance and improvements, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting the true count is higher.
- missing: Independent evidence for: Any unspent labor, hardware, or audit budget at contract close will be returned to the treasury.
- missing: Independent evidence for: Se7en Labs states it has not received ADA from the Cardano Treasury within the last 24 months.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.70
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
- finding: Strongest YES: the proposal substantiates "Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril snapshot bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization since then." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril snapshot bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, and Nix build modernization since then." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a public-good maintenance proposal for established wallet infrastructure with concrete deliverables, oversight, return-of-unspent-funds commitments, and some independently verifiable success metrics. The nudge is small because several important adoption, uniqueness, and cost-efficiency claims remain proposer-asserted, and treasury stewardship cautions against giving much extra weight beyond the deterministic assessment.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting the true count is higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `868e7b5c5af18b033b4c8e8ccead33ca8b1ab8aa7ba7e7e3f47cf59633f3103a`
- snapshot_bundle_hash: `2962ec338b5cc13dd91e791d0cb53407d4afa01cc7dc9f95b3017eb6196b1c2b`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `45e29dd06273ee8ec35264b00dafd2aa30667f62`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5095, "NO": 0.0938, "YES": 0.3968}`

