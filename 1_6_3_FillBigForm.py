# -*- coding: windows-1251 -*-
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("input")
    for element in elements:
       element.send_keys("��� �����")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # �������� ����������� ��� �� 30 ������
    time.sleep(30)
    # ��������� ������� ����� ���� �����������
    browser.quit()

# �� �������� �������� ������ ������ � ����� �����