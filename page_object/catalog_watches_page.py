from playwright.sync_api import Page

from page_object.catalog_page import CatalogPage


class CatalogWatchesPage(CatalogPage):
    WATCHES_URL = "/en/watches"

    def __init__(self, page: Page):
        self.page = page

    def drop_type_filter(self):
        self.page.click("text=Type >> div")