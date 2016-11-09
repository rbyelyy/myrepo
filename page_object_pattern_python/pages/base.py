import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.bbc.com/'
        self.element_timeout = 10

    def navigate(self):
        self.driver.get(self.url)
        assert self.driver.current_url == self.url
        print('Open page: {0}'.format(self.url))

    def wait_for_element_xpath(self, locator):
        wait = WebDriverWait(self.driver, self.element_timeout)
        wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        print('Wait for element: {0}...'.format(locator))

    def wait_for_element_css(self, locator):
        wait = WebDriverWait(self.driver, self.element_timeout)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        print('Wait for element: {0}...'.format(locator))
