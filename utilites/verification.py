from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def save_screenshot(driver):
    from datetime import datetime
    path= r"../defects"
    d=datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    driver.save_screenshot(f"{path}/{d}.png")
def verify_element(driver,element):
    try:
        return element.is_displayed()
    except:
        save_screenshot(driver)
        return False
def click_element(driver,element):
    try:
        element.is_displayed()
        element.click()
        return True
    except:
        save_screenshot(driver)
        return False
def send_keys(driver,ele,inp):
    try:
        ele.send_keys(inp)
        return True
    except:
        save_screenshot(driver)
        return False
def verify_page(driver,excepted):
    try:
        assert driver.title == excepted, f"Title mismatch. Expected: {excepted}, Got: {driver.title}"
        return True
    except AssertionError as e:
        save_screenshot(driver)
        print(f"title doesn't match!!!! {e}")
        return False
    except Exception as e:
        save_screenshot(driver)
        print(f"Error verifying page: {e}")
        return False