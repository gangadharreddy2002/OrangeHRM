from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Login():
    def __init__(self,driver):
        self.driver=driver

    def password_textfield(self):
        passwrd=self.driver.find_element("xpath","//input[@name='password']")
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(passwrd))
    def email_textfield(self):
        email=self.driver.find_element("xpath","//input[@name='username']")
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(email))
    def login_button(self):
        loggin=self.driver.find_element("xpath","//div[@class='oxd-form-actions orangehrm-login-action']")

        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(loggin))
    def forgot_password_link(self):
        forpsd=self.driver.find_element("xpath","//div[@class='orangehrm-login-forgot']")
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(forpsd))