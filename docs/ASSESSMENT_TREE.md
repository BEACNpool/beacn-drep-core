# Assessment Tree

BEACN must not publish a final vote rationale from a shallow score or a short
plain-language statement. Each decision run first builds an `assessment.json`
artifact, then derives the vote rationale from that structured review.

## Required Review Sections

1. Intake
   - action type, status, proposed/expiry epochs, treasury amount, anchor status
   - blocks when baseline governance fields or integrity anchors are missing

2. Claims and evidence
   - source freshness, pinned anchor availability, dossier status, analyst notes
   - distinguishes proposer assertions from replayable public evidence

3. Treasury analysis
   - treasury actions only
   - budget granularity, milestone gates, clawback/refund path, sustainability,
     cost/benefit clarity, treasury-flow regime

4. Risk review
   - execution, governance, technical, and treasury exposure risks
   - mitigation evidence, independent assurance, rollback/remedy path,
     dependency map

5. Counterargument pass
   - strongest YES case
   - strongest NO case
   - strongest ABSTAIN / hold case

6. Synthesis
   - decisive blockers and remaining questions
   - confirms that the final vote is derived from the completed review tree

## Output Contract

Every run should emit:

- `assessment.json` — structured review tree
- `rationale.json` — binding vote/rationale artifact embedding assessment status
- `rationale.md` — public readable artifact including the review tree
- `input_manifest.json` — replay and resource hash manifest

`NEEDS_MORE_INFO` is not a lazy final answer. It must name the missing review
sections or evidence required to reach a directional vote. When evidence remains
insufficient near expiry, policy should decide whether to submit `ABSTAIN`.
