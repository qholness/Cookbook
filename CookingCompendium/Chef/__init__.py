"""Looking for a recipe?
Ask the Chef.
The Chef is a single surveyor object that is utilized for searching for recipes.
The Chef searches the existing repositories created under CookingCompendium.Compendium
and return lists of various objects that help developers find recipes based on inputs.
"""
import random
from CookingCompendium.Compendium import ingredients, flavors, regions, states


def Search(terms, search_vector):
    ret_vector = []
    for term in terms:
        res = search_vector.get(term)
        if res is not None:
            ret_vector.append({
                term: res})
    return ret_vector


def SearchRandom(search_kind: str):
    vectors = {
        'flavors': flavors,
        'ingredients': ingredients,
        'regions': regions,
        'states': states
    }
    search_vector = vectors.get(search_kind)
    if search_vector is None:
        print(f"Couldn't find: '{search_kind}''.")
        print("The following search keys are available:")
        for _ in sorted(vectors.keys()):
            print("\t", _)
        return
    search_key = random.choice(list(search_vector))

    # Recursively search to find anything in case a null search is found
    if len(search_vector[search_key]) == 0:
        return SearchRandom(search_kind)

    return {search_key: search_vector[search_key]}

def search_ingredients(ingredient_search: list):
    return Search(ingredient_search, ingredients)


def search_flavors(flavor_search: list):
    return Search(flavor_search, flavors)
    

def search_state(state_search: list):
    return Search(state_search, states)


def search_region(region_search: list):
    return Search(region_search, regions)


def search_cultures(cultures):
    pass

# def search_