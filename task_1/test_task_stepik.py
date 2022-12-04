import os
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def calc(x_num):
    return str(math.log(abs(12*math.sin(int(x_num)))))


def test_stepik_one(driver):
    driver.get('http://suninjuly.github.io/registration2.html')
    driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Input your first name"]'
    ).send_keys('Vasia')
    driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Input your last name"]'
    ).send_keys('Pupkin')
    driver.find_element(
        By.CSS_SELECTOR, '.form-control.third'
    ).send_keys('hrenov@email.com')
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    text_site = driver.find_element(By.CSS_SELECTOR, '.container h1')
    assert text_site.text == 'Congratulations! You have successfully registered!'


def test_stepik_two(driver):
    driver.get('http://suninjuly.github.io/registration1.html')
    driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Input your first name"]'
    ).send_keys('Vasia')
    driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Input your last name"]'
    ).send_keys('Pupkin')
    driver.find_element(
        By.CSS_SELECTOR, '.form-control.third'
    ).send_keys('hrenov@email.com')
    driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Input your phone:"]'
    ).send_keys('+9874587554554')
    driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Input your address:"]'
    ).send_keys('Muhosranskay 8')
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    text_site = driver.find_element(By.CSS_SELECTOR, '.container h1')
    assert text_site.text == 'Congratulations! You have successfully registered!'


def test_stepik_three(driver):
    driver.get('http://suninjuly.github.io/registration2.html')
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input:required')
    for i in inputs:
        i.send_keys('Hello')
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
    text_site = driver.find_element(By.CSS_SELECTOR, '.container h1')
    assert text_site.text == 'Congratulations! You have successfully registered!'


def test_3(driver):
    driver.get('http://suninjuly.github.io/registration2.html')
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input')
    label = driver.find_elements(By.TAG_NAME, 'label')
    for i, labe in enumerate(label):
        if labe.text[-1] == '*':
            inputs[i].send_keys('cfr')


def test_stepik_4(driver):
    driver.get('https://suninjuly.github.io/math.html')
    x_element = driver.find_element(By.ID, 'input_value')
    x_num = x_element.text
    y_num = calc(x_num)
    enter_field = driver.find_element(By.ID, 'answer')
    enter_field.send_keys(y_num)
    checkbox = driver.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()
    robots_rule = driver.find_element(By.ID, 'robotsRule')
    robots_rule.click()
    submit_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit_button.click()
    print()
    print(Alert(driver).text)
    Alert(driver).accept()


def test_stepik_5(driver):
    driver.get('https://suninjuly.github.io/math.html')
    people_radio = driver.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"


def test_stepik_6(driver):
    driver.get('https://suninjuly.github.io/math.html')
    robots_radio = driver.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None


def test_stepik_7(driver):
    driver.get('http://suninjuly.github.io/get_attribute.html')
    x_element = driver.find_element(By.CSS_SELECTOR, '#treasure')
    x_num = x_element.get_attribute('valuex')
    y_num = calc(x_num)
    enter_field = driver.find_element(By.ID, 'answer')
    enter_field.send_keys(y_num)
    checkbox = driver.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()
    robots_rule = driver.find_element(By.ID, 'robotsRule')
    robots_rule.click()
    submit_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit_button.click()
    print()
    print(Alert(driver).text)
    Alert(driver).accept()


def test_stepik_8(driver):
    driver.get('http://suninjuly.github.io/selects1.html')
    num_one = driver.find_element(By.ID, 'num1')
    num_two = driver.find_element(By.ID, 'num2')
    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(int(num_one.text) + int(num_two.text)))
    submit_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit_button.click()
    print()
    print(Alert(driver).text)
    Alert(driver).accept()


def test_stepik_9(driver):
    driver.get('http://suninjuly.github.io/execute_script.html')
    x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')
    x_num = x_element.text
    y_num = calc(x_num)
    enter_field = driver.find_element(By.ID, 'answer')
    enter_field.send_keys(y_num)
    checkbox = driver.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    checkbox.click()
    driver.execute_script("window.scrollBy(0, 300);")
    robots_rule = driver.find_element(By.ID, 'robotsRule')
    robots_rule.click()
    submit_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit_button.click()
    print()
    print(Alert(driver).text)
    Alert(driver).accept()


def test_stepik_10(driver):
    driver.get('http://suninjuly.github.io/file_input.html')
    driver.find_element(By.NAME, 'firstname').send_keys('Vasia')
    driver.find_element(By.NAME, 'lastname').send_keys('Pypkin')
    driver.find_element(By.NAME, 'email').send_keys('petuh@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    driver.find_element(By.ID, 'file').send_keys(file_path)
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    print()
    print(Alert(driver).text)
    Alert(driver).accept()


def test_stepik_11(driver):
    driver.get('http://suninjuly.github.io/alert_accept.html')
    driver.find_element(By.CSS_SELECTOR, '.container .btn.btn-primary').click()
    Alert(driver).accept()
    x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')
    x_num = x_element.text
    y_num = calc(x_num)
    driver.find_element(By.ID, 'answer').send_keys(y_num)
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    print()
    print(Alert(driver).text)
    Alert(driver).accept()


def test_stepik_12(driver):
    driver.get('http://suninjuly.github.io/redirect_accept.html')
    driver.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary').click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')
    x_num = x_element.text
    y_num = calc(x_num)
    driver.find_element(By.ID, 'answer').send_keys(y_num)
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    print()
    print(Alert(driver).text)
    Alert(driver).accept()


def test_stepik_13(driver):
    driver.get('http://suninjuly.github.io/wait1.html')
    driver.find_element(By.ID, 'verify').click()
    verification_massage = driver.find_element(By.ID, 'verify_message')
    assert verification_massage.text == 'Verification was successful!'


def test_stepik_14(driver):
    driver.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(driver, 10).until(
        ec.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#price'), '100')
    )
    button = driver.find_element(By.ID, 'book')
    button.click()
    x_element = driver.find_element(By.CSS_SELECTOR, '#input_value')
    x_num = x_element.text
    y_num = calc(x_num)
    driver.find_element(By.ID, 'answer').send_keys(y_num)
    driver.find_element(By.ID, 'solve').click()
    print()
    print(Alert(driver).text)
    Alert(driver).accept()
