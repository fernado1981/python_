<a name="top"></a>
[Principal](../README.md)<br/>


# Documentación:
> https://selenium-python.readthedocs.io/<br/>
> https://www.selenium.dev/documentation/es/

# Instalar Selenium con brew:<br>
    brew install selenium-server-standalone

# Drivers:<br/>
    Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads
    Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
    Firefox:	https://github.com/mozilla/geckodriver/releases
    Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/

# Ejemplo de uso:<br/>
    from selenium.webdriver import Chrome

    driver = Chrome()
    Chrome(executable_path='/usr/local/bin/chromedriver')
    driver.get("https://selenium.dev")
    driver.maximize_window()

## Click de un elemento:<br/>
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

## Localizar elemento By Name, escribir y pulsar enter<br/>
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)

## Navegar hacia una url:<br/>
    driver.get("https://selenium.dev")

## Obtener la url actual:<br/>
    driver.current_url

## Obtener el title:<br/>
    driver.title

## Retroceder:<br/>
    driver.back()

## Avanzar:<br/>
    driver.forward()

## Actualizar:<br/>
    driver.refresh()

## Localizar elemento By Id:<br/>
    driver.find_element(By.ID, "cheese")
    usernameField = driver.find_element(By.ID, "username")
    usernameField.clear();
    username.sendKeys("Fernando")
    passwordField = driver.find_element(By.ID, "password")
    passwordField.claer();
    password.sendkeys("*******")

## Localizar By Css_selector, por ejemplo en una lista:<br/>
    driver.find_element_by_css_selector("#cheese #cheddar")

## Localizar todos los elementos de la lista:<br/>
    driver.find_elements_by_css_selector("#cheese li")

# Frames e Iframes:<br/>
Ejemplon HTML:<br/>
--------------
     <div id="modal">
       <iframe id="buttonframe" name="myframe"  src="https://seleniumhq.github.io">
           <button>Click here</button>
       </iframe>
     </div>

Usando el ID<br/>
------------
    driver.switch_to.frame('buttonframe')

Ahora podemos hacer clic en el botón<br/>
------------------------------------
    driver.find_element(By.TAG_NAME, 'button').click()

## salir del iframe:<br/>
    driver.switch_to.default_content()

# Esperas<br/>
Espara hasta que se cumpla una condición:<br/>
-----------------------------------------
    wait.until(some_condition)

> Haz clic en el enlace para activar la alerta:<br/>

    driver.find_element(By.LINK_TEXT, "See an example alert").click()

>  Espera a que se muestre la alerta y almacenala en una variable:<br/>
    
    alert = wait.until(expected_conditions.alert_is_present())

> Almacena el texto de la alerta en una variable:<br/>

    text = alert.text

> Presiona el botón OK:<br/>

    alert.accept()
    
# Formas de hacer scroll:
![Scroll_Down](../Cheat_Sheet/Scroll_down.png)

# Espera Implicita:<br/>
    driver.implicitly_wait(10)

# Salir del navegador al final de una sesión:<br/>
    driver.quit()
[Subir](#top)
