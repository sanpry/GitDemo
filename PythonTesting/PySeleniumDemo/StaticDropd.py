

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_index(1)
#dropdown.select_by_value("F")
dropdown.select_by_visible_text("Female")
