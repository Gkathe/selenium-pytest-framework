import base64
import os
import re
from datetime import datetime

import pytest
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.data_reader import load_json


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     choices=["chrome", "firefox"], help="Navegador a usar")
    parser.addoption("--headless", action="store_true", help="Ejecutar sin interfaz")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        opts = ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1920,1080")
        # evita el popup de "cambia tu contraseña" de Chrome en SauceDemo
        opts.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        })
        drv = webdriver.Chrome(options=opts)
    else:
        opts = FirefoxOptions()
        if headless:
            opts.add_argument("-headless")
        drv = webdriver.Firefox(options=opts)
        drv.set_window_size(1920, 1080)

    yield drv
    drv.quit()


# ---------- Fixtures de páginas ----------
@pytest.fixture
def login_page(driver):
    return LoginPage(driver).load()


@pytest.fixture
def inventory_page(driver, login_page):
    """Deja al usuario ya logueado en el inventario."""
    creds = load_json("users.json")["valid"]
    login_page.login(creds["username"], creds["password"])
    return InventoryPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)


# ---------- Hook: screenshot cuando falla un test ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv:
            os.makedirs("reports/screenshots", exist_ok=True)
            safe_name = re.sub(r"[^\w\-]", "_", item.name)
            path = f"reports/screenshots/{safe_name}_{datetime.now():%H%M%S}.png"
            drv.save_screenshot(path)

            # adjunta la imagen al reporte HTML
            with open(path, "rb") as f:
                encoded = base64.b64encode(f.read()).decode()
            report.extras = getattr(report, "extras", []) + [extras.png(encoded)]