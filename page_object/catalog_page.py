from playwright.sync_api import Page

from model.product import Product
from service.product_creator import ProductCreator


class CatalogPage:
    ACCESSORIES_URL = "/en/accessories"

    def __init__(self, page: Page):
        self.page = page

    def click_sort_button(self):
        self.page.click("text=Sort")

    def click_sort_by_name(self, sort_name: str):
        self.page.click(f"text={sort_name}")

    # def get_list_products(self):
    #     products_list = self.create_list_products
    #     index = 0
    #
    #     for product in products_list:
    #
    #
    #
    # def create_list_products(self):
    #     products_list = []
    #
    #     for item in self.page.query_selector_all("//div[@class='item']"):
    #         product = ProductCreator.product_from_catalog_page()
    #
    #         products_list.append(product)
    #
    #     return products_list
    #
    # def set_product_name(self, product: Product, index: int):
    #     name = self.page.query_selector_all("//a/div/div/div[@class='name']").index(index)