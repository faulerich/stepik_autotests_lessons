
# Работа с выпадающим списком

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

# расчет по формуле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значения
    x1_element = browser.find_element(By.ID, "num1")
    x1 = x1_element.text
    x2_element = browser.find_element(By.ID, "num2")
    x2 = x2_element.text

    # выполняем сложение
    y = int(x1) + int(x2)

    # находим выпадающий список со значениями
    my_dropdown = Select(browser.find_element(By.ID, "dropdown"))
    my_dropdown.select_by_value(str(y))  # ищем элемент с текстом, равным полученному значению


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()