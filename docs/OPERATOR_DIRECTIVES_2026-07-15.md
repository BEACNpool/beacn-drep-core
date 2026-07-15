# Operator Directives — 2026-07-15

Governance record of a delegation of authority. On 2026-07-15 David (the
principal) directed the operator agent to proceed with the full hardening
roadmap and delegated the open values calls that the roadmap had parked,
under the mission framing:

> **"Serve the ecosystem; grow and maintain Cardano in the strongest way
> possible."**

This document records the twelve resolutions made under that delegation, each
with its rationale. It is a record of decisions and their reasoning — not
code. Where a resolution requires doctrine or code changes, those changes ship
through their own gated paths (doctrine amendment protocol, PR review, shadow
validation) and this document is the trace back to who decided what, when, and
why.

## Resolutions

### 1. Envelope-blocked verdicts are capacity-NO, never ABSTAIN

When a treasury ask is blocked purely because the spending envelope (NCL /
budget capacity) cannot accommodate it, the vote is **NO**, not ABSTAIN. In
Conway ratification arithmetic an explicit ABSTAIN removes the DRep's stake
from the denominator, which mechanically *eases* the action's path to
passage — an abstention "on capacity grounds" therefore acts as a mild
endorsement, the opposite of what the verdict means. A capacity block is a
substantive judgment that the treasury cannot afford the ask right now; the
honest on-chain expression of that judgment is NO, with the capacity reasoning
stated in the public rationale.

### 2. Bootstrap-envelope glide (DRAFT ONLY until doctrine v2.0.0)

The bootstrap-subsidy envelope coefficient beta starts at **0.65** and
declines by approximately **0.05 per 73-epoch tranche** (one year), indexed to
epoch — not wall-clock — with a floor of **0**, reaching it around 2033. The
design intent is that the ecosystem's tolerance for subsidized, non-revenue
spending sunsets *ahead of* the reserve's ~5.5–5.8-year half-life, so the
treasury is never still underwriting bootstrap-era generosity after the
funding source that justified it has substantially decayed. This schedule is
**DRAFT ONLY**: it binds nothing until doctrine v2.0.0 ships through the
amendment protocol with shadow validation demonstrating what it would have
changed on the historical ballot.

### 3. Marketing/growth prior: presumed-FAIL-but-rebuttable; DeFi liquidity incentives: hard fail

Marketing and growth-category treasury asks carry a rebuttable presumption of
failure: the category's track record of unverifiable outcomes and
self-reported metrics puts the burden of proof on the proposer, but strong
independent evidence of measurable, attributable ecosystem value can rebut it
case by case. DeFi liquidity incentives are a **hard fail** — no rebuttal
path — because the mechanism is private capture by construction: treasury
funds flow directly to the positions of whoever supplies liquidity during the
incentive window, the "benefit" evaporates when emissions stop, and the
structure cannot be redeemed by better execution. A category prior that
depends on execution quality is rebuttable; one that fails by construction is
not.

### 4. Script-credential DRep migration: approved in principle

Migrating the DRep from a key credential to a script credential (enabling
on-chain enforcement of constraints the signing adapter currently enforces
off-chain) is approved in principle. Sequencing is strict: a written plan
first, then a full preprod rehearsal, and execution only with David's direct
participation — because the migration creates a new DRep identity and every
delegator must actively re-delegate to it once. That re-delegation cost is
paid exactly once and only for a validated design, never for an experiment.

### 5. Doctrine amendments become PR-gated with published cross-model adversarial review

Every doctrine amendment now travels through a pull request, and the review
includes an adversarial pass by a model independent of the one that drafted
the change, with the adversarial review published alongside the amendment.
Doctrine is the one layer that can silently repoint every downstream vote;
single-author edits to it — human or model — are the highest-leverage failure
path this system has. Publishing the adversarial review keeps the disagreement
auditable instead of resolved invisibly.

### 6. Corrections log ships with full candor, including the June-era on-chain anchor defects

