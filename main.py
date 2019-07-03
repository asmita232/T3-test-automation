import selenium
from selnium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")
print("called driver successfully")
