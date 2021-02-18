from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

browser = webdriver.Chrome(r"C:\Users\Work\AppData\Local\Programs\Python\Python38\chromedriver.exe")
browser.maximize_window()

browser.get('https://web.whatsapp.com/')

with open('ChatName.txt', 'r', encoding='utf8') as f:
    ChatName = [name.strip() for name in f.readlines()]

with open('msg.txt', 'r', encoding='utf8') as f:
    msg = f.read()

for name in ChatName:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'

    search_box = WebDriverWait(browser,500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )

    search_box.clear()
    time.sleep(1)

    pyperclip.copy(name)

    search_box.send_keys(Keys.CONTROL + "v")
    time.sleep(2)

    name_xpath = f'//span[@title="{Myself}"]'
    name_title = browser.find_element_by_xpath(name_xpath)

    name_title.click()
    time.sleep(1)

    input_xpath = '//div[@contenteditable="true"][@data-tab="1"][@dir="ltr"]'
    input_box = browser.find_element_by_xpath(input_xpath)

    pyperclip.copy(msg)
    input_box.send_keys(Keys.CONTROL + "v")
    input_box.send_keys(Keys.ENTER)

    time.sleep(2)
    