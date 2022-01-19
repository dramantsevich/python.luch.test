from playwright.sync_api import Page

from page_object.catalog.catalog_page import CatalogPage


class CatalogWatchesPage(CatalogPage):
    WATCHES_URL = "/en/watches"
    HIGHEST_FIRST_URL = "/watches/?sort=PRICE&order=asc"

    def __init__(self, page: Page):
        self.page = page

    def drop_type_filter(self):
        self.page.click("text=Type >> div")

    def get_list_products(self):
        productList = self.create_list_products()
        index = 0

        for product in productList:
            self.set_product_name(product, index)
            self.set_product_article(product, index)
            self.set_product_price(product, index)

            index += 1

        return productList