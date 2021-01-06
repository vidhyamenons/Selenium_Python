from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Rajeev\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://codility-frontend-prod.s3.amazonaws.com/media/task_static/python_selenium_login_page/9a83bda125cd7398f9f482a3d6d45ea4/static/attachments/reference_page.html")
driver.find_element_by_id("email-input").send_keys("login@codility.com")
driver.find_element_by_id("password-input").send_keys("password")
driver.find_element_by_id("login-button").click()
message = driver.find_element_by_css_selector("#container > div").text
print(message)
driver.get("https://codility-frontend-prod.s3.amazonaws.com/media/task_static/python_selenium_login_page/9a83bda125cd7398f9f482a3d6d45ea4/static/attachments/reference_page.html")
driver.find_element_by_id("email-input").send_keys("loginodility.com")
driver.find_element_by_id("password-input").send_keys("password")
driver.find_element_by_id("login-button").click()
print(driver.find_element_by_css_selector("#messages > div").text)
