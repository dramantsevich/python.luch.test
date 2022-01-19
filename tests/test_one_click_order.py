from service.user_creator import user_for_one_click_order, user_for_one_click_order_without_name


class TestOneClickOrder:
    def test_correct_one_click_order(self, app):
        testUser = user_for_one_click_order()
        expectedMessage = "Your message was sent successfully"

        app.goto("/")
        app.main_page.click_watches_to_one_click_order()
        app.main_page.input_fields_in_one_click_order_popup(testUser)
        app.main_page.submit_form_one_click_order()

        assert app.main_page.get_message_from_one_click_order_popup(expectedMessage) is not None

    def test_check_error_message_if_name_is_empty(self, app):
        testUserWithoutName = user_for_one_click_order_without_name()

        app.goto("/")
        app.main_page.click_watches_to_one_click_order()
        app.main_page.input_client_phone_field(testUserWithoutName)
        app.main_page.submit_form_one_click_order()

