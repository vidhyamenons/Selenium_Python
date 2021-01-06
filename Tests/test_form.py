import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import homedata
from utilities.baseclass import BaseClass
from pageObjects.angularHome import mainpage


class TestAngular(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        log.info("Name is "+getData["firstname"])
        homepage = mainpage(self.driver)
        homepage.name().send_keys(getData["firstname"])
        homepage.email().send_keys(getData["secondname"])
        homepage.checkbox().click()
        self.selectoption(homepage.gender(), getData["gender"])
        homepage.submit().click()
        alertText = homepage.alert().text
        assert "Success" in alertText
        log.info("success")
        self.driver.refresh()

#USING TUPLE
   # @pytest.fixture(params=[("Rahul", "shetty", "Male"), ("Anshika", "shetty", "Female")])
    #def getData(self, request):
     #   return request.param
#USING DICTIONARY
    #@pytest.fixture(params=homedata.test_homepg_data)
    #def getData(self, request):
     #   return request.param
#USING EXCEL DATA
    @pytest.fixture(params=homedata.excelData("TestCase2"))
    def getData(self, request):
        return request.param
