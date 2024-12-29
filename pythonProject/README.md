# Pruebas automatizadas CURA Healthcare Service

# Pruebas automatizadas para pedir un taxi en Urban Routes 

- Pruebas funcionales automatizadas para la página web CURA Healthcare Service
# Herramientas 
- lenguaje

  ![Static Badge](https://img.shields.io/badge/Python-%233776AB?style=for-the-badge&logo=python&logoColor=white)

- librería
  
  ![Static Badge](https://img.shields.io/badge/Pytest-%230A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

- Framework
  
  ![Static Badge](https://img.shields.io/badge/Selenium-%2343B02A?style=for-the-badge&logo=selenium&logoColor=black)
- Método: POM 

Para realizar los test se necesitan tener instalados Selenium y pytest

# Test 
- Las pruebas que se ejecutan para la Landing Page son las siguientes:
  -  test_make_an_appointment: Verifica que el botón make an appointment lleva al aréa de Login
  - test_click_drop_down_menu: Verifica que el menú despegable aparece correctamente
  - test_click_home_on_the_menu: Verifica que el botón Home del menú despegable lleve a la Landing page
  - test_click_login_on_the_menu: Verifica que el botón Login del menú despegable lleve a la página de Login
  - test_close_drop_down_menu: Verifica que el menú despegable se pueda cerrar

- Para ejecutar todas las pruebas se puede utilizar el comando: pytest Test.py