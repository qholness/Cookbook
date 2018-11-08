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
        for flavor, ing in zipped_vector:
            ingredients = build_library(
                ingredients, ing, NorthAmericaKey, UsaKey, stateObj.name,
                stateObj.recipes)
            flavors = build_library(
                flavors, flavor, NorthAmericaKey, UsaKey, stateObj.name,
                stateObj.recipes)


for flavor, ing in zip(
    Asia.EastAsia.Japan.flavors,
    Asia.EastAsia.Japan.ingredients
):
    ingredients = build_library(ingredients, ing, 'Asia', 'japan',
        recipes=Asia.EastAsia.Japan.recipes)
    flavors = build_library(flavors, flavor, 'Asia', 'japan',
        recipes=Asia.EastAsia.Japan.recipes)
