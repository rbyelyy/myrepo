import pytest
from page_object_pattern_python.pages.base import Base
from page_object_pattern_python.pages.home import Homepage


def teardown_module():
    pass


if __name__ == "__main__":
    homepage = Homepage()
    homepage.navigate()
    homepage.wait_for_page_to_load()
    cookies_page = homepage.navigate_to_cookies_page()
    cookies_page.wait_for_page_to_load()
    cookies_page.move_to_cookies_settings()
    cookies_page.wait_for_element_xpath(cookies_page.functional_cookies)
    cookies_page.turn_off_functional_cookies()
