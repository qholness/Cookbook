from CookingCompendium.utilities import ignore_in_dir
from CookingCompendium.utilities import build_library
from CookingCompendium.Continents import NorthAmerica


NorthAmericaKey = 'NorthAmerica'
UsaKey = 'USA'

def LoadUsa(ingredients, flavors, regions, states):
    UsaRegionCollection = NorthAmerica.USA.Regions
    for region in dir(UsaRegionCollection):
        if region in ignore_in_dir: continue
        region = getattr(UsaRegionCollection, region)
        if regions.get(region.RegionName) is None:
            regions[region.RegionName] = {}
        for state in dir(region):
            if state in ignore_in_dir: continue
            stateObj = getattr(region, state)
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
            regions[region.RegionName][stateObj.name] = stateObj.recipes
            states[state] = stateObj.recipes
            
    return flavors, ingredients, regions, states