import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def text_xpath(self, text: str):
        return f"//*[text()='{text}']"

    def contains_text_xpath(self, text: str):
        return f"//*[contains(text(),'{text}')]"

    def open_page(self, page: str):
        self.logger.debug("%s: Opening page %s" % (self.class_name, page))
        try:
            self.browser.get(f"{self.browser.url}{page}")
        except WebDriverException:
            error_message = f"Could not be opened page {self.browser.url}{page}"
            self.logger.exception("%s: %s" % (self.class_name, error_message))
            raise WebDriverException(error_message)

    def wait_title(self, title: str):
        self.logger.debug("%s: Waiting for title: %s" % (self.class_name, title))
        try:
            self.wait.until(EC.title_is(title))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            error_message = f"Expected title: '{title}', but was '{self.browser.title}'"
            self.logger.exception("%s: %s" % (self.class_name, error_message))
            raise TimeoutException(error_message)

    def search_element(self, locator: tuple):
        self.logger.debug("%s: Searching element %s" % (self.class_name, locator))
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            error_message = f"Element was not found by the specified selector: {locator}"
            self.logger.exception("%s: %s" % (self.class_name, error_message))
            raise TimeoutException(error_message)

    def search_elements(self, locator: tuple):
        self.logger.debug("%s: Searching elements %s" % (self.class_name, locator))
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            error_message = f"No element was found for the specified selector: {locator}"
            self.logger.exception("%s: %s" % (self.class_name, error_message))
            raise TimeoutException(error_message)

    def search_clickable_element(self, locator: tuple):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            error_message = f"Element was not found by the specified selector: {locator}"
            self.logger.exception("%s: %s" % (self.class_name, error_message))
            raise TimeoutException(error_message)

    def click_action(self, locator: tuple, sleep=1):
        self.logger.debug("%s: Clicking element %s" % (self.class_name, locator))
        ActionChains(self.browser) \
            .pause(sleep).move_to_element(self.search_clickable_element(locator)) \
            .pause(sleep).click() \
            .perform()

    def input(self, locator: tuple, text: str, sleep: int = 0.5):
        self.logger.debug("%s: Input %s in element %s" % (self.class_name, text, locator))
        ActionChains(self.browser).pause(sleep).move_to_element(self.search_clickable_element(locator)).click().perform()
        self.search_element(locator).clear()
        for letter in text:
            self.search_element(locator).send_keys(letter)
        return self

    def _select_list_element(self, locator: tuple):
        select_element = self.search_element(locator)
        return Select(select_element)

    def select_option_by_value(self, locator: tuple, value: str):
        self.logger.debug("%s: Select value=%s in element %s" % (self.class_name, value, locator))
        self._select_list_element(locator).select_by_value(value)

    def select_option_by_text(self, locator: tuple, text: str):
        self.logger.debug("%s: Select %s in element %s" % (self.class_name, text, locator))
        self._select_list_element(locator).select_by_visible_text(text)
