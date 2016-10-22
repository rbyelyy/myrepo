from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class MainPageLocatars(object):
  AUTH          = (By.ID, 'nav-link-yourAccount')
  SEARCH        = (By.CSS_SELECTOR, '#twotabsearchtextbox')


class LoginPageLocatars(object):
  EMAIL         = (By.ID, 'email')
  PASSWORD      = (By.ID, 'password')
  SUBMIT        = (By.ID, 'autorizsubmit')
  ERROR_MESSAGE = (By.CSS_SELECTOR, '.popup__text_error')