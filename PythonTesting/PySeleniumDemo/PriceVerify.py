import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()


driver.find_element_by_css_selector(".search-keyword").send_keys("ber")

time.sleep(2)
buttons = driver.find_elements_by_xpath("//div[@class='product']/div[3]/button")
for button in buttons:
    button.click()

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoCode')))

orignalAmount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoInfo')))
discountAmount = driver.find_element_by_css_selector(".discountAmt").text

assert float(discountAmount) < int(orignalAmount)

print("*******************************NEXT TEST CASE*************************************")

sum = 0
prices = driver.find_elements_by_xpath("//table/tr/td[5]/p")
for price in prices:
    sum = sum + int(price.text)

print(sum)

amt = driver.find_element_by_class_name("totAmt").text
totalamt = int(amt)

assert totalamt == sum, "Total amount is NOT the same as sum of item price"