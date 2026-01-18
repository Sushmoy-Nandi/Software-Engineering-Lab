import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)
driver.get('https://www.grameenphone.com/')
c = driver.find_elements(By.CLASS_NAME,value='swiper-slide')
print(len(c))
time.sleep(100)
driver.close()