# оформляем тесты из 1_6_10 в стиле unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

# создаем тестовый класс с двумя одинаковыми функциями проверки, с разницей - в ссылке. первая - правильная, вторая - нет
class TestAbs(unittest.TestCase):

    # функция с успешным тестом
    def test_link1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("test@test.com")

        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменные текст из элемента welcome_text_elt и ожидаемый текст соответственно
        welcome_text = welcome_text_elt.text
        excepted_text = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, excepted_text, 'No text!')

    # функция с неуспешным тестом
    def test_link2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        input3.send_keys("test@test.com")

        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменные текст из элемента welcome_text_elt и ожидаемый текст соответственно
        welcome_text = welcome_text_elt.text
        excepted_text = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, excepted_text, 'No text')

# конструкция запуска кода напрямую отсюда (не из внешних файлов)
if __name__ == "__main__":
    unittest.main()

# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
