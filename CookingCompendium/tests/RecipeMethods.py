import unittest
from hypothesis import given
import hypothesis.strategies as st
from CookingCompendium.Recipes import TestRecipe as test_recipe


class TestRecipeMethod(unittest.TestCase):
    CI = test_recipe.TestRecipe()
    Technique = CI.TestTechniqueMethod()

    def test_00_set_feeding_size(self):
        self.assertEqual(self.Technique.set_feeding_size(0), "How selfish...")

    @given(size=st.integers())
    def test_01_set_feeding_size_hyp(self, size):
        self.Technique.set_feeding_size(size)

    def test_02_get_recipe(self):
        self.Technique.get_recipe()

    def test_03_get_instructions(self):
        print(self.Technique.get_instructions())

    def test_04_timer(self):
        timer = self.Technique.Timer()
        timer.set_timer(5, 'seconds')

