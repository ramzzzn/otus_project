from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from test_ui.page_objects.base_page import BasePage


class WishListPage(BasePage):
    WISH_LIST = By.XPATH, "//div[@class='products-grid wishlist']"
    BUTTON_REMOVE_ITEM = By.XPATH, "//a[@class='btn-remove action delete']"

    def _product_name_xpath(self, product_name: str):
        return f"//a[normalize-space()='{product_name}']"

    def search_product_in_wish_list(self, product_name: str):
        self.logger.info("Searching product in Wish List")
        ActionChains(self.browser).move_to_element(self.search_element(locator=(By.XPATH, self.WISH_LIST[1] +
                                                                                self._product_name_xpath(product_name)))
                                                   ).perform()

    def remove_product_from_wish_list(self, product_name: str):
        self.logger.info("Removing product from Wish List")
        self.click_action(locator=(By.XPATH, self._product_name_xpath(product_name) +
                                   "/ancestor::div[@class='product-item-info']//div[@class='product-item-actions']"
                                   + self.BUTTON_REMOVE_ITEM[1]))
