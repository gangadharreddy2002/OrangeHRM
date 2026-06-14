from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class Login():
    def __init__(self,driver):
        self.driver=driver
    def password_textfield(self):
        return WebDriverWait(self.driver, 20).until(
            lambda d: d.find_element("xpath","//input[@name='password']"))
    def email_textfield(self):
        return WebDriverWait(self.driver, 20).until(
            lambda d: d.find_element("xpath", "//input[@name='username']"))
    def login_button(self):
        return WebDriverWait(self.driver, 20).until(
            lambda d: d.find_element("xpath","//div[@class='oxd-form-actions orangehrm-login-action']"))
    def forgot_password_link(self):
        return WebDriverWait(self.driver, 20).until(
            lambda d: d.find_element("xpath","//div[@class='orangehrm-login-forgot']"))
