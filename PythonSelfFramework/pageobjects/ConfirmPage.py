from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    id = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    text = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getId(self):
        return self.driver.find_element(*ConfirmPage.id).send_keys("Ind")

    def getCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getText(self):
        return self.driver.find_element(*ConfirmPage.text)