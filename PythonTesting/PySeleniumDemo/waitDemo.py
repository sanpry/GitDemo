import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
#driver.implicitly_wait(5)

driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
#driver.find_element_by_xpath("//button[@type='submit']").click()


time.sleep(2)
driver.find_element_by_xpath("//button[text()='ADD TO CART']").click()

items = driver.find_elements_by_xpath("//div[@class='product']/div/button")
for item in items:
    item.click()

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoCode')))
#time.sleep(5)
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))
#time.sleep(5)
promoMsg = driver.find_element_by_css_selector(".promoInfo").text
assert promoMsg=="Code applied ..!"
print(promoMsg)
