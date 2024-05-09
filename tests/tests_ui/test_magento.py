import allure
import pytest
from page_objects.main_page import MainPage
from page_objects.cart_page import CartPage
from page_objects.product_page import ProductPage
from page_objects.user_login_page import UserLoginPage
from page_objects.wish_list_page import WishListPage
from page_objects.customer_registration_page import CustomerRegistrationPage
from page_objects.company_registration_page import CompanyRegistrationPage
from page_objects.address_book_page import AddressBookPage
from page_objects.add_address_page import AddAddressPage
from page_objects.gift_registry_page import GiftRegistryPage
from page_objects.create_gift_registry_page import CreateGiftRegistryPage
from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_products_page import AdminProductsPage
from page_objects.admin_add_product_page import AdminAddProductPage
from page_objects.admin_catalog_price_rule_page import AdminCatalogPricePage
from page_objects.admin_add_edit_price_rule_page import AdminAddEditPriceRulePage
from page_elements.alert_element import AlertElement
from page_elements.header_element import HeaderElement
from page_elements.sidebar_element import SidebarElement
from page_elements.admin_menu_panel import AdminMenuElement
from page_elements.admin_drpd_menu_element import AdminDropdownMenuElement
from tests.tests_ui.helpers import generate_test_customer, generate_test_data_company, generate_test_address, \
    generate_test_event, generate_test_review, generate_test_product, generate_test_rule


