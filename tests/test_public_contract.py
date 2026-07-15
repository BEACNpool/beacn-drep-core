"""Guards on the public UI's honesty contract.

These assert INTENT, not implementation details. The invariant the site must never break:
the vote BEACN actually CAST on-chain and the recommendation the engine makes TODAY are two
different facts. They can legitimately diverge, and rendering one as if it were the other
would make the transparency site lie.

(The previous version of this file matched exact expressions from the old app.js, so a
legitimate rewrite of the UI broke it while the contract itself was intact. Match on the
contract instead.)
"""
import re
import unittest
from pathlib import Path

WEB = Path(__file__).resolve().parents[2] / "beacn-drep-web"
APP = WEB / "app.assessment.js"


@unittest.skipUnless(APP.exists(), "beacn-drep-web is not checked out beside this repo (CI runs core alone)")
class PublicContractTests(unittest.TestCase):
    def setUp(self):
        self.app = APP.read_text(encoding="utf-8")

    def test_onchain_vote_and_recommendation_are_labelled_distinctly(self):
        """Both facts must be surfaced, under labels a reader cannot confuse."""
        self.assertRegex(self.app, r"BEACN's vote on-chain",
                         "the cast on-chain vote must be labelled as such")
        self.assertRegex(self.app, r"Engine recommendation today",
                         "the current recommendation must be labelled as such")

    def test_proof_link_renders_the_cast_vote_not_the_recommendation(self):
        """The vote badge next to a tx proof must come from onchain_vote, never `decision`."""
        m = re.search(r"function proofHTML\(a\)\s*\{(.*?)\n\}", self.app, re.S)
        self.assertIsNotNone(m, "proofHTML() must exist -- it renders the on-chain proof")
        body = m.group(1)
        self.assertIn("a.onchain_vote", body,
                      "the proof badge must render the vote actually cast")
        self.assertIn("a.transaction_hash", body,
                      "a vote claim must carry its transaction hash")
        self.assertNotIn("a.decision", body,
                         "the recommendation must NEVER be rendered as the on-chain vote")

    def test_divergence_is_disclosed(self):
        """When today's recommendation differs from the cast vote, say so -- do not hide it."""
        self.assertIn("diverged", self.app)
        self.assertRegex(self.app, r"function divergeHTML",
                         "divergence between cast vote and recommendation must be rendered")

    def test_scoring_and_model_influence_are_published(self):
        """The reader must see how it was scored, and that the model moved nothing."""
        self.assertIn("model_vote_influence", self.app)
        self.assertIn("binding_score", self.app)
        self.assertIn("directional_threshold", self.app)

    def test_no_vote_is_stated_plainly_when_none_was_cast(self):
        self.assertRegex(self.app, r"No vote cast on-chain yet")


if __name__ == "__main__":
    unittest.main()
