#  Dependency happens when one class relies too much on another class(or module)
#  If class() needs class() to do its job -> class() DEPENDS on class()

#  Basic dependancy -->

#  creating a class engine that will handle engine behaviour
class Engine:
    def start(self):
        print("Engine started")

#class car creates the engine and handles driving behaviour
class Car:
    def __init__(self):
        self.engine = Engine()      #  <-- creates engine

    def drive(self):        #  <--driving behaviour
        self.engine.start()
        print("car is making vroom vroom sound, ready to go")

car = Car()
car.drive

#---------------------------------------------------------------------------

class Engine:
    def start(self):
        print("*inserts a 2022 Porsche 718 Cayman GT4 RS noise")

class ElectricEngine:
    def start(self):
        print("*inserts a tesla noise...nothing")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("The metal box with wheels is moving")

