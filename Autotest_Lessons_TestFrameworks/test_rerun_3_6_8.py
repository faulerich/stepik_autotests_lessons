
# Плагины и перезапуск тестов

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")

# здесь 2 теста: один заведомо проходит, второй - нет

# при запуске данных тестов командой
# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun_3_6_8.py
# упавший тест будет пепрезапущен, но при втором запуске очевидно тоже упадет
# ответ - 1 failed, 1 passed, 1 rerun