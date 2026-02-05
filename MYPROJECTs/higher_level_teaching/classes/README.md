# 1️⃣ Create a class named Car
class Car:  
    # 2️⃣ Constructor method, runs when a new object is created
    def __init__(self, brand, color):  
        self.brand = brand    # 3️⃣ Property: store the car's brand in this object
        self.color = color    # 4️⃣ Property: store the car's color in this object

    # 5️⃣ Method: a function inside the class that uses object properties
    def drive(self):  
        print(f"The {self.color} {self.brand} is driving!")  # 6️⃣ Action: prints a message using the object's properties

    # 7️⃣ Another method: changes the color of the car
    def repaint(self, new_color):  
        self.color = new_color  # 8️⃣ Update property: set object's color to new_color
        print(f"The car has been repainted to {self.color}.")  # 9️⃣ Confirmation message

# 10️⃣ Create an object of Car class called my_car
my_car = Car("Toyota", "red")  # Calls __init__, sets brand="Toyota", color="red"

# 11️⃣ Call the drive method on my_car
my_car.drive()  # Output: The red Toyota is driving!

# 12️⃣ Call the repaint method on my_car
my_car.repaint("blue")  # Output: The car has been repainted to blue

# 13️⃣ Call drive again to see updated color
my_car.drive()  # Output: The blue Toyota is driving!


| Line                                | What it does                                       |
| ----------------------------------- | -------------------------------------------------- |
| `class Car:`                        | Creates a new class called `Car` (blueprint)       |
| `def __init__(self, brand, color):` | Constructor, runs when a new object is created     |
| `self.brand = brand`                | Stores the `brand` value in the object             |
| `self.color = color`                | Stores the `color` value in the object             |
| `def drive(self):`                  | Defines a method to perform an action (driving)    |
| `print(...)` inside `drive`         | Uses object properties to display a message        |
| `def repaint(self, new_color):`     | Defines another method to change object properties |
| `self.color = new_color`            | Updates the color property of the object           |
| `print(...)` inside `repaint`       | Confirms the change                                |
| `my_car = Car("Toyota", "red")`     | Creates an object (instance) of the class          |
| `my_car.drive()`                    | Calls the method `drive` using the object          |
| `my_car.repaint("blue")`            | Calls `repaint` to change the object’s color       |
| `my_car.drive()`                    | Shows updated property in action                   |
