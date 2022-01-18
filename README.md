#Project
Playwright automation with python

Tools:
- [Playwright](https://github.com/microsoft/playwright-python)
- [Pytest](https://docs.pytest.org/en/6.2.x/)
- [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/)

##Install Guide

1. Install python
2. Install PyCharm
3. Install python dependencies pip install -r requirements.txt
4. Make sure playwright version 1.8+ installed

##Project structure
- conftest.py file contains main fixtures to work
- Page objects stored in page_object folder
- Tests stored in tests folder
- Settings are spread between:
  - pytest.ini
  - settings.py

##Run guide
If you want to run tests in 3 browsers then fill in the parameters in fixture get_browser of the conftest.py file as follows:
```python
@fixture(scope='session', params=['chromium', 'firefox', 'webkit'], ids=['chromium', 'firefox', 'webkit'])
def get_browser(get_playwright, request):
```
If you need to run test only in one of this browsers - leave only one parameter
```python
@fixture(scope='session', params=['chromium'], ids=['chromium']):
def get_browser(get_playwright, request):
```
With mobile devices a similar approach:
```python
@fixture(scope='session', params=["iPhone 11", "Pixel 2"])
def mobile_app(get_playwright, get_browser, request):
```
##Important to know that firefox browser is not used for mobile


##Useful links
- [Documentation for python](https://github.com/microsoft/playwright-python)
- [Device descriptions](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json)
