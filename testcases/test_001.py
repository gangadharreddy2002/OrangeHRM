from POM.login import Login
from utilites.xlutilites import read_data
from utilites.verification import send_keys, click_element
# def test_Tc001(launch):
#     driver=launch
#     login=Login(driver)
#     email=login.email_textfield()
#     send_keys(driver,email,"Admin")
#     pasword=login.password_textfield()
#     send_keys(driver,pasword,"admin123")
#     loginbtn=login.login_button()
#     click_element(driver,loginbtn)
def test_TC001(launch):
    driver=launch
    login=Login(driver)
    d = read_data("../excel_files/login_page.xls", "logindata")
    for i,j in d.items():
        print(f"Attempting login with username: {i}, password: {j}")
        email=login.email_textfield()
        send_keys(driver,email,i)
        pasword=login.password_textfield()
        send_keys(driver,pasword,j)
        loginbtn=login.login_button()
        click_element(driver,loginbtn)