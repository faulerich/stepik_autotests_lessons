
# Задание на execute_script

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# расчет по формуле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    y = calc(x)

    # вводим полученный ответ
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # скроллим страницу вниз
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # сообщаем и доказываем, что мы - робот
    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()
    option2 = browser.find_element(By.ID, "robotCheckbox")
    option2.click()

    # Отправляем заполненную форму
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()