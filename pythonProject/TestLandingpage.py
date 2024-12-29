from selenium import webdriver
from MethodsLandingpage import LandingPage
from LocatorsLadingpage import LandingPageLocators
import time


class TestLandingPage:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://katalon-demo-cura.herokuapp.com/")
        cls.landing_page = LandingPage(cls.driver)
        cls.selectors = LandingPageLocators
        cls.driver.maximize_window()

# 1.Verifica que el botón make an appointment lleva al aréa de Login
    def test_make_an_appointment(self):
        self.landing_page.click_make_an_appointment()
        assert self.landing_page.login_user_view() == "Login"

# 2. Verifica que el menú despegable aparece correctamente
    def test_click_drop_down_menu(self):
        self.landing_page.click_drop_down_menu()
        assert self.landing_page.drop_down_menu_is_displayed() == True

# 3.Verifica que el botón Home del menú despegable lleve a la Landing page
    def test_click_home_on_the_menu(self):
        self.landing_page.home_option_drop_down_menu()
        assert self.landing_page.home_page_view() == "CURA Healthcare Service"

# 4. Verifica que el botón Login del menú despegable lleve a la página de Login
    def test_click_login_on_the_menu(self):
        self.landing_page.click_login_option_drop_menu()
        assert self.landing_page.login_user_view() == "Login"

# 5. Verifica que el menú despegable se pueda cerrar
    def test_close_drop_down_menu(self):
        self.landing_page.close_drop_down_menu()
        assert self.landing_page.home_page_view() == "CURA Healthcare Service"


    @classmethod
    def teardown_class(cls):
        time.sleep(15)
        cls.driver.quit()