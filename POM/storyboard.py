class Storyboard:
    def __init__(self,driver):
        self.driver=driver
    def profile_icon(self):
        return self.driver.find_element("xpath","//span[@class='oxd-userdropdown-tab']")
    def about_button(self):
        return self.driver.find_element("xpath","//a[text()='About']")
    def support_button(self):
        return self.driver.find_element("xpath","//a[text()='Support']")
    def change_password_button(self):
        return self.driver.find_element("xpath","//a[text()='Change Password']")
    def Logout_button(self):
        return self.driver.find_element("xpath","//a[text()='Logout']")
