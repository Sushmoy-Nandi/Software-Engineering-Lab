import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)
driver.get('https://www.google.com')
driver.find_element(By.NAME, value="q").send_keys('flower')
driver.find_element(By.NAME, value='btnK').submit()
time.sleep(100)
driver.close()