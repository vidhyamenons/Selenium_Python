from selenium.webdriver.common.by import By


class homepage:

    def __init__(self, driver):
        self.driver = driver

    log =(By.CSS_SELECTOR, "#email-input")
    password = (By.CSS_SELECTOR, "#password-input")
    button = (By.CSS_SELECTOR, "#login-button")
    msg = (By.CSS_SELECTOR, "#container > div")

    def login(self):
        return self.driver.find_element(*homepage.log)

    def message(self):
        return self.driver.find_element(*homepage.msg)

    def given_password(self):
        return self.driver.find_element(*homepage.password)

    def login_button(self):
        return self.driver.find_element(*homepage.button)
