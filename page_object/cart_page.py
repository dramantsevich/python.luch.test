from playwright.sync_api import Page

from model.product import Product


class LocatorsCartPage:
    GO_TO_ORDER_PAGE_BUTTON = "//a[@class='logo-desktop']"
    PRODUCT_INT_CART_BY_URL = "//h2[@class='bx_ordercart_itemtitle']/a[@href='{}']"
    LIST_PRODUCTS = "/table[@id='basket_items']/tbody/tr"


class CartPage:
    CART_URL = "/en/cart"

    def __init__(self, page: Page):
        self.page = page

    def go_to_order_page(self):
        self.page.click(LocatorsCartPage.GO_TO_ORDER_PAGE_BUTTON)

    def get_product_in_cart_by_url(self, product: Product):
        return self.page.query_selector(LocatorsCartPage.PRODUCT_INT_CART_BY_URL.format(product))

    def get_list_products(self):
        return self.page.query_selector(LocatorsCartPage.LIST_PRODUCTS)
