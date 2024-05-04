from selenium.webdriver.common.by import By
from test_ui.page_objects.base_page import BasePage


class AdminProductsPage(BasePage):
    BUTTON_ADD_NEW_PRODUCT = By.CSS_SELECTOR, "button#add_new_product-button"
    INPUT_SEARCH = By.CSS_SELECTOR, "input#fulltext"
    BUTTON_SEARCH = By.CSS_SELECTOR, "div.data-grid-search-control-wrap > button.action-submit"
    PRODUCT_CHECKBOX = By.XPATH, "//input[@type='checkbox']"
    DROPDOWN_MENU_ACTIONS = By.CSS_SELECTOR, "button.action-select"
    DROPDOWN_MENU_ACTIONS_DELETE = By.XPATH, "//span[text()='Delete']"
    BUTTON_DIALOG_OK = By.CSS_SELECTOR, "button.action-accept"
    SUCCESS_MESSAGE_DELETE = By.XPATH, "//div[text()='A total of 1 record(s) have been deleted.']"

    def open_add_product_page(self):
        self.logger.info("Open => Add Product page")
        self.click_action(self.BUTTON_ADD_NEW_PRODUCT)
        self.wait_title("New Product / Products / Inventory / Catalog / Magento Admin")

    def search_product(self, product_name: str):
        self.logger.info("Searching product")
        self.input(self.INPUT_SEARCH, product_name)
        self.click_action(self.BUTTON_SEARCH)

    def delete_product(self, product_name: str):
        self.logger.info("Deleting product")
        self.click_action(
            locator=(By.XPATH, self.text_xpath(product_name) + "/ancestor::tr" + self.PRODUCT_CHECKBOX[1]))
        self.click_action(self.DROPDOWN_MENU_ACTIONS)
        self.click_action(self.DROPDOWN_MENU_ACTIONS_DELETE)
        self.click_action(self.BUTTON_DIALOG_OK)
        self.search_element(self.SUCCESS_MESSAGE_DELETE)
