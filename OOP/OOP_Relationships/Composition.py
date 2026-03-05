class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        # Create an Engine and store it inside the Car
        self.engine = Engine()   # <-- This is composition

    def drive(self):
        self.engine.start()
        print("Car is driving")