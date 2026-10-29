from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def get_item_names(self):
        return [e.text for e in self.driver.find_elements(*self.ITEM_NAMES)]

    def remove_item(self, product_name):
        slug = product_name.lower().replace(" ", "-")
        self.click((By.ID, f"remove-{slug}"))

    def checkout(self):
        self.click(self.CHECKOUT_BTN)