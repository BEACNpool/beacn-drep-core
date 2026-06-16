#!/usr/bin/env python3
"""Build the precomputed Stage-1/Stage-6 cache for the 9 active proposals.

Claims and human messages were produced by Claude (the reasoning layer) from each
proposal's cached anchor document and BEACN's deterministic verdict. The engine
consumes this via BEACN_DREP_LLM_CACHE and remains the sole writer of artifacts.

All 9 active actions currently resolve to ABSTAIN via the STALE_DATA freshness gate
(the latest export is ~8h old vs the 6h policy limit), so every message leads with
that procedural hold and then explains the proposal on its merits.
"""
import json
from pathlib import Path

OUT = Path("/home/ubuntudesktop/.openclaw/workspace/beacn-drep-core/data/output/llm_cache_active.json")

STALE = (
    "BEACN's autonomous DRep is recording ABSTAIN on this action, and the reason is "
    "procedural rather than a verdict on the proposal's merits. BEACN's on-chain governance "
    "data snapshot is currently about eight hours old, which is beyond the six-hour freshness "
    "limit its policy requires before it will cast a directional vote. When data is this stale "
    "BEACN holds rather than risk voting on an out-of-date picture of the proposal, the treasury, "
    "and the wider vote distribution."
)


def C(claim, category, support, materiality):
    return {"claim": claim, "category": category, "support": support, "materiality": materiality}


cache = {}

# 1. Reforming Treasury Governance (InfoAction, no funds)
cache["gov_action1t5ap7etluvct2x69nj5mfqhurgakuvekyflcsrv2qkrhrs378n3qq3z2c22"] = {
    "claims": {
        "request": {
            "what": "Open a community discussion on reforming Cardano treasury governance",
            "recipient": "Not applicable — informational action, no recipient",
            "amount_ada": "None (InfoAction requests no funds)",
            "deliverables": ["A set of basic propositions for treasury-governance reform, offered for public discussion"],
            "deadline": "Not stated — informational",
        },
        "claims": [
            C("Cardano treasury governance is in a poor state, with a funding impasse and only indirect support from the existing governance system", "governance", "proposer_asserted", "medium"),
            C("Competition between treasury-withdrawal domains has produced community conflict that endangers the ecosystem", "governance", "proposer_asserted", "medium"),
            C("Treasury governance should provide a clear direction, a coherent strategy and a defined process", "governance", "supported_in_proposal", "low"),
        ],
        "summary": "A non-binding InfoAction that requests no treasury funds and asks the community to discuss ideas for reforming treasury governance.",
    },
    "message": STALE + " On the substance, this is an InfoAction: it requests no treasury funds and is purely a call to discuss "
    "reforms to how Cardano governs treasury spending. Nothing is disbursed and nothing changes on-chain as a result of the vote, "
    "so the only thing at stake is whether BEACN lends its voice to opening that discussion. The proposer's claims that treasury "
    "governance is dysfunctional and conflict-prone are reasonable framing but are asserted rather than evidenced, which is acceptable "
    "for a discussion prompt. Once BEACN's data snapshot is refreshed inside the freshness window, it can move to a directional "
    "position on whether to signal support for the conversation, which carries no spending risk.",
}

# 2. Reimburse Ikigai Info Governance Action Deposit (103,000 ADA)
cache["gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq"] = {
    "claims": {
        "request": {
            "what": "Reimburse a 100,000 ADA Info-action deposit that was unrecoverable due to a Cardano node bug, plus 3,000 ADA for lost staking rewards",
            "recipient": "The original Ikigai Info governance action submitter",
            "amount_ada": "103,000 ADA",
            "deliverables": ["A one-time reimbursement payment; no ongoing deliverables"],
            "deadline": "Not stated",
        },
        "claims": [
            C("A node bug let an unregistered stake key be used, leaving the Ikigai submitter unable to recover a 100,000 ADA deposit", "technical", "independently_verifiable", "high"),
            C("An extra 3,000 ADA is requested to compensate for lost staking rewards at roughly 2% per annum", "economic", "proposer_asserted", "medium"),
            C("The action meets the constitution's metadata and treasury-withdrawal formatting requirements", "governance", "supported_in_proposal", "low"),
        ],
        "summary": "A 103,000 ADA one-time reimbursement to an early governance pioneer whose deposit was stranded by a node bug, plus a small staking-reward top-up.",
    },
    "message": STALE + " The request is narrow and sympathetic: 103,000 ADA to reimburse an early governance participant whose 100,000 ADA "
    "Info-action deposit was stranded by a documented Cardano node bug shortly after the Chang hard fork, plus 3,000 ADA for lost staking "
    "rewards. The core fact — that a node defect prevented recovery of the deposit — is independently checkable on-chain and is the strongest "
    "part of the case; the 2%-per-annum staking top-up is a reasonable but proposer-set figure. The amount is small relative to other live "
    "treasury actions and there is no ongoing delivery risk. Once BEACN's snapshot is current and the deep-research record confirms the bug "
    "and the recipient address, this is the kind of low-risk, well-bounded reimbursement on which it could reach a directional vote.",
}

