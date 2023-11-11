from app.shopping_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    return ShoppingCart()

def test_add_item(cart):
    # cart = ShoppingCart()
    cart.add_item("apple", 2)
    assert cart.get_item_count("apple") == 2 # -- check
    assert cart.get_total_items() == 2

def test_remove_item(cart):
    # cart = ShoppingCart()
    cart.add_item("Apple", 3)
    cart.remove_item("Apple", 2)
    assert cart.get_item_count("Apple") == 1
    assert cart.get_total_items() == 1

def test_get_cart_items(cart):
    # cart = ShoppingCart()
    cart.add_item("apple", 3)
    cart.add_item("banana", 4)
    items = cart.get_cart_items()
    assert "apple" in items # -- check
    assert "banana" in items

def test_clear_cart(cart):
    # cart = ShoppingCart()
    cart.add_item("apple",2)
    cart.clear_Cart()
    assert cart.get_total_items() == 0
    assert cart.get_cart_items() == []