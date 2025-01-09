# Parent Class
class Vehicle:
    def move(self):
        # Default implementation (can be overridden by child classes)
        print("The vehicle is moving.")

# Child Class 1 - Car
class Car(Vehicle):
    def move(self):
        print("Driving")

# Child Class 2 - Plane
class Plane(Vehicle):
    def move(self):
        print("Flying")

# Child Class 3 - Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Child Class 4 - Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling")

# Polymorphism in Action
def demonstrate_movement(vehicle):
    vehicle.move()

# Create Objects
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Demonstrate polymorphism
vehicles = [car, plane, boat, bicycle]
print("Polymorphism with Vehicles:")
for vehicle in vehicles:
    demonstrate_movement(vehicle)
