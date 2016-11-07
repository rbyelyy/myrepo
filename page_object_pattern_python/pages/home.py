from selenium.webdriver.common.by import By
from page_object_pattern_python.pages.base import Base
from page_object_pattern_python.pages.cookies import Cookies


class Homepage(Base):
    def __init__(self):
        super().__init__()
        self.url = 'http://www.bbc.com/'
        self.signin_button = '//*[@id="idcta-username"]'
        self.cookies_link = '#orb-contentinfo > div > ul > li.orb-footer-cookies > a'

    def wait_for_page_to_load(self):
        self.wait_for_element_xpath(self.signin_button)

    def navigate_to_cookies_page(self):
        elements = self.driver.find_elements(By.LINK_TEXT, 'Cookies')
        assert len(elements) == 1
        elements[0].click()
        return Cookies(self.driver)
