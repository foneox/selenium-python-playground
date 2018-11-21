import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import *
import time

import os
from slackclient import SlackClient


def test_uz_availability(driver):
    
    with pytest.allure.step('Get UZ'):
        driver.get("https://booking.uz.gov.ua/")
        driver.find_element_by_name("from-title").clear()
        driver.find_element_by_name("from-title").send_keys("Київ")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='ui-id-1']/li[1]")))
        driver.find_element_by_xpath("//*[@id='ui-id-1']/li[1]").click()

        driver.find_element_by_name("to-title").clear()
        driver.find_element_by_name("to-title").send_keys("Івано-Франківськ")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='ui-id-2']/li[1]")))
        driver.find_element_by_xpath("//*[@id='ui-id-2']/li[1]").click()
        
        
        #driver.find_element_by_name("date-hover").send_keys("11.22.2018")
        driver.find_element_by_name("date").set_attribute("value", "2018-11-22")
        #driver.find_element_by_name("date-hover").click()

        #driver.find_element_by_name("date-hover").send_keys("11.22.2018")
        
        
        time.sleep(1)

        #WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.XPATH, "//*[@id='search-frm']/form/div[3]/div/button")))
        driver.find_element_by_xpath("//*[@id='search-frm']/form/div[3]/div/button").click()
        
        time.sleep(10)
        
        
