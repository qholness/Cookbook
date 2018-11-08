import unittest
from CookingCompendium.Recipes.TestRecipe import TestRecipe as test_recipe

class PrintTests(unittest.TestCase):
    tr = test_recipe()
    def test_print_description(self):
        self.tr.show_description()


    def test_print_methods(self):
        self.tr.show_methods()


    def test_build_class(self):
        ci = self.tr.TestTechniqueMethod()
        assert(isinstance(ci, self.tr.TestTechniqueMethod)), "CastIron class not instantiated"

    def test_print_recipe(self):
        self.assertEqual(self.tr.__repr__(), "Test Recipe")

    def test_print_method(self):
        tech = self.tr.TestTechniqueMethod()
        self.assertEqual(tech.__repr__(), "Test Technique")
    