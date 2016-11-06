from selenium.webdriver.common.by import By
from page_object_pattern_python.pages.base import Base


class Cookiespage(Base):
    def __init__(self, driver):
        super().__init__()
        self.url = 'ttp://www.bbc.com/usingthebbc/cookies/'
        self.driver = driver

    logo = '//a[@title = "Using the BBC"]'
    cookies_settings = '#orb-modules > nav.navbar.navbar-topic > div > div > div.navbar-item.navbar-list > ul > li:nth-child(2) > a'
    functional_cookies = '#bbc_functional_cookie_button'

    def wait_for_page_to_load(self):
        self.wait_for_element_xpath(self.logo)

    def move_to_cookies_settings(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.cookies_settings)
        element.click()

    def turn_off_functional_cookies(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.functional_cookies)
        element.click()
