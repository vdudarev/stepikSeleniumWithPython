# -*- coding: windows-1251 -*-
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    browser.find_element_by_css_selector("#answer").send_keys(y)

    # ���������� ����������� �����
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()