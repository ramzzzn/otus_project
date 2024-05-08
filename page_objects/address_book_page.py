import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AddressBookPage(BasePage):
    BUTTON_ADD_NEW_ADDRESS = By.CSS_SELECTOR, "button[title='Add New Address']"
    LINK_DELETE_ADDRESS = By.XPATH, "//a[@role='delete-address']"
    BUTTON_DIALOG_OK = By.CSS_SELECTOR, "button.action-accept"
    BUTTON_DIALOG_CANCEL = By.CSS_SELECTOR, "button.action-dissmiss"
    SUCCESS_MESSAGE = By.CSS_SELECTOR, "div.message-success"

    @allure.step("Открываю страницу добавления адреса получателя")
    def open_add_address_page(self):
        self.logger.info("Open => Add Address page")
        self.click_action(self.BUTTON_ADD_NEW_ADDRESS)
        self.wait_title("Add New Address")

    def _get_parameter(self, param_name: str, value: str):
        return self.search_element(locator=(By.XPATH, f"//td[@data-th='{param_name}'][text()='{value}']"))

    @allure.step("Проверяю наличие добавленного адреса {street_address}")
    def check_additional_address(self, first_name: str, last_name: str, phone: str, street_address: str, city: str,
                                 postal_code: str, country: str):
        self.logger.info("Checking address")
        self._get_parameter("First Name", first_name)
        self._get_parameter("Last Name", last_name)
        self._get_parameter("Street Address", street_address)
        self._get_parameter("City", city)
        self._get_parameter("Country", country)
        self._get_parameter("Zip/Postal Code", postal_code)
        self._get_parameter("Phone", phone)

    @allure.step("Удаляю адрес {street_address}")
    def delete_additional_address(self, street_address: str):
        self.logger.info("Deleting address")
        self.click_action(locator=(By.XPATH, self.text_xpath(street_address) + "/ancestor::tr" +
                                   self.LINK_DELETE_ADDRESS[1]))
        self.click_action(self.BUTTON_DIALOG_OK)
        self.search_element(self.SUCCESS_MESSAGE)
