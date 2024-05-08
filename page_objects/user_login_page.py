import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class UserLoginPage(BasePage):
    INPUT_EMAIL = By.CSS_SELECTOR, "input#email"
    INPUT_PASSWORD = By.CSS_SELECTOR, "input#pass"
    BUTTON_LOGIN = By.CSS_SELECTOR, "button#send2"

    @allure.step("Выполняю вход в систему под пользователем")
    def login_user(self, email: str, password: str):
        self.logger.info("Login as user")
        self.input(self.INPUT_EMAIL, email)
        self.input(self.INPUT_PASSWORD, password)
        self.click_action(self.BUTTON_LOGIN)
