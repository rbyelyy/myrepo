from selenium.webdriver.common.by import By
from page_object_pattern_python.pages.base import BasePage


class Cookies(BasePage):

    url = 'http://www.bbc.com/usingthebbc/cookies/'
    logo = '//a[@title = "Using the BBC"]'
    cookies_settings = '#orb-modules > nav.navbar.navbar-topic > div > div > div.navbar-item.navbar-list > ul > li:nth-child(2) > a'
    functional_cookies = "//label[@for='bbc_functional_cookie']"

    def wait_for_page_to_load(self):
        self.wait_for_element_xpath(self.logo)

    def move_to_cookies_settings(self):
        self.wait_for_element_css(self.cookies_settings)
        element = self.driver.find_element(By.CSS_SELECTOR, self.cookies_settings)
        self.driver.execute_script("arguments[0].click();", element)

    def turn_off_functional_cookies(self):
        print('Turn off {0} element'.format(self.functional_cookies))
        element = self.driver.find_element(By.XPATH, self.functional_cookies)
        self.driver.execute_script("arguments[0].click();", element)
