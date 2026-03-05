#  example of a low cohesion
class Read:
    #  related to the class
    def open_book(self):
        pass

    #  related
    def turn_page(self):
        pass

    #  unrelated
    def Drink_water(self):
        pass

    # related
    def close_book(self):
        pass

#  the method drink_water has nothing to do with class(read)
#  to re arrange that u should do:
class Read:
    #  related to the class
    def open_book(self):
        pass

    #  related
    def turn_page(self):
        pass

    # related
    def close_book(self):
        pass

class person:
    def Drink_water(self):
        pass