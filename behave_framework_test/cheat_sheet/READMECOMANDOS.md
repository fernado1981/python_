<a name='top'></a>
[Principal](../README.md) 

# Comandos comunes:
Los citados en esta sección no significa que seán los unicos, pero si los más itilizados

## Comandos Get:
Ayudan a buscar informacion importante sobre la página/elemento. estos son algunos de los más importantes:  
- **getTitle**, no necesita parámetros, este obtiene el título de la página.

        driver.title

- **getPageSource**, no necesita parámetros, devuelve el código de la página como valor de cadena.
    
         driver.page_source

- **getCurrentUrl**, No necesita parámetros, obtiene la url actual del navegador

        driver.current_url
    
- **getText()**, recupera el texto interior del elemento que se especifique

## Comandos navigate:
permiten navegar entre las diferentes páginas Web.
- **get()**, abre una nueva ventana del exploradory busca la página que se especifique dentro de los parentesis, el parámetro debe ser un objeto string.

       driver.get("https://selenium.dev")
    
- **Retroceder**

        driver.back()

- **Avanzar**

        driver.forward()

- **Actualizar**

        driver.refresh()
    
## Switch_to:
se utiliza para cambiar entre diferentes elementos de la ventana, que de otra manera serían imposibles de acceder
- **cambiar al elemento activo:**

        driver.switch_to.active_element
        
- **cambiar al alert:**

        driver.switch_to.alert

- **cambiar al contenido por defecto:**

        driver.switch_to.default_content
        
- **cambiar al frame:**

        driver.switch_to.frame

- **cambiar a la ventana:**

        driver.switch_to.window
        
## click:
se utiliza para simular click sobre un elemento.

**Ejemplo:**

        python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
        python_button.click()
        
## send_key
se utiliza para escribir sobre elementos tipo textarea, input, ...

        text_area = driver.find_element_by_id('textarea')
        text_area.send_keys("print('Hello World')")
        
simular enter o las flechas:
        
        element.send_keys(" and some", Keys.ENTER)
        element.send_keys(" and some", Keys.ARROW_DOWN)
    
## Cerrar y salir del navegador:
- **close:**

        driver.close()

- **quit:**

        driver.quit()
    
[Subir](#top)
