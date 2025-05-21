# ATM Program with Login and Withdrawal

# Stored credentials and account balance
stored_username = "r123use"
stored_pin = "1234"
account_balance = 1000.0  # Starting balance

print("===== Welcome to the ATM =====")
username = input("Enter username: ")
pin = input("Enter PIN: ")

# Check if login is correct
if username == stored_username and pin == stored_pin:
    print("\nLogin successful!")
    
    # Ask for withdrawal amount
    try:
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        
        if withdraw_amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        elif withdraw_amount > account_balance:
            print("Insufficient balance. Withdrawal denied.")
        else:
            account_balance -= withdraw_amount
            print(f"Withdrawal successful! New balance: ${account_balance:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter a number.")
else:
    print("\nInvalid username or PIN. Access denied.")
