from selenium.webdriver.common.by import By
from test_ui.page_objects.base_page import BasePage


class AddAddressPage(BasePage):
    INPUT_FIRST_NAME = By.CSS_SELECTOR, "input#firstname"
    INPUT_LAST_NAME = By.CSS_SELECTOR, "input#lastname"
    INPUT_PHONE_NUMBER = By.CSS_SELECTOR, "input#telephone"
    INPUT_STREET_ADDRESS = By.CSS_SELECTOR, "input#street_1"
    INPUT_CITY = By.CSS_SELECTOR, "input#city"
    INPUT_POSTAL_CODE = By.CSS_SELECTOR, "input#zip"
    SELECT_COUNTRY = By.CSS_SELECTOR, "select#country"
    BUTTON_SAVE_ADDRESS = By.CSS_SELECTOR, "button[title='Save Address']"

    def add_new_address(self, first_name: str, last_name: str, phone: str, street_address: str, city: str,
                        postal_code: str, country: str):
        self.logger.info("Adding new address")
        self.input(self.INPUT_FIRST_NAME, first_name)
        self.input(self.INPUT_LAST_NAME, last_name)
        self.input(self.INPUT_PHONE_NUMBER, phone)
        self.input(self.INPUT_STREET_ADDRESS, street_address)
        self.input(self.INPUT_CITY, city)
        self.input(self.INPUT_POSTAL_CODE, postal_code)
        self.select_option_by_text(self.SELECT_COUNTRY, country)
        self.click_action(self.BUTTON_SAVE_ADDRESS)
        self.wait_title("Address Book")
