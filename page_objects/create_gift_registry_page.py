import random

import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CreateGiftRegistryPage(BasePage):
    SELECT_GIFT_REGISTRY_TYPE = By.CSS_SELECTOR, "select#type_id"
    BUTTON_NEXT = By.CSS_SELECTOR, "button#submit\.next"
    INPUT_EVENT = By.CSS_SELECTOR, "input#title"
    INPUT_MESSAGE = By.CSS_SELECTOR, "textarea#message"
    INPUT_FIRST_NAME = By.CSS_SELECTOR, "input#registrant\:firstname0"
    INPUT_LAST_NAME = By.CSS_SELECTOR, "input#registrant\:lastname0"
    INPUT_EMAIL = By.CSS_SELECTOR, "input#registrant\:email0"
    SELECT_PRIVACY = By.CSS_SELECTOR, "select#is_public"
    SELECT_STATUS = By.CSS_SELECTOR, "select#is_active"
    SELECT_COUNTRY = By.CSS_SELECTOR, "select#event_country"
    BUTTON_DATEPICKER = By.CSS_SELECTOR, "button.ui-datepicker-trigger"
    DATEPICKER_SELECT_MONTH = By.CSS_SELECTOR, "select.ui-datepicker-month"
    DATEPICKER_SELECT_YEAR = By.CSS_SELECTOR, "select.ui-datepicker-year"
    INPUT_EVENT_DATE = By.CSS_SELECTOR, "input#event_date"
    BUTTON_SAVE = By.CSS_SELECTOR, "button#submit\.save"

    def _select_date(self):
        year = random.randint(2014, 2034)
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day = random.randint(1, 28)
        self.click_action(self.BUTTON_DATEPICKER)
        self.select_option_by_value(self.DATEPICKER_SELECT_YEAR, str(year))
        self.select_option_by_text(self.DATEPICKER_SELECT_MONTH, random.choice(month))
        self.click_action(locator=(By.XPATH, f"//table//a[text()={str(day)}]"))

    @allure.step("Создаю реестр подарков для события {event}")
    def create_gift_registry(self, event: str, message: str, is_public: str, is_active: str, country: str,
                             first_name: str, last_name: str, email: str):
        self.logger.info("Creating Gift Registry")
        self.select_option_by_text(self.SELECT_GIFT_REGISTRY_TYPE, 'Birthday')
        self.click_action(self.BUTTON_NEXT)
        self.input(self.INPUT_EVENT, event)
        self.input(self.INPUT_MESSAGE, message)
        self.select_option_by_value(self.SELECT_PRIVACY, is_public)
        self.select_option_by_value(self.SELECT_STATUS, is_active)
        self.select_option_by_text(self.SELECT_COUNTRY, country)
        self._select_date()
        self.input(self.INPUT_FIRST_NAME, first_name)
        self.input(self.INPUT_LAST_NAME, last_name)
        self.input(self.INPUT_EMAIL, email)
        self.click_action(self.BUTTON_SAVE)
