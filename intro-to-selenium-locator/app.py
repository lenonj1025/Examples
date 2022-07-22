from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# Instantiate a webdriver object
driver = webdriver.Chrome('./chromedriver.exe')

# .get(url) method is how you tell the browser to go to a particular URL
driver.get("http://127.0.0.1:5500/selenium-locator-practice.html")


# ======= class locator ============
# find_element: first occurrence of element
p1 = driver.find_element(By.CLASS_NAME, "someclass")
print(p1.text)  # First paragraph element

# find_elements: collection
list_of_elements_with_class_someclass = driver.find_elements(By.CLASS_NAME, "someclass")
p2 = list_of_elements_with_class_someclass[1]
print(p2.text)  # Second paragraph element

# ======== id locator ============
p3 = driver.find_element(By.ID, "third")
print(p3.text)

# ======== name locator ==========
input_element = driver.find_element(By.NAME, "somename")
input_element.send_keys("hello world")

# ========== XPath locator ===========
variable_1 = driver.find_element(By.XPATH, "//div[@id='someid']/div[2]/p[1]")
print(variable_1.text)

# ======== link text locator =========
about_me_link = driver.find_element(By.LINK_TEXT, "About Me")   # Requires full link text
print(about_me_link.text)
# ======== partial link text locator ===========
about_me_link = driver.find_element(By.PARTIAL_LINK_TEXT, "About")  # Only requires a partial match
print(about_me_link.text)
about_me_link.click()

# sleep for five seconds
time.sleep(5)

# Close the driver and the browser
driver.quit()
