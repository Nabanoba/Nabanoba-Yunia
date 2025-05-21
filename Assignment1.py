# Initial stock items (item: quantity)
stock = {
    "Apples": 50,
    "Bananas": 30,
    "Oranges": 40
}

def display_stock():
    print("\nCurrent Stock:")
    for item, quantity in stock.items():
        print(f"{item}: {quantity}")

def update_stock():
    item = input("Enter the item name to update: ").capitalize()
    if item in stock:
        try:
            change = int(input("Enter the quantity to add/remove (use negative for removing): "))
            stock[item] += change
            print(f"{item} updated. New quantity: {stock[item]}")
        except ValueError:
            print("Invalid quantity. Please enter an integer.")
    else:
        print(f"{item} is not in stock.")

# Menu loop
while True:
    print("\nInventory Management System")
    print("1. Display Stock")
    print("2. Update Stock")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        display_stock()
    elif choice == "2":
        update_stock()
    elif choice == "3":
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
