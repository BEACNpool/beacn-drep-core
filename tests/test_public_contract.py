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
        """A cast vote and today's recommendation must never share a verb: a vote the chain has
        reads "Voted X"; an uncast stance reads "Recommends X" / "Holding". A reader can then
        never mistake one for the other, whatever the layout around them."""
        self.assertRegex(self.app, r"`Voted \$\{v\}`",
                         "a cast on-chain vote must be labelled 'Voted …'")
        self.assertRegex(self.app, r"`Recommends \$\{d\}`",
                         "an uncast recommendation must be labelled 'Recommends …'")

    def test_stance_renders_the_cast_vote_not_the_recommendation(self):
        """The 'Voted' badge must come from onchain_vote, never `decision`."""
        m = re.search(r"function humanStance\(a\)\s*\{(.*?)\n\}", self.app, re.S)
        self.assertIsNotNone(m, "humanStance() must exist -- it renders the stance chip")
        body = m.group(1)
        cast_branch = body.split("const d = a.decision")[0]
        self.assertIn("a.submitted", cast_branch,
                      "the cast branch must be gated on an actual submission")
        self.assertIn("a.onchain_vote", cast_branch,
                      "the 'Voted' chip must render the vote actually cast")
        self.assertNotIn("a.decision", cast_branch,
                         "the recommendation must NEVER be rendered as the on-chain vote")
        self.assertIn("transaction_hash", self.app,
                      "a vote claim must carry its transaction hash")

    def test_divergence_is_disclosed(self):
        """When today's recommendation differs from the cast vote, say so -- do not hide it."""
        self.assertIn("diverged", self.app)
        self.assertRegex(self.app, r"function humanDiverge",
                         "divergence between cast vote and recommendation must be rendered")
        self.assertRegex(self.app, r"The vote stands",
                         "a held vote must be stated as standing, not hidden")

    def test_scoring_and_model_influence_are_published(self):
        """The reader must see how it was scored, and that the model moved nothing."""
        self.assertIn("model_vote_influence", self.app)
        self.assertIn("binding_score", self.app)
        self.assertIn("directional_threshold", self.app)

    def test_no_vote_is_stated_plainly_when_none_was_cast(self):
        self.assertRegex(self.app, r"Not yet cast",
                         "an uncast stance must say plainly that no vote is on-chain yet")


if __name__ == "__main__":
    unittest.main()
