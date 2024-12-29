import time
from selenium import webdriver
from LocatorsLoginpage import LoginPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.selectors = LoginPageLocators

    # Métodos para dirigirse a la Login Page
    def click_drop_down_menu(self):
        WebDriverWait(self.driver,timeout=10).until(EC.presence_of_element_located((By.ID,"menu-toggle")))
        self.driver


    def click_login_option_on_the_menu(self):
        self.driver


    def click_login_option_drop_menu(self):
        self.click_drop_down_menu()
        self.click_login_option_on_the_menu()



