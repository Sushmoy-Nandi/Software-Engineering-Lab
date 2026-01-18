import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(100)
driver.quit()