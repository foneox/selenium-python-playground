import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import *
import time
from commons import slack

import os
from slackclient import SlackClient
from commons import screenshooter

stationCodes = {'Київ': '2200001', 'Івано-Франківськ': '2218200', 'Воловець': '2218145'}

@pytest.mark.parametrize("src,dest,date", [
    ("Київ", "Івано-Франківськ","2018-12-21"),
    ("Івано-Франківськ", "Київ","2018-12-25"),
    ("Київ", "Воловець","2018-12-28"),
    ("Воловець", "Київ","2019-01-02"),
])
def test_uz_availability(driver, src, dest, date):
    
    with pytest.allure.step('Get UZ'):
        driver.get(f"https://booking.uz.gov.ua/?from={stationCodes[src]}&to={stationCodes[dest]}&date={date}&time=00%3A00&url=train-list")
        time.sleep(3)
        screenshot = screenshooter.fullpage_as_png(driver)
        slack.retrying_send_png(screenshot, f"date:{date} from:{src} to: {dest}")
