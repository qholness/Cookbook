from CookingCompendium.Continents import Asia
from CookingCompendium.utilities import build_library
from CookingCompendium.utilities import ignore_in_dir

def LoadAsia(ingredients, flavors):
    for flavor in Asia.EastAsia.Japan.flavors:
        recipes_by_flavor = Asia.EastAsia.Japan.recipes.get(flavor)
        if recipes_by_flavor is not None:
            flavors = build_library(flavors, flavor, 'Asia', 'japan',
                recipes=recipes_by_flavor)
    for ing in Asia.EastAsia.Japan.ingredients:
        recipes_by_ing = Asia.EastAsia.Japan.recipes.get(ing)
        if recipes_by_ing is not None:
            ingredients = build_library(ingredients, ing, 'Asia', 'japan',
                recipes=recipes_by_ing)
    return flavors, ingredients