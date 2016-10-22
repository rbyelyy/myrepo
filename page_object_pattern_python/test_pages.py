import unittest
from selenium import webdriver
from pages import *
#from testCases import test_cases
from locators import *
from selenium.webdriver.common.by import By

# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>
# If you want to run it just a class, you should type: python <module-name.py> <class-name>

class TestPages(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.get("http://korrespondent.net/")

    # def test_page_load(self):
    #     #print "\n" + str(test_cases(0))
    #     page = MainPage(self.driver)
    #     self.assertTrue(page.check_page_loaded())

    def test_authorize_button(self):
        #print "\n" + str(test_cases(3))
        page = MainPage(self.driver)
        loginPage = page.authorize()
        #self.assertTrue(loginPage.check_page_loaded())

    # def test_sign_in_with_valid_user(self):
    #     #print "\n" + str(test_cases(4))
    #     mainPage = MainPage(self.driver)
    #     loginPage = mainPage.click_sign_in_button()
    #     result = loginPage.login_with_valid_user("valid_user")
    #     self.assertIn("yourstore/home", result.get_url())
    #
    # def test_sign_in_with_in_valid_user(self):
    #     #print "\n" + str(test_cases(5))
    #     mainPage = MainPage(self.driver)
    #     loginPage = mainPage.click_sign_in_button()
    #     result = loginPage.login_with_in_valid_user("invalid_user")
    #     self.assertIn("There was a problem with your request", result)

    def tearDown(self):
        pass
        #self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=2).run(suite)