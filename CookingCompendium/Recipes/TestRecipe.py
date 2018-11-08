import warnings
import json
from CookingCompendium.Recipes import Recipe
from CookingCompendium.Techniques.TestTechnique import TestTechnique
state = 'test_state'

class TestRecipe(Recipe):
    def __init__(self, *args, **kwargs):
        super().__init__(
            name = "Test Recipe",
            methods = [".CastIron", ".SlowCooker"],
            description = "A delicious example of a recipe",
            *args, **kwargs)

    class TestTechniqueMethod(TestTechnique):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # x pounds of ground beef
            # y cups of beef stock
            # x potatoes
            self.recipe = [
                {
                    'beef': 
                        f'{1 * self.feeding_size} pounds' if self.units else
                        f'{self.__pounds_to_kilograms__(1) * self.feeding_size} kilograms'
                },
                {
                    'beef stock':
                        f'{2 * self.feeding_size} cups' if self.units else
                        f'{self.__cups_to_liters__(2) * self.feeding_size} liters'
                },
                {
                    'potatoes':
                        f'{1 * self.feeding_size}'
                }
            ]

        def get_recipe(self):
            dump = json.dumps(self.recipe, indent=4)
            print("Recipe:", dump)
            return dump

        def get_instructions(self):
            return f"""Instructions:
            Add 'beef stock', beef, and potatoes to [cooking apparatus].
            Cook for 2 hours.
            Serve warm with love and happiness.
            """
