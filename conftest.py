import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import allure
from allure.constants import AttachmentType

def pytest_addoption(parser):
   parser.addoption("--is_remote_driver", action="store", default="true", help="Run tests remotely")

WEBDRIVER_ENDPOINT = 'http://selenium:4444/wd/hub'



@pytest.fixture()
def driver(request):
    is_remote_driver = request.config.getoption("--is_remote_driver")
    if (is_remote_driver == "true"):
        ff_capabilities = DesiredCapabilities.FIREFOX
        ff_options = Options()
        ff_profile = FirefoxProfile()
        ff_profile.native_events_enabled = True
        browser_driver = webdriver.Remote(
            command_executor=WEBDRIVER_ENDPOINT,
            desired_capabilities=ff_capabilities,
            browser_profile=ff_profile,
            options=ff_options
        )
    elif (is_remote_driver == "false"):
        browser_driver = webdriver.Firefox()
    else:
        raise Exception("is_remote_driver can be only true or false")
    
    yield browser_driver
    screenshot = browser_driver.get_screenshot_as_png()
    allure.attach('screenshot', screenshot, type=AttachmentType.PNG)
    try:
        browser_driver.quit()
    except:
        pass
