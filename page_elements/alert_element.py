from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertElement:
    ALERT_SUCCESS = By.CSS_SELECTOR, "div.message-success"
    ALERT_SUCCESS_CART_LINK = By.XPATH, "//div/a[text()='shopping cart']"

    def __init__(self, browser):
        self.browser = browser
        self.alert_success = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.ALERT_SUCCESS))

    @property
    def shopping_cart(self):
        return self.alert_success.find_element(*self.ALERT_SUCCESS_CART_LINK)