# 3. IO: Hydra (5,100,781 ADA)
cache["gov_action1fah9m7dxu99af8jqdc4mkrgs3va790nyh9tfhycq2wsvrm47p4rsqtcm6ry"] = {
    "claims": {
        "request": {
            "what": "Fund four workstreams to harden and optimize Hydra v2 (performance, operational excellence, ecosystem support, developer experience) to deliver a production-grade Layer 2 scaling solution",
            "recipient": "IO (Input Output)",
            "amount_ada": "5,100,781 ADA",
            "deliverables": ["Feature-complete, hardened Hydra v2", "Performance optimization", "Operational tooling", "Ecosystem and developer-experience support"],
            "deadline": "Not explicitly dated in the extracted body",
        },
        "claims": [
            C("Hydra is the only production-grade Layer 2 on Cardano, already running live workloads for Delta DeFi, Masumi, Intersect and others", "adoption", "proposer_asserted", "high"),
            C("Cardano L1 offers ~2h finality, ~$0.17/tx and ~7-10 TPS, excluding high-performance verticals at the selection stage", "technical", "supported_in_proposal", "medium"),
            C("Hydra delivers sub-second finality and near-zero fees while settling to Cardano L1 as the security backstop", "technical", "supported_in_proposal", "high"),
            C("The four interdependent workstreams will produce a competitive, hardened Hydra v2", "technical", "proposer_asserted", "high"),
        ],
        "summary": "A 5.1M ADA IO request to harden Hydra v2, Cardano's main Layer 2, across four workstreams to make it a competitive, production-grade scaling solution.",
    },
    "message": STALE + " The proposal asks for about 5.1 million ADA for IO to harden and optimize Hydra v2, the Layer 2 the proposal "
    "describes as Cardano's only production-grade scaling solution, across four workstreams. The technical framing — L1's finality, fee and "
    "throughput limits, and Hydra's sub-second, near-zero-fee settlement back to L1 — is coherent and well-described in the document. The "
    "claims that matter most to the decision, namely real production adoption by named projects and the delivery of a feature-complete v2, "
    "are stated by the proposer and would need independent verification of current usage and milestone-gated delivery before a directional "
    "vote. As a multi-million-ADA treasury action it also requires a completed deep-research dossier. Until BEACN's data is fresh and that "
    "dossier and milestone evidence are in hand, it is holding rather than voting directionally.",
}

# 4. Reduce committeeMinSize from 7 to 5 (ParameterChange)
cache["gov_action1cadmygtqv6r64pvwezw859wg36wpwp209cz94cc7ej9fdp7dyphqq58n5ur"] = {
    "claims": {
        "request": {
            "what": "Reduce the minimum Constitutional Committee size (committeeMinSize) from 7 to 5 to improve operational resilience",
            "recipient": "Not applicable — protocol parameter change",
            "amount_ada": "None (ParameterChange)",
            "deliverables": ["On-chain change of committeeMinSize from 7 to 5"],
            "deadline": "Depends on enactment of a separate Plutus cost-model parameter-change action ahead of the van Rossem hard fork",
        },
        "claims": [
            C("With a 7-member committee and committeeMinSize of 7, a single resignation or term expiry would halt the Constitutional Committee and stall much of governance", "governance", "supported_in_proposal", "high"),
            C("Reducing the minimum to 5 improves resilience while keeping constitutional safeguards", "governance", "proposer_asserted", "high"),
            C("The change does not alter the current number of committee members or imply a smaller committee is desired", "governance", "supported_in_proposal", "medium"),
            C("The action was approved by Intersect's Civics Committee (2026-03-13) and Technical Steering Committee (2026-06-03)", "governance", "independently_verifiable", "medium"),
        ],
        "summary": "An Intersect-sponsored parameter change lowering the Constitutional Committee minimum from 7 to 5 to avoid a single resignation halting governance; no funds requested.",
    },
    "message": STALE + " This is a parameter change rather than a spend: it lowers the Constitutional Committee's minimum size from 7 to 5. "
    "The motivating risk is concrete and well-explained — with both the committee and its minimum at 7, a single resignation or term "
    "expiry would drop the committee below quorum and stall a large part of Cardano governance. The proposal is careful to note it does "
    "not change the current membership, and its sponsorship by Intersect's Civics and Technical Steering Committees is a matter of record "
    "that can be checked. Because it carries system-wide governance consequences and is tied to the enactment of a separate cost-model "
    "change ahead of the van Rossem hard fork, BEACN's policy requires fresh data and a clear read of the dependency before a directional "
    "vote. The hold here is procedural staleness, not opposition to the resilience rationale.",
}

