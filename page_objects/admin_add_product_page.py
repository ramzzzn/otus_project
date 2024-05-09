import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdminAddProductPage(BasePage):
    BUTTON_SAVE = By.CSS_SELECTOR, "button#save-button"
    INPUT_PRODUCT_NAME = By.CSS_SELECTOR, "input[name='product[name]']"
    INPUT_SKU = By.CSS_SELECTOR, "input[name='product[sku]']"
    INPUT_PRICE = By.CSS_SELECTOR, "input[name='product[price]']"
    SUCCESS_MESSAGE_ADD = By.XPATH, "//div[text()='You saved the product.']"
    BUTTON_BACK = By.CSS_SELECTOR, "button#back"

    @allure.step("Добавляю новый товар {product_name}")
    def add_new_product(self, product_name: str, sku: str, price: str):
        self.logger.info("Adding new product")
        self.input(self.INPUT_PRODUCT_NAME, product_name)
        self.input(self.INPUT_SKU, sku)
        self.input(self.INPUT_PRICE, price)
        self.click_action(self.BUTTON_SAVE)
        self.search_element(self.SUCCESS_MESSAGE_ADD)

    @allure.step("Переход назад на страницу товаров")
    def back_to_products_page(self):
        self.logger.info("Back to Products Page")
        self.click_action(self.BUTTON_BACK, sleep=2)
        self.wait_title("Products / Inventory / Catalog / Magento Admin")
