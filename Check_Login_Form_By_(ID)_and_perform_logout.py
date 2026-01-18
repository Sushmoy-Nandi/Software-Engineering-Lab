import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)
driver.get('https://practicetestautomation.com/practice-test-login/')
driver.find_element(By.ID,value='username').send_keys('student')
driver.find_element(By.ID,value='password').send_keys("Password123")
driver.find_element(By.ID, value='submit').click()
driver.find_element(By.LINK_TEXT, value='Log out').click()
time.sleep(100)
driver.close()