from pageObjects.homepage import homepage
from utilities.baseclass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        home = homepage(self.driver)
        home.login().send_keys("login@codility.com")
        home.given_password().send_keys("password")
        home.login_button().click()
        expected_message = home.message().text
        print(expected_message)


