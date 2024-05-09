import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminMenuElement:
    ADMIN_MENU = By.CSS_SELECTOR, "ul#nav"
    ADMIN_MENU_DASHBOARD = By.CSS_SELECTOR, "li#menu-magento-backend-dashboard"
    ADMIN_MENU_SALES = By.CSS_SELECTOR, "li#menu-magento-sales-sales"
    ADMIN_MENU_CATALOG = By.CSS_SELECTOR, "li#menu-magento-catalog-catalog"
    ADMIN_MENU_CUSTOMERS = By.CSS_SELECTOR, "li#menu-magento-customer-customer"
    ADMIN_MENU_MARKETING = By.CSS_SELECTOR, "li#menu-magento-backend-marketing"
    ADMIN_MENU_CONTENT = By.CSS_SELECTOR, "li#menu-magento-backend-content"
    ADMIN_MENU_REPORTS = By.CSS_SELECTOR, "li#menu-magento-reports-report"
    ADMIN_MENU_STORES = By.CSS_SELECTOR, "li#menu-magento-backend-stores"
    ADMIN_MENU_SYSTEM = By.CSS_SELECTOR, "li#menu-magento-backend-system"
    ADMIN_MENU_PARTNERS = By.CSS_SELECTOR, "li#menu-magento-marketplace-partners"
    SUBMENU_CATALOG_PRODUCTS = By.CSS_SELECTOR, "li.item-catalog-products"
    SUBMENU_CATALOG_PRICE_RULE = By.CSS_SELECTOR, "li.item-promo-catalog"

    def __init__(self, browser, timeout=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)
        self.logger = browser.logger
        self.admin_menu = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.ADMIN_MENU))

    @property
    def dashboard(self):
        return self.admin_menu.find_element(*self.ADMIN_MENU_DASHBOARD)

    @property
    def sales(self):
        return self.admin_menu.find_element(*self.ADMIN_MENU_SALES)

    @property
    def catalog(self):
        return self.admin_menu.find_element(*self.ADMIN_MENU_CATALOG)

    @property
    def customers(self):
        return self.admin_menu.find_element(*self.ADMIN_MENU_CUSTOMERS)

    @property
    def marketing(self):
        return self.admin_menu.find_element(*self.ADMIN_MENU_MARKETING)

    @property
    def content(self):
        return self.admin_menu.find_element(*self.ADMIN_MENU_CONTENT)

    @property
    def reports(self):
        return self.admin_menu.find_element(*self.ADMIN_MENU_REPORTS)

    @property
    def stores(self):
        return self.admin_menu.find_element(*self.ADMIN_MENU_STORES)

    @property
    def system(self):
        return self.admin_menu.find_element(*self.ADMIN_MENU_SYSTEM)

    @property
    def partners(self):
        return self.admin_menu.find_element(*self.ADMIN_MENU_PARTNERS)

    def wait_title(self, title: str):
        self.logger.debug("Waiting for title: %s" % title)
        try:
            self.wait.until(EC.title_is(title))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG
            )
            error_message = f"Expected title: '{title}', but was '{self.browser.title}'"
            self.logger.exception("%s" % error_message)
            raise TimeoutException(error_message)

    def click_submenu_item(self, element):
        ActionChains(self.browser).pause(1).move_to_element(self.wait.until(
            EC.visibility_of_element_located(element))).click().perform()

    def open_products_page(self):
        self.logger.info("Open => Products page")
        self.catalog.click()
        self.click_submenu_item(self.SUBMENU_CATALOG_PRODUCTS)
        self.wait_title('Products / Inventory / Catalog / Magento Admin')

    def open_catalog_price_rule_page(self):
        self.logger.info("Open => Catalog Price page")
        self.marketing.click()
        self.click_submenu_item(self.SUBMENU_CATALOG_PRICE_RULE)
        self.wait_title('Catalog Price Rule / Promotions / Marketing / Magento Admin')
