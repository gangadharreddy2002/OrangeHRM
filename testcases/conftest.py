from time import sleep
import pytest
from selenium.webdriver import Chrome,ChromeOptions
from utilites.verification import *
from POM.login import Login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
base=r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
@pytest.fixture
def launch():
    opts=ChromeOptions()
    # opts.add_experimental_option("detach",True)
    opts.add_argument("--start-maximized")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    driver=Chrome(opts)
    driver.get(base)
    driver.maximize_window()
    driver.implicitly_wait(10)
    sleep(10)
    # assert driver.title==title,"title is not mathing"
    verify_page(driver,"OrangeHRM")
    yield  driver
    sleep(10)
    driver.close()