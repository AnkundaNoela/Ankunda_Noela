# transportation_system.py

# Method Overriding 
class Vehicle:
    def start_engine(self):
        print("Starting engine with a key")

class ElectricCar(Vehicle):
    def start_engine(self):  # Overriding
        print("Starting electric car silently")

# Method Overloading 
class RoutePlanner:
    def plan_route(self, start=None, end=None, via=None):
        if start and end and via:
            print(f"Planning route from {start} to {end} via {via}")
        elif start and end:
            print(f"Planning direct route from {start} to {end}")
        else:
            print("Please provide start and end locations.")

# MRO 
class Car:
    def fly(self):
        print("Cars can't fly.")

class Aircraft:
    def fly(self):
        print("Flying through the air...")

class FlyingCar(Car, Aircraft):  # Multiple inheritance
    pass


if __name__ == "__main__":
    print("Method Overriding:")
    v = Vehicle()
    e = ElectricCar()
    v.start_engine()
    e.start_engine()

    print("\nMethod Overloading:")
    planner = RoutePlanner()
    planner.plan_route("City A", "City B")
    planner.plan_route("City A", "City B", "City C")

    print("\nMethod Resolution Order (MRO):")
    fc = FlyingCar()
    fc.fly()  # Cars can't fly. (Car is before Aircraft)
    print(FlyingCar.__mro__)
