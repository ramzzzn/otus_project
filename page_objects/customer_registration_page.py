import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CustomerRegistrationPage(BasePage):
    INPUT_FIRST_NAME = By.CSS_SELECTOR, "input#firstname"
    INPUT_LAST_NAME = By.CSS_SELECTOR, "input#lastname"
    INPUT_EMAIL = By.CSS_SELECTOR, "input#email_address"
    INPUT_PASSWORD = By.CSS_SELECTOR, "input#password"
    INPUT_CONFIRM_PASSWORD = By.CSS_SELECTOR, "input#password-confirmation"
    BUTTON_CREATE_ACCOUNT = By.CSS_SELECTOR, "button[title='Create an Account']"

    @allure.step("Регистрирую нового пользователя")
    def register_customer(self, email: str, password: str, first_name: str, last_name: str):
        self.logger.info("Registering a new customer")
        self.input(self.INPUT_FIRST_NAME, first_name)
        self.input(self.INPUT_LAST_NAME, last_name)
        self.input(self.INPUT_EMAIL, email)
        self.input(self.INPUT_PASSWORD, password)
        self.input(self.INPUT_CONFIRM_PASSWORD, password)
        self.click_action(self.BUTTON_CREATE_ACCOUNT)
        self.wait_title("My Account")
