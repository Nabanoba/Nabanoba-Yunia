print("Welcome to the Division Calculator!\n")
print("Enter two numbers, and I'll divide the first by the second.\n")
print("Let's get started!\n")

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero second number.\n")
    else:
        print(f"The result of {num1} ÷ {num2} is {round(result, 2)}\n")
        
        choice = input("Would you like to perform another division? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\nThank you for using the Division Calculator. Goodbye!")
            break
        print("")
