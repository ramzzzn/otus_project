from selenium.webdriver.common.by import By
from test_ui.page_objects.base_page import BasePage


class GiftRegistryPage(BasePage):
    BUTTON_ADD_NEW = By.CSS_SELECTOR, "a.primary.add"
    LINK_DELETE = By.XPATH, "//a[@title='Delete']"
    BUTTON_DIALOG_OK = By.CSS_SELECTOR, "button.action-accept"
    BUTTON_DIALOG_CANCEL = By.CSS_SELECTOR, "button.action-dissmiss"
    SUCCESS_MESSAGE = By.CSS_SELECTOR, "div.message-success"

    def open_add_new_gift_registry(self):
        self.logger.info("Open => Create Gift Registry page")
        self.click_action(self.BUTTON_ADD_NEW)
        self.wait_title("Create Gift Registry")

    def delete_gift_registry(self, event: str):
        self.logger.info("Deleting Gift Registry")
        self.click_action(locator=(By.XPATH, self.contains_text_xpath(event) + "/ancestor::tr" +
                                   self.LINK_DELETE[1]))
        self.click_action(self.BUTTON_DIALOG_OK)
        self.search_element(self.SUCCESS_MESSAGE)
        