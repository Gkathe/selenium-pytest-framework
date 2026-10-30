import pytest

PRODUCTO = "Sauce Labs Backpack"
PRODUCTO_2 = "Sauce Labs Bike Light"


@pytest.mark.smoke
def test_agregar_producto_actualiza_badge(inventory_page):
    inventory_page.add_to_cart(PRODUCTO)
    assert inventory_page.get_cart_count() == 1


@pytest.mark.regression
def test_agregar_dos_productos(inventory_page):
    inventory_page.add_to_cart(PRODUCTO)
    inventory_page.add_to_cart(PRODUCTO_2)
    assert inventory_page.get_cart_count() == 2


@pytest.mark.regression
def test_producto_aparece_en_carrito(inventory_page, cart_page):
    inventory_page.add_to_cart(PRODUCTO)
    inventory_page.go_to_cart()
    assert PRODUCTO in cart_page.get_item_names()


@pytest.mark.regression
def test_quitar_producto_desde_inventario(inventory_page):
    inventory_page.add_to_cart(PRODUCTO)
    inventory_page.remove_from_cart(PRODUCTO)
    assert inventory_page.get_cart_count() == 0


@pytest.mark.regression
def test_quitar_producto_desde_carrito(inventory_page, cart_page):
    inventory_page.add_to_cart(PRODUCTO)
    inventory_page.go_to_cart()
    cart_page.remove_item(PRODUCTO)