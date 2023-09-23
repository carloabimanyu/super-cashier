from tabulate import tabulate

class Item:
    def __init__(self, name: str, quantity: int, price: int):
        """
        Represents an item with a name, quantity, and price.

        Args:
            name (str): The name of the item.
            quantity (int): The quantity of the item.
            price (int): The price of the item.
        """
        if not isinstance(name, str):
            raise ValueError("Item name must be a string.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        if not isinstance(price, int) or price <= 0:
            raise ValueError("Item price must be a positive number.")
        
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total_price = quantity * price

    def update_name(self, new_name: str):
        """
        Update the name of the item.

        Args:
            new_name (str): The new name for the item.
        """
        if not isinstance(new_name, str):
            raise ValueError("Item name must be a string.")
        print(f"Item name updated from {self.name} to {new_name}.")
        self.name = new_name

    def update_quantity(self, new_quantity: int):
        """
        Update the quantity of the item.

        Args:
            new_quantity (int): The new quantity for the item.
        """
        if not isinstance(new_quantity, int) or new_quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        
        print(f"{self.name} quantity updated from {self.quantity} to {new_quantity}")
        self.quantity = new_quantity
        self.total_price = new_quantity * self.price

    def update_price(self, new_price: int):
        """
        Update the price of the item.

        Args:
            new_price (int): The new price for the item.
        """
        if not isinstance(new_price, int) or new_price <= 0:
            raise ValueError("Item price must be a positive number.")
        
        print(f"{self.name} price updated from {self.price} to {new_price}.")
        self.price = new_price
        self.total_price = self.quantity * new_price

class Transaction:
    def __init__(self):
        """
        Represents a transaction with a collection of items.
        """
        self.transaction_details = {}

    def add_item(self, name, quantity, price):
        """
        Add an item to the transaction.

        Args:
            name (str): The name of the item.
            quantity (int): The quantity of the item.
            price (int): The price of the item.
        """
        item = Item(name, quantity, price)
        if name in self.transaction_details.keys():
            prompt = input(f"{name} already in basket. Are you sure to replace it (Y/N)? ")
            if prompt == "Y":
                self.transaction_details.update({item.name: item})
                print(f"{name} pcs of {quantity} with unit price {price} added.")
            elif prompt == "N":
                print("Item addition cancelled.")
            else:
                print("Invalid answer.")
        else:
            self.transaction_details.update({item.name: item})
            print(f"{name} pcs of {quantity} with unit price {price} added.")

    def update_item_name(self, name, new_name):
        """
        Update the name of an item in the transaction.

        Args:
            name (str): The name of the item to update.
            new_name (str): The new name for the item.
        """
        try:
            item = self.transaction_details[name]
            item.update_name(new_name)
            self.transaction_details[new_name] = self.transaction_details.pop(name)
        except KeyError:
            print(f"There is no item called {name}.")

    def update_item_quantity(self, name, new_quantity):
        """
        Update the quantity of an item in the transaction.

        Args:
            name (str): The name of the item to update.
            new_quantity (int): The new quantity for the item.
        """
        try:
            item = self.transaction_details[name]
            item.update_quantity(new_quantity)
        except KeyError:
            print(f"There is no item called {name}.")

    def update_item_price(self, name, new_price):
        """
        Update the price of an item in the transaction.

        Args:
            name (str): The name of the item to update.
            new_price (int): The new price for the item.
        """
        try:
            item = self.transaction_details[name]
            item.update_price(new_price)
        except KeyError:
            print(f"There is no item called {name}.")

    def delete_item(self, name):
        """
        Delete an item from the transaction.

        Args:
            name (str): The name of the item to delete.
        """
        try:
            self.transaction_details.pop(name)
            print(f"{name} deleted.")
        except KeyError:
            print(f"There is no item called {name}.")

    def reset_transaction(self):
        """
        Reset the transaction by clearing all items.
        """
        self.transaction_details = {}
        print("Transaction is reset.")

    def check_order(self):
        """
        Display a table summarizing the items in the transaction.
        """
        if len(self.transaction_details) < 1:
            raise ValueError("There is no item yet.")
        
        headers = ["Item Name", "Quantity", "Price", "Total Price"]
        table_data = []

        for item in self.transaction_details.values():
            table_data.append([item.name, item.quantity, item.price, item.total_price])

        print("\n")
        print(tabulate(table_data, headers=headers, tablefmt="github"))

    def calculate_total_price(self):
        """
        Calculate and display the total price of the transaction, including discounts.
        """
        if len(self.transaction_details) < 1:
            raise ValueError("There is no item yet.")
        
        self.check_order()
        print("\n")
        
        self.total_bill = 0
        for item in self.transaction_details.values():
            self.total_bill += item.total_price

        self.discount_percentage = 0.0
        if self.total_bill > 500000:
            self.discount_percentage = 0.1
        elif self.total_bill > 300000:
            self.discount_percentage = 0.08
        elif self.total_bill > 200000:
            self.discount_percentage = 0.05

        headers = ["Description", "Value"]

        table_data = [
            ["Total price before discount", self.total_bill],
            ["Discount (%)", self.discount_percentage * 100],
            ["Discount amount", self.discount_percentage * self.total_bill],
            ["Total price after discount", self.total_bill * (1 - self.discount_percentage)]
        ]
        
        print(tabulate(table_data, headers=headers, tablefmt="github"))

        return self.total_bill * (1 - self.discount_percentage)