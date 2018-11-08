import unittest
import pprint
from CookingCompendium.Compendium import ingredients, flavors

class TestSearch(unittest.TestCase):
    def test_valid_ingredient_search(self, search_term='potatoes'):
        dot_notation = str(ingredients)\
            .replace(':', '.')\
            .replace("'", '')\
            .replace('{', '')\
            .replace('}', '')\
            .replace(' ', '')\
            .replace(',', '|')
        print(dot_notation)

    def test_invalid_ingredient_search(self, search_term=None):
        assert(ingredients.get(search_term) is None)

    def test_get_ingredient_list(self, search_terms=('pork', 'potatoes', 'beef', 'beans', 'apricots')):
        res = ingredients.get_ingredients(search_terms)

    def test_get_flavor_list(self, search_terms=('sweet and sour', 'sour')):
        res = flavors.get_flavors(search_terms)