@allure.feature('UI tests')
class TestMagento:
    """
    test_add_product_to_cart_from_main_page: Проверка добавления товара в корзину с главной страницы
    test_add_product_to_cart_from_product_page: Проверка добавления товара в корзину со страницы товара
    test_add_product_to_wish_list: Проверка добавления товара в Избранное
    test_review_product: Проверка добавления отзыва по товару
    test_customer_registration: Проверка регистрации покупателя
    test_company_account_registration: Проверка регистрации корпоративного аккаунта компании
    test_add_delete_new_customer_address: Проверка добавления и удаления адреса покупателя
    test_add_delete_gift_registry: Проверка добавления и удаления списка подарков у покупателя
    test_admin_add_new_product: Проверка добавления нового товара в разделе администратора
    test_admin_add_new_catalog_price_rule: Проверка добавления нового правила цены для товаров в разделе администратора
    """

    @pytest.fixture(scope="session")
    def demo_user(self):
        return {
            'email': "roni_cost@example.com",
            'password': "roni_cost3@example.com",
            'first_name': "Veronica",
            'last_name': "Costello"
        }

    @pytest.fixture(scope="session")
    def demo_admin_user(self):
        return {
            'username': "magebit",
            'password': "Demo123"
        }

    @allure.title("Проверка добавления товара в корзину с главной страницы")
    @pytest.mark.parametrize("product_name, size, color", [('Radiant Tee', 'M', 'Blue'),
                                                           ('LifeLong Fitness IV', None, None)
                                                           ], ids=['product_w_attributes', 'product_wo_attributes'])
    def test_add_product_to_cart_from_main_page(self, browser, product_name, size, color):
        MainPage(browser).open_main_page()
        MainPage(browser).add_to_cart_product(product_name, size, color)
        AlertElement(browser).shopping_cart.click()
        CartPage(browser).check_product_is_present_in_cart(product_name)
        if size and color:
            CartPage(browser).get_attribute_from_cart_item(size)
            CartPage(browser).get_attribute_from_cart_item(color)
        CartPage(browser).remove_item_from_cart()

    @allure.title("Проверка добавления товара в корзину со страницы товара")
    @pytest.mark.parametrize("product_name, size, color", [('Breathe-Easy Tank', 'XL', 'Purple'),
                                                           ('Fusion Backpack', None, None)
                                                           ], ids=['product_w_attributes', 'product_wo_attributes'])
    def test_add_product_to_cart_from_product_page(self, browser, product_name, size, color):
        MainPage(browser).open_main_page()
        MainPage(browser).open_product_page(product_name)
        ProductPage(browser).add_to_cart_product(size, color)
        AlertElement(browser).shopping_cart.click()
        CartPage(browser).check_product_is_present_in_cart(product_name)
        if size and color:
            CartPage(browser).get_attribute_from_cart_item(size)
            CartPage(browser).get_attribute_from_cart_item(color)
        CartPage(browser).remove_item_from_cart()

    @allure.title("Проверка добавления товара в Избранное")
    @pytest.mark.parametrize("product_name", ['Hero Hoodie', 'Push It Messenger Bag'])
    def test_add_product_to_wish_list(self, browser, product_name, demo_user):
        MainPage(browser).open_main_page()
        MainPage(browser).open_product_page(product_name)
        ProductPage(browser).add_to_wish_list()
        HeaderElement(browser).sign_in.click()
        UserLoginPage(browser).login_user(**demo_user)
        WishListPage(browser).search_product_in_wish_list(product_name)
        WishListPage(browser).remove_product_from_wish_list(product_name)
        HeaderElement(browser).sign_out()

    @allure.title("Проверка добавления отзыва по товару")
    @pytest.mark.parametrize("product_name", ['Hero Hoodie', 'Push It Messenger Bag'])
    def test_review_product(self, browser, product_name):
        MainPage(browser).open_main_page()
        MainPage(browser).open_product_page(product_name)
        test_review = generate_test_review()
        ProductPage(browser).review_product(**test_review)

    @allure.title("Проверка регистрации покупателя")
    def test_customer_registration(self, browser):
        MainPage(browser).open_main_page()
        HeaderElement(browser).open_customer_reg_page()
        test_user = generate_test_customer()
        CustomerRegistrationPage(browser).register_customer(**test_user)
        HeaderElement(browser).sign_out()
        HeaderElement(browser).sign_in.click()
        UserLoginPage(browser).login_user(**test_user)
        HeaderElement(browser).sign_out()

    @allure.title("Проверка регистрации корпоративного аккаунта компании")
    def test_company_account_registration(self, browser):
        MainPage(browser).open_main_page()
        HeaderElement(browser).open_company_reg_page()
        test_company = generate_test_data_company()
        CompanyRegistrationPage(browser).register_company(**test_company)

    @allure.title("Проверка добавления и удаления адреса покупателя")
    def test_add_delete_new_customer_address(self, browser, demo_user):
        MainPage(browser).open_main_page()
        HeaderElement(browser).sign_in.click()
        UserLoginPage(browser).login_user(**demo_user)
        HeaderElement(browser).open_account_page()
        SidebarElement(browser).address_book.click()
        AddressBookPage(browser).open_add_address_page()
        test_address = generate_test_address()
        AddAddressPage(browser).add_new_address(**test_address)
        AddressBookPage(browser).check_additional_address(**test_address)
        AddressBookPage(browser).delete_additional_address(test_address['street_address'])
        HeaderElement(browser).sign_out()

    @allure.title("Проверка добавления и удаления списка подарков у покупателя")
    def test_add_delete_gift_registry(self, browser, demo_user):
        MainPage(browser).open_main_page()
        HeaderElement(browser).sign_in.click()
        UserLoginPage(browser).login_user(**demo_user)
        HeaderElement(browser).open_account_page()
        SidebarElement(browser).gift_registry.click()
        GiftRegistryPage(browser).open_add_new_gift_registry()
        test_event = generate_test_event()
        CreateGiftRegistryPage(browser).create_gift_registry(**test_event)
        GiftRegistryPage(browser).delete_gift_registry(test_event['event'])
        HeaderElement(browser).sign_out()

    @allure.title("Проверка добавления нового товара в разделе администратора")
    def test_admin_add_new_product(self, browser, demo_admin_user):
        AdminLoginPage(browser).open_login_page()
        AdminLoginPage(browser).login_admin(**demo_admin_user)
        AdminMenuElement(browser).open_products_page()
        AdminProductsPage(browser).open_add_product_page()
        test_product = generate_test_product()
        AdminAddProductPage(browser).add_new_product(**test_product)
        AdminAddProductPage(browser).back_to_products_page()
        AdminProductsPage(browser).search_product(test_product['product_name'])
        AdminProductsPage(browser).delete_product(test_product['product_name'])
        AdminDropdownMenuElement(browser).sign_out()

    @allure.title("Проверка добавления нового правила цены для товаров в разделе администратора")
    def test_admin_add_new_catalog_price_rule(self, browser, demo_admin_user):
        AdminLoginPage(browser).open_login_page()
        AdminLoginPage(browser).login_admin(**demo_admin_user)
        AdminMenuElement(browser).open_catalog_price_rule_page()
        AdminCatalogPricePage(browser).open_add_new_rule_page()
        test_rule = generate_test_rule()
        AdminAddEditPriceRulePage(browser).add_new_rule(**test_rule)
        AdminCatalogPricePage(browser).search_rule_by_name(test_rule['rule_name'])
        AdminCatalogPricePage(browser).edit_rule(test_rule['rule_name'])
        AdminAddEditPriceRulePage(browser).delete_rule()
        AdminDropdownMenuElement(browser).sign_out()
