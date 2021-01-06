import time

import pytest
from selenium import webdriver

from utilities.baseclass import BaseClass

@pytest.mark.usefixtures("setup")
class TestBasic():
    def test_basic(self, getData):
        self.driver.find_element_by_id("email-input").send_keys("login@codility.com")
        self.driver.find_element_by_id("password-input").send_keys("password")
        self.driver.find_element_by_id("login-button").click()
        time.sleep(2)
        message1 = self.driver.find_element_by_css_selector("#container > div").text
        assert "Welcome" in message1
        self.driver.refresh()
        self.driver.find_element_by_id("email-input").send_keys(getData[0])
        self.driver.find_element_by_id("password-input").send_keys(getData[1])
        time.sleep(2)
        self.driver.find_element_by_id("login-button").click()
        message2 = self.driver.find_element_by_css_selector("#messages > div").text
        self.driver.refresh()
        assert "Arr!" in message2
        assert "Enter" in message2


@pytest.fixture(params=[("unknown@codility.com", "password"), ("codility.com", "password")])
def getData(request):
   return request.param

@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Rajeev\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get(
        "https://codility-frontend-prod.s3.amazonaws.com/media/task_static/python_selenium_login_page/9a83bda125cd7398f9f482a3d6d45ea4/static/attachments/reference_page.html")
    request.cls.driver = driver
    return driver

