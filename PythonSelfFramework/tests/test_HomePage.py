import pytest

from TestData.HomePageData import HomePageData
from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["name"]) #keyname
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys(getData["pwd"])
        homepage.getChkBox().click()
        self.selectDropdown(homepage.getGender(), getData["gender"])
        radioButtons = homepage.getJobStatus()
        for radioButton in radioButtons:
            # print(radioButton.text)
            if radioButton.text == getData["status"]:
                radioButton.click()
        homepage.getDob().send_keys(getData["dob"])
        homepage.getSubmit().click()
        msg = homepage.getMsg().text
        print(msg)

        assert "The Form has been submitted successfully!." in msg, "test failed"
        self.driver.get_screenshot_as_file("finalscreen.png")
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    def getData(self, request):
        return request.param
