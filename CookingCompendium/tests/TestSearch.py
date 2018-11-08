import unittest
from CookingCompendium.Compendium import ingredients, flavors

class TestSearch(unittest.TestCase):

    def test_invalid_ingredient_search(self, search_term=None):
        assert(ingredients.get(search_term) is None)

    def test_get_ingredient_list(self, search_terms=('pork', 'potatoes', 'beef', 'beans', 'apricots')):
        res = ingredients.get_ingredients(search_terms)

    def test_get_flavor_list(self, search_terms=('sweet and sour', 'sour', 'bland')):
        res = flavors.get_flavors(search_terms)
        print(flavors)
