from selenium.webdriver.common.by import By
from page_object_pattern_python.pages.base import BasePage
from page_object_pattern_python.pages.cookies import Cookies


class HomePage(BasePage):

    url = 'http://www.bbc.com/'
    signin_button = '//*[@id="idcta-username"]'
    cookies_link = '#orb-contentinfo > div > ul > li.orb-footer-cookies > a'

    def wait_for_element_on_the_page(self):
        self.wait_for_element_xpath(self.signin_button)

    def navigate_to_cookies_page(self):
        print('Open page: {0}'.format(Cookies.url))
        elements = self.driver.find_elements(By.LINK_TEXT, 'Cookies')
        assert len(elements) == 1
        elements[0].click()
        return Cookies(self.driver)
