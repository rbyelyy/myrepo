from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from page_object_pattern_python.pages.base import Base


class Cookies(Base):
    def __init__(self, driver):
        super().__init__()
        self.url = 'ttp://www.bbc.com/usingthebbc/cookies/'
        self.driver = driver

    logo = '//a[@title = "Using the BBC"]'
    cookies_settings = '#orb-modules > nav.navbar.navbar-topic > div > div > div.navbar-item.navbar-list > ul > li:nth-child(2) > a'
    functional_cookies = "//label[@for='bbc_functional_cookie']"

    def wait_for_page_to_load(self):
        self.wait_for_element_xpath(self.logo)

    def move_to_cookies_settings(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.cookies_settings)
        element.click()

    def turn_off_functional_cookies(self):
        element = self.driver.find_element(By.XPATH, self.functional_cookies)
        self.driver.execute_script("arguments[0].click();", element)