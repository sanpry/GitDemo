from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("swetha gj")
driver.find_element_by_name("email").send_keys("sanpry@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("123")
driver.find_element_by_id("exampleCheck1").click()
dropDown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropDown.select_by_visible_text("Female")

radioButtons = driver.find_elements_by_xpath("//div[@class='form-check form-check-inline']")
for radioButton in radioButtons:
    if radioButton.text == "Employed":
        print(radioButton.text)
        radioButton.click()
driver.find_element_by_name("bday").send_keys("16-12-1990")
driver.find_element_by_xpath("//input[@type='submit']").click()
msg = driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text
print(msg)

assert "The Form has been submitted successfully!." in msg, "test failed"
driver.get_screenshot_as_file("finalscreen.png")

