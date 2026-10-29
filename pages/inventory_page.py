from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    SORT_SELECT = (By.CSS_SELECTOR, ".product_sort_container")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    @staticmethod
    def _slug(product_name):
        return product_name.lower().replace(" ", "-")

    def get_title(self):
        return self.get_text(self.TITLE)

    def get_product_names(self):
        return [e.text for e in self.find_all(self.ITEM_NAMES)]

    def get_product_prices(self):
        return [float(e.text.replace("$", "")) for e in self.find_all(self.ITEM_PRICES)]

    def sort_by(self, value):  # az | za | lohi | hilo
        Select(self.find(self.SORT_SELECT)).select_by_value(value)

    def add_to_cart(self, product_name):
        self.click((By.ID, f"add-to-cart-{self._slug(product_name)}"))

    def remove_from_cart(self, product_name):
        self.click((By.ID, f"remove-{self._slug(product_name)}"))

    def get_cart_count(self):
        if self.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)