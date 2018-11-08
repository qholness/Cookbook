import unittest
from CookingCompendium.Recipes import TortillaSoup as ts

class PrintTests(unittest.TestCase):
    def test_print_description(self):
        ts.description()


    def test_print_methods(self):
        ts.methods()


    def test_build_class(self):
        ci = ts.CastIron()
        assert(isinstance(ci, ts.CastIron)), "CastIron class not instantiated"
    