import pytest
from page_object_pattern_python.pages.home import HomePage
from selenium import webdriver


class Browser(object):
    types = []


def factory(browser_type):
    class Firefox(Browser):
        @staticmethod
        def start():
            return webdriver.Firefox()

    class Other(Browser):
        def start(self):
            pass

    if browser_type == "Firefox":
        return Firefox().start()
    if browser_type == "Other":
        return Other().start()
    assert 0, "Bad shape creation: " + browser_type


@pytest.yield_fixture(scope='session')
def set_browser():
    """
    Set up FF browser instance
    """
    driver = factory('Firefox')
    yield driver
    print("Stop browser instance: %s " % driver)
    driver.quit()


def test_cookies(set_browser):
    """
    Example test case for showing 'pytest' and POM pattern
    :param set_browser: browser instance
    """
    homepage = HomePage(set_browser)
    homepage.navigate()
    homepage.wait_for_element_on_the_page()
    cookies_page = homepage.navigate_to_cookies_page()
    cookies_page.wait_for_page_to_load()
    cookies_page.move_to_cookies_settings()
    cookies_page.wait_for_element_xpath(cookies_page.functional_cookies)
    cookies_page.turn_off_functional_cookies()





