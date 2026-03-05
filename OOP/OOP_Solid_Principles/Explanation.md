Solid principle are a way to make your code more maintainable, flexible, and easier to understand
S-Single Responsibility
O-Open/Closed
L-Liskov
I-Interface Segregation
D-Dependency Inversion

#  Single Responsibility Principle
- class() should have only one reason to change; each class should focus on only one thing(responsibility),If a class does too many thing it becomes harder to maintain
e.g/
>> this is a poor example since one class does 2 things
class Employee:
    def calculate_salary(self):
        pass

    def save_to_database(self):
        pass

>> Here theres 2 class, each with there own responsibility
class SalaryCalculator:
    def calculate_salary(self,employee):
        pass

class EmployeeRepository:
    def save_to_database(self):
        pass

#  Open/Closed Principle
- class() should be open for extension but closed for modification: you should be able to change/add new features without changing existing code.
e.g/
>> This class has been modify for new behaviour; bad practice
class Discount:
    def apply(self, price, type):
        if type == "student":
            return price * 0.9
        elif type == "vip":
            return price * 0.8

>> Here this example uses inheritance; good practice
>> This use of extending functionality without changing the class(Discount) is what is expected when refering to Open/Closed
class Discount:
    def apply(self, price):
        return price

class StuddentDiscount(Discount):
    def apply(self, price):
        return price * 0.9

class VIPDiscount(Discount):
    def apply(self, price):
        return price * 0.8

#  Liskov Substitution Principle
- Subclasses should be replaceable for their base class without breaking the program; if a function uses a base class, it should work with derived classes as well
e.g/
>> this class(es) are since class(Bird) expect every bird to fly.
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostrich can't fly)  << This violates LSP 

>> This example seperates flying birds from non-flying ones.
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

#  Interface Segragration Principle
- Don't force classes to implement interfaces they dont use;kee interfaces small and specific instead
e.g/
>> This example shows how class(Robot) inherits a method he has no need of using.
class WorkerInterface:
    def work(self):
        pass
    def eat(self):
        pass

class Robot(WorkerInterface):
    def work(self):
        print("Working")
    def eat(self):
        pass << Robots dont eat; uneeded use of class(WorkInterface)

>> This example splits interface.
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Robot(Workable):
    def work(self):
    print("Robot working")

#  Dependancy Inversion 
- 