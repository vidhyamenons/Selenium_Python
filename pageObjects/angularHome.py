from selenium.webdriver.common.by import By


class mainpage:
    def __init__(self, driver):
        self.driver = driver

    input1 = (By.XPATH, "//div[@class='form-group'][1]/input")
    input2 = (By.CSS_SELECTOR, "[name='email']")
    input3 = (By.CSS_SELECTOR, "#exampleCheck1")
    input4 = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    input5 = (By.CSS_SELECTOR, "[value='Submit']")
    input6 = (By.XPATH, "//div[ @class ='container']/div[2]")


    def name(self):
        return self.driver.find_element(*mainpage.input1)

    def email(self):
        return self.driver.find_element(*mainpage.input2)

    def checkbox(self):
        return self.driver.find_element(*mainpage.input3)

    def gender(self):
        return self.driver.find_element(*mainpage.input4)

    def submit(self):
        return self.driver.find_element(*mainpage.input5)

    def alert(self):
        return self.driver.find_element(*mainpage.input6)