# 5. Tweag Core Cardano Infrastructure 2026-2027 (18,263,496 ADA)
cache["gov_action1zljrlljt9cxlz7ra2nep43nxg0r54wcnrgexyuhuam9ah0ws607qq2vcg4x"] = {
    "claims": {
        "request": {
            "what": "Fund Tweag by Modus Create to deliver 3 interdependent work packages of core infrastructure, centred on mainnet deployment of Peras (faster finality), plus History Expiry and conformance testing",
            "recipient": "Tweag by Modus Create",
            "amount_ada": "18,263,496 ADA (stated USD $4,565,874)",
            "deliverables": ["Peras v1 production cryptography, KillSwitch and mainnet readiness", "History Expiry / partial-history nodes", "Conformance testing and correctness scaffolding"],
            "deadline": "2026-2027 delivery window",
        },
        "claims": [
            C("Peras v1 (faster finality, ~2 min vs ~12 min) remains undeployed on mainnet and requires production cryptography and hard-fork readiness", "technical", "supported_in_proposal", "high"),
            C("The 3 work packages are interdependent and should be funded as a single delivery pipeline, not a modular menu", "technical", "proposer_asserted", "medium"),
            C("The 18,263,496 ADA ask is based on $176/hour senior-engineer rates and a conservative 0.25 ADA/USD conversion", "economic", "proposer_asserted", "high"),
            C("Peras and Leios are required to unlock higher transaction volume, staking rewards and TVL", "economic", "proposer_asserted", "medium"),
        ],
        "summary": "An 18.26M ADA request for Tweag to deliver Peras mainnet finality plus History Expiry and conformance testing over 2026-2027, priced off senior-engineer hourly rates.",
    },
    "message": STALE + " At about 18.26 million ADA this is one of the largest live treasury actions, funding Tweag by Modus Create to "
    "deliver core protocol infrastructure — chiefly the mainnet deployment of Peras for faster finality, plus History Expiry and "
    "conformance testing. The technical need is well-documented: Peras v1 is genuinely not yet on mainnet and the work it describes is "
    "real. The budget is transparently derived from a stated hourly rate and ADA/USD assumption, which is good practice, but the rate, the "
    "hours and the single-pipeline framing are proposer-set figures that warrant independent cost scrutiny at this scale. A request of this "
    "size demands a completed deep-research dossier, milestone-gated disbursement and a clear view of treasury runway — exactly the checks "
    "BEACN cannot complete on an eight-hour-old snapshot. It is therefore holding until the data is fresh and that evidence is in hand.",
}

