from selenium.webdriver.common.by import By
from test_ui.page_objects.base_page import BasePage


class CartPage(BasePage):
    PRODUCT_ITEM_DETAILS = By.XPATH, "//tbody//div[@class='product-item-details']"
    BUTTON_REMOVE_ITEM = By.CSS_SELECTOR, "a.action-delete"
    EMPTY_CART = By.CSS_SELECTOR, "div.cart-empty"

    def _get_value_from_cart_item(self, selector: str):
        return self.search_element(locator=(By.XPATH, self.PRODUCT_ITEM_DETAILS[1] + selector))

    def get_product_name_from_cart_item(self, product_name: str):
        self.logger.info("Getting product from cart")
        return self._get_value_from_cart_item(selector=f"//a[text()='{product_name}']")

    def get_attribute_from_cart_item(self, attribute_value: str):
        self.logger.info("Getting attribute from cart")
        return self._get_value_from_cart_item(selector=f"//dl/dd[normalize-space()='{attribute_value}']")

    def remove_item_from_cart(self):
        self.logger.info("Removing product from cart")
        self.click_action(self.BUTTON_REMOVE_ITEM)
        self.search_element(self.EMPTY_CART)
