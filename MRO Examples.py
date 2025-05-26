# Example 1: Basic Multiple Inheritance
class ParentA:
    def greet(self):
        print("Hello from ParentA")

class ParentB:
    def greet(self):
        print("Hello from ParentB")

class Child(ParentA, ParentB):
    pass

child = Child()
child.greet()  # Output: Hello from ParentA
# Explanation: Since Child inherits ParentA first, its greet() is called due to Python's MRO.


# Example 2: Phone and Camera example
class Device:
    def info(self):
        print("This is a device.")

class Phone(Device):
    def info(self):
        print("This is a phone.")

class Camera(Device):
    def info(self):
        print("This is a camera.")

class SmartPhone(Phone, Camera):
    pass

sp = SmartPhone()
sp.info()  # Output: This is a phone.
# Explanation: SmartPhone inherits Phone and Camera. Because Phone is listed first, Phone.info() is called by MRO.
