from playwright.sync_api import Page


class LocatorsProductPage:
    PRODUCT_TYPE = "//div[@class='prop-title' and contains(text(),'Product type')]/following-sibling::div[@class='prop-value']/a"
    PRODUCT_COLOR = "//div[@class='prop-title' and contains(text(),'Colour')]/following-sibling::div[@class='prop-value']/a"
    PRODUCT_GENDER = "//div[@class='prop-title' and contains(text(),'Type')]/following-sibling::div[@class='prop-value']/a"
    PRODUCT_MOVEMENT = "//div[@class='prop-title' and contains(text(),'Movement')]/following-sibling::div[@class='prop-value']/a"


class ProductPage:

    def __init__(self, page: Page):
        self.page = page

    def get_current_url(self):
        return self.page.url

    def get_product_type(self):
        return self.page.inner_text(LocatorsProductPage.PRODUCT_TYPE)

    def get_product_color_type(self):
        return self.page.inner_text(LocatorsProductPage.PRODUCT_COLOR)

    def get_product_gender_type(self):
        return self.page.inner_text(LocatorsProductPage.PRODUCT_GENDER)

    def get_product_movement_type(self):
        return self.page.inner_text(LocatorsProductPage.PRODUCT_MOVEMENT)
