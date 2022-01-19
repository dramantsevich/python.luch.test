from playwright.sync_api import Page


class SearchPage:
    SEARCH_URL = '/en/search'

    def __init__(self, page: Page):
        self.page = page

    def enter_search_input(self, string: str):
        self.page.type("text=Enter search query Go >> input[name='q']", string)
        self.page.click("input:has-text('Go')")

    def click_to_product(self):
        self.page.click("a.name")
