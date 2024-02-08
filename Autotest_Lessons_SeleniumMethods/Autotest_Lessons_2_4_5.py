import time

# Как работают методы get и find_element

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
# без паузы тест упадет, т.к. find_element начнет отрабатывать раньше, чем get "отчитается" о своем выполнении
# time.sleep(1)
# но, если, например, интернет медленный и секунды по какой-то еще причине не хватит, чтобы get "отчитался" об открытии страницы,
# то можем воспользоваться Selenium Waits (Implicit Waits)

# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text