import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element_by_class_name("search-keyword").send_keys("ber")

itemNames = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]

list = []
#items = driver.find_elements_by_xpath("//div[@class='products']/div/div/h4")
items = driver.find_elements_by_css_selector("h4.product-name")
for item in items:
    list.append(item.text)

#buttons = driver.find_elements_by_xpath("//div[@class='product']/div[3]/button")
#list = []
#for button in buttons:
    #list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)

print(list)
assert itemNames == list, "items do not match"



