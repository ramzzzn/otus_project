import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdminLoginPage(BasePage):
    INPUT_USERNAME = By.CSS_SELECTOR, "input#username"
    INPUT_PASSWORD = By.CSS_SELECTOR, "input#login"
    BUTTON_SIGN_IN = By.CSS_SELECTOR, "button.action-login"
    BUTTON_CLOSE_MESSAGE = By.CSS_SELECTOR, "aside.modal-system-messages button.action-close"

    @allure.step("Открываю страницу авторизации в раздел администрирования")
    def open_login_page(self):
        self.logger.info("Open => Admin Login page")
        self.open_page(page='/admin')
        self.wait_title("Magento Admin")

    @allure.step("Выполняю авторизацию под УЗ администратора")
    def login_admin(self, username: str, password: str):
        self.logger.info("Login to the admin panel")
        self.input(self.INPUT_USERNAME, username)
        self.input(self.INPUT_PASSWORD, password)
        self.click_action(self.BUTTON_SIGN_IN)
        self.wait_title("Dashboard / Magento Admin")
        # # закрытие системного сообщения после логина - особенность UI
        # self.click_action(self.BUTTON_CLOSE_MESSAGE)





