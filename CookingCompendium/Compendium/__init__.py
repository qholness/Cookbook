from CookingCompendium.Search import Ingredients, Flavors, Regions, States
from CookingCompendium.Compendium.LoadUsa import LoadUsa
from CookingCompendium.Compendium.LoadAsia import LoadAsia


ingredients = Ingredients()
flavors = Flavors()
regions = Regions()
states = States()

# Add USA states to search set
flavors, ingredients, regions, states = \
    LoadUsa(ingredients, flavors, regions, states)
flavors, ingredients = LoadAsia(ingredients, flavors)


def get_state_recipes():
    from CookingCompendium.Continents.NorthAmerica.USA import Regions
