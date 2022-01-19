from pytest import mark

type_filters = {
    'argnames': 'filter_type_name',
    'argvalues': ['Unisex', 'Women'],
    'ids': ['test with Unisex type of product in filter', 'test with Women type of product in filter']
}

movement_filters = {
    'argnames': 'movement_type_name',
    'argvalues': ['Quartz', 'Mechanical'],
    'ids': ['test with Quartz movement type of product in filter', 'test with Mechanical movement type of product in filter']
}


class TestFilters:
    @mark.parametrize(**type_filters)
    def test_check_correct_type_filter(self, app, filter_type_name):
        app.goto(app.catalog_watches_page.WATCHES_URL)
        app.catalog_watches_page.drop_type_filter()
        app.catalog_page.click_filter_by_name(filter_type_name)
        app.catalog_page.click_more_info_of_product()

        assert filter_type_name in app.product_page.get_product_gender_type(), 'check correct type filter'

    @mark.parametrize(**movement_filters)
    def test_check_correct_movement_filter(self, app, movement_type_name):
        app.goto(app.catalog_watches_page.WATCHES_URL)
        app.catalog_page.click_filter_by_name(movement_type_name)
        app.catalog_page.click_more_info_of_product()

        assert movement_type_name in app.product_page.get_product_movement_type(), 'check correct movement type filter'


