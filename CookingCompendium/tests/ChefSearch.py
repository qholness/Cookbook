import unittest
from CookingCompendium import Chef

class TestBasicSearch(unittest.TestCase):
    def test_find_sour(self):
        Chef.search_flavors