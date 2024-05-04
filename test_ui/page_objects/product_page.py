import random

from selenium.webdriver.common.by import By
from test_ui.page_objects.base_page import BasePage


class ProductPage(BasePage):
    BUTTON_ADD_TO_CART = By.XPATH, "//button[@title='Add to Cart']"
    BUTTON_ADD_TO_WISH_LIST = By.CSS_SELECTOR, "div.product-addto-links button[data-action='add-to-wishlist']"
    TAB_REVIEW = By.CSS_SELECTOR, "div > a#tab-label-reviews-title"
    INPUT_NICKNAME = By.CSS_SELECTOR, "input#nickname_field"
    INPUT_SUMMARY = By.CSS_SELECTOR, "input#summary_field"
    INPUT_REVIEW = By.CSS_SELECTOR, "textarea#review_field"
    BUTTON_SUBMIT_REVIEW = By.CSS_SELECTOR, "button.submit"
    RATING_ELEMENT = By.CSS_SELECTOR, "div.review-control-vote"
    SUCCESS_MESSAGE = By.CSS_SELECTOR, "div.message-success"

    def _select_product_attribute(self, attribute: str, attribute_value: str):
        return f"//div[@class='swatch-attribute {attribute}']//div[@aria-label='{attribute_value}']"

    def _select_product_size(self, size: str):
        self.click_action(locator=(By.XPATH, self._select_product_attribute(attribute='size', attribute_value=size)))

    def _select_product_color(self, color: str):
        self.click_action(locator=(By.XPATH, self._select_product_attribute(attribute='color', attribute_value=color)))

    def add_to_cart_product(self, size: str, color: str):
        self.logger.info("Adding product to cart")
        if size and color:
            self._select_product_size(size)
            self._select_product_color(color)
        self.click_action(self.BUTTON_ADD_TO_CART)

    def add_to_wish_list(self):
        self.logger.info("Adding product to wish list")
        self.click_action(self.BUTTON_ADD_TO_WISH_LIST)
        self.wait_title("My Wish List")

    def _rate_product(self):
        self.click_action(locator=(By.CSS_SELECTOR, self.RATING_ELEMENT[1] +
                                   f" > label#Rating_{str(random.randint(1, 5))}_label"), timeout=1)

    def review_product(self, nickname: str, summary: str, review: str):
        self.logger.info("Review product")
        self.click_action(self.TAB_REVIEW)
        self._rate_product()
        self.input(self.INPUT_NICKNAME, nickname)
        self.input(self.INPUT_SUMMARY, summary)
        self.input(self.INPUT_REVIEW, review)
        self.click_action(self.BUTTON_SUBMIT_REVIEW, timeout=1)
        self.search_element(self.SUCCESS_MESSAGE)
