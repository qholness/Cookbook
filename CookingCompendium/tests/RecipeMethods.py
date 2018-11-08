import unittest
from hypothesis import given
import hypothesis.strategies as st
from CookingCompendium.Recipes import TortillaSoup as ts


class TestRecipeMethod(unittest.TestCase):
    CI = ts.CastIronMethod()

    def test_set_ingredients(self):
        self.CI.set_ingredients()

    def test_set_feeding_size(self):
        assert(self.CI.set_feeding_size(0) == "How selfish...")

    @given(size=st.integers())
    def test_set_feeding_size_hyp(self, size):
        self.CI.set_feeding_size(size)
