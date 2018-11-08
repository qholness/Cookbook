import unittest


class BasicTestClass(unittest.TestCase):
    def test__00__basic_import(self):
        """Checking file structure and import routes"""
        from CookingCompendium.Recipes import TestRecipe


if __name__ == '__main__':
    unittest.main()