# 6. Rare Evo and Dev Gov Day 2026 sponsorship (2,750,000 ADA)
cache["gov_action18a9sytyez02jl8ee4ryz5xu7heg587m5tu6nr7fkd3ex30umnnjqq27e7ey"] = {
    "claims": {
        "request": {
            "what": "Fund Cardano as title sponsor of Rare Evo 2026 and the second Rare Dev Gov Day (July 28-31, 2026, Las Vegas)",
            "recipient": "Rare Network",
            "amount_ada": "2,750,000 ADA (stated USD $660,000 at $0.24)",
            "deliverables": ["Title sponsorship of the Rare Evo 2026 main stage and global livestream", "Support for Rare Dev Gov Day 2026", "Return of 20% of VIP ticket sales to the Cardano treasury"],
            "deadline": "Event dates July 28-31, 2026",
        },
        "claims": [
            C("Rare Network has operated in Cardano since 2020 and runs one of the largest independently operated blockchain conferences", "adoption", "proposer_asserted", "medium"),
            C("Title sponsorship will strengthen Cardano's global visibility, governance participation and developer engagement", "adoption", "proposer_asserted", "high"),
            C("Rare Network will return 20% of all VIP ticket sales (≈$900 retail) to the Cardano treasury", "economic", "proposer_asserted", "medium"),
            C("The ask is 2,750,000 ADA, valued at $660,000 at a $0.24 ADA price", "economic", "supported_in_proposal", "medium"),
        ],
        "summary": "A 2.75M ADA event-sponsorship request positioning Cardano as title sponsor of Rare Evo 2026 and Dev Gov Day, with a pledge to return 20% of VIP ticket sales to the treasury.",
    },
    "message": STALE + " The request is 2.75 million ADA to make Cardano the title sponsor of Rare Evo 2026 and the associated Dev Gov "
    "Day in Las Vegas, with a pledge to return 20% of VIP ticket sales to the treasury. Event sponsorship is inherently harder to evaluate "
    "than infrastructure: the central claims about reach, governance participation and developer engagement are marketing projections that "
    "are asserted rather than measured, and the value Cardano receives depends on outcomes that are difficult to verify after the fact. The "
    "20% VIP rebate is a sensible alignment mechanism but its dollar value is uncertain. For a spend of this size BEACN would want concrete, "
    "independently verifiable success metrics and a milestone or rebate structure before committing treasury funds, alongside its standard "
    "deep-research dossier. With the data snapshot stale, the correct action today is to hold rather than vote directionally.",
}

# 7. Cardano Critical Integrations V2 (23,000,000 ADA)
cache["gov_action1cp0w6zwgwpj98jtu3r2q838lgwmhs6j49l58zx4q05lx220lmzaqqztnljz"] = {
    "claims": {
        "request": {
            "what": "Fund a Year-2 contracted cost and a 12-month enhancement and maintenance program for critical integrations delivered under CCI V1 (Circle USDCx, LayerZero, Pyth, Dune), plus a new native Fireblocks integration",
            "recipient": "The Cardano Critical Integrations team / partners",
            "amount_ada": "23,000,000 ADA (stated USD $5,750,000 at $0.25)",
            "deliverables": ["12 months operations and maintenance of CCI V1 integrations", "Contracted Year-2 licensing/platform fees for Circle, LayerZero, Pyth, Dune", "New full native Fireblocks integration"],
            "deadline": "12-month program",
        },
        "claims": [
            C("CCI V1 integrations (Circle, LayerZero, Pyth, Dune) require ongoing annual licensing/service payments to remain operational", "economic", "supported_in_proposal", "high"),
            C("Without maintenance funding the previously delivered integrations risk degradation or going offline", "technical", "proposer_asserted", "high"),
            C("The program creates a recurring annual treasury dependency for third-party infrastructure", "economic", "supported_in_proposal", "high"),
            C("A new full native Fireblocks integration is included alongside maintenance of existing ones", "technical", "proposer_asserted", "medium"),
        ],
        "summary": "A 23M ADA request to pay Year-2 licensing and 12 months of maintenance for the Circle/LayerZero/Pyth/Dune integrations and to add Fireblocks — a recurring treasury dependency.",
    },
    "message": STALE + " This action requests 23 million ADA to cover Year-2 licensing and twelve months of maintenance for integrations "
    "delivered under the first Critical Integrations budget — Circle USDCx, LayerZero, Pyth and Dune — and to add a native Fireblocks "
    "integration. The proposal is candid that these are recurring costs: the named integrations need ongoing annual payments to stay live. "
    "That candour is useful, but it also surfaces the central risk BEACN weighs heavily — a standing, recurring treasury dependency on "
    "third-party infrastructure, where declining to fund later could strand work already paid for. The maintenance-need claims are partly "
    "evidenced by the contracts described, while the consequences of under-funding are asserted. A large, recurring commitment like this "
    "needs a completed dossier, line-item licensing costs and a sustainability plan that reduces dependence over time. With stale data, "
    "BEACN holds rather than voting directionally.",
}

