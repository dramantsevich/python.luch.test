from pytest import mark

ddt = {
    'argnames': 'sort_name',
    'argvalues': [('First popular')],
    'ids': ['test with sort - First popular']
}

class TestAccessories:
    @mark.parametrize(**ddt)
    def test_check_sort_first_popular(self, app, sort_name):
        app.goto(app.catalog_page.ACCESSORIES_URL)
        app.catalog_page.click_sort_button()
        app.catalog_page.click_sort_by_name(sort_name)
        # app.catalog_page.click_sort_by_name()
    # def setup(self):
    #     print('hello')

    # def test_sometest(self, desktop_app):
    #     desktop_app.cart_page.go_to_order_page()
    #     desktop_app.order_page.something()
    # def test_new_testcase(self, desktop_app):
    #     desktop_app
    #     # desktop_app.login()
    #     # desktop_app.create_test()
    #     # desktop_app.open_test()
    #     # assert desktop_app.check_test_created()
    #     # desktop_app.delete_test()

    # def teardown(self):
    #     print('world')