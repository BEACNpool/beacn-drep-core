# Rationale: gov_action1jr84r96lnsvu9yd6c0jhxe9gj5r7vnd2pgkntc6klplxdpyzz4tqqc9uldx
Recommendation: **ABSTAIN**
Score: `0.01` (raw `0.01` + doctrine-LLM nudge `+0.03`) | Confidence: `0.5725` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a info action: 8 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on Budget: ₳5M Loan for Cardano's Global Listing Expansion - Powered by Snek. This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a InfoAction. The cached anchor describes the request as: Budget: ₳5M Loan for Cardano's Global Listing Expansion - Powered by Snek. The strongest grounded claim is: This proposal seeks a 5,000,000 ada budget loan from the Cardano Treasury to fund the Cardano Global Listing Expansion, a strategic initiative led by the Snek Foundation to list SNEK on top-tier centralized exchanges, retail brokers, and trading platforms.

Reason code: RULE_THRESHOLD_UNMET.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: InfoAction
- finding: Status: expired
- finding: Proposed epoch: 580
- finding: Expires after epoch: 587
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Budget: ₳5M Loan for Cardano's Global Listing Expansion - Powered by Snek
- finding: Recipient: 
- finding: Stated amount: not stated in document
- finding: Deliverables: This proposal seeks a 5,000,000 ada budget loan from the Cardano Treasury to fund the Cardano Global Listing Expansion, a strategic initiative led by the Snek Foundation to list SNEK on top-tier centralized exchanges, retail brokers, and trading platforms., This proposal is the first-ever loan-based treasury withdrawal in Cardano governance, introducing a new model of accountability where funds are not given as grants but repaid with interest., As part of the governance process, a Board of Advisors will be appointed to ensure transparent execution and maximize ecosystem alignment., This board will include high-profile industry veterans like Tal Cohen (former CEO of Kraken), Phillip Pon (CEO of Emurgo), Fahmi Syed (President of Midnight Foundation), and Frederik Gregaard (CEO of Cardano Foundation), with additional top-tier names to be...
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, independently_verifiable, high materiality): This proposal seeks a 5,000,000 ada budget loan from the Cardano Treasury to fund the Cardano Global Listing Expansion, a strategic initiative led by the Snek Foundation to list SNEK on top-tier centralized exchanges, retail brokers, and trading platforms.
- finding: Claim (economic, independently_verifiable, high materiality): This proposal is the first-ever loan-based treasury withdrawal in Cardano governance, introducing a new model of accountability where funds are not given as grants but repaid with interest.
- finding: Claim (governance, independently_verifiable, medium materiality): As part of the governance process, a Board of Advisors will be appointed to ensure transparent execution and maximize ecosystem alignment.
- finding: Claim (other, independently_verifiable, low materiality): This board will include high-profile industry veterans like Tal Cohen (former CEO of Kraken), Phillip Pon (CEO of Emurgo), Fahmi Syed (President of Midnight Foundation), and Frederik Gregaard (CEO of Cardano Foundation), with additional top-tier names to be...
- finding: Claim (adoption, independently_verifiable, low materiality): Who we are Snek Foundation is a grassroots organization responsible for launching and maintaining the SNEK ecosystem.
- finding: Claim (economic, independently_verifiable, high materiality): Snek has never raised external funds for exchange listings and has operated for the past 29 months, entirely self-funded through its revenue and treasury.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "This proposal seeks a 5,000,000 ada budget loan from the Cardano Treasury to fund the Cardano Global Listing Expansion, a strategic initiative led by the Snek Foundation to list SNEK on top-tier centralized exchanges, retail brokers, and trading platforms." and clears the evidence gates.
- finding: Strongest NO: weak controls, unclear delivery, or governance precedent could outweigh the benefit of InfoAction.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Flag score present (3), reducing confidence.
- Intake: Action type: InfoAction
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This proposal seeks a 5,000,000 ada budget loan from the Cardano Treasury to fund the Cardano Global Listing Expansion, a strategic initiative led by the Snek Foundation to list SNEK on top-tier centralized exchanges, retail brokers, and trading platforms." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was +0.030 (display cap ±0.05) and had zero influence on the binding score: Doctrine-aware offline lean for a info action: 8 well-supported claim(s). Net bounded adjustment +0.030 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Rule-based system; does not infer unstated intent.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `fd4fe82911c3e1201a2551fbd0d71de617aaca1d4d0b0435d852c73322d92fe9`
- snapshot_bundle_hash: `81ad58e51ad53d28a9124a87334b39409819582d1061a791e9b2774b74fb7b6d`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `15`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.4631, "NO": 0.2584, "YES": 0.2784}`

