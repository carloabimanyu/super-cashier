from cashier import Item, Transaction
import pytest

# Test the Item class
def test_item_creation():
    item = Item("ItemName", 5, 1000)
    assert item.name == "ItemName"
    assert item.quantity == 5
    assert item.price == 1000
    assert item.total_price == 5000

def test_item_update_name():
    item = Item("ItemName", 5, 1000)
    item.update_name("NewName")
    assert item.name == "NewName"

def test_item_update_quantity():
    item = Item("ItemName", 5, 1000)
    item.update_quantity(3)
    assert item.quantity == 3
    assert item.total_price == 3000

def test_item_update_price():
    item = Item("ItemName", 5, 1000)
    item.update_price(1500)
    assert item.price == 1500
    assert item.total_price == 7500

# Test the Transaction class
def test_transaction_add_item():
    transaction = Transaction()
    transaction.add_item("Item1", 5, 1000)
    assert len(transaction.transaction_details) == 1

def test_transaction_update_item_name():
    transaction = Transaction()
    transaction.add_item("Item1", 5, 1000)
    transaction.update_item_name("Item1", "NewItem")
    assert transaction.transaction_details["NewItem"].name == "NewItem"

def test_transaction_update_item_quantity():
    transaction = Transaction()
    transaction.add_item("Item1", 5, 1000)
    transaction.update_item_quantity("Item1", 10)
    assert transaction.transaction_details["Item1"].quantity == 10
    assert transaction.transaction_details["Item1"].total_price == 10000

def test_transaction_update_item_price():
    transaction = Transaction()
    transaction.add_item("Item1", 5, 1000)
    transaction.update_item_price("Item1", 2000)
    assert transaction.transaction_details["Item1"].price == 2000
    assert transaction.transaction_details["Item1"].total_price == 10000

def test_transaction_delete_item():
    transaction = Transaction()
    transaction.add_item("Item1", 5, 1000)
    transaction.delete_item("Item1")
    assert len(transaction.transaction_details) == 0

def test_transaction_reset_transaction():
    transaction = Transaction()
    transaction.add_item("Item1", 5, 1000)
    transaction.reset_transaction()
    assert len(transaction.transaction_details) == 0

def test_transaction_calculate_total_price():
    transaction = Transaction()
    transaction.add_item("Item1", 10, 20000)
    transaction.add_item("Item2", 5, 10000)
    assert transaction.calculate_total_price() == 237500

if __name__ == "__main__":
    pytest.main()