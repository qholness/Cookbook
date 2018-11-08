from CookingCompendium.Ingredients import Ingredients, Flavors
from CookingCompendium.Continents import (
    NorthAmerica,
    Asia
)
from CookingCompendium.Continents.utilities import build_library
from CookingCompendium.Ingredients import (
    pepper
)


ignore_in_dir = ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
ingredients = Ingredients()
flavors = Flavors()
NorthAmericaKey = 'NorthAmerica'
UsaKey = 'USA'

# Add USA states to search set
for state in dir(NorthAmerica.USA):
    if state not in ignore_in_dir:
        stateObj = getattr(NorthAmerica.USA, state)
        zipped_vector = zip(
            stateObj.flavors,
            stateObj.ingredients
        )
        for flavor in stateObj.flavors:
            recipes_by_flavor = stateObj.recipes.get(flavor)
            if recipes_by_flavor is not None:
                flavors = build_library(
                    flavors, flavor, NorthAmericaKey, UsaKey, stateObj.name,
                    recipes_by_flavor)
        for ing in stateObj.ingredients:
            recipes_by_ingredient = stateObj.recipes.get(ing)
            if recipes_by_ingredient is not None:
                ingredients = build_library(
                    ingredients, ing, NorthAmericaKey, UsaKey, stateObj.name,
                    recipes_by_ingredient)


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
    
