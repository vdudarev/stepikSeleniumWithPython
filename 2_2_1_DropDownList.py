# -*- coding: windows-1251 -*-
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_css_selector("#num1").text)
    x2 = int(browser.find_element_by_css_selector("#num2").text)
    y = x + x2

    #el = browser.find_element_by_css_selector("option[value='" + y + "']")
    #el.click()
    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_value(str(y))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()