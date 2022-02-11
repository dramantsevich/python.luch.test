from playwright.sync_api import Page

from model.user import User


class LocatorsMainPage:
    ONE_CLICK_ORDER_BUTTON = "//div[@class='owl-item active']//span[@class='oneclick-btn _big _js-b-pop-oneclick'][1]"
    USER_NAME_INPUT = "input[name='form_text_38']"
    USER_PHONE_INPUT = "input[name='form_text_39']"
    USER_EMAIL_INPUT = "[placeholder='mail@domen.com']"
    SUBMIT_FORM = "text=Send form"
    POPUP_MESSAGE = "//div[contains(text(),'{}')]"


class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def click_watches_to_one_click_order(self):
        self.page.click(LocatorsMainPage.ONE_CLICK_ORDER_BUTTON)

    def input_fields_in_one_click_order_popup(self, user: User):
        self.page.fill(LocatorsMainPage.USER_NAME_INPUT, user.get_name())
        self.page.fill(LocatorsMainPage.USER_PHONE_INPUT, user.get_phone())
        self.page.fill(LocatorsMainPage.USER_EMAIL_INPUT, user.get_email())

    def submit_form_one_click_order(self):
        self.page.click(LocatorsMainPage.SUBMIT_FORM)

    def get_message_from_one_click_order_popup(self, message: str):
        return self.page.inner_text(LocatorsMainPage.POPUP_MESSAGE.format(message))

    def input_client_phone_field(self, user: User):
        self.page.fill(LocatorsMainPage.USER_PHONE_INPUT, user.get_phone())
