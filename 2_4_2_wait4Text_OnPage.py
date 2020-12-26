# -*- coding: windows-1251 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # ������� Selenium ��������� � ������� 12 ������, ���� ����� �� ������ ������ 100
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element_by_css_selector("#book")
    button.click()

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)

    browser.find_element_by_css_selector("#answer").send_keys(y)

    # ���������� ����������� �����
    button = browser.find_element_by_css_selector("#solve")
    button.click()

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()