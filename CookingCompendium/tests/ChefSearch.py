import unittest
import json
from CookingCompendium import Chef


class TestBasicSearch(unittest.TestCase):
    def test_00_find_bland_tangy(self):
        search_vector = ('bland', 'tangy')
        Chef.search_flavors(search_vector)
    
    def test_01_search_state(self):
        search_vector = ('test_state', )
        Chef.search_state(search_vector)

    def test_02_search_region(self):
        search_vector = ('Mountain West', )
        Chef.search_region(search_vector)

    def test_03_search_random(self):
        """Test Chef.SearchRandom w/ something in the search dictionary"""
        self.assertIsNotNone(Chef.SearchRandom('states'))

    def test_04_search_random_return_none(self):
        """Test Chef.SearchRandom with something not in the search dictionary"""
        self.assertIsNone(Chef.SearchRandom('alksjdaslkjdsajlk'))
