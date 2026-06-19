# Rationale: gov_action1vrkk4dpuss8l3z9g4uc2rmf8ks0f7j534zvz9v4k85dlc54wa3zsqq68rx0
Recommendation: **NO**
Score: `-0.3033` (raw `-0.3233` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7933` | Readiness: `0.0`
> Reasoning layer (codex-offline-review): Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).

## Plain-language explanation (codex-offline-review)
BEACN records NO on Amaru Treasury Withdrawal 2025. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Amaru Treasury Withdrawal 2025. The recorded treasury amount is 1.50M ADA. The strongest grounded claim is: Amaru is an open-source project implementing a new fully interoperable block-producing node for Cardano.

Residual uncertainty remains limited to the replayed evidence and the public resources cited by the run manifest.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 566
- finding: Expires after epoch: 573
- finding: Treasury request: 1.50M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: complete
- finding: Requested: Amaru Treasury Withdrawal 2025
- finding: Recipient: 
- finding: Stated amount: 1.50M ADA
- finding: Deliverables: Amaru is an open-source project implementing a new fully interoperable block-producing node for Cardano., It aims to improve the network's overall accessibility and robustness without compromising its safety and security., This treasury withdrawal of ₳1.5M follows a previously submitted and now approved budget proposal., It is split across five script addresses each covering a scope of a work (ledger, consensus, mercenaries and marketing) and a contingency reserve.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, independently_verifiable, low materiality): Amaru is an open-source project implementing a new fully interoperable block-producing node for Cardano.
- finding: Claim (economic, independently_verifiable, high materiality): It aims to improve the network's overall accessibility and robustness without compromising its safety and security.
- finding: Claim (economic, independently_verifiable, high materiality): This treasury withdrawal of ₳1.5M follows a previously submitted and now approved budget proposal.
- finding: Claim (economic, independently_verifiable, low materiality): It is split across five script addresses each covering a scope of a work (ledger, consensus, mercenaries and marketing) and a contingency reserve.
- finding: Claim (economic, independently_verifiable, low materiality): Who we are Amaru is a multi-entity effort that currently sits under PRAGMA: a member-based, not-for-profit association for open-source blockchain software projects.
- finding: Claim (economic, independently_verifiable, low materiality): Five members with equal power currently drive PRAGMA's strategy and operations: Blink Labs, Cardano Foundation, dcSpark, Sundae Labs, and TxPipe.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1.50M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable
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
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Amaru is an open-source project implementing a new fully interoperable block-producing node for Cardano." and clears the evidence gates.
- finding: Strongest NO: weak controls, unclear delivery, or governance precedent could outweigh the benefit of TreasuryWithdrawals.
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
- Treasury analysis: Requested ADA: 1.50M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Amaru is an open-source project implementing a new fully interoperable block-producing node for Cardano." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by +0.020 (clamped to ±0.05): Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury fee-flow signal is in unsustainable regime (advisory penalty applied).
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `46f314fc29fe72df2246b793971c68e38f375afd1e18cd6cbdff960890bc0cdc`
- snapshot_bundle_hash: `5ea6f4fa4572bbc56d1a1a041006fedba28a2426bd1ddd8ec6c0695c2c55444f`
- soul_commit: `6bf4a7d7baa636417ad929e543cfb8be8fae1f03`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `20e0915ebc437140b55ee25e28adbae01e97032d`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `275`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1985, "NO": 0.7565, "YES": 0.0449}`

