import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad): #using fixture name even in method to return values
        log = self.getLogger()
        log.info(dataLoad)
        log.info(dataLoad[0])
        log.info(dataLoad[2])
        #print(dataLoad)
        #print(dataLoad[0])
        #print(dataLoad[2])