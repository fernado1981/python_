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
