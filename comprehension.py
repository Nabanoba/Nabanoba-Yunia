# Create a dictionary of squares for even numbers only
squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(squares)
