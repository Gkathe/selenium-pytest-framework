from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_info(self, first, last, postal):
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BTN)

    def finish(self):
        self.click(self.FINISH_BTN)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)

    def get_confirmation(self):
        return self.get_text(self.COMPLETE_HEADER)