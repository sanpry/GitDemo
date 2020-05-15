from selenium.webdriver.common.by import By

from pageobjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//ul[@class='navbar-nav']/li[2]")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    chkBox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    jobStatus = (By.XPATH, "//div[@class='form-check form-check-inline']")
    dob = (By.NAME, "bday")
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage
        #self.driver.find_element_by_xpath("//ul[@class='navbar-nav']/li[2]").click()


    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.email)


    def getPassword(self):
        return self.driver.find_element(*HomePage.password)


    def getChkBox(self):
        return self.driver.find_element(*HomePage.chkBox)


    def getGender(self):
        return self.driver.find_element(*HomePage.gender)


    def getJobStatus(self):
        return self.driver.find_elements(*HomePage.jobStatus)


    def getDob(self):
        return self.driver.find_element(*HomePage.dob)


    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)


    def getMsg(self):
        return self.driver.find_element(*HomePage.message)