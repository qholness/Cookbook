class Recipe(object):
    def __init__(self, name, description, methods):
        self.name = name
        self.description = description
        self.methods = methods
    
    def show_description(self):
        print(self.description)

    def show_methods(self):
        for m in self.methods:
            print('\t', m)

    def __repr__(self):
        return "%s" % (self.name, )