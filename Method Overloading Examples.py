# Example 1: HelloGreeter - greet with or without a name
class HelloGreeter:
    def greet(self, name=None):
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello!")

g = HelloGreeter()
g.greet("Emma")
g.greet()


# Example 2: Multiplier - multiply one or two numbers
class Multiplier:
    def multiply(self, a, b=1):
        print("Result:", a * b)

m = Multiplier()
m.multiply(5)
m.multiply(5, 3)
