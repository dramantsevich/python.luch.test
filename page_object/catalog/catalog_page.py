import re

from playwright.sync_api import Page

from model.product import Product
from service.product_creator import product_from_catalog_page


class LocatorsCatalogPage:
    SORT_BUTTON = "text=Sort"
    ITEM = ".item"
    PRODUCT_NAME = "//a/div/div/div[@class='name']"
    PRODUCT_ARTICLE = "//a/div/div/div[@class='article']"
    PRODUCT_PRICE = "//a/div/div/div/div/div[@class='price']/span"
    FILTER_BY_NAME = "label:has-text('{}')"
    MORE_INFO_BUTTON = "text=More info"


class CatalogPage:
    ACCESSORIES_URL = "/en/accessories"

    def __init__(self, page: Page):
        self.page = page

    def click_sort_button(self):
        self.page.click(LocatorsCatalogPage.SORT_BUTTON)

    def click_sort_by_name(self, sort_name: str):
        with self.page.expect_navigation(wait_until='load'):
            self.page.click(f"text={sort_name}")

    def create_list_products(self):
        productsList = list()

        for element in self.page.query_selector_all(LocatorsCatalogPage.ITEM):
            product = product_from_catalog_page()

            productsList.append(product)

        return productsList

    def set_product_name(self, product: Product, index: int):
        listName = self.page.query_selector_all(LocatorsCatalogPage.PRODUCT_NAME)
        tempIndex = 0

        for name in listName:
            if tempIndex == index:
                product.set_name(name.inner_text())
                break

            tempIndex += 1

        return product

    def set_product_article(self, product: Product, index: int):
        listArticle = self.page.query_selector_all(LocatorsCatalogPage.PRODUCT_ARTICLE)
        tempIndex = 0

        for article in listArticle:
            if tempIndex == index:
                product.set_article(int(article.inner_text()))
                break

            tempIndex += 1

        return product

    def set_product_price(self, product: Product, index: int):
        listPrice = self.page.query_selector_all(LocatorsCatalogPage.PRODUCT_PRICE)
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
            self.page.click(LocatorsCatalogPage.FILTER_BY_NAME.format(filterName))

    def click_more_info_of_product(self):
        self.page.click(LocatorsCatalogPage.MORE_INFO_BUTTON)
