import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from hamcrest import *


def test_uz_availability(driver):
    
    with pytest.allure.step('Get UZ'):
        driver.get("https://booking.uz.gov.ua/")
