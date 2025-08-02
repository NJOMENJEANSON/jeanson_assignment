def format_currency(amount):
    """Format number as currency with $ and 2 decimal places"""
    return f"${amount:,.2f}"

def display_inventory_value(inventory):
    """Calculate and display total inventory value"""
    total = sum(item["price"] * item["stock"] for item in inventory.values())
    print(f"\nCurrent Inventory Value: {format_currency(total)}")

def check_low_stock(inventory):
    """Display items with stock ≤ 5 units"""
    low_stock = {name: data for name, data in inventory.items() if data["stock"] <= 5}
    if low_stock:
        print("\n⚠️ LOW STOCK ALERT:")
        for name, data in low_stock.items():
            print(f"- {name} ({data['stock']} units remaining)")
    else:
        print("\nNo low stock items.")

def search_by_category(inventory):
    """Search and display items by category"""
    category = input("Category to search: ").strip().title()
    matches = {name: data for name, data in inventory.items() if data["category"].title() == category}
    
    if matches:
        print(f"\nFound {len(matches)} items in {category}:")
        for name, data in matches.items():
            print(f"• {name} - {format_currency(data['price'])} ({data['stock']} in stock)")
    else:
        print(f"\nNo items found in category: {category}")

def add_new_item(inventory):
    """Add a new item to inventory"""
    name = input("Item name: ").strip().title()
    if name in inventory:
        print("Item already exists in inventory!")
        return
    
    try:
        price = float(input("Price: $"))
        stock = int(input("Initial stock: "))
        category = input("Category: ").strip().title()
        
        inventory[name] = {
            "price": price,
            "stock": stock,
            "category": category
        }
        print(f"{name} added to inventory.")
    except ValueError:
        print("Invalid input! Please enter numbers for price and stock.")

def update_stock(inventory):
    """Add or remove stock for existing item"""
    name = input("Item name: ").strip().title()
    if name not in inventory:
        print("Item not found in inventory!")
        return
    
    try:
        action = input("Add or remove stock? (a/r): ").lower()
        amount = int(input("Amount: "))
        
        if action == 'a':
            inventory[name]["stock"] += amount
            print(f"Added {amount} units to {name}.")
        elif action == 'r':
            if inventory[name]["stock"] >= amount:
                inventory[name]["stock"] -= amount
                print(f"Removed {amount} units from {name}.")
            else:
                print("Cannot remove more stock than available!")
        else:
            print("Invalid action! Please enter 'a' or 'r'.")
    except ValueError:
        print("Invalid input! Please enter a whole number for amount.")

def main():
    inventory = {
        "Laptop": {"price": 999.99, "stock": 2, "category": "Electronics"},
        "Phone": {"price": 599.99, "stock": 15, "category": "Electronics"},
        "Mouse": {"price": 24.99, "stock": 3, "category": "Accessories"},
        "Keyboard": {"price": 49.99, "stock": 8, "category": "Accessories"}
    }
    
    while True:
        print("\n=== SMART INVENTORY MANAGER ===")
        display_inventory_value(inventory)
        check_low_stock(inventory)
        
        print("\nMenu Options:")
        print("1. Add new item")
        print("2. Update stock")
        print("3. Search by category")
        print("4. Check low stock items")
        print("5. Calculate total value")
        print("6. Exit")
        
        choice = input("\nChoose option: ").strip()
        
        if choice == '1':
            add_new_item(inventory)
        elif choice == '2':
            update_stock(inventory)
        elif choice == '3':
            search_by_category(inventory)
        elif choice == '4':
            check_low_stock(inventory)
        elif choice == '5':
            display_inventory_value(inventory)
        elif choice == '6':
            print("Exiting inventory manager. Goodbye!")
            break
        else:
            print("Invalid option! Please choose 1-6.")

if __name__ == "__main__":
    main()
