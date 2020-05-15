import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.find_element_by_id("fromCity").click()
driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("del")
time.sleep(5)

cities = driver.find_elements_by_css_selector("p[class*='appendBottom5 blackText']")
print(len(cities))
for city in cities:
    print(city.text)
    if city.text == "Del Rio, United States":
        city.click()
        print("FOUND matching from city")
        break
driver.find_element_by_xpath("//p[text()='Delhi, India']").click()