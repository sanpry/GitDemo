from selenium.webdriver.common.by import By
from pageobjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    chkOut = (By.CSS_SELECTOR, ".btn-primary")
    success = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getChkOut(self):
        return self.driver.find_element(*CheckoutPage.chkOut)

    def getSuccess(self):
        self.driver.find_element(*CheckoutPage.success).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
