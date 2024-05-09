import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CompanyRegistrationPage(BasePage):
    INPUT_COMPANY_NAME = By.CSS_SELECTOR, "input#company_name"
    INPUT_LEGAL_NAME = By.CSS_SELECTOR, "input#legal_name"
    INPUT_COMPANY_EMAIL = By.CSS_SELECTOR, "input#company_email"
    INPUT_STREET_ADDRESS = By.CSS_SELECTOR, "input#street0"
    INPUT_CITY = By.CSS_SELECTOR, "input#city"
    INPUT_POSTAL_CODE = By.CSS_SELECTOR, "input#postcode"
    INPUT_PHONE_NUMBER = By.CSS_SELECTOR, "input#telephone"
    INPUT_EMAIL = By.CSS_SELECTOR, "input#email_address"
    INPUT_FIRST_NAME = By.CSS_SELECTOR, "input#firstname"
    INPUT_LAST_NAME = By.CSS_SELECTOR, "input#lastname"
    SELECT_COUNTRY = By.CSS_SELECTOR, "select#country_id"
    BUTTON_SUBMIT = By.CSS_SELECTOR, "button.action.save"
    SUCCESS_MESSAGE = By.CSS_SELECTOR, "div.message-success"

    @allure.step("Регистрирую аккаунт компании {company_name}")
    def register_company(self, company_name: str, company_legal_name: str, email: str, street_address: str, city: str,
                         postal_code: str, phone: str, admin_email: str, admin_first_name: str, admin_last_name: str):
        self.logger.info("Registering a new company")
        self.input(self.INPUT_COMPANY_NAME, company_name)
        self.input(self.INPUT_LEGAL_NAME, company_legal_name)
        self.input(self.INPUT_COMPANY_EMAIL, email)
        self.input(self.INPUT_STREET_ADDRESS, street_address)
        self.input(self.INPUT_CITY, city)
        self.select_option_by_value(self.SELECT_COUNTRY, "RU")
        self.input(self.INPUT_POSTAL_CODE, postal_code)
        self.input(self.INPUT_PHONE_NUMBER, phone)
        self.input(self.INPUT_EMAIL, admin_email)
        self.input(self.INPUT_FIRST_NAME, admin_first_name)
        self.input(self.INPUT_LAST_NAME, admin_last_name)
        self.click_action(self.BUTTON_SUBMIT, sleep=0.7)
        self.wait_title("Create New Company")
        self.search_element(self.SUCCESS_MESSAGE)
