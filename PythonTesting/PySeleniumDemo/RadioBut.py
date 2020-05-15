import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

rbuttons = driver.find_elements_by_xpath("//input[@type='radio']")
rbuttons[2].click()
for rbutton in rbuttons:
    rbutton.click()
    assert rbutton.is_selected()
    time.sleep(2)

print(driver.find_element_by_css_selector("#displayed-text").is_displayed())
driver.find_element_by_css_selector("#hide-textbox").click()
print(driver.find_element_by_css_selector("#displayed-text").is_displayed())