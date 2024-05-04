from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class AdminDropdownMenuElement:
    DROPDOWN_MENU = By.CSS_SELECTOR, "div.admin-user"
    SIGN_OUT_LINK = By.CSS_SELECTOR, "a.account-signout"

    def __init__(self, browser, timeout=5):
        self.browser = browser
        self.logger = browser.logger
        self.wait = WebDriverWait(browser, timeout)
        self.admin_dropdown_menu = self.wait.until(EC.visibility_of_element_located(self.DROPDOWN_MENU))

    def _click_menu_element(self, element):
        ActionChains(self.browser).move_to_element(element).click().perform()

    def sign_out(self):
        self.logger.info("Sign out!")
        # особенность UI - после загрузки страницы нужно подождать какое-то время, т.к кнопка вызова меню неактивна
        ActionChains(self.browser).pause(2).move_to_element(self.admin_dropdown_menu).click().perform()
        self.wait.until(EC.visibility_of_element_located(self.SIGN_OUT_LINK)).click()
        self.wait.until(EC.title_is("Magento Admin"))
