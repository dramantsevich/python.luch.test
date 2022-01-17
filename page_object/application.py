from playwright.sync_api import Playwright
from .cart_page import CartPage
from page_object.catalog_page import CatalogPage
from .order_page import OrderPage

class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=False, device=None, **kwargs):
        device_config = playwright.devices.get(device)
        if device_config is not None:
            device_config.update(kwargs)
        else:
            device_config = kwargs
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context(**device_config)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.cart_page = CartPage(self.page)
        self.order_page = OrderPage(self.page)
        self.catalog_page = CatalogPage(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()