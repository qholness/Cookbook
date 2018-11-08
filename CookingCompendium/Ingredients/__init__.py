class Ingredients(dict):
    def get_ingredients(self, ingredient_list=[]):
        ret_vec = []
        fails = set()
        for ing in set(ingredient_list):
            get_val = self.get(ing)
            if get_val is not None:
                ret_vec.append({ing: get_val})
            else:
                fails.add(ing)
        if len(fails) > 0:
            print("Couldn't find info for:")
            for ing in fails:
                print(f"\t{ing}")
        if len(ret_vec) > 0:
            print("Found some cultures that use your search:")
            for ing in ret_vec:
                print(f"\t{ing}")
        return ret_vec


class Flavors(Ingredients):
    def get_flavors(self, flavor_list):
        return self.get_ingredients(ingredient_list=flavor_list)