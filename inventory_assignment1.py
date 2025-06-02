
inventory = [
    {"name": "Cherries", "quantity": 50, "price": 0.99},
    {"name": "Mangoes", "quantity": 30, "price": 0.59},
    {"name": "Oranges", "quantity": 20, "price": 1.29},
]

def display_menu():
    print("\n===== Inventory Management Menu =====")
    print("1. View Inventory")
    print("2. Update Stock Quantity")
    print("3. Add New Item")
    print("4. Exit")

def display_inventory():
    print("\n--- Current Inventory ---")
    for item in inventory:
        print(f"Name: {item['name']} | Quantity: {item['quantity']} | Price: ${item['price']:.2f}")

def update_stock():
    name = input("Enter item name to update: ").strip()
    found = False
    for item in inventory:
        if item["name"].lower() == name.lower():
            try:
                new_quantity = int(input("Enter new quantity: "))
                item["quantity"] = new_quantity
                print("Quantity updated.")
                found = True
                break
            except ValueError:
                print("Invalid quantity.")
    if not found:
        print("Item not found.")

def add_item():
    name = input("Enter item name: ").strip()
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory.append({"name": name, "quantity": quantity, "price": price})
        print("New item added.")
    except ValueError:
        print("Invalid input. Please enter numbers for quantity and price.")


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        display_inventory()
    elif choice == "2":
        update_stock()
    elif choice == "3":
        add_item()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
