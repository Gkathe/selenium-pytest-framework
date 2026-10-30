import pytest

PRODUCTO = "Sauce Labs Backpack"


@pytest.fixture
def en_checkout(inventory_page, cart_page):
    """Deja al usuario en la pantalla de datos del checkout con 1 producto."""
    inventory_page.add_to_cart(PRODUCTO)
    inventory_page.go_to_cart()
    cart_page.checkout()


@pytest.mark.smoke
def test_checkout_completo(en_checkout, checkout_page):
    checkout_page.fill_info("Ana", "Pérez", "110111")
    checkout_page.finish()
    assert "Thank you for your order" in checkout_page.get_confirmation()


@pytest.mark.negative
@pytest.mark.parametrize("first,last,postal,error", [
    ("", "Pérez", "110111", "First Name is required"),
    ("Ana", "", "110111", "Last Name is required"),
    ("Ana", "Pérez", "", "Postal Code is required"),
])
def test_checkout_campos_obligatorios(en_checkout, checkout_page, first, last, postal, error):
    checkout_page.fill_info(first, last, postal)
    assert error in checkout_page.get_error()