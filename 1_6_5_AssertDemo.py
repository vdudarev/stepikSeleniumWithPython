# -*- coding: windows-1251 -*-
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # ��� ���, ������� ��������� ������������ ����
    browser.find_element_by_css_selector(".first").send_keys("name")
    browser.find_element_by_css_selector(".second").send_keys("surname")
    browser.find_element_by_css_selector(".third").send_keys("email")

    # ���������� ����������� �����
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ���������, ��� ������ ������������������
    # ���� �������� ��������
    time.sleep(1)

    # ������� �������, ���������� �����
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # ���������� � ���������� welcome_text ����� �� �������� welcome_text_elt
    welcome_text = welcome_text_elt.text

    # � ������� assert ���������, ��� ��������� ����� ��������� � ������� �� �������� �����
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # �������� ����� ��������� ������� ���������� ����������� �������
    time.sleep(10)
    # ��������� ������� ����� ���� �����������
    browser.quit()