import pytest


@pytest.mark.smoke
def test_inventario_muestra_6_productos(inventory_page):
    assert len(inventory_page.get_product_names()) == 6


@pytest.mark.regression
def test_orden_az(inventory_page):
    inventory_page.sort_by("az")
    names = inventory_page.get_product_names()
    assert names == sorted(names)


@pytest.mark.regression
def test_orden_za(inventory_page):
    inventory_page.sort_by("za")
    names = inventory_page.get_product_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.regression
def test_orden_precio_menor_a_mayor(inventory_page):
    inventory_page.sort_by("lohi")
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices)


@pytest.mark.regression
def test_orden_precio_mayor_a_menor(inventory_page):
    inventory_page.sort_by("hilo")
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices, reverse=True)