<a name='top'></a>
[Principal](../README.md) 

## Herramienta importante:

**selectorshub:** <https://selectorshub.com/>

## LOCALIZADORES:
   
    - By.id("id")
    - By.name("name")
    - By.linkText("linktext")
    - By.partialLinkText("partialLinkTexdt")
    - By.tagName("tagname")

### **cssSelector:**<br/>
**Nota:**cssSelector y Xpath, son los mas utilizados dado que puede que no este el elemento necesario pero siempre habrá algún elemento que podamos coger.
* Atributo id:<br/>
	**sintax:** input#firstname, Donde el # se refiere al id
		
		Driver.findElement(By.cssSelector("input#firstname");
		Driver.findElement(By.cssSelector("#firstname");
* Atributo class:<br/>
	**sintax:** Input.firstname, Donde el . Hace referencia a la clase firstname
		
		Driver.findElement(By.cssSelector("input.firstname");
		Driver.findElement(By.cssSelector(".firstname");
**Nota:** Se pueden concatenar varias clases con el . (".class.class1")
* Por multiples atributos:
    
        <div class="ajax_enabled" style="display:block">
        Driver.findElement(By.cssSelector("div[class='ajax_enabled'][style='display:block']"));

### **XPath**
**Nota:** NUNCA se debe XPath absoluto, pues si se agrega un nuevo elemento el path cambiaria invalidado el elemento por el path absoluto.<br/>
Xpath relativo: es el más común o más utilizado, se basan en los atributos de los elementos html.<br/>
- **sintax:** xpath=//tagname[@attribute='value']
donde:
* **//:** selecciona el siguiente nodo
* **Tagname:** etiqueta del elemnto
* **@:** seleciona un atributo
* **Attribute:** atributo del elemento
* **Value:** valor del atributo

**Ejemplos:**<br/>
<input id=‘email’ name=‘email’ placehoplder=‘ntroduce tu email’ …><br/>
By.xpath(“//input[@placeholder=\”introduce tu email”]”)<br/>

    <input id=‘email’ name=‘email’ …..>
    By.xpath(“//input[@name=‘email’]”)

    <input id=‘email’ name=‘email’ type=‘email’ …..>
    By.xpath(“//input[@type=‘email’]”)

**Nota:** Si no se conoce el tag name del elemento, se puede utilizar el comodín *<br/>
**Ejemplo:** Buscar todos los elementos que cumplan la siguiente propiedad:<br/>
(//*[@class=‘login_form’])

Si hay mas de una vez el mismo atributo, se utiliza [num_posicion] para indicar el que deseamos seleccionar<br/>
**Ejemplo:** selecionar el segundo elemento quer contenga la class=‘login_form’
    
    <tr>
    <td class=‘login_form’></td>
    <td class=‘login_form’></td>
    </tr>

(//*[@class=‘login_form’])[2]

**Combinar atributos**<br/> 
    
    //input[@name=‘sex’][@value=‘1’]
    //input[@name=‘sex’ and @value=‘1’]
    //*[@name=‘sex’][@value=‘1’]

Contains, se suele utilizar para buscar los textos, el elemento que contenga un texto determinado

    //*[contains(text(),’some text’)]

Diferencias xpath vs cssSelector:

    Xpath: //input[@placeholder=‘valor’]
    Css: input[placeholder=‘valor’]
    
[Subir](#top)
