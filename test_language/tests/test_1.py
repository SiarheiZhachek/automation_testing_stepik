from selenium.webdriver.common.by import By


def test_add_to_cart_button(driver):
    driver.get(
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    )
    add_to_cart_button = driver.find_element(
        By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket'
    )
    british = driver.find_element(By.CSS_SELECTOR, 'select [value="en-gb"]')
    russian = driver.find_element(By.CSS_SELECTOR, 'select [value="ru"]')
    if british.is_selected():
        assert british.is_selected()
        assert add_to_cart_button.is_displayed()
        assert add_to_cart_button.text == 'Add to basket'
    else:
        assert russian.is_selected()
        assert add_to_cart_button.is_displayed()
        assert add_to_cart_button.text == 'Добавить в корзину'
