# Super Cashier

## 1. Requirements and Objectives

The project objective is create self-service cashier that can manage transactions of items. The requirements for this program including:
- Create and manage items (name, quantity, and price).
- Add, update, and remove items from transaction.
- Calculate total price of the transaction with discounts applied.

## 2. Process

Here's the process of Super Cashier program.

1. **Create Transaction**: Initialize an empty transaction object to store items.

2. **Add Item**: After creating the transaction object, you can add items to it.

3. **Update Item**: You able to update an item's name, quantity, or price.

4. **Delete Item**: If you need, you can remove an item from the transaction.

5. **Check Order**: You can view the current list of items in the transaction.

6. **Calculate Total Price**: Calculate the total price of the transaction, including discounts. Discounts are applied based on total price threshold.

## 3. Code Explanation

The code consists of two classes: `Item` and `Transaction`, each serving specific purposes.

### `Item` Class
The `Item` class represents an individual item. Here's an explanation of its methods:

- `__init__(self, name: str, quantity: int, price: int)`: Initializes an item with the provided name, quantity, and price. It also calculates the total price of the item.

- `update_name(self, new_name: str)`: Updates the name of the item.

- `update_quantity(self, new_quantity: int)`: Updates the quantity of the item, recalculating the total price.

- `update_price(self, new_price: int)`: Updates the price of the item, recalculating the total price.

### `Transaction` Class
The `Transaction` class manages a collection of items and performs various operations on them. Here's an explanation of its methods:

- `__init__(self)`: Initializes an empty transaction.

- `add_item(self, name, quantity, price)`: Adds an item to the transaction.

- `update_item_name(self, name, new_name)`: Updates the name of an item in the transaction.

- `update_item_quantity(self, name, new_quantity)`: Updates the quantity of an item in the transaction, recalculating the total price.

- `update_item_price(self, name, new_price)`: Updates the price of an item in the transaction, recalculating the total price.

- `delete_item(self, name)`: Deletes an item from the transaction.

- `reset_transaction(self)`: Clears all items from the transaction.

- `check_order(self)`: Displays a summary table of the transaction.

- `calculate_total_price(self)`: Calculates total price of the transaction including discounts.

## 4. Sample Usage

Below are sample usage of the `Transaction` class:

```python
# Create a transaction
transaction = Transaction()

# Add items to the transaction
transaction.add_item("Item A", 2, 10000)
transaction.add_item("Item B", 3, 15000)

# Update item name, quantity, and price
transaction.update_item_name("Item A", "New Item A")
transaction.update_item_quantity("New Item A", 5)
transaction.update_item_price("New Item A", 12000)

# Delete an item
transaction.delete_item("Item B")

# Calculate and display the total price
total_price = transaction.calculate_total_price()
```

```
Item A pcs of 2 with unit price 10000 added.
Item B pcs of 3 with unit price 15000 added.
Item name updated from Item A to New Item A.
New Item A quantity updated from 1 to 5
New Item A price updated from 10000 to 12000.
Item B deleted.

| Item Name   | Quantity   | Price     | Total Price     |
|-------------|------------|-----------|-----------------|
| New Item A  | 5          | 12000     | 60000           |

Total price before discount 60000
Discount (%) 0.0
Discount amount 0.0
Total price after discount 60000
```

## 5. Conclusion

This self-service cashier provides a convenient way to manage transactions of items, including adding, updating, and deleting items, as well as calculating the total price with discounts. 