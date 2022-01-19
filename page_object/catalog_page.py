import re

from playwright.sync_api import Page

from model.product import Product
from service.product_creator import ProductCreator, product_from_catalog_page


class CatalogPage:
    ACCESSORIES_URL = "/en/accessories"

    def __init__(self, page: Page):
        self.page = page

    def click_sort_button(self):
        self.page.click("text=Sort")

    def click_sort_by_name(self, sort_name: str):
        with self.page.expect_navigation(wait_until='load'):
            self.page.click(f"text={sort_name}")

    def create_list_products(self):
        productsList = list()

        for element in self.page.query_selector_all(".item"):
            product = product_from_catalog_page()

            productsList.append(product)

        return productsList

    def set_product_name(self, product: Product, index: int):
        listName = self.page.query_selector_all("//a/div/div/div[@class='name']")
        tempIndex = 0

        for name in listName:
            if tempIndex == index:
                product.set_name(name.inner_text())
                break

            tempIndex += 1

        return product

    def set_product_price(self, product: Product, index: int):
        listPrice = self.page.query_selector_all("//a/div/div/div/div/div[@class='price']/span")
        tempIndex = 0
        productPrice: str

        for price in listPrice:
            if tempIndex == index:
                productPrice = price.inner_text().replace("\\s+", "")
                pattern = re.compile("[^mr][\\d]+")
                res = pattern.findall(productPrice)

                product.set_price(res[0])
                break

            tempIndex += 1

        return product

    def click_filter_by_name(self, filterName: str):
        with self.page.expect_navigation(wait_until='load'):
            self.page.click("label:has-text('" + filterName + "')")

    def click_more_info_of_product(self):
        self.page.click("text=More info")