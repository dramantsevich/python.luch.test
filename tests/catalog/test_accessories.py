from pytest import mark

ddt = {
    'argnames': 'sort_name',
    'argvalues': ['First popular'],
    'ids': ['test with sort - First popular']
}

accessories_product_type = {
    'argnames': 'product_type',
    'argvalues': ['A bracelet', 'Wallet'],
    'ids': ['test with A bracelet product type', 'test with Wallet product type']
}

accessories_color_type = {
    'argnames': 'product_color_type',
    'argvalues': ['Green', 'Marsal'],
    'ids': ['test with Green product color type', 'test with Marsal product color type']
}

class TestAccessories:
    @mark.parametrize(**ddt)
    def test_check_sort_first_popular(self, app, sort_name):
        app.goto(app.catalog_page.ACCESSORIES_URL)
        app.catalog_page.click_sort_button()
        app.catalog_page.click_sort_by_name(sort_name)

        assert len(app.catalog_accessories_page.get_list_products()) > 0, 'list products exist elements'

    @mark.parametrize(**accessories_product_type)
    def test_check_correct_accessories_product_type(self, app, product_type):
        app.goto(app.catalog_page.ACCESSORIES_URL)
        app.catalog_page.click_filter_by_name(product_type)
        app.catalog_page.click_more_info_of_product()

        expected = product_type
        actual = app.product_page.get_product_type()

        assert expected in actual, 'correct accessories product type'

    @mark.parametrize(**accessories_color_type)
    def test_check_correct_accessories_color(self, app, product_color_type):
        app.goto(app.catalog_page.ACCESSORIES_URL)
        app.catalog_page.click_filter_by_name(product_color_type)
        app.catalog_page.click_more_info_of_product()

        assert product_color_type in app.product_page.get_product_color_type(), 'correct product color type'