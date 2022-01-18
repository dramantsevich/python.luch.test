from playwright.sync_api import Page


class ProductPage:

    def __init__(self, page: Page):
        self.page = page

    def get_product_type(self):
        return self.page.inner_text("//div[@class='prop-title' and contains(text(),'Product type')]/following-sibling::div[@class='prop-value']/a")

    def get_product_color_type(self):
        return self.page.inner_text("//div[@class='prop-title' and contains(text(),'Colour')]/following-sibling::div[@class='prop-value']/a")