# Example 1: Vehicle and Car
class Vehicle:
    def start_engine(self):
        print("Starting generic engine...")

class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine with keyless entry...")

v = Vehicle()
v.start_engine()

c = Car()
c.start_engine()


# Example 2: Employee and Manager
class Employee:
    def get_role(self):
        print("Employee")

class Manager(Employee):
    def get_role(self):
        print("Manager - manages team")

e = Employee()
e.get_role()

m = Manager()
m.get_role()
