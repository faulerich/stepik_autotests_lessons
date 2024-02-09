
# ждем нужный текст на странице

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# расчет по формуле
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не станет равной 100$
button1 = browser.find_element(By.ID, "book")

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
button1.click()

# в открывшейся странице решаем уже известную задачу
# считываем значение x
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text

y = calc(x)

# вводим полученный ответ
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

# Отправляем заполненную форму
button2 = browser.find_element(By.ID, "solve")
# прокручиваем для обнаружения кнопки в зоне видимости
browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
button2.click()

time.sleep(5)