from cashier import Item, Transaction

if __name__ == "__main__":
    transaction = Transaction()

    while True:
        print("\nWelcome to our self-service cashier.")
        print("Options:")
        print("1. Add item")
        print("2. Update item name")
        print("3. Update item quantity")
        print("4. Update item price")
        print("5. Delete item")
        print("6. Reset transaction")
        print("7. Check order")
        print("8. Calculate total price")
        print("9. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = int(input("Enter price: "))
            transaction.add_item(name, quantity, price)

        elif choice == "2":
            name = input("Enter item name to update: ")
            new_name = input("Enter new name: ")
            transaction.update_item_name(name, new_name)

        elif choice == "3":
            name = input("Enter item name to update: ")
            new_quantity = int(input("Enter new quantity: "))
            transaction.update_item_quantity(name, new_quantity)

        elif choice == "4":
            name = input("Enter item name to update: ")
            new_price = int(input("Enter new price: "))
            transaction.update_item_price(name, new_price)

        elif choice == "5":
            name = input("Enter item name to delete: ")
            transaction.delete_item(name)

        elif choice == "6":
            transaction.reset_transaction()

        elif choice == "7":
            transaction.check_order()

        elif choice == "8":
            total_price = transaction.calculate_total_price()
            print(f"Total price after discount: {total_price}")

        elif choice == "9":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")