import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)
driver.get('https://www.grameenphone.com/')
link = driver.find_elements(By.TAG_NAME, value="a")
division = driver.find_elements(By.TAG_NAME, value="div")
print(len(link))
print(len(division))
time.sleep(100)
driver.close()