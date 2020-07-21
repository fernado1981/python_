# Documentación:
https://selenium-python.readthedocs.io/<br/>
https://www.selenium.dev/documentation/es/

# Instalar Selenium con brew:<br>
> brew install selenium-server-standalone

# Drivers:<br/>
Chrome:	https://sites.google.com/a/chromium.org/chromedriver/downloads<br/>
Edge:	https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/<br/>
Firefox:	https://github.com/mozilla/geckodriver/releases<br/>
Safari:	https://webkit.org/blog/6900/webdriver-support-in-safari-10/<br/>

# Ejemplo de uso:<br/>
from selenium.webdriver import Chrome<br/>

driver = Chrome()<br/>
Chrome(executable_path='/usr/local/bin/chromedriver')<br/>
driver.get("https://selenium.dev")<br/>
driver.maximize_window()<br/>

## Click de un elemento:<br/>
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()<br/>

## Localizar elemento By Name, escribir y pulsar enter<br/>
driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)<br/>

## Navegar hacia una url:<br/>
driver.get("https://selenium.dev")<br/>

## Obtener la url actual:<br/>
driver.current_url<br/>

## Obtener el title:<br/>
driver.title<br/>

## Retroceder:<br/>
driver.back()<br/>

## Avanzar:<br/>
driver.forward()<br/>

## Actualizar:<br/>
driver.refresh()<br/>

## Localizar elemento By Id:<br/>
driver.find_element(By.ID, "cheese")<br/>
<br/>
usernameField = driver.find_element(By.ID, "username")<br/>
usernameField.clear();<br/>
username.sendKeys("Fernando")<br/>
passwordField = driver.find_element(By.ID, "password")<br/>
passwordField.claer();<br/>
password.sendkeys("*******")<br/>

## Localizar By Css_selector, por ejemplo en una lista:<br/>
driver.find_element_by_css_selector("#cheese #cheddar")<br/>
<br/>
/* <ol id=cheese>"<br/>
/* <li id=cheddar>…"<br/>
/* <li id=brie>…"<br/>
/* <li id=rochefort>…"<br/>
/* <li id=camembert>…"<br/>
/* </ul>"<br/>

## Localizar todos los elementos de la lista:<br/>
driver.find_elements_by_css_selector("#cheese li")<br/>

# Frames e Iframes:<br/>
Ejemplon HTML:<br/>
--------------
<div id="modal"><br/>
  <iframe id="buttonframe" name="myframe"  src="https://seleniumhq.github.io"><br/>
   <button>Click here</button><br/>
 </iframe><br/>
</div><br/>

Usando el ID<br/>
------------
driver.switch_to.frame('buttonframe')<br/>

Ahora podemos hacer clic en el botón<br/>
------------------------------------
driver.find_element(By.TAG_NAME, 'button').click()<br/>

## salir del iframe:<br/>
driver.switch_to.default_content()<br/>

# Esperas<br/>
Espara hasta que se cumpla una condición:<br/>
-----------------------------------------
wait.until(some_condition)<br/>

Haz clic en el enlace para activar la alerta:<br/>
---------------------------------------------
driver.find_element(By.LINK_TEXT, "See an example alert").click()<br/>

Espera a que se muestre la alerta y almacenala en una variable:<br/>
---------------------------------------------------------------
alert = wait.until(expected_conditions.alert_is_present())<br/>

Almacena el texto de la alerta en una variable:<br/>
-----------------------------------------------
text = alert.text<br/>

Presiona el botón OK:<br/>
--------------------
alert.accept()<br/>

# Espera Implicita:<br/>
driver.implicitly_wait(10)<br/>

# Salir del navegador al final de una sesión:<br/>
driver.quit()<br/>
