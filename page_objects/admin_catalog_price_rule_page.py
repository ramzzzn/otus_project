import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdminCatalogPricePage(BasePage):
    BUTTON_ADD_NEW_RULE = By.CSS_SELECTOR, "button#add"
    INPUT_RULE_NAME = By.CSS_SELECTOR, "input#promo_catalog_grid_filter_name"
    BUTTON_SEARCH = By.CSS_SELECTOR, "div.admin__filter-actions > button[title='Search']"
    LINK_EDIT = By.XPATH, "//a[text()='Edit']"

    @allure.step("Открываю страницу добавления нового правила цены")
    def open_add_new_rule_page(self):
        self.logger.info("Open => Add Rule page")
        self.click_action(self.BUTTON_ADD_NEW_RULE)
        self.wait_title("New Catalog Price Rule / Catalog Price Rule / Promotions / Marketing / Magento Admin")

    @allure.step("Выполняю поиск правила {rule_name}")
    def search_rule_by_name(self, rule_name: str):
        self.logger.info("Searching rule %s" % rule_name)
        self.input(self.INPUT_RULE_NAME, rule_name)
        self.click_action(self.BUTTON_SEARCH)

    @allure.step("Открываю страницу редактирования правила {rule_name}")
    def edit_rule(self, rule_name: str):
        self.logger.info("Open => Edit Rule page")
        self.click_action(locator=(By.XPATH, self.contains_text_xpath(rule_name) + "/ancestor::tr" + self.LINK_EDIT[1]))
        self.wait_title(f"{rule_name} / Catalog Price Rule / Promotions / Marketing / Magento Admin")



