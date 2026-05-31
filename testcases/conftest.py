from time import sleep
import pytest
from selenium.webdriver import Chrome,ChromeOptions
from OrangeHRM.utilites.verification import *
base=r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
@pytest.fixture
def launch():
    opts=ChromeOptions()
    opts.add_experimental_option("detach",True)
    driver=Chrome(opts)
    driver.get(base)
    driver.maximize_window()
    driver.implicitly_wait(10)
    # sleep(10)
    # assert driver.title==title,"title is not mathing"
    verify_page(driver,"OrangeHRM")
    yield  driver
    sleep(10)
    driver.close()