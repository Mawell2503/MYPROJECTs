class Bob:
    def build(self, house,):
        if house == None:
            return "homeless"
        elif house == "needs building":
            return "Bob is on his way"
        
from abc import ABC, abstractmethod
#first defining what a room is
class Room(ABC):
    @abstractmethod
    def build(self):
        pass
#using build from room allows to use build method
class kitchen(Room):
    def build(self):
        print("Building a Kitchen")

class basement(Room):
    def build(self):
        print("Building a Basement")


class lakaz:
    def add_room(self, room : Room):
        room.build()

        