from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver.exe')

driver.get("http://127.0.0.1:5500/employee-overview.html")

p1 = driver.find_elements(By.XPATH, "//*[contains(text(), '$')")
print(p1.text)

time.sleep(5)

driver.quit()
