import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class MainPage(BasePage):
    BANNER_PROMO_YOGA = By.CSS_SELECTOR, "a.block-promo.home-main"
    BANNER_PROMO_PANTS = By.CSS_SELECTOR, "a.block-promo.home-pants"
    BANNER_PROMO_TEES = By.CSS_SELECTOR, "a.block-promo.home-t-shirts"
    BANNER_PROMO_ERIN = By.CSS_SELECTOR, "a.block-promo.home-erin"
    BANNER_PROMO_PERFORMANCE = By.CSS_SELECTOR, "a.block-promo.home-performance"
    BANNER_PROMO_ECO = By.CSS_SELECTOR, "a.block-promo.home-eco"
    BUTTON_ADD_TO_CART = By.XPATH, "//button[@title='Add to Cart']"
    ALERT_SUCCESS = By.CSS_SELECTOR, "div.message-success"

    @allure.step("Открываю главную страницу")
    def open_main_page(self):
        self.logger.info("Open => Main page")
        self.open_page(page='')
        self.wait_title("Magento 2 Commerce (Enterprise) B2B Demo - Magebit")

    def _select_product_card(self, product_name: str):
        return f"//a[@title='{product_name}']/ancestor::div[@class='product-item-info']"

    def _select_product_attribute(self, product_name: str, attribute: str, attribute_value: str):
        return self._select_product_card(product_name) + f"//div[@class='swatch-attribute {attribute}']" \
                                                         f"//div[@aria-label='{attribute_value}']"

    def _select_product_size(self, product_name: str, size: str):
        self.click_action(locator=(By.XPATH, self._select_product_attribute(product_name=product_name, attribute='size',
                                                                            attribute_value=size)))

    def _select_product_color(self, product_name: str, color: str):
        self.click_action(
            locator=(By.XPATH, self._select_product_attribute(product_name=product_name, attribute='color',
                                                              attribute_value=color)))

    @allure.step("Добавляю товар {product_name}, с размером {size} и цветом {color} в корзину")
    def add_to_cart_product(self, product_name: str, size: str, color: str):
        self.logger.info("Adding product to cart")
        ActionChains(self.browser).move_to_element(self.search_element(
            locator=(By.XPATH, self._select_product_card(product_name=product_name)))).perform()
        if size and color:
            self._select_product_size(product_name, size)
            self._select_product_color(product_name, color)
        self.click_action(locator=(By.XPATH, self._select_product_card(product_name=product_name) +
                                   self.BUTTON_ADD_TO_CART[1]), sleep=3)
        self.search_element(self.ALERT_SUCCESS)

    @allure.step("Открываю страницу товара {product_name}")
    def open_product_page(self, product_name: str):
        self.logger.info("Open => Product page")
        self.click_action(locator=(By.XPATH, self._select_product_card(product_name=product_name)))
        self.wait_title(f"{product_name}")
