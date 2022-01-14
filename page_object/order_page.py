from playwright.sync_api import Page


class OrderPage:
    def __init__(self, page: Page):
        self.page = page

    def something(self):
        self.page.click("//a[@class='logo-desktop']")
        print('sometihn')


