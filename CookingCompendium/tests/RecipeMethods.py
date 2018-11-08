import unittest
from CookingCompendium.Recipes import TortillaSoup as ts


class TestRecipeMethod(unittest.TestCase):
    CI = ts.CastIronMethod()

    def test_set_ingredients(self):
        self.CI.set_ingredients()

    def test_set_feeding_size(self):
        assert(self.CI.set_feeding_size(0) == "How selfish...")
        self.CI.set_feeding_size(4)
