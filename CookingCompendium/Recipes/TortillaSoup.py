import warnings
from CookingCompendium.Techniques.CastIron import CastIron
recipe_name = "Tortilla Soup"

def description():
    print("\n"
        "Tortilla Soup is a delicious dish of Spanish origin and an easy dish to "
        "make even with the crunched schedule of a modern-day Programmer.\n"
        "There are various ways to approach tortilla soup and various spices you can "
        "add or subtract to make it unique to your tastes.\n"
        "This recipe is meant to serve as a basic approach to making torilla soup for you to subclass."
    )


def methods():
    """Displays methods of making this recipe"""
    print("\n" + "\n".join((
        ".CastIron",
        ".SlowCooker"
    )))


class CastIronMethod(CastIron):
    def set_ingredients(self):
        if self.feeding_size > 0:
            self.ingredients = {
                'chicken': 'up to you'
            }
            return
        warnings.warn("Set .set_feeding_size(number_of_people: int)")
