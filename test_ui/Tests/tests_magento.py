import pytest
from test_ui.page_objects.main_page import MainPage
from test_ui.page_objects.cart_page import CartPage
from test_ui.page_objects.product_page import ProductPage
from test_ui.page_objects.user_login_page import UserLoginPage
from test_ui.page_objects.wish_list_page import WishListPage
from test_ui.page_objects.customer_registration_page import CustomerRegistrationPage
from test_ui.page_objects.company_registration_page import CompanyRegistrationPage
from test_ui.page_objects.address_book_page import AddressBookPage
from test_ui.page_objects.add_address_page import AddAddressPage
from test_ui.page_objects.gift_registry_page import GiftRegistryPage
from test_ui.page_objects.create_gift_registry_page import CreateGiftRegistryPage
from test_ui.page_objects.admin_login_page import AdminLoginPage
from test_ui.page_objects.admin_products_page import AdminProductsPage
from test_ui.page_objects.admin_add_product_page import AdminAddProductPage
from test_ui.page_objects.admin_catalog_price_rule_page import AdminCatalogPricePage
from test_ui.page_objects.admin_add_edit_price_rule_page import AdminAddEditPriceRulePage
from test_ui.page_elements.alert_element import AlertElement
from test_ui.page_elements.header_element import HeaderElement
from test_ui.page_elements.sidebar_element import SidebarElement
from test_ui.page_elements.admin_menu_panel import AdminMenuElement
from test_ui.page_elements.admin_drpd_menu_element import AdminDropdownMenuElement
from test_ui.Tests.helpers import generate_test_customer, generate_test_data_company, generate_test_address, \
    generate_test_event, generate_test_review, generate_test_product, generate_test_rule


class TestMagento:
    """
    test_add_product_to_cart_from_main_page: Добавление товара в корзину с главной страницы.
    test_add_product_to_cart_from_product_page: Добавление товара в корзину со страницы товара.
    test_add_product_to_wish_list: Добавление товара в Избранное.
    test_review_product: Добавление отзыва по товару.
    test_customer_registration: Регистрация покупателя.
    test_company_account_registration: Регистрация корпоративного аккаунта.
    test_add_delete_new_customer_address: Добавление и удаление адреса покупателя.
    test_add_delete_gift_registry: Добавление и удаление списка подарков у покупателя.
    test_admin_add_new_product: Добавление нового товара в разделе администратора.
    test_admin_add_new_catalog_price_rule: Добавление нового правила цены для товаров в разделе администратора.
    """

    @pytest.fixture(scope="session")
    def demo_user(self):
        return {
            'email': "roni_cost@example.com",
            'password': "roni_cost3@example.com"
        }

    @pytest.fixture(scope="session")
    def demo_admin_user(self):
        return {
            'username': "magebit",
            'password': "Demo123"
        }

    @pytest.mark.parametrize("product_name, size, color", [('Radiant Tee', 'M', 'Blue'),
                                                           ('LifeLong Fitness IV', None, None)
                                                           ], ids=['product_w_attributes', 'product_wo_attributes'])
    def test_add_product_to_cart_from_main_page(self, browser, product_name, size, color):
        MainPage(browser).open_main_page()
        MainPage(browser).add_to_cart_product(product_name, size, color)
        AlertElement(browser).shopping_cart.click()
        CartPage(browser).get_product_name_from_cart_item(product_name)
        if size and color:
            CartPage(browser).get_attribute_from_cart_item(size)
            CartPage(browser).get_attribute_from_cart_item(color)
        CartPage(browser).remove_item_from_cart()

    @pytest.mark.parametrize("product_name, size, color", [('Breathe-Easy Tank', 'XL', 'Purple'),
                                                           ('Fusion Backpack', None, None)
                                                           ], ids=['product_w_attributes', 'product_wo_attributes'])
    def test_add_product_to_cart_from_product_page(self, browser, product_name, size, color):
        MainPage(browser).open_main_page()
        MainPage(browser).open_product_page(product_name)
        ProductPage(browser).add_to_cart_product(size, color)
        AlertElement(browser).shopping_cart.click()
        CartPage(browser).get_product_name_from_cart_item(product_name)
        if size and color:
            CartPage(browser).get_attribute_from_cart_item(size)
            CartPage(browser).get_attribute_from_cart_item(color)
        CartPage(browser).remove_item_from_cart()

    @pytest.mark.parametrize("product_name", ['Hero Hoodie', 'Push It Messenger Bag'])
    def test_add_product_to_wish_list(self, browser, product_name, demo_user):
        MainPage(browser).open_main_page()
        HeaderElement(browser).sign_in.click()
        UserLoginPage(browser).login_user(**demo_user)
        MainPage(browser).open_product_page(product_name)
        ProductPage(browser).add_to_wish_list()
        WishListPage(browser).search_product_in_wish_list(product_name)
        WishListPage(browser).remove_product_from_wish_list(product_name)
        HeaderElement(browser).sign_out()

    @pytest.mark.parametrize("product_name", ['Hero Hoodie', 'Push It Messenger Bag'])
    def test_review_product(self, browser, product_name):
        MainPage(browser).open_main_page()
        MainPage(browser).open_product_page(product_name)
        test_review = generate_test_review()
        ProductPage(browser).review_product(**test_review)

    def test_customer_registration(self, browser):
        MainPage(browser).open_main_page()
        HeaderElement(browser).open_customer_reg_page()
        test_user = generate_test_customer()
        CustomerRegistrationPage(browser).register_customer(**test_user)
        HeaderElement(browser).sign_out()

    def test_company_account_registration(self, browser):
        MainPage(browser).open_main_page()
        HeaderElement(browser).open_company_reg_page()
        test_company = generate_test_data_company()
        CompanyRegistrationPage(browser).register_company(**test_company)

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
