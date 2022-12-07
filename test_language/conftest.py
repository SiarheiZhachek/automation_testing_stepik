import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_chrome
from selenium.webdriver.firefox.options import Options as Options_ff


@pytest.fixture(scope='function')
def driver(browser_options, language_options):
    if browser_options == 'ff' and language_options == 'en':
        with allure.step('Rune Firefox and language English'):
            options = Options_ff()
            options.set_preference("intl.accept_languages", language_options)
            driver_browser = webdriver.Firefox(options=options)
    elif browser_options == 'ff':
        with allure.step('Rune Firefox'):
            driver_browser = webdriver.Firefox()
    elif language_options == 'en':
        with allure.step('Rune Chrome with English'):
            options = Options_chrome()
            options.add_experimental_option('prefs', {'intl.accept_languages': language_options})
            driver_browser = webdriver.Chrome(options=options)
    else:
        with allure.step('Rune Chrome'):
            driver_browser = webdriver.Chrome()
    # driver_browser.set_window_size(660, 880)
    driver_browser.maximize_window()
    driver_browser.implicitly_wait(10)
    yield driver_browser
    driver_browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Укажите значение браузера, поумолчанию Chrome'
    )
    parser.addoption(
        '--language',
        action='store',
        default='rus',
        help='Укажите язык по умолчанию, Русский'
    )


@pytest.fixture(scope='session')
def browser_options(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def language_options(request):
    return request.config.getoption('--language')

