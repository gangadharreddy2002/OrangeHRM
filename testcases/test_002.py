from POM.login import Login
from POM.storyboard import *
from conftest import *

def test_Tc001(launch):
    driver=launch
    login=Login(driver)
    email=login.email_textfield()
    send_keys(driver,email,"Admin")
    pasword=login.password_textfield()
    send_keys(driver,pasword,"admin123")
    loginbtn=login.login_button()
    click_element(driver,loginbtn)
    storyboard=Storyboard(driver)
    drop=storyboard.profile_icon()
    click_element(driver,drop)
    about_button=storyboard.about_button()
    click_element(driver,about_button)