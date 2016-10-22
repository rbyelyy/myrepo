from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base import Page
from locators import *

# Page opjects are written in this module.
# Depends on the page functionality we can have more functions for new classes


class MainPage(Page):
    def check_page_loaded(self):
        return True if self.find_element(*MainPageLocatars.AUTH) else False

    def authorize(self):
        self.hover(*MainPageLocatars.AUTH).click()
        return LoginPage(self.driver)

    def search_item(self):
        self.hover(*MainPageLocatars.SEARCH).click()

class LoginPage(Page):
    def check_page_loaded(self):
        return True if self.find_element(*LoginPageLocatars.EMAIL) else False

    def enter_email(self, user):
        self.driver.find_element(*LoginPageLocatars.EMAIL).send_keys('ttt@ttt.com')

    def enter_password(self, user):
        self.driver.find_element(*LoginPageLocatars.PASSWORD).send_keys('123123123')

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocatars.SUBMIT).click()

    def login(self, user):
        self.enter_email(user)
        self.enter_password(user)
        self.click_login_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return HomePage(self.driver)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*LoginPageLocatars.ERROR_MESSAGE).text    

class HomePage(Page):
    pass
    
class SignUpPage(Page):
    pass