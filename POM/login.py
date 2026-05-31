class Login():
    def __init__(self,driver):
        self.driver=driver
    def email_textfield(self):
        return self.driver.find_element("xpath","//input[@name='username']")
    def password_textfield(self):
        return self.driver.find_element("xpath","//input[@name='password']")
    def login_button(self):
        return self.driver.find_element("xpath","//div[@class='oxd-form-actions orangehrm-login-action']")
    def forgot_password_link(self):
        return self.driver.find_element("xpath","//div[@class='orangehrm-login-forgot']")