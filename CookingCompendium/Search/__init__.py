class Base(dict):
    def get_search(self, search_list=[]):
        ret_vec = []
        fails = set()
        for ing in set(search_list):
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


class Ingredients(Base):
    def get_ingredients(self, search_list):
        return self.get_search(search_list)
    

class Flavors(Base):
    def get_flavors(self, search_list):
        return self.get_search(search_list)


class Regions(Base):
    def get_regions(self, search_list):
        return self.get_search(search_list)


class States(Base):
    def get_states(self, search_list):
        return self.get_search(search_list)