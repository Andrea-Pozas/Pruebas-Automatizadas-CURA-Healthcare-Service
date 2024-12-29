from selenium.webdriver.common.by import By


class LoginPageLocators:
    #Localizadores para el formulario de incio de sesión
    username_field = (By.ID, "txt-username")
    password_field = (By.ID, "txt-password")
    login_button = (By.ID, "btn-login")
    # Localizadores para el Menú despegable
    drop_down_menu = (By.ID, "menu-toggle")
    home_option = (By.XPATH, '//*[text()="Home"]')
    login_option = (By.XPATH, '//*[text()="Login"]')
