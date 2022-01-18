import os

from pytest import fixture
from playwright.sync_api import sync_playwright
from page_object.application import App
import settings
import pytest


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
def app(get_browser, request):
    base_url = request.config.getini('base_url')
    app = App(get_browser, base_url=base_url, **settings.BROWSER_OPTIONS)
    yield app
    app.close()


@fixture(scope='session', params=['chromium'], ids=['chromium'])
def get_browser(get_playwright, request):
    browser = request.param
    os.environ['PWBROWSER'] = browser
    headless = request.config.getini("headless")
    if headless == "True":
        headless = True
    else:
        headless = False

    if browser == 'chromium':
        bro = get_playwright.chromium.launch(headless=headless)
    elif browser == 'firefox':
        bro = get_playwright.firefox.launch(headless=headless)
    elif browser == 'webkit':
        bro = get_playwright.webkit.launch(headless=headless)
    else:
        assert False, 'unsupported browser type'

    yield bro
    bro.close()
    del os.environ['PWBROWSER']


@fixture(scope='session', params=["iPhone 11", "Pixel 2"])
def mobile_app(get_playwright, get_browser, request):
    if os.environ.get('PWBROWSER') == 'firefox':
        pytest.skip()
    base_url = request.config.getini('base_url')
    device = request.param
    device_config = get_playwright.devices.get(device)
    if device_config is not None:
        device_config.update(settings.BROWSER_OPTIONS)
    else:
        device_config = settings.BROWSER_OPTIONS
    app = App(get_browser, base_url=base_url, **device_config)
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
    parser.addoption('--browser', action='store', default='chromium')
    parser.addini('base_url', help='base url of site under test', default='https://luch.by/en')
    parser.addini('headless', help='run browser in headless mode', default='False')
