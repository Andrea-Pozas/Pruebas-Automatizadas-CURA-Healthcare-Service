from selenium import webdriver
from LocatorsLoginpage import LoginPageLocators
from MethodsLoginpage import LoginPage
import time



class TestLoginPage:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://katalon-demo-cura.herokuapp.com/")
        cls.login_page = LoginPage
        cls.selectors = LoginPageLocators
        cls.driver.maximize_window()

    def test_click_login_on_the_menu(self):
        self.login_page.click_login_option_on_the_menu()

    @classmethod
    def teardown_class(cls):
        time.sleep(15)
        cls.driver.quit()