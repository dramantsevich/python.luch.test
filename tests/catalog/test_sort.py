class TestSort:
    def test_check_sort_lowest_first(self, app):
        app.goto(app.catalog_watches_page.WATCHES_URL)
        app.catalog_watches_page.click_sort_button()
        app.catalog_watches_page.click_sort_by_name("Price: lowest first")

        assert len(app.catalog_watches_page.get_list_products()) > 0, 'sorting is not working properly'

    def test_chert_sort_highest_first(self, app):
        app.goto(app.catalog_watches_page.HIGHEST_FIRST_URL)

        assert len(app.catalog_watches_page.get_list_products()) > 0, 'sorting is not working properly'
