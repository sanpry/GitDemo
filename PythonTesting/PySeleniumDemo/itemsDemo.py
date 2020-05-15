import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
buttons = driver.find_elements_by_xpath("//div[@class='product']/div[3]/button")
list = []
for button in buttons:
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

print(list)
#items = driver.find_elements_by_xpath("//h4[@class='product-name']")
#itemName = []
#for item in items:
    #itemName.append(item.text)

#print(itemName)

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

items = driver.find_elements_by_xpath("//table/tr/td[2]/p")
list2 = []
for item in items:
    list2.append(item.text)

print(list2)

assert list == list2


