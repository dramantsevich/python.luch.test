from playwright.sync_api import Page

from page_object.catalog_page import CatalogPage


class CatalogAccessoriesPage(CatalogPage):

    def __init__(self, page: Page):
        self.page = page

    def get_list_products(self):
        productList = self.create_list_products()
        index = 0

        for product in productList:
            self.set_product_name(product, index)
            self.set_product_price(product, index)

            index += 1

        return productList

