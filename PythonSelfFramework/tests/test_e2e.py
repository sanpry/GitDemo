import time

from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        # homePage.shopItems().click()
        # checkoutPage = CheckoutPage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("Getting all the card names")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            log.info(card.text)
            if card.text == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        checkoutpage.getChkOut().click()
        confirmPage = checkoutpage.getSuccess()
        #confirmPage = ConfirmPage(self.driver)
        confirmPage.getId()
        log.info("entering country name")
        self.verifyLinkPresence("India")
        confirmPage.getCountry().click()
        confirmPage.getCheckbox().click()
        time.sleep(2)
        confirmPage.getPurchase().click()
        print(confirmPage.getText().text)
        self.driver.get_screenshot_as_file("screen.png")