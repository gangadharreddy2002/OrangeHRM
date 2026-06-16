from POM.login import *
from utilites.verification import *
def login(launch):
    driver=launch
    login=Login(driver)
    email=login.email_textfield()
    send_keys(driver,email,"Admin")
    psd=login.password_textfield()
    send_keys(driver,psd,"admin123")
    loginbtn=login.login_button()
    click_element(driver,loginbtn)