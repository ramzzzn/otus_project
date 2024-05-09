from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SidebarElement:
    SIDEBAR_MAIN = By.CSS_SELECTOR, "div.sidebar.sidebar-main"

    def __init__(self, browser):
        self.browser = browser
        self.sidebar_account = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.SIDEBAR_MAIN))

    def _search_sidebar_item(self, item: str):
        return self.sidebar_account.find_element(By.XPATH, f"//ul[@class='nav items']//a[normalize-space()='{item}']")

    @property
    def my_account(self):
        return self._search_sidebar_item("My Account")

    @property
    def my_orders(self):
        return self._search_sidebar_item("My Orders")

    @property
    def my_d_products(self):
        return self._search_sidebar_item("My Downloadable Products")

    @property
    def my_req_lists(self):
        return self._search_sidebar_item("My Requisition Lists")

    @property
    def my_wish_list(self):
        return self._search_sidebar_item("My Wish List")

    @property
    def address_book(self):
        return self._search_sidebar_item("Address Book")

    @property
    def account_info(self):
        return self._search_sidebar_item("Account Information")

    @property
    def store_credit(self):
        return self._search_sidebar_item("Store Credit")

    @property
    def stored_pmnt_methods(self):
        return self._search_sidebar_item("Stored Payment Methods")

    @property
    def gift_card(self):
        return self._search_sidebar_item("Gift Card")

    @property
    def company_structure(self):
        return self._search_sidebar_item("Company Structure")

    @property
    def reward_points(self):
        return self._search_sidebar_item("Reward Points")

    @property
    def gift_registry(self):
        return self._search_sidebar_item("Gift Registry")

    @property
    def my_product_reviews(self):
        return self._search_sidebar_item("My Product Reviews")

    @property
    def newsletter_sub(self):
        return self._search_sidebar_item("Newsletter Subscription")

    @property
    def my_invitations(self):
        return self._search_sidebar_item("My Invitations")
