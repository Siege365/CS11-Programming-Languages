item_names = []
item_prices = {}

while True:
    print("======== INVENTORY MENU ========")
    print("[1] Add Item")
    print("[2] Update Price")
    print("[3] Display Items")
    print("[4] Exit")
    
    choice = input("Choice: ")
    
    if choice == "1":
        item_name = input("Enter item name: ")
        
        if item_name in item_names:
            print("Item already exists in the inventory.")
        else:
            item_price = input("Enter price: ")
            item_names.append(item_name)
            item_prices[item_name] = item_price
            print("Item added successfully!")
    
    elif choice == "2":
        item_name = input("Enter item name to update: ")
        
        if item_name in item_names:
            new_price = input("Enter new price: ")
            item_prices[item_name] = new_price
            print("Price updated successfully!")
        else:
            print("Item not found in the inventory.")
    
    elif choice == "3":
        if len(item_names) == 0:
            print("No items in inventory.")
        else:
            print("\n--- Inventory List ---")
            for item in item_names:
                print(f"{item}: {item_prices[item]}")
    
    elif choice == "4":
        print("Exiting system...")
        break
    
    print()
