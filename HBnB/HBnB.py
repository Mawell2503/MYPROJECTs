class Diagram:
    def register(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def create(self):
        pass
    
class PresentationLayer(Diagram):
    def __init__(self):
        pass

class API(PresentationLayer):
    pass

class Services(PresentationLayer):
    pass


class BusinessLogicLayer(Diagram):
    def __init__(self, id, name):
        self.id = id
        self.name = name



class User(BusinessLogicLayer):
    def __init__(self, email, password):
        super().__init__(id, name)
        self.email = email
        self.password = password
        
class Place(BusinessLogicLayer):
    def __init__(self, description, price, owner):
        super().__init__(id, name)
        self.description = description
        self.price = price
        self.owner = owner

class Review(BusinessLogicLayer):
    def __init__(self, text, rating, user, place):
        super().__init__(id)
        self.text = text
        self.rating = rating
        self.user = user
        self.place = place

class Amenity(BusinessLogicLayer):
    super().__init__(id, name)


class PersistenceLayer(Diagram):
    pass

class Repository(PersistenceLayer):
    pass

class Storage(PersistenceLayer):
    pass

class Database(PersistenceLayer):
    pass