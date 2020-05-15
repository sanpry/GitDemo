import time

import console as console
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_xpath("//ul[@class='navbar-nav']/li[2]").click()  #shop button

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

items = driver.find_elements_by_xpath("//app-card[@class='col-lg-3 col-md-6 mb-3']/div")
for item in items:
    itemName = item.find_element_by_xpath("div/h4/a").text   #child xpath
    if itemName == "Blackberry":
        item.find_element_by_xpath("div[2]/button/i").click() #child xpath

driver.find_element_by_class_name("btn-primary").click()
time.sleep(2)
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element_by_link_text("India").click()

driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@value='Purchase']").click()

print(driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)

driver.get_screenshot_as_file("screen.png")