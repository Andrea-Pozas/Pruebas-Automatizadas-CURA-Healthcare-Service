import time

from selenium import webdriver
from LocatorsLadingpage import LandingPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LandingPage:
    def __init__(self, driver):
        self.driver = driver
        self.selectors = LandingPageLocators

    # 1.Métodos para el botón make an appointment
    def click_make_an_appointment(self):
        WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located((By.ID, "btn-make-appointment" )))
        self.driver.find_element(*self.selectors.botton_make_an_appointment).click()

    def login_user_view(self):
        return self.driver.find_element(*self.selectors.Login_text).text

    # 2. Métodos para el menú despegable
    def click_drop_down_menu(self):
        WebDriverWait(self.driver, timeout=15).until(EC.presence_of_element_located((By.ID, "menu-toggle")))
        self.driver.find_element(*self.selectors.drop_down_menu).click()

    def drop_down_menu_is_displayed(self):
        return self.driver.find_element(*self.selectors.drop_down_menu).is_displayed()

    # 3. Métodos para el botón Home del menú despegable
    def click_home_option_on_the_menu(self):
        self.driver.find_element(*self.selectors.home_option).click()

    def home_page_view(self):
        return self.driver.find_element(*self.selectors.text_Home_page_CURE_HealthCare).text

    def home_option_drop_down_menu(self):
        self.click_drop_down_menu()
        self.click_home_option_on_the_menu()

    # 4.Métodos para el botón Login del menú despegable
    def click_login_option_on_the_menu(self):
        self.driver.find_element(*self.selectors.login_option).click()

    def click_login_option_drop_menu(self):
        self.click_drop_down_menu()
        self.click_login_option_on_the_menu()

    # 5. Metodos para cerrar el menú

    def close_drop_down_menu(self):
        self.click_drop_down_menu()
        self.click_drop_down_menu()