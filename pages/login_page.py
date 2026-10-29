from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self):
        self.open(BASE_URL)
        return self

    def login(self, username, password):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)
    