# -*- coding: windows-1251 -*-
from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# ���, ������� ��������� ������������ ����

# ���������� ���� "���"
nameInput = browser.find_element_by_css_selector(".first_class [placeholder='������� ���']")
nameInput.send_keys("�����")

# ���������� ���� "�������"
lastnameInput = browser.find_element_by_css_selector(".second_class [placeholder='������� �������']")
lastnameInput.send_keys("�������")

# ���������� ���� "Email"
emailInput = browser.find_element_by_css_selector(".third_class [placeholder='������� Email']")
emailInput.send_keys("maria@testmail.com")

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
assert "�����������! �� ������� �����������������!" == welcome_text
#browser.close()