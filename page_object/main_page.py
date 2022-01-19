from playwright.sync_api import Page

from model.user import User


class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def click_watches_to_one_click_order(self):
        self.page.click("//div[@class='owl-item active']//span[@class='oneclick-btn _big _js-b-pop-oneclick'][1]")

    def input_fields_in_one_click_order_popup(self, user: User):
        self.page.fill("input[name=\"form_text_38\"]", user.get_name())
        self.page.fill("input[name=\"form_text_39\"]", user.get_phone())
        self.page.fill("[placeholder=\"mail@domen.com\"]", user.get_email())

    def submit_form_one_click_order(self):
        self.page.click("text=Send form")

    def get_message_from_one_click_order_popup(self, message: str):
        return self.page.inner_text("//div[contains(text(),'" + message + "')]")

    def input_client_phone_field(self, user: User):
        self.page.fill("input[name=\"form_text_39\"]", user.get_phone())
