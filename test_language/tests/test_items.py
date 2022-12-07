from selenium.webdriver.common.by import By


def test_add_to_cart_button(driver, language_options):
    driver.get(
        f'http://selenium1py.pythonanywhere.com/{language_options}/catalogue/coders-at-work_207/'
    )
    add_to_cart_button = driver.find_element(
        By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket'
    )
    assert add_to_cart_button.is_displayed()
