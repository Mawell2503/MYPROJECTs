#  Solid Principle
#  this class tree, it is a bad single responsibility example
#  class tree has many responsibilities
#  growing, checking_growth, saving the growth details.

class tree:
    def __init__(self, soil, growth = 0):
        self.soil = soil
        self.growth = growth
        self.last_checked_growth = growth

    def grow(self, nutrient):
        if nutrient in self.soil:
            print("tree is growing")
            self.growth += 1
        else:
            print("soil is infertile")

    def check_growth(self):
        if self.growth > self.last_checked_growth:
            print("Growth level increased:", self.growth)
        else:
            print("No growth since last check.")
            self._last_checked_growth = self.growth 

    def save_growth_info(self):
        pass



#  here is how u utilise single repsonsibility
#  class tree only has to grow now
#  it does not concern itself with checking_growth or saving_info

class tree:
    def __init__(self, soil, growth = 0):
        self.soil = soil
        self.growth = growth
        self.last_checked_growth = growth

    def grow(self, nutrient):
        if nutrient in self.soil:
            print("tree is growing")
            self.growth += 1
        else:
            print("soil is infertile")