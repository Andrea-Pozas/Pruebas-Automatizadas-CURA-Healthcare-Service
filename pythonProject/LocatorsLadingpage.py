from selenium.webdriver.common.by import By


class LandingPageLocators:
    # Localizadores para el botón make an appointment
    botton_make_an_appointment = (By.ID, "btn-make-appointment")
    Login_text = (By.XPATH, "//h2[text()='Login']")
    # Localizadores para el Menú despegable
    drop_down_menu = (By.ID, "menu-toggle")
    home_option = (By.XPATH, '//*[text()="Home"]')
    login_option = (By.XPATH ,'//*[text()="Login"]')
    text_Home_page_CURE_HealthCare = (By.XPATH, '//strong[text()="CURA Healthcare Service"]')

