from playwright.sync_api import Browser
from .cart_page import CartPage
from page_object.catalog.catalog_page import CatalogPage
from page_object.catalog.catalog_accessories_page import CatalogAccessoriesPage
from page_object.catalog.catalog_watches_page import CatalogWatchesPage
from .order_page import OrderPage
from .product_page import ProductPage


class App:
    def __init__(self, browser: Browser, base_url: str, **kwargs):
        self.browser = browser
        self.context = self.browser.new_context(**kwargs)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.cart_page = CartPage(self.page)
        self.order_page = OrderPage(self.page)
        self.catalog_page = CatalogPage(self.page)
        self.catalog_accessories_page = CatalogAccessoriesPage(self.page)
        self.product_page = ProductPage(self.page)
        self.catalog_watches_page = CatalogWatchesPage(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def close(self):
        self.page.close()
        self.context.close()