import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Base(metaclass=Singleton):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = self.set_base_url()
        self.element_timeout = 10

    def navigate(self):
        if self.url:
            self.driver.get(self.url)

    def wait_for_element_xpath(self, locator):
        wait = WebDriverWait(self.driver, self.element_timeout)
        wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    def wait_for_element_css(self, locator):
        wait = WebDriverWait(self.driver, self.element_timeout)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))

    @pytest.fixture
    def set_base_url(self):
            self.url = 'http://www.bbc.com/'