The public corrections log ships complete: it includes the June-era defects in
on-chain rationale anchors alongside every other correction, stated plainly.
A transparency system that curates its own error history is doing exactly the
thing it exists to prevent; the credibility of every future rationale rests on
the record showing that when this system was wrong, it said so first and
specifically. Candor about past defects is cheaper than the discount the
public correctly applies to a sanitized log.

**Amended later the same day (David's direction):** the corrections *page* was
removed from the pre-launch site — beta-era defects will not headline a product
that has not launched. `corrections.json` remains published in the repo,
append-only and hash-chained, so the record is intact and provable; the page
returns (or its content folds into a launch retrospective) when the site goes
public. The data was never curated; only its placement changed.

### 7. No git-history rewrite of the web repo; retention + mirror removal instead; data-repo split deferred and pre-announced

The web repo's git history is not rewritten. History rewriting on a public
transparency repo destroys the very property the repo exists to provide —
that past states remain verifiable — and breaks every clone and pinned commit
downstream. Instead: a retention policy going forward, removal of the
redundant mirror that doubled every artifact commit, and a possible future
split of bulky data into a dedicated data repo. That split is deferred, and if
it happens it will be pre-announced so no one auditing the record is surprised
by a layout change.

### 8. The DRep stays fully agentic — no human approval gate — with anomaly rate-guards as the compensating control

No human approval gate is added to the voting path. The system's value
proposition is a DRep whose behavior is fully determined by published
doctrine, published evidence, and deterministic gates — a human sign-off step
reintroduces exactly the private, unauditable judgment the architecture
removes, and in practice becomes a rubber stamp that dilutes accountability
without adding safety. The compensating control is mechanical: anomaly
rate-guards (per-run vote caps, fee caps, debounce persistence, and the
fail-closed gate stack) bound the damage of any single bad run, and the kill
switch remains one environment variable away.

### 9. Delegation-growth posture: hold flat until the rubric/budget doctrine lands through shadow validation; publish a self-pivotality metric

The DRep does not campaign for delegation growth until the treasury
rubric/budget doctrine has shipped through shadow validation. Soliciting stake
while the decision framework that stake would amplify is still being hardened
gets the order of operations backwards. In parallel, the system will publish a
self-pivotality metric — how often this DRep's stake was actually decisive in
ratification outcomes — so both delegators and the operator can see the
system's real marginal influence rather than inferring it from raw stake
numbers.

### 10. No autonomous emergency fast-path; the break-glass runbook is the operator lane

The system gets no autonomous "emergency mode" that relaxes gates under time
pressure. Expiry pressure is precisely the condition under which an automated
shortcut would be most tempting and least safe — every gate exists because
its absence already caused or nearly caused a wrong action. The escape lane
for a red pipeline near an expiry is a human operator following
`docs/BREAK_GLASS_VOTE_RUNBOOK.md`, which drives the same gated code by hand
and skips nothing.

### 11. Orchestration stays in the workspace repo for now; a dedicated beacn-drep-ops repo is deferred

The cron wrappers and orchestration scripts remain in the private workspace
repo rather than moving into a fifth public repo now. The 4-repo separation
(soul/resources/core/web) covers everything that determines or evidences a
vote; the orchestration layer determines only *when* the deterministic
pipeline runs, not what it decides. A dedicated `beacn-drep-ops` repo is
deferred until it can be created under David's own GitHub account, so its
provenance matches the other four from its first commit.

### 12. CIP-100 vote anchors deferred until anchor permanence ships; no CIP-136 conformance claims

Adopting CIP-100 JSON-LD metadata for vote anchors is deferred until an
anchor-permanence commitment — IPFS pinning plus stable URLs — ships first.
Upgrading the anchor *format* before guaranteeing the anchor *persists* would
add machine-readable polish to references that can still rot, which is
backwards for a system whose gate 4 hash-verifies anchors at vote time.
Separately, the system makes no CIP-136 conformance claims: CIP-136 is scoped
to Constitutional Committee vote rationales, and claiming conformance as a
DRep would be borrowing a standard that does not apply.

---

*Recorded 2026-07-15 by the operator agent under David's delegation. Doctrine
changes referenced above (resolutions 1–3) remain non-binding drafts until
they ship through the beacn-drep-soul amendment protocol.*
