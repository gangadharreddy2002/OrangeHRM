from time import sleep
import pytest
from selenium.webdriver import Chrome,ChromeOptions
from utilites.verification import *
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
    verify_page(driver,"OrangeHRM")
    yield  driver
    sleep(10)
    driver.close()