<a name="top"></a>

## behave_framework_test
Framework para automatización de pruebas BDD (Behavior Driven Development) para (front-back) con python
behave, con una gran documentación que podréis encontrar en su web oficial, la cual dejo mencionada en el siguiente apartado.

### Documentación:
- **behave:** <https://behave.readthedocs.io/en/stable/>
- **cucumber:** <https://cucumber.io/>
- **selenium:** <https://www.selenium.dev/documentation/es/>

## Instalación de requerimientos:
      pip3 install behave
      pip3 install behave2cucumber
      pip3 install cucumber-tag-expressions
      pip3 install behave-html-formatter

## Instalación más reciente desde repositorio behave:
      pip3 install git+https://github.com/behave/behave
      
## Actualización:

      pip3 install -U behave

## REQUISITOS MÍNIMOS:
**Nota:** mantener una estructura de proyecto uniforme ayuda a mantener el proyecto.
- La implementación completa debe estar presente en el directorio 'features'.
- Los archivos de caracteristicas (* .feature) deben estar presentes en el directorio 'features', incluido 'environment.py' (que contiene los ganchos necesarios para la inicialización y finalización).
- La implementación de las definiciones de pasos de las caracteristicas debe estar presente en el directorio features/steps.
- Las opciones de configuración que se ubicarán en archivos .ini / .cfg. 
- Los reportes los pondremos en un directorio aparte reports

      features/                       # implementación completa
          everything.feature          # ficheros .feature y environment.py
          steps/steps.py              # implementación de las definiciones de steps del feature *.py
          reports/                    # donde se guardarán los reportes de las preubas ejecutadas
    
### Creación estructura con pycharm:
#### **Step 1 (proyecto):**
      create a new proyect
      location (la desada por el usuario)
      new enviroment using virtualenv
      base interpreter: /usr/bin/python3
      interpreter: Python3.8

#### **Step 2 (estructura):**
- **Nota:** sobre el directorio principal del proyecto creado,
      
      new Python Package llamado web
      
- **Nota:** repetir este proceso para el package features y dentro de el para el package steps
      
      new Directory llamado reports

#### **Step 3 (behave.ini):**
- crear el fichero de configuración behave.ini (Consiste en una o secciones más nombradas(cada sección esta delimitada por []), cada una de las cuales puede contener opciones individuales con nombres y valores), en la raiz del proyecto con el siguiente contenido:
**Nota:** opciones de configuración que se ubicarán en archivos .ini / .cfg

      [behave]
      stderr_capture = False
      stdout_capture = False
      [behave.formatters]
      html = behave_html_formatter:HTMLFormatter
      [Environment]
      Browser = chrome
      #Browser = firefox
      [behave.userdata]
      browser = chrome
      #browser = firefox

**Nota:** En caso de querer utilizar firefox, deberemos comentar tanto Enviroment como userdata el browser de chrome y descomentar el de firefox

#### **Step 4 (fixtures.py):**
- Crear el fichero tipo python llamado fixtures (lógica auxiliar para la ejecución de la automatización de pruebas) y agregar el siguiente contenido:

      from selenium import webdriver
      from web.web import Web


      def browser_chrome(context, timeout=30, **kwargs):
          #Chrome
          browser = webdriver.Chrome()
          #Firefox
          #browser = webdriver.Firefox()
          web = Web(browser)
          context.web = web
          yield context.web
          browser.quit()

**Nota:** En caso de querer usar firefox, deberemos comentar la instancia a webdriver.Chrome(), y descomentar la de webdriver.firefox()

#### **Step 5 (web/factory.py):**
- crear el fichero tipo phyton dentro de web llamado factory.py (obtendremos el webdriver en funcion del browser seleccionado), con el siguiente contenido:

      from selenium import webdriver
      from web.web import Web


      def get_web(browser):
          if browser == "chrome":
              return Web(webdriver.Chrome())
          if browser == "firefox":
              return Web(webdriver.Firefox())
              
 #### **Step 6 (web/web.py):**
 - Generamos el fichero para el comportamiento de los localizadores de la web, llamado web.py, con el siguiente contenido:
 **Nota:** este fichero ira creciendo a medida que necesitemos usar mas métodos
 
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC


        class Web(object):
            __TIMEOUT = 10

            def __init__(self, web_driver):
                super().__init__()
                self._web_driver_wait = WebDriverWait(web_driver, Web.__TIMEOUT)
                self._web_driver = web_driver

            def open(self, url):
                self._web_driver.get(url)

            def maximize(self):
                self._web_driver.maximize_window()

            def close(self):
                self._web_driver.quit()

            def get_url(self):
                return self._web_driver.current_url

            def get_title(self):
                return self._web_driver.title

            def get_text(self, xpath):
                return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).text

            # Helper functions that are used to identify the web locators in Selenium Python tutorial

            def find_by_xpath(self, xpath):
                return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

            def find_by_xpath_displayed(self, xpath):
                return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath))).is_displayed()

            def finds_by_xpath_displayed(self, xpath):
                return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

            def find_by_id(self, id_value):
                return self._web_driver_wait.until(EC.visibility_of_element_located((By.ID, id_value)))

            def find_by_id_displayed(self, id_value):
                return self._web_driver_wait.until(EC.presence_of_element_located((By.ID, id_value))).is_displayed()

#### **Step 7 (features/environment.py):**
- Creación del fichero environment.py, con el siguiente contenido:

      from web.factory import get_web


      def before_all(context):
          web = get_web(context.config.userdata['browser'])
          context.web = web
          
**Nota:** si nos fijamos estamos haciendo uso de la función get_web definida en el fichero factory.py y le estamos pasando el contenido de la variable browser declarada en el fichero behave.ini de configuración, dentro de la variable browser, declarada en la sección [baheve.userdata]

**Nota:** Environment.py (que contiene los ganchos(hooks) necesarios para la inicialización y finalización) es un archivo de entorno de Python Behave. Se puede utilizar para definir códig* que debe ejecutarse antes y después de que ocurran ciertos eventos durante el ciclo de automatización de la prueba de Selenium<br/>

Tipos de funciones de enviroment:
- before_step (context, step), after_step (context, step), se ejecuta antes y después de cada step
- before_scenario (context, scenario), after_scenario (context, scenario): ejecutado antes y después de cada scenario.
- before_scenario (context, feature), after_scenario (context, feature): se ejecuta antes y después de cada feature.
- before_all (context), after_all (context): se ejecuta antes y después de la ejecución de todo el ciclo de prueba.

#### **Step 8 (features/prueba.feature):**
- creación del fichero *.feature, el cual contendra el gerking a ejecutar

- **cucumber_gerking:** <https://cucumber.io/docs/gherkin/reference/>

#### **Step 9 (features/steps/prueba_steps.py):**
- creación de los ficheros de steps para los gerking y los hooks necesarios

- **cucumber_step:** <https://cucumber.io/docs/cucumber/step-definitions/#:~:text=A%20Step%20Definition%20is%20a,matching%20step%20definition%20to%20execute.>

[Subir](#top)
