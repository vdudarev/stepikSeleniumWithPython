# -*- coding: windows-1251 -*-
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("input[name='firstname']").send_keys("name")
    browser.find_element_by_css_selector("input[name='lastname']").send_keys("surname")
    browser.find_element_by_css_selector("input[name='email']").send_keys("email")

    import os

    current_dir = os.path.abspath(os.path.dirname(__file__))  # �������� ���� � ���������� �������� ������������ �����
    file_path = os.path.join(current_dir, 'file.txt')  # ��������� � ����� ���� ��� �����
    browser.find_element_by_css_selector("#file").send_keys(file_path)

    # ���������� ����������� �����
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()