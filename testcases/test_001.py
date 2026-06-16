from POM.login import Login
from utilites.xlutilites import read_data
from utilites.verification import send_keys, click_element
# class Test_Login():
def test_datadriver_login(launch):
    d = read_data("excel_files/login_page.xls", "logindata")
    for i,j in d.items():
        driver = launch
        login = Login(driver)
        print(f"Attempting login with username: {i}, password: {j}")
        email=login.email_textfield()
        send_keys(driver,email,i)
        pasword=login.password_textfield()
        send_keys(driver,pasword,j)
        loginbtn=login.login_button()
        click_element(driver,loginbtn)
