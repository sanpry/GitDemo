import time
from _ast import arguments

import document
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe",options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").get_attribute("value"))

print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)

time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")