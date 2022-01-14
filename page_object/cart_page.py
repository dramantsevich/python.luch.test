from playwright.sync_api import Page

from model.product import Product


class CartPage:
    CART_URL = "/en/cart"

    def __init__(self, page: Page):
        self.page = page

    def go_to_order_page(self):
        self.page.click("//a[@class='logo-desktop']")

    def get_product_in_cart_by_url(self, product: Product):
        return self.page.query_selector(f"//h2[@class='bx_ordercart_itemtitle']/a[@href='\"{product}\"']")

    def get_list_products(self):
        return self.page.query_selector("/table[@id='basket_items']/tbody/tr")
