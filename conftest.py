from pytest import fixture
from playwright.sync_api import sync_playwright
from page_object.application import App
import settings

# @fixture(autouse=True, scope='session')
# def preconditions():
#     print('setup init state')
#
# @fixture(autouse=True, scope='session')
# def postconditions():
#     yield
#     print('setup postcondition state')

@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@fixture(scope='session')
def app(get_playwright, request):
    base_url = request.config.getini('base_url')
    app = App(get_playwright, base_url=base_url)
    # app.goto('/')
    yield app
    app.close()

@fixture(scope='session')
def mobile_app(get_playwright, request):
    base_url = request.config.getini('base_url')
    device = request.config.getoption('--device')
    app = App(get_playwright, base_url=base_url, device=device)
    # app.goto('/')
    yield app
    app.close()

# @fixture(scope='session')
# def desktop_app_auth(desktop_app):
#     app = desktop_app
#     app.goto('/login')
#     app.login('', '')
#     yield app
# **settings.USER #распаковка dictionary
def pytest_addoption(parser):
    parser.addoption('--device', action='store', default='')
    parser.addini('base_url', help='base url of site under test', default='https://luch.by/en')