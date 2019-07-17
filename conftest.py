import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: Chrome or firefox")
    parser.addoption('--language', action='store', default='en', help='Choose UI language to test')

@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        #Выключаем режим w3c, падают тесты с textarea
        options.add_experimental_option('w3c', False)
        #Передаем язык
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        print('Browser {} still is not implemented'.format(browser_name))
    yield browser
    browser.quit()