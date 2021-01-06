import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\Rajeev\\Downloads\\chromedriver_win32\\chromedriver.exe")
    elif browser == "firefox":
        print("Firefox")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    #driver.get("https://codility-frontend-prod.s3.amazonaws.com/media/task_static/python_selenium_login_page/9a83bda125cd7398f9f482a3d6d45ea4/static/attachments/reference_page.html")
    request.cls.driver = driver
    return driver




