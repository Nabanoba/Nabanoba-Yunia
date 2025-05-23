# Step 1: Define the custom exception
class NotPositiveNumberError(Exception):
    def __init__(self, number):
        super().__init__(f"Invalid input: {number} is not a positive number.")

# Step 2: Function to check for positive number
def check_positive(number):
    if number <= 0:
        raise NotPositiveNumberError(number)
    else:
        print(f"{number} is a positive number.")

# Example usage
try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
except NotPositiveNumberError as e:
    print(e)
