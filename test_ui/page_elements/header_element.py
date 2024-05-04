from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class HeaderElement:
    HEADER_PANEL = By.CSS_SELECTOR, "div.panel.header"
    SIGN_IN_LINK = By.XPATH, "//a[normalize-space()='Sign In']"
    CREATE_ACCOUNT_MENU = By.XPATH, "//div[@class='panel header']//span[text()='Create an Account']"
    CREATE_CUSTOMER_LINK = By.XPATH, "//a[text()='Create New Customer']"
    CREATE_COMPANY_ACCOUNT_LINK = By.XPATH, "//a[text()='Create New Company Account']"
    CUSTOMER_MENU = By.CSS_SELECTOR, "button.switch"
    SIGN_OUT_LINK = By.XPATH, "//a[normalize-space()='Sign Out']"
    MY_ACCOUNT_LINK = By.XPATH, "//a[normalize-space()='My Account']"

    def __init__(self, browser, timeout=5):
        self.browser = browser
        self.logger = browser.logger
        self.wait = WebDriverWait(browser, timeout)
        self.header_panel = self.wait.until(EC.visibility_of_element_located(self.HEADER_PANEL))

    @property
    def sign_in(self):
        return self.header_panel.find_element(*self.SIGN_IN_LINK)

    @property
    def create_account_menu(self):
        return self.header_panel.find_element(*self.CREATE_ACCOUNT_MENU)

    @property
    def customer_menu(self):
        return self.header_panel.find_element(*self.CUSTOMER_MENU)

    def _click_header_element(self, element):
        ActionChains(self.browser).move_to_element(element).click().perform()

    def _open_create_account_menu(self, locator: tuple):
        self._click_header_element(self.create_account_menu)
        try:
            self.wait.until(EC.visibility_of_element_located(locator)).click()
        except TimeoutException:
            raise AssertionError(f"Не найден ни один элемент по указанному селектору: {locator}")

    def open_login_page(self):
        self.logger.info("Open => Login page")
        self._click_header_element(self.sign_in)
        self.wait.until(EC.title_is('Customer Login'))

    def open_customer_reg_page(self):
        self.logger.info("Open => Create Customer page")
        self._open_create_account_menu(self.CREATE_CUSTOMER_LINK)
        self.wait.until(EC.title_is('Create New Customer Account'))

    def open_company_reg_page(self):
        self.logger.info("Open => Create Company page")
        self._open_create_account_menu(self.CREATE_COMPANY_ACCOUNT_LINK)
        self.wait.until(EC.title_is('New Company'))

    def sign_out(self):
        self.logger.info("Sign out!")
        self._click_header_element(self.customer_menu)
        self.wait.until(EC.visibility_of_element_located(self.SIGN_OUT_LINK)).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='You are signed out']")))

    def open_account_page(self):
        self.logger.info("Open => My Account page")
        self._click_header_element(self.customer_menu)
        self.wait.until(EC.visibility_of_element_located(self.MY_ACCOUNT_LINK)).click()
        self.wait.until(EC.title_is('My Account'))
