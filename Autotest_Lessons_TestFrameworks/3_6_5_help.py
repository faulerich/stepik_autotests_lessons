
# считывание текста сообщения об ошибке (Correct или Incorrect)

import json
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# расчет по формуле
def calc():
  return str(math.log(int(time.time())))

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
        # ожидание страницы 5 сек
        browser.implicitly_wait(5)
        # переходим по ссылке
        link = f"https://stepik.org/lesson/236895/step/1?auth=login"
        browser.get(link)
        # вводим логин и пароль
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='E-mail']")
        input1.send_keys(login)
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Пароль']")
        input2.send_keys(password)
        # Отправляем заполненную форму авторизации
        button = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader ")
        button.click()
        time.sleep(5)
        # вводим полученный ответ, очищая перед этим поле
        input1 = browser.find_element(By.XPATH, "//textarea[@placeholder='Напишите ваш ответ здесь...']")
        #input1.clear()

        y = calc()
        #input1.send_keys(y)
        time.sleep(5)

        # Отправляем заполненную форму с подсчитанным ответом
        #button = browser.find_element(By.CLASS_NAME, "submit-submission")
        #button.click()
        time.sleep(3)

        # проверяем, есть ли на странице текст "Correct!"
        #msgText = browser.find_element(By.XPATH, "//p[@class='smart-hints__hint']/text()").text
        msgText = browser.find_element(By.XPATH, "//div[@id='ember470']/p").text
        print (msgText)
        excepted_text = "Correct!"
        # assert excepted_text in msgText.text