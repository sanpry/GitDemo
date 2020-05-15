from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.familysearch.org/en/")
driver.maximize_window()
driver.find_element_by_xpath("//button[@aria-owns='search']").click()
#action = ActionChains(driver)
#action.move_to_element(driver.find_element_by_xpath("//button[@aria-owns='search']")).click().perform()
#wait = WebDriverWait(driver, 5)
#wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Genealogies")))
#action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()
driver.find_element_by_link_text("Genealogies").click()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()
action.double_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()