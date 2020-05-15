import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element_by_id("name").send_keys("Option3")
validatetext = "Option3"

driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to_alert()
time.sleep(2)
alerttext = alert.text
print(alerttext)
assert validatetext in alerttext
alert.accept()