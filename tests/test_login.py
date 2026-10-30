import pytest
from utils.data_reader import load_json

users = load_json("users.json")


@pytest.mark.smoke
def test_login_exitoso(login_page, driver):
    from pages.inventory_page import InventoryPage
    login_page.login(**users["valid"])
    assert "inventory" in driver.current_url
    assert InventoryPage(driver).get_title() == "Products"


@pytest.mark.negative
def test_usuario_bloqueado(login_page):
    login_page.login(**users["locked"])
    assert "locked out" in login_page.get_error()


@pytest.mark.negative
@pytest.mark.parametrize(
    "case", users["invalid_cases"],
    ids=lambda c: f"{c['username'] or 'vacio'}-{c['password'] or 'vacio'}"
)
def test_login_invalido(login_page, case):
    login_page.login(case["username"], case["password"])
    assert case["error"] in login_page.get_error()