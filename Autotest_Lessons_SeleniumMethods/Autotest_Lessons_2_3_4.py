
# принимаем alert

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# расчет по формуле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # нажимаем кнопку вызова alert'а
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # соглашаемся с confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # в открывшейся странице решаем уже известную задачу
    # считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    y = calc(x)

    # вводим полученный ответ
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()