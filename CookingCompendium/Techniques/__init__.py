from . import *

class TechniqueBase(object):
    def __init__(self, feeding_size=0):
        self.feeding_size = feeding_size

    def set_feeding_size(self, number_of_people):
        if number_of_people > 0:
            self.feeding_size = number_of_people
        if number_of_people < 2:
            return "How selfish..."

    def show_ingredients(self):
        try:
            getattr(self, 'ingredients')
            print(self.ingredients)
        except:
            print(".ingredients not set")
