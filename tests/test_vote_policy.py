"""Tests for the deterministic vote-revision policy (anti-churn)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from beacn_drep import vote_policy as vp  # noqa: E402

CFG = dict(vp.DEFAULTS)  # min_persistence_*=2, hysteresis_margin=0.04, min_confidence=0.60


def hist(*recs):
    return [{"recommendation": r, "score": 0.0, "run_id": f"r{i}"} for i, r in enumerate(recs)]


class PersistenceTests(unittest.TestCase):
    def test_trailing_count(self):
        self.assertEqual(vp.persistence(hist("NO", "ABSTAIN", "ABSTAIN"), "ABSTAIN"), 2)
        self.assertEqual(vp.persistence(hist("ABSTAIN", "NO"), "ABSTAIN"), 0)
        self.assertEqual(vp.persistence(hist(), "NO"), 0)

    def test_record_idempotent_per_run(self):
        led = {}
        vp.record(led, "a1", "NO", -0.2, "runX", cap=60)
        vp.record(led, "a1", "NO", -0.2, "runX", cap=60)  # same run_id -> replace
        self.assertEqual(len(led["a1"]), 1)
        vp.record(led, "a1", "NO", -0.2, "runY", cap=60)  # new run -> append
        self.assertEqual(len(led["a1"]), 2)


class FreshVoteTests(unittest.TestCase):
    def test_fresh_abstain_casts_immediately(self):
        d = vp.decide(recommendation="ABSTAIN", score=-0.05, confidence=0.5,
                      directional_threshold=0.12, onchain_vote=None,
                      history=hist("ABSTAIN"), cfg=CFG)
        self.assertEqual(d.action, "CAST")

    def test_fresh_directional_held_until_persistent(self):
        d = vp.decide(recommendation="NO", score=-0.20, confidence=0.5,
                      directional_threshold=0.12, onchain_vote=None,
                      history=hist("NO"), cfg=CFG)  # persist=1 < 2, conf<0.60
        self.assertEqual(d.action, "HOLD")

    def test_fresh_directional_casts_when_persistent(self):
        d = vp.decide(recommendation="NO", score=-0.20, confidence=0.5,
                      directional_threshold=0.12, onchain_vote=None,
                      history=hist("NO", "NO"), cfg=CFG)
        self.assertEqual(d.action, "CAST")

    def test_fresh_directional_casts_when_confident(self):
        d = vp.decide(recommendation="YES", score=0.20, confidence=0.75,
                      directional_threshold=0.12, onchain_vote=None,
                      history=hist("YES"), cfg=CFG)  # persist=1 but conf>=0.60
        self.assertEqual(d.action, "CAST")


class RevisionTests(unittest.TestCase):
    def test_noop_when_aligned(self):
        d = vp.decide(recommendation="ABSTAIN", score=-0.05, confidence=0.5,
                      directional_threshold=0.12, onchain_vote="Abstain",
                      history=hist("ABSTAIN", "ABSTAIN"), cfg=CFG)
        self.assertEqual(d.action, "NOOP")

    def test_revision_held_when_not_persistent(self):
        # on-chain NO, engine just flipped to ABSTAIN for one run
        d = vp.decide(recommendation="ABSTAIN", score=-0.05, confidence=0.5,
                      directional_threshold=0.12, onchain_vote="VoteNo",
                      history=hist("NO", "ABSTAIN"), cfg=CFG)  # persist=1 < 2
        self.assertEqual(d.action, "HOLD")
        self.assertIn("not persistent", d.reason)

    def test_revision_to_abstain_approved_when_persistent_and_clear(self):
        # ABSTAIN held 2 runs, score -0.05 is clearly inside the dead-band (margin -0.07 < -0.04)
        d = vp.decide(recommendation="ABSTAIN", score=-0.05, confidence=0.5,
                      directional_threshold=0.12, onchain_vote="VoteNo",
                      history=hist("ABSTAIN", "ABSTAIN"), cfg=CFG)
        self.assertEqual(d.action, "REVISE")

    def test_revision_to_abstain_held_within_hysteresis(self):
        # persistent ABSTAIN but score -0.10 is within hysteresis of threshold 0.12
        # margin = 0.10 - 0.12 = -0.02 ; -0.02 > -0.04 -> still too close, HOLD
        d = vp.decide(recommendation="ABSTAIN", score=-0.10, confidence=0.5,
                      directional_threshold=0.12, onchain_vote="VoteNo",
                      history=hist("ABSTAIN", "ABSTAIN"), cfg=CFG)
        self.assertEqual(d.action, "HOLD")
        self.assertIn("hysteresis", d.reason)

    def test_revision_to_directional_requires_margin(self):
        # persistent NO but score -0.13 only 0.01 past threshold (< hysteresis 0.04) -> HOLD
        d = vp.decide(recommendation="NO", score=-0.13, confidence=0.5,
                      directional_threshold=0.12, onchain_vote="Abstain",
                      history=hist("NO", "NO"), cfg=CFG)
        self.assertEqual(d.action, "HOLD")

    def test_revision_to_directional_approved_with_margin(self):
        d = vp.decide(recommendation="NO", score=-0.20, confidence=0.5,
                      directional_threshold=0.12, onchain_vote="Abstain",
                      history=hist("NO", "NO"), cfg=CFG)
        self.assertEqual(d.action, "REVISE")


class EvidenceAbsenceCannotRetractTests(unittest.TestCase):
    """Missing evidence must never pull a cast directional vote back off the chain.

    Regression: on 2026-07-11 the live run logged
    "revision YES->ABSTAIN held: not persistent (persist=1/2)" for the van Rossem hard
    fork. The ABSTAIN existed only because decision_support/protocol_readiness_profiles.csv
    was header-only (no producer script exists), which drove score to 0.0 — deep inside the
    dead-band, so hysteresis *approved* the retraction. The next run would have hit
    persist=2/2 and retracted a real on-chain YES over an empty file.
    """

    def test_van_rossem_scenario_holds_instead_of_retracting(self):
        d = vp.decide(recommendation="ABSTAIN", score=0.0, confidence=0.5,
                      directional_threshold=0.12, onchain_vote="VoteYes",
                      history=hist("ABSTAIN", "ABSTAIN"), cfg=CFG,
                      abstain_reason_code="MISSING_PROTOCOL_READINESS_EVIDENCE")
        self.assertEqual(d.action, "HOLD")
        self.assertIn("evidence-absence", d.reason)

    def test_every_absence_code_holds_against_a_live_yes(self):
        for code in vp.EVIDENCE_ABSENCE_ABSTAIN_CODES:
            with self.subTest(code=code):
                d = vp.decide(recommendation="ABSTAIN", score=0.0, confidence=0.5,
                              directional_threshold=0.12, onchain_vote="VoteYes",
                              history=hist("ABSTAIN", "ABSTAIN"), cfg=CFG,
                              abstain_reason_code=code)
                self.assertEqual(d.action, "HOLD")

    def test_affirmative_blocker_may_still_retract(self):
        # A hard blocker is a real finding about the action, not missing homework --
        # it must remain able to revise a live YES to ABSTAIN.
        d = vp.decide(recommendation="ABSTAIN", score=0.0, confidence=0.5,
                      directional_threshold=0.12, onchain_vote="VoteYes",
                      history=hist("ABSTAIN", "ABSTAIN"), cfg=CFG,
                      abstain_reason_code="HARD_BLOCKER_PRESENT")
        self.assertEqual(d.action, "REVISE")

    def test_genuine_neutral_score_may_still_retract(self):
        d = vp.decide(recommendation="ABSTAIN", score=0.0, confidence=0.5,
                      directional_threshold=0.12, onchain_vote="VoteYes",
                      history=hist("ABSTAIN", "ABSTAIN"), cfg=CFG,
                      abstain_reason_code="RULE_THRESHOLD_UNMET")
        self.assertEqual(d.action, "REVISE")

    def test_absence_code_does_not_block_a_fresh_abstain(self):
        # Nothing on-chain yet -> there is no directional vote to protect; a conservative
        # fresh ABSTAIN must still cast.
        d = vp.decide(recommendation="ABSTAIN", score=0.0, confidence=0.5,
                      directional_threshold=0.12, onchain_vote=None,
                      history=hist("ABSTAIN"), cfg=CFG,
                      abstain_reason_code="MISSING_PROTOCOL_READINESS_EVIDENCE")
        self.assertEqual(d.action, "CAST")


class NonVotableTests(unittest.TestCase):
    def test_needs_more_info_skipped(self):
        d = vp.decide(recommendation="NEEDS_MORE_INFO", score=0.0, confidence=0.2,
                      directional_threshold=0.12, onchain_vote=None,
                      history=hist("NEEDS_MORE_INFO"), cfg=CFG)
        self.assertEqual(d.action, "SKIP")


if __name__ == "__main__":
    unittest.main()
