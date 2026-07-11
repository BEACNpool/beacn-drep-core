# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the hard fork is high-impact and the required readiness evidence was not complete. This is a conservative, evidence-based hold, not a rejection of the upgrade’s goals.

The action asks Cardano mainnet to move from protocol version 10.0 to 11.0 in an intra-era hard fork that remains in Conway. The proposal says this would add new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153, make Plutus built-ins consistently available across Plutus V1, V2, and V3, support native case expressions in Untyped Plutus Core, and tighten several ledger and node validation rules.

Several core claims were reviewable: the pinned anchor was available, the protocol-version change was clearly stated, the linked CIPs and performance results were checkable, and the proposal acknowledged the need for at least 85% stake pool readiness before ratification. But important claims were still too thin for a directional vote: performance gains from case expressions, full no-regression testing, audit details, mitigation evidence, independent assurance, and a complete readiness packet covering stake pools, exchanges, dApps, testnet results, constitutional alignment, security review, and rollback or containment planning.

Because hard forks are permanent, operator-sensitive changes, BEACN’s rules require more than proposer assertions for readiness and risk. A YES or NO vote would be unblocked by independently pinned evidence for the missing readiness checks, security review details, mitigation evidence, and testing results showing the upgrade is safe to execute across the ecosystem.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