# 8. 5am.earth Trust Layer (10,000,000 ADA)
cache["gov_action142ndnn9hycuuwld5ddemash2l709ln06qjgfeudq77z45nf3fpdqqn7pwux"] = {
    "claims": {
        "request": {
            "what": "Build an open, Cardano-anchored trust layer for global agricultural supply chains using Veridian self-sovereign identity and a Cardano on-chain satellite oracle",
            "recipient": "5am.earth Foundation",
            "amount_ada": "10,000,000 ADA (hard cap)",
            "deliverables": ["M1 Stand-Up (Month 6)", "M2 Closed Loop (Month 12)", "M3 Self-Sustaining (Month 18)", "500,000 registered farmers across India, Cambodia and Kenya"],
            "deadline": "18-month programme",
        },
        "claims": [
            C("The programme will reach 500,000 registered farmers across India, Cambodia and Kenya during the funded period", "adoption", "proposer_asserted", "high"),
            C("Around 500 million smallholder farmers lack formal trust infrastructure that lenders, insurers and certifiers rely on", "economic", "independently_verifiable", "medium"),
            C("The 18-month programme is structured around three named milestones (M1 Stand-Up, M2 Closed Loop, M3 Self-Sustaining)", "technical", "supported_in_proposal", "high"),
            C("The trust layer combines Veridian self-sovereign identity with a Cardano on-chain satellite oracle and will become self-sustaining", "technical", "proposer_asserted", "high"),
        ],
        "summary": "A 10M ADA (hard-capped) 18-month programme to build a Cardano-anchored agricultural trust layer reaching 500,000 farmers across three countries, with three defined milestones.",
    },
    "message": STALE + " The 5am.earth Foundation requests up to 10 million ADA, hard-capped, to build a Cardano-anchored trust layer for "
    "agricultural supply chains, combining self-sovereign identity for farmers with an on-chain satellite oracle. The proposal is notably "
    "well-structured for a venture of this kind: it is milestone-based (Stand-Up at month six, Closed Loop at month twelve, Self-Sustaining "
    "at month eighteen) and hard-capped, both of which are positive treasury-control signals. The headline reach figure of 500,000 farmers "
    "across India, Cambodia and Kenya, and the claim that the system becomes self-sustaining, are ambitious and currently asserted; the "
    "broader problem it targets is real and checkable. The decisive questions for a vote are execution risk in three developing-market "
    "geographies and whether disbursement is genuinely gated on the named milestones. BEACN needs fresh data and a completed dossier to "
    "weigh those, so it is holding today.",
}

# 9. Eternl: Path to Sustainability (1,680,000 ADA)
cache["gov_action1ngpqafax5rvp8lcgey4asvqtycrh4e56fwp8cn2r9trx2ysryhtsqdm3w3z"] = {
    "claims": {
        "request": {
            "what": "Fund 12 months of operations, maintenance and improvements for the Eternl non-custodial Cardano wallet while it transitions toward a paid Pro plan",
            "recipient": "Eternl",
            "amount_ada": "1,680,000 ADA (stated ≈$420,000/year)",
            "deliverables": ["12 months of frontend/backend maintenance and development", "Backend infrastructure and user support", "Launch of a paid Pro plan toward self-sustainability"],
            "deadline": "12-month period (2026-2027)",
        },
        "claims": [
            C("Eternl serves about 100,000 browser-extension users and ~30,000 across Android and iOS", "adoption", "proposer_asserted", "high"),
            C("Roughly 5,500 Pro subscribers (≈4.2% of the install base) would fully cover the ~$420,000 annual cost", "economic", "proposer_asserted", "high"),
            C("Annual operating cost is around $420,000 (~1,680,000 ADA)", "economic", "supported_in_proposal", "medium"),
            C("Eternl is a primary gateway for Cardano payments, staking, governance and DApp interaction", "adoption", "proposer_asserted", "medium"),
        ],
        "summary": "A 1.68M ADA request to fund one year of Eternl wallet operations while it launches a paid Pro plan intended to make it self-sustaining.",
    },
    "message": STALE + " Eternl requests about 1.68 million ADA — roughly $420,000 — to fund a year of operations and maintenance for its "
    "widely used non-custodial wallet while it stands up a paid Pro plan intended to make it self-sustaining. The proposal's strength is "
    "that it names a concrete path off treasury funding: it estimates that around 5,500 Pro subscribers, about 4.2% of its install base, "
    "would cover annual costs. That conversion assumption is the load-bearing claim and is currently the proposer's projection rather than "
    "demonstrated revenue, and the install-base figures are self-reported. The amount is modest relative to other live actions and the "
    "public good of a maintained, widely used wallet is real. The directional question is the credibility of the sustainability plan and "
    "whether funding is staged against it. BEACN is holding only because its data snapshot is stale; once fresh, this is a tractable case.",
}

OUT.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"wrote {OUT} with {len(cache)} entries")
for aid, v in cache.items():
    print(f"  {aid[:30]}  claims={len(v['claims']['claims'])}  msg_chars={len(v['message'])}")
