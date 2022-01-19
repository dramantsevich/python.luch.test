from pytest import mark

search = {
    'argnames': 'article',
    'argvalues': ['77431556', '272081648']
}

class TestSearchPage:
    @mark.parametrize(**search)
    def test_check_correct_search(self, app, article):
        app.goto(app.search_page.SEARCH_URL)
        app.search_page.enter_search_input(article)
        app.search_page.click_to_product()

        assert article in app.product_page.get_current_url()
