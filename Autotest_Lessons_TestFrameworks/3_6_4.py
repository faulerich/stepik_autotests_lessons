
# Задание: авторизация на сайте

# !!! для работы теста необходимо в текущей папке иметь файл config.json вида:
# login = load_config['login_stepik']
# password = load_config['password_stepik']

import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1?auth=login"

@pytest.fixture(scope="session")
def load_config():
    # Открываем файл с конфигом в режиме чтения
    with open('config.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLogin:
    def test_authorization(self, browser, load_config):
        login = load_config['login_stepik']
        password = load_config['password_stepik']
        # переходим по ссылке
        browser.get(link)
        # !!! заменить на нормальные ожидания
        time.sleep(5)
        # вводим логин и пароль
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='E-mail']")
        input1.send_keys(login)
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Пароль']")
        input2.send_keys(password)

time.sleep(5)