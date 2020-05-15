import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 7).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectDropdown(self, locator, text):
        dropDown = Select(locator)
        dropDown.select_by_visible_text(text)

    def getLogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        fileHandler = logging.FileHandler('logfile.log')
        logger.addHandler(fileHandler)

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        return logger
