from playwright.sync_api import Page


class LocatorsSearchPage:
    SEARCH_INPUT = "text=Enter search query Go >> input[name='q']"
    SEARCH_INPUT_BUTTON = "input:has-text('Go')"
    PRODUCT_BUTTON = "a.name"


class SearchPage:
    SEARCH_URL = '/en/search'

    def __init__(self, page: Page):
        self.page = page

    def enter_search_input(self, string: str):
        self.page.type(LocatorsSearchPage.SEARCH_INPUT, string)
        self.page.click(LocatorsSearchPage.SEARCH_INPUT_BUTTON)

    def click_to_product(self):
        self.page.click(LocatorsSearchPage.PRODUCT_BUTTON)
