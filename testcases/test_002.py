from POM.storyboard import *
from utilites.verification import *
from testcases.login import login
def test_Tc001(launch):
    driver=launch
    login(driver)
    storyboard=Storyboard(driver)
    drop=storyboard.profile_icon()
    click_element(driver,drop)
    about_button=storyboard.about_button()
    click_element(driver,about_button)
    cancel_button=storyboard.about_cancel()
    click_element(driver,cancel_button)
def test_Tc002(launch):
    driver=launch
    login(driver)
    storyboard=Storyboard(driver)
    drop=storyboard.profile_icon()
    click_element(driver,drop)
    support=storyboard.support_button()
    click_element(driver,support)
    verify_page(driver,"https://opensource-demo.orangehrmlive.com/web/index.php/help/support")
    print("support page is displayed")