from selenium.webdriver.common.by import By
from test_ui.page_objects.base_page import BasePage


class AdminAddEditPriceRulePage(BasePage):
    BUTTON_SAVE = By.CSS_SELECTOR, "button#save"
    INPUT_RULE_NAME = By.CSS_SELECTOR, "input[name='name']"
    LABEL_ACTIVE = By.CSS_SELECTOR, "label.admin__actions-switch-label"
    SELECT_WEBSITES = By.CSS_SELECTOR, "select[name='website_ids']"
    SELECT_CUSTOMER_GROUPS = By.CSS_SELECTOR, "div.admin__action-multiselect"
    SELECT_CUSTOMER_GROUPS_BUTTON_DONE = By.CSS_SELECTOR, "button[data-bind='click: applyChange']"
    COLLAPSIBLE_TITLE_ACTIONS = By.XPATH, "//span[text()='Actions']"
    INPUT_DISCOUNT_AMOUNT = By.CSS_SELECTOR, "input[name='discount_amount']"
    BUTTON_DELETE = By.CSS_SELECTOR, "button#delete"
    BUTTON_DIALOG_OK = By.CSS_SELECTOR, "button.action-accept"
    SUCCESS_MESSAGE_DELETE = By.XPATH, "//div[text()='You deleted the rule.']"

    def _select_customer_group(self, customer_group: str):
        self.click_action(self.SELECT_CUSTOMER_GROUPS)
        self.click_action(locator=(By.XPATH, self.text_xpath(customer_group) + "/ancestor::div/input"))
        self.click_action(self.SELECT_CUSTOMER_GROUPS_BUTTON_DONE)

    def add_new_rule(self, rule_name: str, customer_group: str, discount: str):
        self.logger.info("Adding new rule")
        self.input(self.INPUT_RULE_NAME, rule_name)
        self.click_action(self.LABEL_ACTIVE)
        self.select_option_by_value(self.SELECT_WEBSITES, '1')
        self._select_customer_group(customer_group)
        self.click_action(self.COLLAPSIBLE_TITLE_ACTIONS)
        self.input(self.INPUT_DISCOUNT_AMOUNT, discount, timeout=1) # ждем, пока пройдет анимация раскрытия элемента
        self.click_action(self.BUTTON_SAVE)
        self.wait_title("Catalog Price Rule / Promotions / Marketing / Magento Admin")
        self.search_element(locator=(By.XPATH, self.contains_text_xpath("You saved the rule.")))

    def delete_rule(self):
        self.logger.info("Deleting rule")
        self.click_action(self.BUTTON_DELETE)
        self.click_action(self.BUTTON_DIALOG_OK)
        self.wait_title("Catalog Price Rule / Promotions / Marketing / Magento Admin")
        self.search_element(self.SUCCESS_MESSAGE_DELETE)
