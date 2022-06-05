import time
from selenium import webdriver

driver = webdriver.Chrome("/home/ubuntu/chromedriver.exe")
driver.get ("http://wikipedia.org")
print(driver.title)
time.sleep(8)
driver.quit()
