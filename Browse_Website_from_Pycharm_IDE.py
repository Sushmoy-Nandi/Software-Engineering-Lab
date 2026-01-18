import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)
driver.get('https://www.grameenphone.com/')
print(driver.title)
driver.maximize_window()
time.sleep(100)
driver.quit()
