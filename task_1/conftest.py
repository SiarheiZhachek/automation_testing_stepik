import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver_chrome = webdriver.Chrome()
    # driver.set_window_size(660, 880)
    driver_chrome.maximize_window()
    driver_chrome.implicitly_wait(10)
    yield driver_chrome
    driver_chrome.quit()
