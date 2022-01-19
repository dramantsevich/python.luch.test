from model.user import User

NAME = "Dzmitrytest"
SURNAME = "Dzmitrytest"
PHONE = "123456789121"
EMAIL = "test@test.by"
CITY = "Minsk"


def user_for_one_click_order():
    return User(NAME, SURNAME, PHONE, EMAIL, CITY)


def user_for_one_click_order_without_name():
    return User("", "", PHONE, EMAIL, "")


class UserCreator:
    pass
